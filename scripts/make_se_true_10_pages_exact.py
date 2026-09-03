#!/usr/bin/env python3
"""
True 10-12 Page Software Engineering (CS24353) Master Suite Compiler.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

SE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "software-engineering"))
HTML_DIR = os.path.join(SE_DIR, "html")
PDF_DIR = os.path.join(SE_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_se_master_suite import wrap_html, generate_pdf
from push_se_to_all_10_pages_final import (
    M1_CONTENT, M1_MEGA,
    M2_CONTENT, M2_MEGA,
    M3_CONTENT, M3_MEGA,
    M4_CONTENT, M4_MEGA,
    M5_CONTENT, M5_MEGA,
    SE_REVISION_MEGA, SE_LAB_GUIDE
)

# ----------------- MODULE 1 ULTRA EXPANSION -----------------
M1_ULTRA = r"""
<h2 class="section-title">Topic 15: Project Network Crashing & Cost-Time Tradeoff Analysis</h2>
<p>When a project must meet an accelerated statutory deadline, <strong>Project Crashing</strong> compresses activity durations by allocating additional engineering resources:</p>

<div class="formula-card">
  <div class="formula-title">📐 Activity Cost Slope Formula</div>
  $$\mathbf{\text{Cost Slope} = \frac{\text{Crash Cost } (C_c) - \text{Normal Cost } (C_n)}{\text{Normal Duration } (D_n) - \text{Crash Duration } (D_c)} = \frac{\Delta C}{\Delta D}}$$
  <p><strong>Rule of Optimal Crashing:</strong> Always crash the activity on the <em>Critical Path</em> that has the <strong>Lowest Cost Slope</strong>!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 11: Complete Critical Path Network Crashing</div>
  <p>Critical path consists of Activity A ($D_n = 5, D_c = 3, C_n = \$1000, C_c = \$1600$) and Activity B ($D_n = 8, D_c = 5, C_n = \$2000, C_c = \$3200$):</p>
  <ul>
    <li>$$\text{Cost Slope (A)} = \frac{1600 - 1000}{5 - 3} = \frac{600}{2} = \mathbf{\$300/\text{day}}$$</li>
    <li>$$\text{Cost Slope (B)} = \frac{3200 - 2000}{8 - 5} = \frac{1200}{3} = \mathbf{\$400/\text{day}}$$</li>
    <li>$$\mathbf{\text{To crash project by 2 days: Crash Activity A by 2 days at minimum extra cost } = 2 \times \$300 = \mathbf{\$600!}}}$$</li>
  </ul>
</div>

<h2 class="section-title">Topic 16: Boehm's Top 10 Software Risk Items & Mitigation Strategies</h2>
<table class="custom-table">
  <thead><tr><th>Rank</th><th>Software Risk Item</th><th>Standard Engineering Mitigation Strategy</th></tr></thead>
  <tbody>
    <tr><td><strong>1</strong></td><td>Personnel Shortfalls</td><td>Staff with top talent, job matching, cross-training, retention incentives.</td></tr>
    <tr><td><strong>2</strong></td><td>Unrealistic Schedules and Budgets</td><td>Detailed COCOMO/FP estimation, design-to-cost, incremental feature scoping.</td></tr>
    <tr><td><strong>3</strong></td><td>Developing Wrong Software Functions</td><td>Prototyping, user journey mapping, early user surveys, acceptance tests.</td></tr>
    <tr><td><strong>4</strong></td><td>Developing Wrong User Interface</td><td>Task analysis, prototyping, human factors interaction design, usability tests.</td></tr>
    <tr><td><strong>5</strong></td><td>Gold Plating (Unnecessary Complexity)</td><td>Requirements scrubbing, cost-benefit analysis, strict Change Control Board.</td></tr>
    <tr><td><strong>6</strong></td><td>Continuing Stream of Requirements Changes</td><td>High-change threshold baseline, information hiding, agile sprints.</td></tr>
    <tr><td><strong>7</strong></td><td>Shortfalls in Externally Furnished Components</td><td>Benchmarking, vendor audits, formal capability assessments.</td></tr>
    <tr><td><strong>8</strong></td><td>Shortfalls in Externally Performed Tasks</td><td>Pre-award audits, competitive team design, milestone inspections.</td></tr>
    <tr><td><strong>9</strong></td><td>Real-Time Performance Shortfalls</td><td>Simulation, high-speed prototyping, architectural instrumentation.</td></tr>
    <tr><td><strong>10</strong></td><td>Straining Computer Science Capabilities</td><td>Technical analysis, proof-of-concept prototyping, fallback algorithms.</td></tr>
  </tbody>
</table>
"""

# ----------------- MODULE 2 ULTRA EXPANSION -----------------
M2_ULTRA = r"""
<h2 class="section-title">Topic 27: Non-Functional Requirements (NFR) Framework & Softgoal Interdependency</h2>
<p>The <strong>Chung et al. NFR Framework</strong> models non-functional requirements as <strong>Softgoals</strong> that are "satisficed" rather than strictly satisfied:</p>
<ul>
  <li><strong>NFR Softgoal:</strong> Abstract quality target (e.g., `Security`, `High Throughput`).</li>
  <li><strong>Operationalization:</strong> Concrete design or architectural decision that contributes positively or negatively to the softgoal (e.g., `JWT Authentication`, `AES-256 Encryption`).</li>
  <li><strong>Interdependency Contribution Types:</strong>
    <ul>
      <li>`MAKE (++)`: Strongly positive contribution.</li>
      <li>`HELP (+)`: Moderately positive contribution.</li>
      <li>`HURT (-)`: Moderately negative contribution (e.g., Heavy Encryption <em>HURTS</em> Latency!).</li>
      <li>`BREAK (--)`: Catastrophic negative conflict.</li>
    </ul>
  </li>
</ul>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 12: Requirements Prioritization via Analytical Hierarchy Process (AHP)</div>
  <p>Compare 3 Requirements ($R_1, R_2, R_3$) in a Pairwise Comparison Matrix $\mathbf{A}$ where $R_1$ is $3\times$ more important than $R_2$, and $R_1$ is $6\times$ more important than $R_3$:</p>
  $$\mathbf{A} = \begin{bmatrix} 1 & 3 & 6 \\ 1/3 & 1 & 2 \\ 1/6 & 1/2 & 1 \end{bmatrix} \implies \text{Normalized Weight Vector } \mathbf{W} = \begin{bmatrix} \mathbf{0.667 \ (66.7\%)} \\ \mathbf{0.222 \ (22.2\%)} \\ \mathbf{0.111 \ (11.1\%)} \end{bmatrix}$$
  $$\mathbf{\text{Priority Order: } R_1 \text{ (Must-Have)} \gg R_2 \text{ (Should-Have)} \gg R_3 \text{ (Could-Have)}}$$
</div>
"""

# ----------------- MODULE 3 ULTRA EXPANSION -----------------
M3_ULTRA = r"""
<h2 class="section-title">Topic 41: Object Constraint Language (OCL) in UML Modeling</h2>
<p><strong>OCL</strong> is a formal declarative specification language used within UML class diagrams to specify precise mathematical constraints and business rules without implementation code:</p>

<pre><code class="language-text">-- Invariant: Bank Account balance cannot drop below overdraft limit
context BankAccount
inv: self.balance >= -self.overdraftLimit

-- Pre-condition and Post-condition on withdrawal operation
context BankAccount::withdraw(amount: Real): Boolean
pre: amount > 0 and (self.balance - amount >= -self.overdraftLimit)
post: self.balance = self.balance@pre - amount and result = true
</code></pre>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Architecture Case: Refactoring Legacy Code to Strategy Design Pattern</div>
  <p><strong>Problem:</strong> A monolithic billing class uses complex nested conditionals: `if (type == "CREDIT") chargeCredit(); else if (type == "PAYPAL") chargePayPal(); ...` (Violates Open/Closed Principle!).</p>
  <p><strong>Refactoring Solution:</strong></p>
  <ol>
    <li>Define common interface: `public interface PaymentStrategy { void pay(double amount); }`.</li>
    <li>Implement concrete classes: `CreditCardStrategy`, `PayPalStrategy`, `CryptoStrategy`.</li>
    <li>Context class `ShoppingCart` accepts `PaymentStrategy` via constructor, achieving $100\%$ decoupled extensibility!</li>
  </ol>
</div>
"""

# ----------------- MODULE 4 ULTRA EXPANSION -----------------
M4_ULTRA = r"""
<h2 class="section-title">Topic 49: Modified Condition / Decision Coverage (MC/DC) Truth Table Derivation</h2>
<p>In safety-critical avionics (DO-178C Level A), a complex decision $D = (A \lor B) \land C$ requires MC/DC test suite construction:</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 13: MC/DC Test Pair Construction ($N+1 = 4$ Test Cases)</div>
  <table class="custom-table">
    <thead><tr><th>Test #</th><th>Condition $A$</th><th>Condition $B$</th><th>Condition $C$</th><th>Decision Outcome $D$</th><th>Independent Effect Verified</th></tr></thead>
    <tbody>
      <tr><td><strong>T1</strong></td><td>True</td><td>False</td><td>True</td><td><strong>True</strong></td><td>Base True Case</td></tr>
      <tr><td><strong>T2</strong></td><td>False</td><td>False</td><td>True</td><td><strong>False</strong></td><td><strong>$A$ independently affects $D$</strong> (Compare T1 vs T2: only $A$ flips!)</td></tr>
      <tr><td><strong>T3</strong></td><td>False</td><td>True</td><td>True</td><td><strong>True</strong></td><td><strong>$B$ independently affects $D$</strong> (Compare T2 vs T3: only $B$ flips!)</td></tr>
      <tr><td><strong>T4</strong></td><td>True</td><td>False</td><td>False</td><td><strong>False</strong></td><td><strong>$C$ independently affects $D$</strong> (Compare T1 vs T4: only $C$ flips!)</td></tr>
    </tbody>
  </table>
  $$\mathbf{\text{Minimal MC/DC Test Suite: } \{T_1, T_2, T_3, T_4\} \quad (\text{Exactly } N+1 = 3+1 = 4 \text{ Test Cases!})}$$
</div>

<h2 class="section-title">Topic 50: Loop Testing Methodologies</h2>
<ul>
  <li><strong>Simple Loops ($n$ iterations):</strong> Test (1) Skip loop entirely ($0$), (2) Exactly 1 pass, (3) Exactly 2 passes, (4) Typical $m$ passes ($m < n$), (5) Boundary $n-1, n, n+1$ passes.</li>
  <li><strong>Nested Loops:</strong> Start at innermost loop with minimum outer values, test innermost loop, work outward, and finish with all loops at maximum iterations.</li>
</ul>
"""

# ----------------- MODULE 5 ULTRA EXPANSION -----------------
M5_ULTRA = r"""
<h2 class="section-title">Topic 57: COCOMO II 5 Scale Factors ($W_i$)</h2>
<p>In <strong>COCOMO II</strong>, project size diseconomy of scale is determined by 5 Scale Factors ($W_i$ rated 0 to 5):</p>
$$\mathbf{B = 0.91 + 0.01 \times \sum_{i=1}^5 W_i \qquad E = A \times (\text{KSLOC})^B \times \prod \text{EM}_i}$$
<table class="custom-table">
  <thead><tr><th>Scale Factor</th><th>Meaning</th><th>Impact on Exponent $B$</th></tr></thead>
  <tbody>
    <tr><td><strong>1. PREC (Precedentedness)</strong></td><td>Domain familiarity and team past project experience.</td><td>High experience lowers $B \rightarrow 0.91$ (Economy of scale).</td></tr>
    <tr><td><strong>2. FLEX (Development Flexibility)</strong></td><td>Relaxation of strict pre-defined requirement specs.</td><td>High flexibility lowers $B$.</td></tr>
    <tr><td><strong>3. RESL (Architecture / Risk Resolution)</strong></td><td>Percentage of risks resolved prior to development.</td><td>Early risk resolution lowers $B$.</td></tr>
    <tr><td><strong>4. TEAM (Team Cohesion)</strong></td><td>Team communication and shared vision.</td><td>High cohesion lowers $B$.</td></tr>
    <tr><td><strong>5. PMAT (Process Maturity)</strong></td><td>SEI CMMI Process maturity rating.</td><td>CMMI Level 5 drops $W_5 \rightarrow 0.0$.</td></tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 14: Defect Density & Phase Containment Effectiveness (PCE)</div>
  <p>In a $40 \text{ KLOC}$ system, 120 defects were detected during development inspections, and 30 defects were discovered in production:</p>
  $$\mathbf{\text{Defect Density} = \frac{\text{Total Defects}}{\text{Size in KLOC}} = \frac{120 + 30}{40} = \frac{150}{40} = \mathbf{3.75 \text{ Defects/KLOC}}}$$
  $$\mathbf{\text{Phase Containment Effectiveness (PCE)} = \frac{\text{In-Phase Defects}}{\text{In-Phase} + \text{Escaped Defects}} = \frac{120}{120 + 30} = \frac{120}{150} = \mathbf{0.80 = 80.0\%}}$$
</div>
"""

# ----------------- REVISION ULTRA EXPANSION -----------------
SE_REVISION_ULTRA = SE_REVISION_MEGA + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 9: Complete Software Metric Formulas</div>
  <ul>
    <li><strong>Halstead Volume:</strong> $V = (N_1 + N_2)\log_2(n_1 + n_2)$</li>
    <li><strong>Halstead Difficulty:</strong> $D = \frac{n_1}{2} \times \frac{N_2}{n_2}$</li>
    <li><strong>Halstead Effort:</strong> $E = D \times V$</li>
    <li><strong>Halstead Time:</strong> $T = E / 18 \text{ seconds}$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 10: Complete SCM Baseline Lifecycle</div>
  $$\text{Working Copy} \xrightarrow{\text{Commit}} \text{Repository} \xrightarrow{\text{Review/Audit}} \text{Approved Baseline} \xrightarrow{\text{CR/CCB}} \text{New Version}$$
</div>
"""

def execute_ultra_se():
    m1_full = M1_CONTENT + M1_MEGA + M1_ULTRA
    m2_full = M2_CONTENT + M2_MEGA + M2_ULTRA
    m3_full = M3_CONTENT + M3_MEGA + M3_ULTRA
    m4_full = M4_CONTENT + M4_MEGA + M4_ULTRA
    m5_full = M5_CONTENT + M5_MEGA + M5_ULTRA

    print("SE M1 Chars:", len(m1_full))
    print("SE M2 Chars:", len(m2_full))
    print("SE M3 Chars:", len(m3_full))
    print("SE M4 Chars:", len(m4_full))
    print("SE M5 Chars:", len(m5_full))

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
        SE_REVISION_ULTRA
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
        SE_LAB_GUIDE
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
    execute_ultra_se()
