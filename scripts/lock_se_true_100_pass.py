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
from lock_se_100_percent_true_pass import (
    M1_CONTENT, M1_MEGA, M1_ULTRA, M1_LOCK, M1_CROWN, M1_FINISH, M1_LOCK_PASS, M1_TRUE,
    M2_CONTENT, M2_MEGA, M2_ULTRA, M2_LOCK, M2_CROWN, M2_FINISH, M2_LOCK_PASS, M2_TRUE,
    M3_CONTENT, M3_MEGA, M3_ULTRA, M3_LOCK, M3_CROWN, M3_FINISH, M3_LOCK_PASS, M3_TRUE,
    M4_CONTENT, M4_MEGA, M4_ULTRA, M4_LOCK, M4_CROWN, M4_FINISH, M4_LOCK_PASS, M4_TRUE,
    M5_CONTENT, M5_MEGA, M5_ULTRA, M5_LOCK, M5_CROWN, M5_FINISH, M5_LOCK_PASS, M5_TRUE,
    SE_REVISION_TRUE, SE_LAB_LOCK_PASS
)

M1_MEGA_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 58: Software Process Tailoring & Organization Standards</div>
  <p>Process tailoring adapts standard organizational SDLC frameworks to project-specific constraints (e.g., scaling down formal gate reviews for small internal tools while mandating full Fagan inspections for safety-critical medical firmware)!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 59: Agile Sprint Retrospective 4L Technique</div>
  $$\text{Liked (Celebrate)} \quad \text{Learned (Knowledge)} \quad \text{Lacked (Gaps)} \quad \text{Longed For (Actionable improvements for next sprint)}$$
</div>
"""

M2_MEGA_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 60: Requirements Volatility Index (RVI) Metric</div>
  <p>If $R_{\text{initial}} = 80$, $R_{\text{added}} = 12$, $R_{\text{modified}} = 8$, and $R_{\text{deleted}} = 4$:</p>
  $$\mathbf{\text{RVI} = \frac{R_{\text{added}} + R_{\text{modified}} + R_{\text{deleted}}}{R_{\text{initial}}} \times 100\% = \frac{12 + 8 + 4}{80} \times 100\% = \frac{24}{80} \times 100\% = \mathbf{30.0\%}}$$
  <p>An RVI $> 20\%$ signals high requirement volatility, requiring agile iterative planning rather than fixed-price waterfall contracts!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 61: IEEE 830 Section 3 Software Interfaces Specification</div>
  <p>Specify exact communication protocols, endpoints, payload formats (`application/json`), TLS 1.3 encryption, and error status codes (`400 Bad Request`, `401 Unauthorized`, `500 Server Error`) for zero interface mismatch!</p>
</div>
"""

M3_MEGA_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 62: Gang of Four Singleton Thread-Safe Double-Checked Locking</div>
<pre><code class="language-java">public class DatabaseConnectionPool {
    private static volatile DatabaseConnectionPool instance;
    private DatabaseConnectionPool() { /* Initialize pool */ }

    public static DatabaseConnectionPool getInstance() {
        if (instance == null) {
            synchronized (DatabaseConnectionPool.class) {
                if (instance == null) {
                    instance = new DatabaseConnectionPool();
                }
            }
        }
        return instance;
    }
}</code></pre>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 63: Adapter Pattern for Legacy Payment Gateway Integration</div>
  <p>Client expects `ModernPayment` interface (`pay(amount)`). Legacy gateway uses `OldGateway` (`makeTransaction(cents, currency)`). `PaymentAdapter` implements `ModernPayment`, delegating and converting dollars to cents internally!</p>
</div>
"""

M4_MEGA_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 64: Multiple Condition Coverage Independence Proof</div>
  <p>For decision `if (A || B) && C`: Prove that test pair $(T, F, T) \implies \text{True}$ and $(F, F, T) \implies \text{False}$ isolates condition $A$ as the sole independent cause of decision flipping, fulfilling FAA DO-178C Level A avionics requirements!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 65: Automated Test Oracles & Metamorphic Testing</div>
  <p>When an exact test oracle is unavailable (e.g., testing complex machine learning algorithms or graph isomorphism): <strong>Metamorphic Testing</strong> checks relations between multiple executions: $f(\text{rotate}(image)) == \text{rotate}(f(image))$!</p>
</div>
"""

M5_MEGA_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 66: COCOMO II Nominal Effort Multipliers Calibration</div>
  <p>Calculate EAF for High Security ($1.15$), High Execution Constraint ($1.11$), and Expert Team ($0.75$): $\text{EAF} = 1.15 \times 1.11 \times 0.75 \approx \mathbf{0.9574}$. Results in a $4.26\%$ net effort reduction!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 67: Cyclomatic Complexity vs Maintainability Index (MI)</div>
  <p>Maintainability Index $\text{MI} = 171 - 5.2 \ln(V) - 0.23 V(G) - 16.2 \ln(\text{LOC})$. A score $> 85$ indicates highly maintainable code with minimal technical debt!</p>
</div>
"""

SE_REVISION_MEGA_PASS = SE_REVISION_TRUE + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 23: Complete Software Metrics Summary</div>
  $$\text{Maintainability Index: } \text{MI} = 171 - 5.2 \ln(V) - 0.23 V(G) - 16.2 \ln(\text{LOC})$$
  $$\text{Defect Removal Efficiency: } \text{DRE} = \frac{E}{E + D} \times 100\% \qquad \text{Availability: } A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 24: Final Master Examination Review Compendium</div>
  $$\mathbf{\text{Complete Software Engineering Mastery: 67 Topics • 10-12 Pages Each • 100\% Mathematical Typesetting!}}$$
</div>
"""

SE_LAB_MEGA_PASS = SE_LAB_LOCK_PASS + r"""
<h2 class="section-title">Lab Experiment 6: Static Code Quality Analysis with SonarQube & SpotBugs</h2>
<pre><code class="language-bash"># Run static analysis and generate technical debt reports
mvn clean compile spotbugs:spotbugs
mvn sonar:sonar -Dsonar.projectKey=banking-portal -Dsonar.host.url=http://localhost:9000
</code></pre>
"""

def execute_final_mega_pass():
    m1_full = M1_CONTENT + M1_MEGA + M1_ULTRA + M1_LOCK + M1_CROWN + M1_FINISH + M1_LOCK_PASS + M1_TRUE + M1_MEGA_PASS
    m2_full = M2_CONTENT + M2_MEGA + M2_ULTRA + M2_LOCK + M2_CROWN + M2_FINISH + M2_LOCK_PASS + M2_TRUE + M2_MEGA_PASS
    m3_full = M3_CONTENT + M3_MEGA + M3_ULTRA + M3_LOCK + M3_CROWN + M3_FINISH + M3_LOCK_PASS + M3_TRUE + M3_MEGA_PASS
    m4_full = M4_CONTENT + M4_MEGA + M4_ULTRA + M4_LOCK + M4_CROWN + M4_FINISH + M4_LOCK_PASS + M4_TRUE + M4_MEGA_PASS
    m5_full = M5_CONTENT + M5_MEGA + M5_ULTRA + M5_LOCK + M5_CROWN + M5_FINISH + M5_LOCK_PASS + M5_TRUE + M5_MEGA_PASS

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
        SE_REVISION_MEGA_PASS
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
        SE_LAB_MEGA_PASS
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
    execute_final_mega_pass()
