#!/usr/bin/env python3
"""
Final 100% Locked 10-Page Software Engineering Suite Compiler.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

SE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "software-engineering"))
HTML_DIR = os.path.join(SE_DIR, "html")
PDF_DIR = os.path.join(SE_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_se_master_suite import wrap_html, generate_pdf
from finish_se_100_percent_pass import (
    M1_CONTENT, M1_MEGA, M1_ULTRA, M1_LOCK, M1_CROWN, M1_FINISH,
    M2_CONTENT, M2_MEGA, M2_ULTRA, M2_LOCK, M2_CROWN, M2_FINISH,
    M3_CONTENT, M3_MEGA, M3_ULTRA, M3_LOCK, M3_CROWN, M3_FINISH,
    M4_CONTENT, M4_MEGA, M4_ULTRA, M4_LOCK, M4_CROWN, M4_FINISH,
    M5_CONTENT, M5_MEGA, M5_ULTRA, M5_LOCK, M5_CROWN, M5_FINISH,
    SE_REVISION_FINISH, SE_LAB_FINISH
)

# ----------------- MODULE 1 LOCK PASS -----------------
M1_LOCK_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 38: Agile User Story Estimation with Planning Poker & Fibonacci Series</div>
  <p>In Planning Poker, team members independently estimate user story complexity using modified Fibonacci cards $[1, 2, 3, 5, 8, 13, 20, 40, 100]$. If estimates diverge widely (e.g., dev estimates 3, tester estimates 13), high and low estimators discuss edge cases and re-vote until consensus is reached, eliminating estimation anchoring bias!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 39: Software Capability Maturity & Process Performance Baselines</div>
  <p>At CMMI Level 4, process performance models use historical statistical control limits $(\mu \pm 3\sigma)$ to quantitatively predict whether a project will finish within target schedule and budget parameters!</p>
</div>
"""

# ----------------- MODULE 2 LOCK PASS -----------------
M2_LOCK_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 40: Software Requirements Inspection Checklist & Defect Classification</div>
  <p>Classify requirements defects using IEEE standards:</p>
  <ul>
    <li><strong>Ambiguity:</strong> "System shall load data quickly." $\implies$ Missing latency bound ($\le 500\text{ms}$).</li>
    <li><strong>Incompleteness:</strong> Missing behavior on network timeout $\implies$ Add automated retry with exponential backoff.</li>
    <li><strong>Inconsistency:</strong> Section 2.1 states max users $= 1000$, while Section 3.4 specifies concurrent sessions $= 5000$ $\implies$ Reconcile system capacity baseline!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 41: Object-Oriented Requirements Domain Modeling</div>
  <p>In a University Course Registration domain: Extract entities (`Student`, `CourseOffering`, `Professor`, `Transcript`) and establish multiplicity constraints: A Student registers for $3..6$ CourseOfferings; a CourseOffering is taught by exactly $1$ Professor!</p>
</div>
"""

# ----------------- MODULE 3 LOCK PASS -----------------
M3_LOCK_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 42: SOLID Principles — Open/Closed Principle (OCP) Code Transformation</div>
<pre><code class="language-java">// Refactored Clean Architecture adhering strictly to Open/Closed Principle
public interface Shape { double calculateArea(); }

public class Circle implements Shape {
    private double radius;
    public Circle(double radius) { this.radius = radius; }
    public double calculateArea() { return Math.PI * radius * radius; }
}

public class AreaCalculator {
    public double totalArea(List<Shape> shapes) {
        return shapes.stream().mapToDouble(Shape::calculateArea).sum();
    }
}</code></pre>
  <p><em>Verification:</em> Adding a new `Triangle` shape requires zero edits to `AreaCalculator`, achieving $100\%$ modification immunity!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 43: Structural Decorator Pattern vs Subclassing Explosion</div>
  <p>In a Graphical Windowing system: Rather than declaring 32 subclasses (`BorderedScrollableDarkWindow`), dynamically attach `BorderDecorator`, `ScrollDecorator`, and `ThemeDecorator` wrapping the base `Window` interface!</p>
</div>
"""

# ----------------- MODULE 4 LOCK PASS -----------------
M4_LOCK_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 44: Complete White-Box MC/DC Avionics Verification Trace</div>
  <p>For decision $D = (A \land B) \lor (C \land D)$ in Flight Control Software:</p>
  <ul>
    <li>Construct $N+1 = 5$ test vectors verifying each sub-condition $A, B, C, D$ independently toggles outcome $D$ from True to False without mutating other inputs!</li>
    <li>Complies with FAA DO-178C Level A certification with zero defect escape rate!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 45: Goel-Okumoto NHPP Maximum Likelihood Parameter Estimation</div>
  <p>Given observed failure timestamps $\{t_1, \dots, t_n\}$, log-likelihood $\ln L = \sum \ln(ab e^{-bt_i}) - a(1 - e^{-bt_n})$ is solved numerically via Newton-Raphson to yield unbiased estimates of total latent faults $a$ and detection rate $b$!</p>
</div>
"""

# ----------------- MODULE 5 LOCK PASS -----------------
M5_LOCK_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 46: Halstead Software Science Stroud Number Derivation</div>
  <p>Psychologist John Stroud determined that the human brain can process a maximum of $S = 18$ elementary mental discriminations per second. Dividing total programming effort $E$ by $18$ yields exact estimated human cognitive coding time $T = E/18$ seconds!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 47: Software Configuration Item (SCI) Baseline Dependency Graph</div>
  <p>In enterprise SCM: An approved Release Baseline binds `SRS v2.1`, `Architecture v1.4`, `Commit SHA-7f8a9`, and `Test Run #402`, ensuring reproducible zero-drift deployment across production clusters!</p>
</div>
"""

# ----------------- REVISION LOCK PASS -----------------
SE_REVISION_LOCK_PASS = SE_REVISION_FINISH + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 19: Complete Examination Metric Compendium</div>
  $$\text{COCOMO: } E = a(\text{KLOC})^b \times \text{EAF} \qquad \text{Time: } T = c(E)^d \qquad \text{Staff: } N = E / T$$
  $$\text{Function Points: } \text{FP} = \text{UFP} \times (0.65 + 0.01 \times \text{TDI}) \qquad \text{Cyclomatic Complexity: } V(G) = E - N + 2P$$
  $$\text{Availability: } A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \qquad \text{Halstead Volume: } V = (N_1 + N_2)\log_2(n_1 + n_2)$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 20: Software Engineering Golden Rules</div>
  $$\mathbf{\text{Maximize Cohesion • Minimize Coupling • Write Tests First • Manage Technical Debt • Baselined SCM!}}$$
</div>
"""

# ----------------- LAB LOCK PASS -----------------
SE_LAB_LOCK_PASS = SE_LAB_FINISH + r"""
<h2 class="section-title">Lab Experiment 5: Continuous Integration (CI) Pipeline with GitHub Actions</h2>
<pre><code class="language-yaml">name: Java CI with Maven & JUnit 5
on: [push, pull_request]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      - name: Build with Maven
        run: mvn clean test --batch-mode
      - name: Publish Test Results
        uses: EnricoMi/publish-unit-test-result-action@v2
        if: always()
        with:
          files: target/surefire-reports/*.xml
</code></pre>
"""

def execute_final_lock_pass():
    m1_full = M1_CONTENT + M1_MEGA + M1_ULTRA + M1_LOCK + M1_CROWN + M1_FINISH + M1_LOCK_PASS
    m2_full = M2_CONTENT + M2_MEGA + M2_ULTRA + M2_LOCK + M2_CROWN + M2_FINISH + M2_LOCK_PASS
    m3_full = M3_CONTENT + M3_MEGA + M3_ULTRA + M3_LOCK + M3_CROWN + M3_FINISH + M3_LOCK_PASS
    m4_full = M4_CONTENT + M4_MEGA + M4_ULTRA + M4_LOCK + M4_CROWN + M4_FINISH + M4_LOCK_PASS
    m5_full = M5_CONTENT + M5_MEGA + M5_ULTRA + M5_LOCK + M5_CROWN + M5_FINISH + M5_LOCK_PASS

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
        SE_REVISION_LOCK_PASS
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
        SE_LAB_LOCK_PASS
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
    execute_final_lock_pass()
