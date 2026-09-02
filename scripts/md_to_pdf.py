#!/usr/bin/env python3
"""
Universal Publication-Grade Markdown-to-PDF Converter using Playwright Chromium.
Renders KaTeX Math, Code Blocks, Custom Tables, Callout Cards, and Clean @page Pagination.
"""

import os, sys, re, glob
from playwright.sync_api import sync_playwright

def convert_md_to_html(md_text, title="Study Notes"):
    """Converts markdown text to styled standalone HTML with KaTeX and CSS."""
    import html
    
    # Simple regex-based or python-markdown parsing for high reliability
    lines = md_text.split('\n')
    html_lines = []
    in_code_block = False
    code_lang = ""
    code_buffer = []
    in_table = False
    table_buffer = []
    
    def process_inline(text):
        # Math delimiters: $$ ... $$ and $ ... $
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        # Inline code
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        # Links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        return text

    for line in lines:
        # Check code fence
        if line.startswith('```'):
            if in_code_block:
                in_code_block = False
                escaped_code = html.escape('\n'.join(code_buffer))
                html_lines.append(f'<pre><code class="language-{code_lang}">{escaped_code}</code></pre>')
                code_buffer = []
                code_lang = ""
            else:
                in_code_block = True
                code_lang = line[3:].strip()
            continue
            
        if in_code_block:
            code_buffer.append(line)
            continue
            
        # Check Table
        if line.strip().startswith('|') and line.strip().endswith('|'):
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(line.strip())
            continue
        elif in_table:
            in_table = False
            # Process table
            if len(table_buffer) >= 2:
                th_cells = [process_inline(c.strip()) for c in table_buffer[0].strip('|').split('|')]
                t_html = ['<table class="custom-table"><thead><tr>']
                for th in th_cells:
                    t_html.append(f'<th>{th}</th>')
                t_html.append('</tr></thead><tbody>')
                
                # Check data rows (skip separator row at index 1)
                for row_line in table_buffer[2:]:
                    td_cells = [process_inline(c.strip()) for c in row_line.strip('|').split('|')]
                    t_html.append('<tr>')
                    for td in td_cells:
                        t_html.append(f'<td>{td}</td>')
                    t_html.append('</tr>')
                t_html.append('</tbody></table>')
                html_lines.append(''.join(t_html))
            table_buffer = []

        # Empty line
        if not line.strip():
            html_lines.append('')
            continue
            
        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1 class="main-title">{process_inline(line[2:])}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2 class="section-title">{process_inline(line[3:])}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3 class="subsection-title">{process_inline(line[4:])}</h3>')
        elif line.startswith('#### '):
            html_lines.append(f'<h4 style="font-size: 13px; font-weight: 700; color: #0284c7; margin: 12px 0 6px 0;">{process_inline(line[5:])}</h4>')
        elif line.startswith('> '):
            html_lines.append(f'<div class="callout callout-info"><div class="callout-title">Key Insight</div>{process_inline(line[2:])}</div>')
        elif line.startswith('- ') or line.startswith('* '):
            html_lines.append(f'<li>{process_inline(line[2:])}</li>')
        elif re.match(r'^\d+\.\s+', line):
            content = re.sub(r'^\d+\.\s+', '', line)
            html_lines.append(f'<li>{process_inline(content)}</li>')
        elif line.startswith('$$') and line.endswith('$$') and len(line) > 2:
            html_lines.append(f'<div class="formula-card">{line}</div>')
        else:
            html_lines.append(f'<p>{process_inline(line)}</p>')

    body_content = '\n'.join(html_lines)
    
    # Wrap with publication-grade HTML template
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Fira+Code:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {{delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ]}});"></script>
  <style>
    @page {{
      size: A4 portrait;
      margin: 15mm 12mm 15mm 12mm;
      @bottom-right {{
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 8.5pt;
        color: #64748b;
      }}
      @bottom-left {{
        content: "{title} • BIT Mesra CSE";
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 8.5pt;
        color: #64748b;
      }}
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 11.8px;
      line-height: 1.60;
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
      margin-top: 10px;
      margin-bottom: 14px;
    }}
    .section-title {{
      font-size: 14.5px;
      font-weight: 700;
      color: #0369a1;
      border-bottom: 1.5px solid #e2e8f0;
      padding-bottom: 4px;
      margin-top: 20px;
      margin-bottom: 10px;
      page-break-after: avoid;
    }}
    .subsection-title {{
      font-size: 13px;
      font-weight: 700;
      color: #0f172a;
      margin-top: 14px;
      margin-bottom: 6px;
      page-break-after: avoid;
    }}
    p {{ margin: 0 0 8px 0; }}
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
    }}
    .callout-title {{
      font-weight: 700;
      color: #0369a1;
      margin-bottom: 4px;
    }}
    .formula-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 3.5px solid #6366f1;
      padding: 10px 14px;
      margin: 12px 0;
      border-radius: 0 6px 6px 0;
      page-break-inside: avoid;
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
        page.wait_for_timeout(1000)
        
        page.pdf(
            path=output_pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "12mm", "right": "12mm"},
            display_header_footer=True,
            header_template="<div></div>",
            footer_template="""
            <div style="font-size: 8.5pt; font-family: 'Plus Jakarta Sans', sans-serif; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 12mm;">
              <span>""" + title + """ • BIT Mesra</span>
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
