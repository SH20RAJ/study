#!/usr/bin/env python3
"""
Artificial Intelligence (CS24307) — Complete Neuroscience-Backed Study Suite Generator
BIT Mesra | B.Tech CSE 5th Semester (NEP Scheme 2024–25)

Generates:
1. Module 1: Intelligent Agents & PEAS Notes (11-13 Pages)
2. Module 2: Search Algorithms & Game Playing Notes (11-13 Pages)
3. Module 3: Knowledge Representation & Logic Notes (11-13 Pages)
4. Module 4: Planning & Bayesian Reasoning Notes (11-13 Pages)
5. Module 5: Machine Learning Foundations Notes (11-13 Pages)
6. 10-Page Master Quick Revision Guide (10 Pages)
7. Full Course Master Book (50+ Pages)
"""

import os
import sys
from playwright.sync_api import sync_playwright

from ai_module1_content import AI_M1_EXHAUSTIVE
from ai_module2_content import AI_M2_EXHAUSTIVE
from ai_module3_content import AI_M3_EXHAUSTIVE
from ai_module4_content import AI_M4_EXHAUSTIVE
from ai_module5_content import AI_M5_EXHAUSTIVE
from ai_revision_content import AI_REVISION_EXHAUSTIVE

BASE_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');

:root {
  --primary: #059669;       /* Emerald Green */
  --primary-light: #ecfdf5;
  --accent: #10b981;        /* Mint */
  --secondary: #4f46e5;     /* Indigo */
  --success: #059669;
  --success-bg: #ecfdf5;
  --warning: #d97706;
  --warning-bg: #fffbeb;
  --danger: #dc2626;
  --danger-bg: #fef2f2;
  --dark: #0f172a;
  --text: #1e293b;
  --text-muted: #64748b;
  --border: #cbd5e1;
  --bg-card: #ffffff;
  --bg-page: #f8fafc;
}

@page {
  size: A4 portrait;
  margin: 14mm 11mm 14mm 11mm;
  @bottom-right {
    content: "Page " counter(page);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8pt;
    color: #64748b;
  }
  @bottom-left {
    content: "Artificial Intelligence (CS24307) | BIT Mesra CSE";
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8pt;
    color: #64748b;
  }
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: var(--text);
  background-color: #ffffff;
  line-height: 1.58;
  font-size: 12.2px;
  padding: 0;
}

.page-container {
  max-width: 100%;
  margin: 0 auto;
  background: #ffffff;
  padding: 0;
}

.doc-header {
  border-bottom: 2.5px solid var(--primary);
  padding-bottom: 14px;
  margin-bottom: 18px;
}

.badge-container {
  display: flex;
  gap: 8px;
  margin-bottom: 8px;
  flex-wrap: wrap;
}

.badge {
  display: inline-block;
  padding: 3px 9px;
  font-size: 9.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-radius: 4px;
}

.badge-green { background: #d1fae5; color: #065f46; }
.badge-purple { background: #ede9fe; color: #5b21b6; }
.badge-blue { background: #dbeafe; color: #1e40af; }
.badge-amber { background: #fef3c7; color: #92400e; }

h1.doc-title {
  font-size: 21px;
  font-weight: 800;
  color: var(--dark);
  line-height: 1.25;
  margin-bottom: 4px;
}

.doc-subtitle {
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 500;
}

.toc-box {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 22px;
}

.toc-title {
  font-size: 13px;
  font-weight: 700;
  color: #15803d;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px 20px;
  font-size: 11.2px;
}

h2.section-title {
  font-size: 15.5px;
  font-weight: 700;
  color: var(--dark);
  border-left: 4px solid var(--primary);
  padding-left: 10px;
  margin: 22px 0 10px 0;
  page-break-after: avoid;
}

h3.subsection-title {
  font-size: 13.2px;
  font-weight: 700;
  color: #047857;
  margin: 16px 0 6px 0;
  page-break-after: avoid;
}

p { margin-bottom: 8px; text-align: justify; }

.callout {
  border-radius: 6px;
  padding: 10px 14px;
  margin: 10px 0;
  font-size: 11.5px;
  border-left: 4px solid;
  page-break-inside: avoid;
}
.callout-info { background: #ecfdf5; border-color: #10b981; color: #064e3b; }
.callout-warning { background: #fffbeb; border-color: #f59e0b; color: #78350f; }

.callout-title {
  font-weight: 700;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.custom-table {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0;
  font-size: 11px;
  page-break-inside: avoid;
}

.custom-table th, .custom-table td {
  border: 1px solid #cbd5e1;
  padding: 7px 10px;
  text-align: left;
}

.custom-table th {
  background: #f1f5f9;
  font-weight: 700;
  color: #1e293b;
}

pre {
  background: #0f172a;
  color: #f8fafc;
  padding: 11px 14px;
  border-radius: 6px;
  font-family: 'Fira Code', monospace;
  font-size: 10.8px;
  margin: 10px 0;
  page-break-inside: avoid;
  overflow-x: auto;
}

code {
  font-family: 'Fira Code', monospace;
  background: #f1f5f9;
  color: #0f172a;
  padding: 2px 5px;
  border-radius: 4px;
  font-size: 11px;
}

pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}

.qa-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 4px solid var(--secondary);
  border-radius: 6px;
  padding: 11px 15px;
  margin: 12px 0;
  page-break-inside: avoid;
}

.qa-q {
  font-weight: 700;
  color: var(--dark);
  margin-bottom: 6px;
  font-size: 12.2px;
}

.qa-a {
  color: #334155;
  font-size: 11.5px;
  line-height: 1.55;
}

.worked-box {
  background: #ffffff;
  border: 1.5px solid #10b981;
  border-radius: 8px;
  padding: 14px 18px;
  margin: 14px 0;
  page-break-inside: avoid;
}

.worked-title {
  font-size: 12.8px;
  font-weight: 800;
  color: #065f46;
  margin-bottom: 10px;
}

.formula-card {
  background: #ecfdf5;
  border-left: 4px solid #059669;
  padding: 10px 14px;
  margin: 10px 0;
  font-size: 11.8px;
  page-break-inside: avoid;
}

.diagram-container {
  margin: 14px auto;
  text-align: center;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 10px;
  page-break-inside: avoid;
}

.diagram-caption {
  font-size: 10px;
  color: var(--text-muted);
  font-weight: 600;
  margin-top: 6px;
}

.page-break {
  page-break-before: always;
  break-before: page;
}
"""

def wrap_html(title, subtitle, badge, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>
  <style>{BASE_CSS}</style>
</head>
<body>
  <div class="page-container">
    <div class="doc-header">
      <div class="badge-container">
        <span class="badge badge-green">CS24307 — Theory (3.0 Cr)</span>
        <span class="badge badge-purple">{badge}</span>
        <span class="badge badge-blue">BIT Mesra</span>
        <span class="badge badge-amber">NEP Scheme</span>
      </div>
      <h1 class="doc-title">{title}</h1>
      <div class="doc-subtitle">{subtitle}</div>
    </div>
    {content}
  </div>
</body>
</html>"""

AI_MODULES = [
    ("Module 1: Intelligent Agents & PEAS", "Definitions of AI, Turing Test, Rationality, PEAS Framework & 5 Agent Types", "Module I Notes", AI_M1_EXHAUSTIVE, "Module_1_Intelligent_Agents_Notes"),
    ("Module 2: Search Algorithms & Game Playing", "Uninformed Search (BFS/DFS/UCS/IDS), Heuristic A*, Minimax & Alpha-Beta Pruning", "Module II Notes", AI_M2_EXHAUSTIVE, "Module_2_Search_Algorithms_Notes"),
    ("Module 3: Knowledge Representation & Logic", "Propositional Logic, Entailment, CNF, First-Order Logic, Unification (MGU) & Resolution", "Module III Notes", AI_M3_EXHAUSTIVE, "Module_3_Knowledge_Logic_Notes"),
    ("Module 4: Planning & Probabilistic Reasoning", "STRIPS, PDDL, Graphplan Mutex, Bayes' Rule, Bayesian Belief Networks & d-separation", "Module IV Notes", AI_M4_EXHAUSTIVE, "Module_4_Planning_Bayes_Notes"),
    ("Module 5: Machine Learning Foundations", "Inductive Learning, ID3 Decision Trees (Entropy/Gain), Perceptrons & Backpropagation", "Module V Notes", AI_M5_EXHAUSTIVE, "Module_5_Machine_Learning_Notes"),
    ("Artificial Intelligence — 10-Page Master Quick Revision", "High-Yield Formula Sheet, Complexity Matrix & Top 10 BIT Mesra PYQ Solutions", "10-Page Master Revision", AI_REVISION_EXHAUSTIVE, "AI_10_Page_Master_Revision"),
]

def build_all_ai():
    base_dir = "/Users/shaswatraj/Desktop/study/artificial-intelligence"
    html_dir = os.path.join(base_dir, "html")
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(html_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    print("Launching Chromium for exhaustive Artificial Intelligence suite...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=True
        )
        
        # Executive Master Cover Page for Page 1
        master_cover_page = """
        <div style="padding: 10px 0;">
          <div style="background: linear-gradient(135deg, #10b981, #059669); color: #ffffff; padding: 24px; border-radius: 10px; margin-bottom: 20px;">
            <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #d1fae5; margin-bottom: 6px;">Executive Master Study Guide & Algorithmic Problem Bank</div>
            <h2 style="font-size: 24px; font-weight: 800; line-height: 1.2; margin-bottom: 8px; color: #ffffff;">Artificial Intelligence (CS24307)</h2>
            <p style="font-size: 12.5px; color: #ecfdf5;">Birla Institute of Technology, Mesra | B.Tech CSE 5th Semester (NEP 2024–25 Scheme)</p>
          </div>

          <h3 class="subsection-title" style="margin-top: 0;">📚 Complete Course Structure & Algorithmic Matrix</h3>
          <table class="custom-table" style="margin-bottom: 20px;">
            <thead>
              <tr><th>Module</th><th>Core Syllabus Scope</th><th>Key Algorithms & Formulations</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Module I</strong></td><td>Intelligent Agents & Problem Solving</td><td>PEAS Description, Environment Types, State Space Formulation, Uninformed Search (BFS, DFS, DLS, IDDFS, UCS)</td></tr>
              <tr><td><strong>Module II</strong></td><td>Informed Search & Game AI</td><td>Greedy Best-First, A* Search (Admissibility & Consistency Proofs), IDA*, Hill Climbing, Simulated Annealing, Minimax, Alpha-Beta Pruning, CSP</td></tr>
              <tr><td><strong>Module III</strong></td><td>Knowledge & Logic Resolution</td><td>Propositional Logic (PL), First-Order Logic (FOL), CNF Conversion, Forward & Backward Chaining, Resolution Refutation</td></tr>
              <tr><td><strong>Module IV</strong></td><td>Planning & Probabilistic Reasoning</td><td>STRIPS, PDDL Action Schemas, Planning Graphs, Bayesian Belief Networks (BBN), Conditional Independence, d-separation</td></tr>
              <tr><td><strong>Module V</strong></td><td>Learning & Neural Networks</td><td>Inductive Learning, Decision Tree (ID3 Information Gain), Perceptrons, Multi-Layer Perceptrons (MLP), Backpropagation</td></tr>
            </tbody>
          </table>

          <div class="callout callout-info">
            <div class="callout-title">🎯 Exam Preparation & High-Yield Strategy</div>
            This publication-grade master book consolidates all 5 modules with formal search completeness & optimality proofs, KaTeX-rendered logic formulations, game tree pruning traces, and model answers to BIT Mesra end-semester examination questions.
          </div>
        </div>
        """

        full_course_body = master_cover_page
        for title, subtitle, badge, body, filename in AI_MODULES:
            html_content = wrap_html(title, subtitle, badge, body)
            html_file = os.path.join(html_dir, f"{filename}.html")
            pdf_file = os.path.join(pdf_dir, f"{filename}.pdf")

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)

            page = browser.new_page()
            page.goto(f"file://{html_file}", wait_until="networkidle")
            page.wait_for_timeout(1800)
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
                full_course_body += f"<div class='page-break'></div>{body}"

        # Full Course Master
        full_master_html = wrap_html(
            "Artificial Intelligence (CS24307) — Full Course Master Book",
            "Complete End-to-End B.Tech CSE 5th Semester Study Book & PYQ Bank",
            "Full Course Master",
            full_course_body
        )
        full_html_file = os.path.join(html_dir, "AI_Full_Course_Master.html")
        full_pdf_file = os.path.join(pdf_dir, "AI_Full_Course_Master.pdf")
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
    build_all_ai()
