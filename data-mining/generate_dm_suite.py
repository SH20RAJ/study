#!/usr/bin/env python3
"""
Data Mining Concepts and Techniques (CS24303) - Comprehensive 10-15 Page/Module Study Suite Generator
BIT Mesra (NEP Scheme 2024-25)

Generates publication-grade, neuroscience-backed, deeply comprehensive study notes:
1. Module 1: Introduction to Data Mining, Data Objects & Proximity (14 Topics | ~14 Pages)
2. Module 2: Data Preprocessing, Normalization & Reduction (6 Topics | ~12 Pages)
3. Module 3: Data Warehousing, OLAP Cubes & AOI (9 Topics | ~14 Pages)
4. Module 4: Frequent Pattern Mining: Apriori & FP-Growth (7 Topics | ~15 Pages)
5. Module 5: Advanced Pattern Mining & Applications (10 Topics | ~12 Pages)
6. 10-Page Master Quick Revision Notes (Dense Exam Night Cheat Book)
7. Full Course Master Book (End-to-End Mega Book ~65-70 Pages)
"""

import os
import sys
from playwright.sync_api import sync_playwright

BASE_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');

:root {
  --primary: #0f766e;       /* Deep Teal */
  --primary-light: #f0fdfa;
  --accent: #0284c7;        /* Sky Blue */
  --secondary: #d97706;     /* Amber */
  --success: #059669;
  --success-bg: #ecfdf5;
  --warning: #d97706;
  --warning-bg: #fffbeb;
  --danger: #dc2626;
  --danger-bg: #fef2f2;
  --purple: #7e22ce;
  --purple-bg: #faf5ff;
  --dark: #0f172a;
  --text: #1e293b;
  --text-muted: #64748b;
  --border: #cbd5e1;
  --bg-card: #ffffff;
  --bg-page: #f8fafc;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: var(--text);
  background-color: var(--bg-page);
  line-height: 1.65;
  font-size: 12.5px;
  padding: 0;
}

.page-container {
  max-width: 920px;
  margin: 0 auto;
  background: #ffffff;
  padding: 38px 44px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}

.doc-header {
  border-bottom: 3px solid var(--primary);
  padding-bottom: 18px;
  margin-bottom: 22px;
}

.badge-container {
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.badge {
  display: inline-block;
  padding: 3px 10px;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-radius: 4px;
}

.badge-teal { background: #ccfbf1; color: #0f766e; }
.badge-amber { background: #fef3c7; color: #92400e; }
.badge-green { background: #d1fae5; color: #065f46; }
.badge-blue { background: #e0f2fe; color: #0369a1; }
.badge-purple { background: #ede9fe; color: #5b21b6; }

h1.doc-title {
  font-size: 24px;
  font-weight: 800;
  color: var(--dark);
  line-height: 1.25;
  margin-bottom: 5px;
}

.doc-subtitle {
  font-size: 12.5px;
  color: var(--text-muted);
  font-weight: 500;
}

.toc-box {
  background: #f0fdfa;
  border: 1px solid #99f6e4;
  border-radius: 8px;
  padding: 16px 20px;
  margin-bottom: 26px;
  page-break-inside: avoid;
}

.toc-title {
  font-size: 13.5px;
  font-weight: 700;
  color: #0f766e;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 24px;
  font-size: 11.5px;
}

h2.section-title {
  font-size: 16.5px;
  font-weight: 700;
  color: var(--dark);
  border-left: 4px solid var(--primary);
  padding-left: 10px;
  margin: 28px 0 12px 0;
  page-break-after: avoid;
}

h3.subsection-title {
  font-size: 13.8px;
  font-weight: 700;
  color: #0d9488;
  margin: 18px 0 8px 0;
  page-break-after: avoid;
}

h4.subsubsection-title {
  font-size: 12.8px;
  font-weight: 700;
  color: #1e3a8a;
  margin: 14px 0 6px 0;
  page-break-after: avoid;
}

p { margin-bottom: 9px; text-align: justify; }

.callout {
  border-radius: 6px;
  padding: 11px 15px;
  margin: 12px 0;
  font-size: 11.8px;
  border-left: 4px solid;
  page-break-inside: avoid;
}

.callout-info { background: #f0fdf4; border-color: #16a34a; color: #14532d; }
.callout-blue { background: #f0fdfa; border-color: #0f766e; color: #134e4a; }
.callout-warning { background: #fffbeb; border-color: #d97706; color: #78350f; }
.callout-danger { background: #fef2f2; border-color: #dc2626; color: #7f1d1d; }
.callout-pyq { background: #faf5ff; border-color: #9333ea; color: #581c87; }
.callout-neuro { background: #eff6ff; border-color: #2563eb; color: #1e3a8a; }

.callout-title {
  font-weight: 700;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}

table.custom-table {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0;
  font-size: 11.5px;
  background: #ffffff;
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid var(--border);
  page-break-inside: avoid;
}

table.custom-table th {
  background: #134e4a;
  color: #ffffff;
  font-weight: 600;
  text-align: left;
  padding: 7px 10px;
  font-size: 11px;
}

table.custom-table td {
  padding: 6px 10px;
  border-bottom: 1px solid #e2e8f0;
  vertical-align: middle;
}

table.custom-table tr:nth-child(even) td { background-color: #f8fafc; }

code {
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  background: #f1f5f9;
  color: #0f172a;
  padding: 1.5px 4px;
  border-radius: 3px;
  border: 1px solid #e2e8f0;
}

pre {
  background: #0f172a;
  color: #f8fafc;
  padding: 10px 14px;
  border-radius: 6px;
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  line-height: 1.45;
  overflow-x: auto;
  margin: 10px 0;
  page-break-inside: avoid;
}

ul, ol { margin: 6px 0 10px 18px; font-size: 12px; }
li { margin-bottom: 3.5px; }

.diagram-container {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px;
  margin: 14px 0;
  text-align: center;
  page-break-inside: avoid;
}

.diagram-caption {
  font-size: 10px;
  font-weight: 600;
  color: var(--text-muted);
  margin-top: 6px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.qa-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 12px 16px;
  margin: 12px 0;
  page-break-inside: avoid;
}

.qa-q { font-weight: 700; color: #0f766e; font-size: 12.3px; margin-bottom: 5px; }
.qa-a { font-size: 11.8px; color: var(--text); }

.worked-box {
  background: #f8fafc;
  border: 1px solid #94a3b8;
  border-left: 5px solid #0284c7;
  border-radius: 6px;
  padding: 12px 16px;
  margin: 14px 0;
  page-break-inside: avoid;
}

.worked-title {
  font-size: 12.5px;
  font-weight: 700;
  color: #0369a1;
  margin-bottom: 6px;
}

.formula-card {
  background: #f0fdf4;
  border: 1px solid #86efac;
  border-radius: 6px;
  padding: 10px 14px;
  margin: 10px 0;
  text-align: center;
  page-break-inside: avoid;
}

.page-break {
  page-break-before: always;
  break-before: page;
}

@media print {
  body { background: #ffffff; font-size: 11.8px; }
  .page-container { padding: 0; max-width: 100%; box-shadow: none; }
  @page {
    size: A4 portrait;
    margin: 14mm 11mm 14mm 11mm;
    @bottom-right {
      content: "Page " counter(page);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8px;
      color: #94a3b8;
    }
    @bottom-left {
      content: "Data Mining (CS24303) Study Notes | BIT Mesra";
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8px;
      color: #94a3b8;
    }
  }
  .toc-box, .diagram-container, .callout, table, pre, .qa-card, .worked-box, .formula-card {
    page-break-inside: avoid;
  }
}
"""

def wrap_html(title, subtitle, badge_text, body_html):
    template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"></script>
<style>__BASE_CSS__</style>
</head>
<body>
<div class="page-container">
  <div class="doc-header">
    <div class="badge-container">
      <span class="badge badge-teal">CS24303 — Theory (3.0 Cr)</span>
      <span class="badge badge-amber">__BADGE__</span>
      <span class="badge badge-green">BIT Mesra | NEP Scheme</span>
    </div>
    <h1 class="doc-title">__TITLE__</h1>
    <div class="doc-subtitle">__SUBTITLE__</div>
  </div>
  __BODY__
  <div style="margin-top: 25px; padding-top: 14px; border-top: 1px solid var(--border); font-size: 10px; color: var(--text-muted); display: flex; justify-content: space-between;">
    <span>Data Mining Concepts & Techniques (CS24303) — In-Depth Study Suite</span>
    <span>BIT Mesra | B.Tech CSE (5th Sem)</span>
  </div>
</div>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  });
</script>
</body>
</html>"""
    return template.replace("__TITLE__", title).replace("__SUBTITLE__", subtitle).replace("__BADGE__", badge_text).replace("__BODY__", body_html).replace("__BASE_CSS__", BASE_CSS)

# Import the 5 module bodies from modular files or embedded rich strings
from dm_module1_content import DM_M1_EXHAUSTIVE
from dm_module2_content import DM_M2_EXHAUSTIVE
from dm_module3_content import DM_M3_EXHAUSTIVE
from dm_module4_content import DM_M4_EXHAUSTIVE
from dm_module5_content import DM_M5_EXHAUSTIVE
from dm_revision_content import DM_REVISION_EXHAUSTIVE

MODULES = [
    ("Module 1: Data Attributes & Proximity Metrics", "KDD Pipeline, 4 Attribute Types, Boxplots, Euclidean & Cosine Distance", "Module I Notes (14 Topics)", DM_M1_EXHAUSTIVE, "Module_1_Data_Attributes_Notes"),
    ("Module 2: Data Preprocessing & Normalization", "Data Cleaning, Chi-Square Correlation, Min-Max, Z-Score & PCA Reduction", "Module II Notes (6 Topics)", DM_M2_EXHAUSTIVE, "Module_2_Preprocessing_Notes"),
    ("Module 3: Data Warehousing & OLAP Cubes", "Star/Snowflake Schemas, Data Cube Computation & 5 OLAP Operations", "Module III Notes (9 Topics)", DM_M3_EXHAUSTIVE, "Module_3_Data_Warehouse_Notes"),
    ("Module 4: Apriori & FP-Growth Pattern Mining", "Support/Confidence, Apriori Join & Prune, FP-Tree Mining & Lift", "Module IV Notes (7 Topics)", DM_M4_EXHAUSTIVE, "Module_4_Pattern_Mining_Notes"),
    ("Module 5: Advanced Pattern Mining & Applications", "Multilevel Rules, Antimonotonic Constraints, Colossal & Closed Patterns", "Module V Notes (10 Topics)", DM_M5_EXHAUSTIVE, "Module_5_Advanced_Mining_Notes"),
    ("Data Mining — 10-Page Master Quick Revision", "High-Yield Formula Sheet, Schema Matrices & Top BIT Mesra PYQ Solutions", "10-Page Master Revision", DM_REVISION_EXHAUSTIVE, "Data_Mining_10_Page_Master_Revision"),
]

def build_all_dm():
    base_dir = "/Users/shaswatraj/Desktop/study/data-mining"
    html_dir = os.path.join(base_dir, "html")
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(html_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    print("Launching Chromium for exhaustive Data Mining suite...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=True
        )
        full_course_body = ""
        for title, subtitle, badge, body, filename in MODULES:
            html_content = wrap_html(title, subtitle, badge, body)
            html_file = os.path.join(html_dir, f"{filename}.html")
            pdf_file = os.path.join(pdf_dir, f"{filename}.pdf")

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)

            page = browser.new_page()
            page.goto(f"file://{html_file}", wait_until="networkidle")
            page.wait_for_timeout(2000)
            page.pdf(
                path=pdf_file,
                format="A4",
                print_background=True,
                margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
                prefer_css_page_size=True
            )
            page.close()
            print(f"✅ Generated {pdf_file} ({os.path.getsize(pdf_file)} bytes)")
            
            if "10-Page" not in title:
                full_course_body += f"<div style='page-break-before: always;'>{body}</div>"

        # Full Course Master
        full_master_html = wrap_html(
            "Data Mining Concepts and Techniques (CS24303) — Full Course Master Book",
            "Complete End-to-End B.Tech CSE 5th Semester Study Book & PYQ Bank (46 Topics)",
            "Full Course Master (46 Topics)",
            full_course_body
        )
        full_html_file = os.path.join(html_dir, "Data_Mining_Full_Course_Master.html")
        full_pdf_file = os.path.join(pdf_dir, "Data_Mining_Full_Course_Master.pdf")
        with open(full_html_file, "w", encoding="utf-8") as f:
            f.write(full_master_html)

        page = browser.new_page()
        page.goto(f"file://{full_html_file}", wait_until="networkidle")
        page.wait_for_timeout(3500)
        page.pdf(
            path=full_pdf_file,
            format="A4",
            print_background=True,
            margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
            prefer_css_page_size=True
        )
        page.close()
        print(f"🎉 Generated Full Course Master Book: {full_pdf_file} ({os.path.getsize(full_pdf_file)} bytes)")
        browser.close()

if __name__ == "__main__":
    build_all_dm()
