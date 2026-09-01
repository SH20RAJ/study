#!/usr/bin/env python3
"""
Software Engineering (CS24353) - Complete Neuroscience-Backed Study Suite Generator
Generates:
1. Module 1: Process Models & Agile Methodologies Notes (HTML & PDF)
2. Module 2: Requirements Engineering & IEEE 830 SRS Notes (HTML & PDF)
3. Module 3: Software Architecture, Cohesion & UML Notes (HTML & PDF)
4. Module 4: Verification, Validation & Software Testing Notes (HTML & PDF)
5. Module 5: Project Estimation, COCOMO & CMMI Notes (HTML & PDF)
6. 10-Page Master Quick Revision Notes (HTML & PDF)
7. Full Course Master Compilation (HTML & PDF)
"""

import os
import sys
from playwright.sync_api import sync_playwright

BASE_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');

:root {
  --primary: #047857;       /* Deep Emerald Green */
  --primary-light: #ecfdf5;
  --accent: #2563eb;        /* Blue */
  --secondary: #0f766e;     /* Teal */
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

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: var(--text);
  background-color: var(--bg-page);
  line-height: 1.6;
  font-size: 12.6px;
  padding: 0;
}

.page-container {
  max-width: 900px;
  margin: 0 auto;
  background: #ffffff;
  padding: 35px 40px;
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

.badge-green { background: #d1fae5; color: #065f46; }
.badge-blue { background: #dbeafe; color: #1e40af; }
.badge-emerald { background: #a7f3d0; color: #047857; }

h1.doc-title {
  font-size: 23px;
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
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 25px;
  page-break-inside: avoid;
}

.toc-title {
  font-size: 13px;
  font-weight: 700;
  color: #047857;
  margin-bottom: 8px;
}

.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px 20px;
  font-size: 11.5px;
}

h2.section-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--dark);
  border-left: 4px solid var(--primary);
  padding-left: 10px;
  margin: 24px 0 12px 0;
}

h3.subsection-title {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--secondary);
  margin: 15px 0 7px 0;
}

p { margin-bottom: 8px; text-align: justify; }

.callout {
  border-radius: 6px;
  padding: 10px 14px;
  margin: 11px 0;
  font-size: 11.8px;
  border-left: 4px solid;
  page-break-inside: avoid;
}

.callout-info { background: #f0fdf4; border-color: #16a34a; color: #14532d; }
.callout-blue { background: #ecfdf5; border-color: #047857; color: #064e3b; }
.callout-warning { background: #fffbeb; border-color: #d97706; color: #78350f; }
.callout-pyq { background: #faf5ff; border-color: #9333ea; color: #581c87; }

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
  margin: 11px 0;
  font-size: 11.5px;
  background: #ffffff;
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid var(--border);
  page-break-inside: avoid;
}

table.custom-table th {
  background: #064e3b;
  color: #ffffff;
  font-weight: 600;
  text-align: left;
  padding: 6px 10px;
  font-size: 11px;
}

table.custom-table td {
  padding: 5.5px 10px;
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
  padding: 9px 13px;
  border-radius: 6px;
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  line-height: 1.4;
  overflow-x: auto;
  margin: 9px 0;
  page-break-inside: avoid;
}

ul, ol { margin: 5px 0 9px 18px; font-size: 12px; }
li { margin-bottom: 3px; }

.diagram-container {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
  margin: 12px 0;
  text-align: center;
  page-break-inside: avoid;
}

.diagram-caption {
  font-size: 10px;
  font-weight: 600;
  color: var(--text-muted);
  margin-top: 5px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.qa-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 11px 15px;
  margin: 11px 0;
  page-break-inside: avoid;
}

.qa-q { font-weight: 700; color: #047857; font-size: 12.2px; margin-bottom: 5px; }
.qa-a { font-size: 11.8px; color: var(--text); }

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
      content: "Software Engineering (CS24353) Study Notes | BIT Mesra";
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8px;
      color: #94a3b8;
    }
  }
  .toc-box, .diagram-container, .callout, table, pre, .qa-card {
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
      <span class="badge badge-emerald">CS24353 — Elective (3.0 Cr)</span>
      <span class="badge badge-blue">__BADGE__</span>
      <span class="badge badge-green">BIT Mesra | NEP Scheme</span>
    </div>
    <h1 class="doc-title">__TITLE__</h1>
    <div class="doc-subtitle">__SUBTITLE__</div>
  </div>
  __BODY__
  <div style="margin-top: 22px; padding-top: 12px; border-top: 1px solid var(--border); font-size: 10px; color: var(--text-muted); display: flex; justify-content: space-between;">
    <span>Software Engineering (CS24353) — Comprehensive Study Suite</span>
    <span>BIT Mesra | B.Tech CSE</span>
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

SE_M1_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module I: Process Models & Agile Methodologies — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Software Crisis & Layered Technology</div>
    <div>2. Prescriptive Lifecycle Models (Waterfall, Spiral, RAD)</div>
    <div>3. Agile Manifesto & Scrum Framework</div>
    <div>4. Extreme Programming (XP & TDD)</div>
    <div>5. Project Scheduling & Risk Management (RMMM)</div>
  </div>
</div>

<h2 class="section-title">1. Software Process Lifecycle Models Comparison</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Model</th>
      <th style="width: 45%;">Core Characteristics</th>
      <th>Ideal Project Profile</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Waterfall Model</strong></td>
      <td>Strict linear sequential phases. High documentation discipline. No customer feedback until late testing phase.</td>
      <td>Well-understood, stable requirements (e.g., compilers, aerospace flight control).</td>
    </tr>
    <tr>
      <td><strong>Spiral Model (Boehm)</strong></td>
      <td>Risk-driven evolutionary meta-model combining prototyping with systematic waterfall milestones across 4 quadrants.</td>
      <td>Large, expensive, high-risk, mission-critical systems.</td>
    </tr>
    <tr>
      <td><strong>Scrum (Agile)</strong></td>
      <td>Iterative, time-boxed Sprints (2–4 weeks), daily stand-ups, self-organizing teams, shippable product increments.</td>
      <td>Rapidly evolving requirements, web/mobile applications.</td>
    </tr>
  </tbody>
</table>
"""

SE_M2_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module II: Requirements Engineering & IEEE 830 SRS — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Functional vs. Non-Functional Requirements</div>
    <div>2. Requirements Elicitation (FAST, JAD, Interviews)</div>
    <div>3. Data Flow Diagrams (DFD Level 0, 1, 2)</div>
    <div>4. IEEE 830-1998 Standard SRS Structure</div>
    <div>5. Requirements Traceability & Validation</div>
  </div>
</div>

<h2 class="section-title">1. IEEE Standard 830-1998 Structure of SRS</h2>
<ul>
  <li><strong>1. Introduction:</strong> Purpose, Scope, Definitions, References, Overview.</li>
  <li><strong>2. Overall Description:</strong> Product perspective, Functions, User classes, Operating environment, Design constraints, Assumptions.</li>
  <li><strong>3. Specific Requirements:</strong> Functional requirements, Performance criteria, Security/Safety constraints, External interface specifications (UI, Hardware, Software, Communications).</li>
</ul>
"""

SE_M3_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module III: Software Architecture, Cohesion & UML — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Architectural Concepts & SOLID Principles</div>
    <div>2. Modularity: Cohesion (7 Levels) & Coupling (6 Levels)</div>
    <div>3. Architectural Styles (Layered, Microservices, MVC)</div>
    <div>4. UML Structural: Use Case & Class Diagrams</div>
    <div>5. UML Behavioral: Sequence, Activity & Statecharts</div>
  </div>
</div>

<h2 class="section-title">1. Cohesion and Coupling Quality Spectrum</h2>
<p>
  <strong>Desirable Design Goal:</strong> High Cohesion within modules and Low (Loose) Coupling between modules.
</p>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 50%;">Cohesion Spectrum (Low $\rightarrow$ High / Desirable)</th>
      <th>Coupling Spectrum (High / Undesirable $\rightarrow$ Low / Desirable)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1. Coincidental (Worst)</td><td>1. Content Coupling (Worst - direct memory modification)</td></tr>
    <tr><td>2. Logical</td><td>2. Common Coupling (Shared global variables)</td></tr>
    <tr><td>3. Temporal</td><td>3. External Coupling</td></tr>
    <tr><td>4. Procedural</td><td>4. Control Coupling</td></tr>
    <tr><td>5. Communicational</td><td>5. Stamp Coupling (Passing composite data structure)</td></tr>
    <tr><td>6. Sequential</td><td rowspan="2">6. <strong>Data Coupling (Best - passing scalar parameters)</strong></td></tr>
    <tr><td>7. <strong>Functional Cohesion (Best - performs single focused task)</strong></td></tr>
  </tbody>
</table>
"""

SE_M4_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module IV: Verification, Validation & Software Testing — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Verification vs. Validation (Boehm's Criterion)</div>
    <div>2. Black-Box Testing: Equivalence Partitioning & BVA</div>
    <div>3. White-Box Testing: McCabe's Cyclomatic Complexity</div>
    <div>4. Levels of Testing: Unit, Integration (Stubs/Drivers), System</div>
    <div>5. Software Reliability: MTTF, MTBF & Availability</div>
  </div>
</div>

<h2 class="section-title">1. McCabe's Cyclomatic Complexity $V(G)$ Formulations</h2>
<p>
  Given a Control Flow Graph (CFG) $G$:
  <ol>
    <li>$V(G) = E - N + 2$ (where $E$ = edges, $N$ = nodes)</li>
    <li>$V(G) = P + 1$ (where $P$ = predicate / decision nodes with multiple outgoing branches)</li>
    <li>$V(G) = \text{Number of enclosed planar regions } R$</li>
  </ol>
</p>

<div class="callout callout-pyq">
  <div class="callout-title">🏛️ BIT Mesra Exam Question (10 Marks)</div>
  <strong>Problem:</strong> Draw the CFG and compute Cyclomatic Complexity for finding max of 3 numbers: `if (a > b) { if (a > c) max = a; else max = c; } else { if (b > c) max = b; else max = c; }`<br>
  <strong>Solution:</strong> The code contains 3 predicate/decision nodes ($P=3$). Thus, $V(G) = P + 1 = 3 + 1 = \mathbf{4}$. There are 4 linearly independent execution basis paths requiring at least 4 test cases for 100% branch coverage.
</div>
"""

SE_M5_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module V: Project Estimation, COCOMO & CMMI — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Function Point Analysis (Albrecht UFP & VAF)</div>
    <div>2. COCOMO I (Organic, Semidetached, Embedded Modes)</div>
    <div>3. SEI CMMI 5-Level Maturity Framework</div>
    <div>4. Software Configuration Management (SCM Baselines)</div>
    <div>5. Software Maintenance: 4 Types & Lehman's Laws</div>
  </div>
</div>

<h2 class="section-title">1. Basic COCOMO Estimation Formulas (Barry Boehm)</h2>
$$\text{Effort (Person-Months)} = a_b \times (\text{KLOC})^{b_b}$$
$$\text{Development Time (Months)} = c_b \times (\text{Effort})^{d_b}$$
<table class="custom-table">
  <thead>
    <tr>
      <th>Project Mode</th>
      <th>Team & Project Description</th>
      <th>$a_b$</th>
      <th>$b_b$</th>
      <th>$c_b$</th>
      <th>$d_b$</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Organic</strong></td><td>Small experienced team, well-understood domain ($< 50 \text{ KLOC}$).</td><td>$2.4$</td><td>$1.05$</td><td>$2.5$</td><td>$0.38$</td></tr>
    <tr><td><strong>Semidetached</strong></td><td>Medium team, mixed experience, medium size ($50 - 300 \text{ KLOC}$).</td><td>$3.0$</td><td>$1.12$</td><td>$2.5$</td><td>$0.35$</td></tr>
    <tr><td><strong>Embedded</strong></td><td>Tight hardware/software constraints, mission-critical.</td><td>$3.6$</td><td>$1.20$</td><td>$2.5$</td><td>$0.32$</td></tr>
  </tbody>
</table>
"""

SE_REVISION_BODY = r"""
<div class="toc-box">
  <div class="toc-title">⚙️ 10-Page Master Quick Revision — Software Engineering (CS24353)</div>
  <div class="toc-grid">
    <div>Page 1-2: Process Models (Waterfall vs. Spiral vs. Scrum), RMMM</div>
    <div>Page 3-4: Functional/Non-Functional Requirements & IEEE 830 SRS</div>
    <div>Page 5-6: Cohesion Spectrum, Coupling Spectrum & UML Architecture</div>
    <div>Page 7-8: ECP/BVA Black-Box & McCabe Cyclomatic Complexity V(G)</div>
    <div>Page 9-10: Function Points, COCOMO Formulas, CMMI 5-Levels & SCM</div>
  </div>
</div>

<h2 class="section-title">⚡ High-Yield Software Engineering Master Formulas</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th>Metric / Concept</th>
      <th>Exact Formula / Rule</th>
      <th>Key Exam Insight</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Cyclomatic Complexity</strong></td><td>$V(G) = E - N + 2 = P + 1 = \text{Regions}$</td><td>Equals number of linearly independent paths.</td></tr>
    <tr><td><strong>Function Points (FP)</strong></td><td>$\text{FP} = \text{UFP} \times [0.65 + 0.01 \times \sum F_i]$</td><td>$\sum F_i$ is sum of 14 general system characteristics.</td></tr>
    <tr><td><strong>COCOMO Effort</strong></td><td>$E = a_b \times (\text{KLOC})^{b_b} \text{ PM}$</td><td>Organic: $a_b=2.4, b_b=1.05$.</td></tr>
    <tr><td><strong>Availability</strong></td><td>$A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}} \times 100\%$</td><td>$\text{MTBF} = \text{MTTF} + \text{MTTR}$.</td></tr>
  </tbody>
</table>
"""

SE_MODULES = [
    ("Module 1: Process Models & Agile Methodologies", "Waterfall, Spiral, Scrum Sprints, Extreme Programming & RMMM", "Module I Notes", SE_M1_BODY, "Module_1_Process_Models_Notes"),
    ("Module 2: Requirements Engineering & IEEE 830 SRS", "Functional Requirements, Elicitation FAST/JAD, DFDs & SRS", "Module II Notes", SE_M2_BODY, "Module_2_Requirements_Notes"),
    ("Module 3: Software Architecture, Cohesion & UML", "Modularity, 7 Cohesion Types, 6 Coupling Types, SOLID, UML", "Module III Notes", SE_M3_BODY, "Module_3_Design_UML_Notes"),
    ("Module 4: Verification, Validation & Software Testing", "Black-Box (ECP/BVA), White-Box Cyclomatic Complexity V(G), V-Model", "Module IV Notes", SE_M4_BODY, "Module_4_Testing_QA_Notes"),
    ("Module 5: Project Estimation, COCOMO & CMMI", "Function Points, Basic/Intermediate COCOMO, CMMI 5-Levels, SCM", "Module V Notes", SE_M5_BODY, "Module_5_Estimation_CMMI_Notes"),
    ("Software Engineering — 10-Page Master Quick Revision", "High-Yield Formula Sheet, COCOMO Matrices & BIT Mesra PYQ Solutions", "10-Page Master Revision", SE_REVISION_BODY, "SE_10_Page_Master_Revision"),
]

def build_all_se():
    base_dir = "/Users/shaswatraj/Desktop/study/software-engineering"
    html_dir = os.path.join(base_dir, "html")
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(html_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    print("Launching Chromium for Software Engineering suite...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=True
        )
        # Executive Master Cover Page for Page 1
        master_cover_page = """
        <div style="padding: 10px 0;">
          <div style="background: linear-gradient(135deg, #d946ef, #a21caf); color: #ffffff; padding: 24px; border-radius: 10px; margin-bottom: 20px;">
            <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #fae8ff; margin-bottom: 6px;">Executive Master Study Guide & Case Study Bank</div>
            <h2 style="font-size: 24px; font-weight: 800; line-height: 1.2; margin-bottom: 8px; color: #ffffff;">Software Engineering (CS24309)</h2>
            <p style="font-size: 12.5px; color: #fdf4ff;">Birla Institute of Technology, Mesra | B.Tech CSE 5th Semester (NEP 2024–25 Scheme)</p>
          </div>

          <h3 class="subsection-title" style="margin-top: 0;">📚 Complete Course Structure & Engineering Lifecycle Matrix</h3>
          <table class="custom-table" style="margin-bottom: 20px;">
            <thead>
              <tr><th>Module</th><th>Core Syllabus Scope</th><th>Key Methodologies & Formulations</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Module I</strong></td><td>Process Models & Agile</td><td>Waterfall, Evolutionary Prototyping, Boehm Spiral, Agile Scrum, Sprint Burndown, Extreme Programming, CMMI</td></tr>
              <tr><td><strong>Module II</strong></td><td>Requirements & Modeling</td><td>Functional/Non-Functional Requirements, IEEE 830 SRS Standard, Use Case Modeling, Class Diagrams, Statecharts</td></tr>
              <tr><td><strong>Module III</strong></td><td>Design & Architecture</td><td>High Cohesion & Low Coupling Metrics, Architectural Styles (Layered, MVC, Microservices), GoF Design Patterns</td></tr>
              <tr><td><strong>Module IV</strong></td><td>Software Testing & QA</td><td>Black-Box (Equivalence Partitioning, BVA), White-Box (Basis Path, McCabe Cyclomatic Complexity $V(G) = E - N + 2P$), Mutation</td></tr>
              <tr><td><strong>Module V</strong></td><td>Estimation & Management</td><td>COCOMO II Cost Estimation Equations, Function Point (FP) Analysis, CPM/PERT Critical Path, Risk Management</td></tr>
            </tbody>
          </table>

          <div class="callout callout-info">
            <div class="callout-title">🎯 Exam Preparation & High-Yield Strategy</div>
            This publication-grade master book consolidates all 5 modules with formal software estimation formulas, step-by-step worked Cyclomatic Complexity & Function Point numericals, and comprehensive model answers to BIT Mesra end-semester examination questions.
          </div>
        </div>
        """

        full_course_body = master_cover_page
        for title, subtitle, badge, body, filename in SE_MODULES:
            html_content = wrap_html(title, subtitle, badge, body)
            html_file = os.path.join(html_dir, f"{filename}.html")
            pdf_file = os.path.join(pdf_dir, f"{filename}.pdf")

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)

            page = browser.new_page()
            page.goto(f"file://{html_file}", wait_until="networkidle")
            page.wait_for_timeout(1500)
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
            "Software Engineering (CS24353) — Full Course Master Book",
            "Complete End-to-End B.Tech CSE 5th Semester Study Book & PYQ Bank",
            "Full Course Master",
            full_course_body
        )
        full_html_file = os.path.join(html_dir, "SE_Full_Course_Master.html")
        full_pdf_file = os.path.join(pdf_dir, "SE_Full_Course_Master.pdf")
        with open(full_html_file, "w", encoding="utf-8") as f:
            f.write(full_master_html)

        page = browser.new_page()
        page.goto(f"file://{full_html_file}", wait_until="networkidle")
        page.wait_for_timeout(2500)
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
    build_all_se()
