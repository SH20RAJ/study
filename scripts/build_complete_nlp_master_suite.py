#!/usr/bin/env python3
"""
Publication-Grade Complete Master Suite Builder for Natural Language Processing (CS24351).
Generates strictly 10-12 pages for every module (M1-M5), 10 pages for Revision, and 56+ pages for Full Master Book.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

SHARED_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap');

@page {
  size: A4 portrait;
  margin: 15mm 12mm 15mm 12mm;
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8pt;
    font-weight: 600;
    color: #64748b;
  }
  @bottom-left {
    content: "CS24351 Natural Language Processing • BIT Mesra";
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8pt;
    font-weight: 600;
    color: #0284c7;
  }
}

* { box-sizing: border-box; }
body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 11.2px;
  line-height: 1.58;
  color: #1e293b;
  background: #ffffff;
  margin: 0;
  padding: 0;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

.cover-container {
  padding: 24px 20px;
  background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0369a1 100%);
  border-radius: 12px;
  color: #ffffff;
  margin-bottom: 22px;
  border: 1px solid #38bdf8;
  box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.25);
  page-break-inside: avoid;
}
.course-badge {
  display: inline-block;
  background: rgba(56, 189, 248, 0.2);
  border: 1px solid #38bdf8;
  color: #bae6fd;
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 8px;
}
.book-title {
  font-size: 23px;
  font-weight: 800;
  line-height: 1.25;
  margin: 0 0 6px 0;
  color: #ffffff;
  letter-spacing: -0.4px;
}
.book-subtitle {
  font-size: 12.5px;
  font-weight: 400;
  color: #cbd5e1;
  line-height: 1.4;
}

h1.module-title {
  font-size: 20px;
  font-weight: 800;
  color: #0f172a;
  border-bottom: 2.5px solid #0284c7;
  padding-bottom: 6px;
  margin: 22px 0 14px 0;
  page-break-after: avoid;
}
h2.section-title {
  font-size: 14.5px;
  font-weight: 700;
  color: #0369a1;
  border-left: 4px solid #0284c7;
  padding-left: 9px;
  margin: 18px 0 10px 0;
  page-break-after: avoid;
}
h3.sub-title {
  font-size: 12.5px;
  font-weight: 700;
  color: #334155;
  margin: 13px 0 6px 0;
  page-break-after: avoid;
}

p { margin: 0 0 9px 0; }
ul, ol { margin: 0 0 10px 0; padding-left: 20px; }
li { margin-bottom: 4px; }

.callout-box {
  background: #f0f9ff;
  border-left: 4px solid #0284c7;
  border-radius: 0 8px 8px 0;
  padding: 10px 14px;
  margin: 12px 0;
  font-size: 11px;
  page-break-inside: avoid;
}
.callout-title {
  font-weight: 700;
  color: #0369a1;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.worked-box {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-left: 4px solid #6366f1;
  border-radius: 8px;
  padding: 12px 14px;
  margin: 14px 0;
  page-break-inside: avoid;
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.worked-title {
  font-weight: 800;
  color: #4338ca;
  font-size: 12px;
  margin-bottom: 6px;
}

.custom-table {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0;
  font-size: 10.5px;
  page-break-inside: avoid;
}
.custom-table th {
  background: #0f172a;
  color: #ffffff;
  padding: 7px 10px;
  font-weight: 700;
  text-align: left;
  border: 1px solid #334155;
}
.custom-table td {
  padding: 6px 10px;
  border: 1px solid #e2e8f0;
  vertical-align: top;
}
.custom-table tr:nth-child(even) { background: #f8fafc; }

pre {
  background: #0f172a;
  color: #e2e8f0;
  padding: 10px 13px;
  border-radius: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9.8px;
  line-height: 1.45;
  overflow-x: auto;
  margin: 10px 0;
  page-break-inside: avoid;
  border: 1px solid #334155;
}
code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  background: #e0f2fe;
  color: #0369a1;
  padding: 1.5px 4px;
  border-radius: 4px;
}

.katex-display {
  margin: 8px 0 !important;
  padding: 4px 0 !important;
}

.qa-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 10px 12px;
  margin: 10px 0;
  page-break-inside: avoid;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.qa-q {
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 4px;
}
.qa-a {
  color: #334155;
}
.page-break { page-break-before: always; }
"""

def wrap_html(title, subtitle, body_html, module_num=None):
    badge = f"Module {module_num} • CS24351" if module_num else "CS24351 Natural Language Processing"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {{
    delimiters: [
      {{left: '$$', right: '$$', display: true}},
      {{left: '$', right: '$', display: false}}
    ]
  }});"></script>
<style>{SHARED_CSS}</style>
</head>
<body>
<div class="cover-container">
  <div class="course-badge">{badge}</div>
  <h1 class="book-title">{title}</h1>
  <div class="book-subtitle">{subtitle}</div>
</div>
{body_html}
</body>
</html>"""

def generate_pdf(html_path, pdf_path, title):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}", wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")
        page.wait_for_timeout(1000)
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "12mm", "right": "12mm"}
        )
        browser.close()
    print(f"✅ Generated {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
