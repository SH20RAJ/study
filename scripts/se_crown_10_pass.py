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
from lock_se_true_100_pass import (
    M1_CONTENT, M1_MEGA, M1_ULTRA, M1_LOCK, M1_CROWN, M1_FINISH, M1_LOCK_PASS, M1_TRUE, M1_MEGA_PASS,
    M2_CONTENT, M2_MEGA, M2_ULTRA, M2_LOCK, M2_CROWN, M2_FINISH, M2_LOCK_PASS, M2_TRUE, M2_MEGA_PASS,
    M3_CONTENT, M3_MEGA, M3_ULTRA, M3_LOCK, M3_CROWN, M3_FINISH, M3_LOCK_PASS, M3_TRUE, M3_MEGA_PASS,
    M4_CONTENT, M4_MEGA, M4_ULTRA, M4_LOCK, M4_CROWN, M4_FINISH, M4_LOCK_PASS, M4_TRUE, M4_MEGA_PASS,
    M5_CONTENT, M5_MEGA, M5_ULTRA, M5_LOCK, M5_CROWN, M5_FINISH, M5_LOCK_PASS, M5_TRUE, M5_MEGA_PASS,
    SE_REVISION_MEGA_PASS, SE_LAB_MEGA_PASS
)

M1_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 68: Software Process Metric Dashboards (Lead Time vs Cycle Time)</div>
  <p>• <strong>Lead Time:</strong> Total calendar duration from initial customer story creation to production deployment.<br>• <strong>Cycle Time:</strong> Active engineering duration from when a developer begins writing code on a task to when it passes code review and CI tests. Measuring both exposes organizational approval bottlenecks!</p>
</div>
"""

M2_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 69: Requirements Elicitation Cognitive Biases</div>
  <p>Identify and mitigate cognitive biases in stakeholder interviews: (1) <strong>Availability Heuristic</strong> (users request features based on recent memorable outages), (2) <strong>Anchoring Bias</strong> (over-weighting the initial executive suggestion), (3) <strong>Confirmation Bias</strong> (analysts only hearing feedback supporting their pet architecture)!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 70: Use Case Generalization vs Extension</div>
  <p>`Make Payment` is a generalized base use case specialized by `Make Credit Card Payment` and `Make Crypto Payment` via standard object-oriented polymorphism!</p>
</div>
"""

M3_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 71: Structural Facade Pattern in Complex Subsystems</div>
  <p>In a home theater system: `HomeTheaterFacade` exposes a single simple `watchMovie()` method that coordinates `Projector.on()`, `SoundSystem.setVolume()`, `DvdPlayer.play()`, and `Lights.dim()`, shielding external callers from 15 separate low-level interfaces!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 72: Behavioral Command Pattern with Undo Mechanism</div>
  <p>Each user action is an instance of `Command` with `execute()` and `undo()` methods stored on a history stack, enabling infinite multi-level undo/redo operations!</p>
</div>
"""

M4_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 73: Branch Coverage vs Condition Coverage Counterexample</div>
  <p>For `if (A && B)`: Test cases $(T, T) \implies \text{True}$ and $(F, F) \implies \text{False}$ achieve $100\%$ branch coverage, but completely fail to test condition $A=T, B=F$ or $A=F, B=T$, proving why Condition Coverage is strictly required!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 74: Automated Regression Test Prioritization (APFD Metric)</div>
  <p>Average Percentage of Faults Detected (APFD) measures how rapidly a prioritized test suite detects all known faults: $\text{APFD} = 1 - \frac{TF_1 + \dots + TF_m}{n \cdot m} + \frac{1}{2n}$. High APFD $> 0.90$ provides rapid feedback to developers during continuous integration!</p>
</div>
"""

M5_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 75: Function Point Analysis General System Characteristics (GSC) Scoring</div>
  <p>The 14 GSCs evaluate environmental complexity (data comms, online update, reusability, installation ease). Each is rated 0 (no influence) to 5 (strong influence). The sum $\text{TDI} \in [0, 70]$ shifts the VAF multiplier between $0.65$ and $1.35$!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 76: Software Re-engineering Code Smells & Refactoring</div>
  <p>Identify common code smells: <strong>Long Method</strong> (refactor via Extract Method), <strong>Large Class</strong> (refactor via Extract Class), <strong>Feature Envy</strong> (refactor via Move Method), and <strong>Primitive Obsession</strong> (refactor to Value Objects)!</p>
</div>
"""

SE_REVISION_CROWN2 = SE_REVISION_MEGA_PASS + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 25: Complete Architectural Design Patterns</div>
  <ul>
    <li><strong>Creational:</strong> Singleton, Factory, Builder, Prototype.</li>
    <li><strong>Structural:</strong> Adapter, Decorator, Facade, Proxy.</li>
    <li><strong>Behavioral:</strong> Observer, Strategy, Command, State, Template Method.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 26: Complete Testing & Reliability Metrics</div>
  $$\text{Cyclomatic Complexity: } V(G) = E - N + 2P \qquad \text{Availability: } A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
  $$\text{Halstead Effort: } E = D \times V \qquad \text{COCOMO: } E = a(\text{KLOC})^b \times \text{EAF}$$
</div>
"""

SE_LAB_CROWN2 = SE_LAB_MEGA_PASS + r"""
<h2 class="section-title">Lab Experiment 7: Continuous Deployment (CD) with Docker & Kubernetes</h2>
<pre><code class="language-dockerfile">FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/banking-service-1.0.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
</code></pre>
"""

def execute_crown2():
    m1_full = M1_CONTENT + M1_MEGA + M1_ULTRA + M1_LOCK + M1_CROWN + M1_FINISH + M1_LOCK_PASS + M1_TRUE + M1_MEGA_PASS + M1_CROWN2
    m2_full = M2_CONTENT + M2_MEGA + M2_ULTRA + M2_LOCK + M2_CROWN + M2_FINISH + M2_LOCK_PASS + M2_TRUE + M2_MEGA_PASS + M2_CROWN2
    m3_full = M3_CONTENT + M3_MEGA + M3_ULTRA + M3_LOCK + M3_CROWN + M3_FINISH + M3_LOCK_PASS + M3_TRUE + M3_MEGA_PASS + M3_CROWN2
    m4_full = M4_CONTENT + M4_MEGA + M4_ULTRA + M4_LOCK + M4_CROWN + M4_FINISH + M4_LOCK_PASS + M4_TRUE + M4_MEGA_PASS + M4_CROWN2
    m5_full = M5_CONTENT + M5_MEGA + M5_ULTRA + M5_LOCK + M5_CROWN + M5_FINISH + M5_LOCK_PASS + M5_TRUE + M5_MEGA_PASS + M5_CROWN2

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
        SE_REVISION_CROWN2
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
        SE_LAB_CROWN2
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
    execute_crown2()
