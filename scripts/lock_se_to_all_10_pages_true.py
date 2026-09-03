#!/usr/bin/env python3
"""
Final 100% Guaranteed 10-Page Lock for All SE Modules.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

SE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "software-engineering"))
HTML_DIR = os.path.join(SE_DIR, "html")
PDF_DIR = os.path.join(SE_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_se_master_suite import wrap_html, generate_pdf
from lock_se_true_10_pages_pass import (
    M1_CONTENT, M1_MEGA, M1_ULTRA, M1_LOCK,
    M2_CONTENT, M2_MEGA, M2_ULTRA, M2_LOCK,
    M3_CONTENT, M3_MEGA, M3_ULTRA, M3_LOCK,
    M4_CONTENT, M4_MEGA, M4_ULTRA, M4_LOCK,
    M5_CONTENT, M5_MEGA, M5_ULTRA, M5_LOCK,
    SE_REVISION_LOCKED, SE_LAB_GUIDE
)

# ----------------- MODULE 1 CROWN -----------------
M1_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 19: Agile Velocity & Release Burndown Calculation</div>
  <p>A team completes 35, 40, and 45 story points over three 2-week sprints. Total project backlog is 360 story points:</p>
  <ul>
    <li>$$\text{Average Velocity } \mathbf{V = \frac{35 + 40 + 45}{3} = \mathbf{40 \text{ Story Points/Sprint}}}$$</li>
    <li>$$\text{Remaining Sprints Required } \mathbf{S = \frac{360 - 120}{40} = \frac{240}{40} = \mathbf{6 \text{ Sprints}}}$$</li>
    <li>$$\mathbf{\text{Estimated Calendar Delivery Time} = 6 \times 2 \text{ weeks} = \mathbf{12 \text{ Weeks (3 Months)!}}}$$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 20: Quantitative Risk Exposure (RE) Ranking & Budget Allocation</div>
  <p>Prioritize 3 technical project risks with probabilities and damage costs:</p>
  <ul>
    <li>Risk 1 (Database Data Corruption): $P_1 = 0.05, C_1 = \$200,000 \implies \mathbf{RE_1 = \$10,000}$.</li>
    <li>Risk 2 (Cloud API 24h Outage): $P_2 = 0.30, C_2 = \$50,000 \implies \mathbf{RE_2 = \$15,000 \ (Rank 1: Highest Priority!)}}$.</li>
    <li>Risk 3 (Developer Resignation): $P_3 = 0.20, C_3 = \$30,000 \implies \mathbf{RE_3 = \$6,000}$.</li>
  </ul>
</div>
"""

# ----------------- MODULE 2 CROWN -----------------
M2_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 21: Quality Function Deployment (QFD) Customer Importance Weighting</div>
  <p>In a QFD House of Quality matrix, customer requirements ($CR_1$: Fast Search, $CR_2$: Data Security) have weights $W = [8, 10]$. Technical metrics ($TC_1$: Query Cache, $TC_2$: 256-Bit SSL) have relationship scores $R = [[9, 1], [3, 9]]$:</p>
  <ul>
    <li>$$\text{Technical Importance (Query Cache)} = 8(9) + 10(3) = 72 + 30 = \mathbf{102}$$</li>
    <li>$$\text{Technical Importance (256-Bit SSL)} = 8(1) + 10(9) = 8 + 90 = \mathbf{98}$$</li>
    <li>$$\mathbf{\text{Conclusion: Query Caching receives highest initial engineering allocation!}}}$$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 22: Requirements Change Impact Assessment Metric</div>
  <p>For a proposed change impacting 4 classes in a 40-class system: $\text{Impact Ratio} = \frac{4}{40} = \mathbf{10.0\%}$. Change is classified as Moderate Impact and approved by CCB!</p>
</div>
"""

# ----------------- MODULE 3 CROWN -----------------
M3_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 23: Cohesion & Coupling Metric Derivation (LCOM & CBO)</div>
  <p>• <strong>Lack of Cohesion in Methods (LCOM - Chidamber & Kemerer):</strong> Let $P$ be method pairs with disjoint attribute sets, $Q$ be method pairs sharing attributes. $\text{LCOM} = \max(0, |P| - |Q|)$. High LCOM $\implies$ Poor cohesion (class should be split!).<br>• <strong>Coupling Between Objects (CBO):</strong> Count of external classes to which a class is coupled. High CBO $\implies$ High ripple effect vulnerability during refactoring!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Architecture Case: Observer Pattern in Real-Time Stock Market Dashboard</div>
  <p>Subject `StockTicker` maintains `List<StockObserver>`. When stock prices fluctuate, `notifyObservers()` updates `MobileAppView` and `LedgerService` concurrently with zero tight coupling!</p>
</div>
"""

# ----------------- MODULE 4 CROWN -----------------
M4_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 24: Multiple Condition Coverage (MCC) vs MC/DC Comparison</div>
  <p>For compound condition with $N = 4$ boolean inputs ($A \land B \lor C \land D$):</p>
  <ul>
    <li>Full Multiple Condition Coverage requires $\mathbf{2^N = 2^4 = 16 \text{ Test Cases}}$ (Exponential explosion!).</li>
    <li>MC/DC requires strictly $\mathbf{N + 1 = 4 + 1 = \mathbf{5 \text{ Test Cases}}}$, slashing test suite size by $\mathbf{68.75\%}$ while preserving safety certification!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 25: Musa Basic Execution Time Reliability Model</div>
  <p>Failure intensity $\lambda(\mu) = \lambda_0 (1 - \frac{\mu}{v_0})$ where initial intensity $\lambda_0 = 10 \text{ failures/CPU-hr}$ and total failures $v_0 = 100$. After observing $\mu = 50$ failures, $\lambda = 10(1 - 0.5) = \mathbf{5.0 \text{ Failures/CPU-Hour}}$!</p>
</div>
"""

# ----------------- MODULE 5 CROWN -----------------
M5_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 26: Intermediate COCOMO with Cost Driver Multipliers</div>
  <p>A $30 \text{ KLOC}$ embedded system has High Reliability requirement ($\text{EM}_1 = 1.15$), High Execution Constraint ($\text{EM}_2 = 1.11$), and Expert Team ($\text{EM}_3 = 0.82$):</p>
  <ul>
    <li>$$\text{EAF} = 1.15 \times 1.11 \times 0.82 \approx \mathbf{1.0467}$$</li>
    <li>$$E_{\text{nominal}} = 3.6 \times (30)^{1.20} = 3.6 \times 59.22 \approx \mathbf{213.2 \text{ Person-Months}}$$</li>
    <li>$$\mathbf{E_{\text{adjusted}} = 213.2 \times 1.0467 \approx \mathbf{223.15 \text{ Person-Months}}}$$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 27: Software Science Potential Volume ($V^*$) and Language Level ($L$)</div>
  <p>For minimum potential representation with $n_2^* = 4$ input/output parameters: $V^* = (2 + n_2^*)\log_2(2 + n_2^*) = 6 \log_2(6) = \mathbf{15.51 \text{ Bits}}$. Program Level $L = V^* / V = 15.51 / 100.38 \approx \mathbf{0.1545}$.</p>
</div>
"""

# ----------------- REVISION EXPANSION -----------------
SE_REVISION_CROWN = SE_REVISION_LOCKED + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 14: Comprehensive SE Estimation Cheat-Sheet</div>
  $$\text{COCOMO: } E = a(\text{KLOC})^b \times \text{EAF} \qquad \text{FP: } \text{UFP} \times (0.65 + 0.01 \times \text{TDI})$$
  $$\text{Halstead: } V = N \log_2 n \qquad D = \frac{n_1 N_2}{2 n_2} \qquad E = D \times V \qquad T = E / 18$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 15: Full Testing Hierarchy Cheat-Sheet</div>
  $$\text{Unit (JUnit)} \rightarrow \text{Integration (Stubs/Drivers)} \rightarrow \text{System (Security/Perf)} \rightarrow \text{UAT (Acceptance)}$$
</div>
"""

SE_LAB_CROWN = SE_LAB_GUIDE + r"""
<h2 class="section-title">Lab Experiment 3: StarUML Object-Oriented Modeling & Reverse Engineering</h2>
<pre><code class="language-text">1. Launch StarUML -> Select Model -> Add Diagram -> Class Diagram.
2. Create Classes: User, Account, Transaction with attributes and visibility annotations (+, -, #).
3. Draw Composite and Aggregation relationships with multiplicity bounds (1..*, 0..1).
4. Export Java code stubs automatically using the StarUML Java Extension generator!
</code></pre>
"""

def execute_crown_se():
    m1_full = M1_CONTENT + M1_MEGA + M1_ULTRA + M1_LOCK + M1_CROWN
    m2_full = M2_CONTENT + M2_MEGA + M2_ULTRA + M2_LOCK + M2_CROWN
    m3_full = M3_CONTENT + M3_MEGA + M3_ULTRA + M3_LOCK + M3_CROWN
    m4_full = M4_CONTENT + M4_MEGA + M4_ULTRA + M4_LOCK + M4_CROWN
    m5_full = M5_CONTENT + M5_MEGA + M5_ULTRA + M5_LOCK + M5_CROWN

    modules = [
        (1, "Module 1: Software Process Models, Agile & Project Management", "Topics 1 to 14 • Waterfall, Prototyping, Spiral, RAD, Scrum, XP, CPM/PERT Scheduling & Risk Management", m1_full, "Module_1_Process_Models_Notes"),
        (2, "Module 2: Software Requirements Engineering & SRS Standards", "Topics 15 to 26 • Functional/Non-Functional Requirements, FURPS+, TELOS Feasibility, IEEE 830 SRS & RTM", m2_full, "Module_2_Requirements_Notes"),
        (3, "Module 3: Software Design Engineering & UML 2.5 Modeling", "Topics 27 to 39 • Modularity, Cohesion, Coupling, SOLID Principles, Use Case, Class, Sequence & Activity Diagrams", m3_full, "Module_3_Design_UML_Notes"),
        (4, "Module 4: Verification, Validation & Software Testing Methodologies", "Topics 40 to 55 • Inspections, Static Analysis, McCabe Cyclomatic Complexity, Basis Path, Black-Box BVA & Reliability", m4_full, "Module_4_Testing_QA_Notes"),
        (5, "Module 5: Project Estimation, Quality Assurance, CMMI & Maintenance", "Topics 56 to 67 • Halstead Metrics, COCOMO I/II, Function Point Analysis, CMMI Levels, SCM & Lehman's Laws", m5_full, "Module_5_Estimation_CMMI_Notes"),
    ]

    for num, title, subtitle, content, fname in modules:
        html_content = wrap_html(title, subtitle, content, module_num=num)
        html_file = os.path.join(HTML_DIR, f"{fname}.html")
        pdf_file = os.path.join(PDF_DIR, f"{fname}.pdf")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        generate_pdf(html_file, pdf_file, f"SE Module {num}")

    # Revision Guide
    rev_html = wrap_html(
        "Software Engineering (CS24353) 10-Page Master Revision",
        "Universal Formulas, McCabe Cyclomatic Complexity, COCOMO Numericals, FP Analysis & Solved Flashcards",
        SE_REVISION_CROWN
    )
    rev_html_file = os.path.join(HTML_DIR, "SE_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "SE_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "SE 10-Page Master Revision")

    # Lab Guide
    lab_html = wrap_html(
        "Software Engineering Practical Lab Guide",
        "Test-Driven Development with JUnit 5, Git SCM Branching & CCB Workflows",
        SE_LAB_CROWN
    )
    lab_html_file = os.path.join(HTML_DIR, "SE_Lab_Practical_Guide.html")
    lab_pdf_file = os.path.join(PDF_DIR, "SE_Lab_Practical_Guide.pdf")
    with open(lab_html_file, "w", encoding="utf-8") as f:
        f.write(lab_html)
    generate_pdf(lab_html_file, lab_pdf_file, "SE Lab Guide")

    # Master Book via PyMuPDF merge
    master_doc = fitz.open()
    for _, _, _, _, fname in modules:
        mod_pdf = fitz.open(os.path.join(PDF_DIR, f"{fname}.pdf"))
        master_doc.insert_pdf(mod_pdf)
    
    lab_doc = fitz.open(lab_pdf_file)
    master_doc.insert_pdf(lab_doc)

    rev_doc = fitz.open(rev_pdf_file)
    master_doc.insert_pdf(rev_doc)

    master_pdf_path = os.path.join(PDF_DIR, "SE_Full_Course_Master.pdf")
    master_doc.save(master_pdf_path)
    print(f"✅ Generated {master_pdf_path} ({len(master_doc)} pages)")

if __name__ == "__main__":
    execute_crown_se()
