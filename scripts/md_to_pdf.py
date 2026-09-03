#!/usr/bin/env python3
"""
Universal Publication-Grade Markdown-to-PDF Converter using Playwright Chromium.
Renders KaTeX Math, Code Blocks, Custom Tables, Callout Cards, and Clean @page Pagination.
"""

import os, sys, re, html
from playwright.sync_api import sync_playwright

def convert_md_to_html(md_text, title="Study Notes"):
    """Converts markdown text to styled standalone HTML with KaTeX and CSS."""
    lines = md_text.split('\n')
    html_lines = []
    
    in_code_block = False
    code_lang = ""
    code_buffer = []
    
    in_math_block = False
    math_buffer = []
    
    in_table = False
    table_buffer = []
    
    in_list = False
    list_type = "ul"
    
    def process_inline(text):
        if not text:
            return ""
        # Protect inline math placeholders
        math_matches = []
        def math_repl(m):
            math_matches.append(m.group(0))
            return f"__MATH_PLACEHOLDER_{len(math_matches)-1}__"
        
        # Replace inline $...$ (not preceded or followed by $)
        text = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', math_repl, text)
        
        # Bold **text**
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # Italic *text* or _text_
        text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
        # Inline code `code`
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        # Links [text](url)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        
        # Restore math placeholders
        for idx, orig_math in enumerate(math_matches):
            text = text.replace(f"__MATH_PLACEHOLDER_{idx}__", orig_math)
            
        return text

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html_lines.append(f'</{list_type}>')
            in_list = False

    def close_table():
        nonlocal in_table, table_buffer
        if in_table:
            if len(table_buffer) >= 2:
                th_cells = [process_inline(c.strip()) for c in table_buffer[0].strip('|').split('|')]
                t_html = ['<table class="custom-table"><thead><tr>']
                for th in th_cells:
                    t_html.append(f'<th>{th}</th>')
                t_html.append('</tr></thead><tbody>')
                
                for row_line in table_buffer[2:]:
                    td_cells = [process_inline(c.strip()) for c in row_line.strip('|').split('|')]
                    t_html.append('<tr>')
                    for td in td_cells:
                        t_html.append(f'<td>{td}</td>')
                    t_html.append('</tr>')
                t_html.append('</tbody></table>')
                html_lines.append(''.join(t_html))
            table_buffer = []
            in_table = False

    for line in lines:
        stripped = line.strip()
        
        # 1. Code Blocks
        if stripped.startswith('```'):
            close_list()
            close_table()
            if in_code_block:
                in_code_block = False
                escaped_code = html.escape('\n'.join(code_buffer))
                html_lines.append(f'<pre><code class="language-{code_lang}">{escaped_code}</code></pre>')
                code_buffer = []
                code_lang = ""
            else:
                in_code_block = True
                code_lang = stripped[3:].strip()
            continue
            
        if in_code_block:
            code_buffer.append(line)
            continue

        # 2. Math Blocks ($$...$$)
        if stripped.startswith('$$'):
            close_list()
            close_table()
            if in_math_block:
                # Closing math block
                in_math_block = False
                # If there's content on the closing line after $$
                after_dollars = stripped[2:].strip()
                if after_dollars:
                    math_buffer.append(after_dollars)
                math_content = '\n'.join(math_buffer)
                html_lines.append(f'<div class="formula-card"><div class="katex-block">$${math_content}$$</div></div>')
                math_buffer = []
            else:
                # Check if it's single line $$ formula $$
                if stripped.endswith('$$') and len(stripped) > 2:
                    formula = stripped[2:-2].strip()
                    html_lines.append(f'<div class="formula-card"><div class="katex-block">$${formula}$$</div></div>')
                else:
                    in_math_block = True
                    inner = stripped[2:].strip()
                    if inner:
                        math_buffer.append(inner)
            continue
            
        if in_math_block:
            math_buffer.append(line)
            continue

        # 3. Markdown Tables
        if stripped.startswith('|') and stripped.endswith('|'):
            close_list()
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(stripped)
            continue
        elif in_table:
            close_table()

        # 4. Empty Lines
        if not stripped:
            close_list()
            continue

        # 5. Headers
        if stripped.startswith('# '):
            close_list()
            html_lines.append(f'<h1 class="main-title">{process_inline(stripped[2:])}</h1>')
        elif stripped.startswith('## '):
            close_list()
            html_lines.append(f'<h2 class="section-title">{process_inline(stripped[3:])}</h2>')
        elif stripped.startswith('### '):
            close_list()
            html_lines.append(f'<h3 class="subsection-title">{process_inline(stripped[4:])}</h3>')
        elif stripped.startswith('#### '):
            close_list()
            html_lines.append(f'<h4 style="font-size: 13px; font-weight: 700; color: #0284c7; margin: 12px 0 6px 0;">{process_inline(stripped[5:])}</h4>')
        elif stripped.startswith('> '):
            close_list()
            html_lines.append(f'<div class="callout callout-info"><div class="callout-title"><i class="fa-solid fa-lightbulb"></i> Key Insight</div><p style="margin:0;">{process_inline(stripped[2:])}</p></div>')
        elif stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list or list_type != "ul":
                close_list()
                in_list = True
                list_type = "ul"
                html_lines.append('<ul>')
            html_lines.append(f'<li>{process_inline(stripped[2:])}</li>')
        elif re.match(r'^\d+\.\s+', stripped):
            if not in_list or list_type != "ol":
                close_list()
                in_list = True
                list_type = "ol"
                html_lines.append('<ol>')
            content = re.sub(r'^\d+\.\s+', '', stripped)
            html_lines.append(f'<li>{process_inline(content)}</li>')
        elif stripped == '---':
            close_list()
            html_lines.append('<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 18px 0;">')
        else:
            close_list()
            html_lines.append(f'<p>{process_inline(line)}</p>')

    close_list()
    close_table()
    
    body_content = '\n'.join(html_lines)
    
    # Wrap with publication-grade HTML template
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  
  <style>
    @page {{
      size: A4 portrait;
      margin: 16mm 14mm 16mm 14mm;
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 11.5px;
      line-height: 1.62;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}
    .main-title {{
      font-size: 22px;
      font-weight: 800;
      color: #0f172a;
      border-bottom: 2px solid #0284c7;
      padding-bottom: 8px;
      margin-top: 14px;
      margin-bottom: 14px;
      letter-spacing: -0.4px;
    }}
    .section-title {{
      font-size: 14.5px;
      font-weight: 700;
      color: #0369a1;
      border-bottom: 1.5px solid #e2e8f0;
      padding-bottom: 4px;
      margin-top: 22px;
      margin-bottom: 10px;
      page-break-after: avoid;
    }}
    .subsection-title {{
      font-size: 12.8px;
      font-weight: 700;
      color: #0f172a;
      margin-top: 16px;
      margin-bottom: 6px;
      page-break-after: avoid;
    }}
    p {{ margin: 0 0 8px 0; text-align: justify; }}
    ul, ol {{ margin: 0 0 10px 0; padding-left: 20px; }}
    li {{ margin-bottom: 4px; }}
    .custom-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
      font-size: 10.8px;
      page-break-inside: avoid;
    }}
    .custom-table th, .custom-table td {{
      border: 1px solid #cbd5e1;
      padding: 6px 9px;
      text-align: left;
      vertical-align: top;
    }}
    .custom-table th {{
      background: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
    }}
    .custom-table tr:nth-child(even) {{ background: #f8fafc; }}
    .callout {{
      border-left: 3.5px solid #0284c7;
      background: #f0f9ff;
      padding: 10px 14px;
      margin: 12px 0;
      border-radius: 0 6px 6px 0;
      page-break-inside: avoid;
      font-size: 11px;
    }}
    .callout-title {{
      font-weight: 700;
      color: #0369a1;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .formula-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #6366f1;
      padding: 10px 16px;
      margin: 12px 0;
      border-radius: 6px;
      page-break-inside: avoid;
      text-align: center;
    }}
    .katex-block {{
      font-size: 12px;
      margin: 4px 0;
    }}
    .katex-display {{
      margin: 6px 0 !important;
    }}
    pre {{
      background: #0f172a;
      color: #f8fafc;
      padding: 10px 14px;
      border-radius: 6px;
      font-family: 'Fira Code', monospace;
      font-size: 10px;
      line-height: 1.45;
      overflow-x: auto;
      margin: 10px 0;
      page-break-inside: avoid;
    }}
    code {{
      font-family: 'Fira Code', monospace;
      font-size: 10.5px;
      background: #f1f5f9;
      color: #0369a1;
      padding: 1px 4px;
      border-radius: 3px;
    }}
    pre code {{
      background: transparent;
      color: inherit;
      padding: 0;
    }}
  </style>
</head>
<body>
  {body_content}
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      if (window.renderMathInElement) {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ]
        }});
      }}
    }});
  </script>
</body>
</html>"""
    return full_html

def convert_md_file_to_pdf(md_file_path, output_pdf_path, title=None):
    """Reads a markdown file and compiles it into a PDF via Playwright."""
    if not os.path.exists(md_file_path):
        print(f"❌ Markdown file not found: {md_file_path}")
        return False
        
    with open(md_file_path, "r", encoding="utf-8") as f:
        md_text = f.read()
        
    if not title:
        subj = os.path.basename(os.path.dirname(md_file_path)).replace('-', ' ').title()
        title = f"{subj} — Complete Master Notes"
        
    html_content = convert_md_to_html(md_text, title=title)
    
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    temp_html_path = output_pdf_path.replace(".pdf", ".temp.html")
    
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath(temp_html_path)}", wait_until="networkidle")
        
        # Explicitly invoke KaTeX in browser to guarantee rendering
        page.evaluate("""() => {
            if (window.renderMathInElement) {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ]
                });
            }
        }""")
        page.wait_for_timeout(1200)
        
        page.pdf(
            path=output_pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "16mm", "bottom": "16mm", "left": "14mm", "right": "14mm"},
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=f"""
            <div style="font-size: 8.5pt; font-family: 'Plus Jakarta Sans', sans-serif; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 14mm;">
              <span>{title} • BIT Mesra</span>
              <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
            </div>
            """
        )
        browser.close()
        
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
        
    print(f"✅ Generated: {output_pdf_path} ({os.path.getsize(output_pdf_path)} bytes)")
    return True

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    if len(sys.argv) >= 3:
        convert_md_file_to_pdf(sys.argv[1], sys.argv[2], title=sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        # Convert all subject all.md files into all.pdf
        subjects = [
            ("compiler-design", "Compiler Design (CS24301) — Complete Course Master Notes"),
            ("data-communication-and-networks", "Data Communication & Networks (CS24305) — Complete Master Notes"),
            ("data-mining", "Data Mining Concepts & Techniques (CS24303) — Complete Master Notes"),
            ("artificial-intelligence", "Artificial Intelligence (CS24307) — Complete Master Notes"),
            ("natural-language-processing", "Natural Language Processing (CS24351) — Complete Master Notes"),
            ("software-engineering", "Software Engineering (CS24353) — Complete Master Notes")
        ]
        
        for subj, title in subjects:
            md_path = os.path.join(base_dir, subj, "all.md")
            pdf_path = os.path.join(base_dir, subj, "pdf", "all.pdf")
            if os.path.exists(md_path):
                print(f"Converting {md_path} -> {pdf_path}...")
                convert_md_file_to_pdf(md_path, pdf_path, title=title)
