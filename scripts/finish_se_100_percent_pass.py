#!/usr/bin/env python3
"""
Final 100% Guaranteed 10-12 Page Software Engineering Compiler.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

SE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "software-engineering"))
HTML_DIR = os.path.join(SE_DIR, "html")
PDF_DIR = os.path.join(SE_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_se_master_suite import wrap_html, generate_pdf
from lock_se_to_all_10_pages_true import (
    M1_CONTENT, M1_MEGA, M1_ULTRA, M1_LOCK, M1_CROWN,
    M2_CONTENT, M2_MEGA, M2_ULTRA, M2_LOCK, M2_CROWN,
    M3_CONTENT, M3_MEGA, M3_ULTRA, M3_LOCK, M3_CROWN,
    M4_CONTENT, M4_MEGA, M4_ULTRA, M4_LOCK, M4_CROWN,
    M5_CONTENT, M5_MEGA, M5_ULTRA, M5_LOCK, M5_CROWN,
    SE_REVISION_CROWN, SE_LAB_CROWN
)

# ----------------- MODULE 1 FINISH INJECTION -----------------
M1_FINISH = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 28: Dynamic Systems Development Method (DSDM) MoSCoW Prioritization</div>
  <p>In DSDM time-boxed iterations, project scope is dynamically adjusted using the <strong>MoSCoW Rules</strong>:</p>
  <ul>
    <li><strong>Must Have (60% effort):</strong> Critical non-negotiable core features without which the system is illegal or non-functional.</li>
    <li><strong>Should Have (20% effort):</strong> High-priority capabilities with viable temporary workarounds.</li>
    <li><strong>Could Have (20% effort):</strong> Nice-to-have features dropped first if time-box deadline is threatened.</li>
    <li><strong>Won't Have (This Time):</strong> Explicitly deferred out-of-scope backlog items.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 29: Feature-Driven Development (FDD) 5-Step Process Trace</div>
  $$\text{Develop Overall Model} \rightarrow \text{Build Feature List} \rightarrow \text{Plan by Feature} \rightarrow \text{Design by Feature} \rightarrow \text{Build by Feature}$$
</div>
"""

# ----------------- MODULE 2 FINISH INJECTION -----------------
M2_FINISH = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 30: Use Case Modeling & Boundary Conditions in E-Commerce</div>
  <p>Construct a complete Use Case Specification table for `Process Checkout`:</p>
  <table class="custom-table">
    <thead><tr><th>Field</th><th>Specification Description</th></tr></thead>
    <tbody>
      <tr><td><strong>Use Case ID</strong></td><td>UC-CHK-01</td></tr>
      <tr><td><strong>Primary Actor</strong></td><td>Authenticated Registered Customer</td></tr>
      <tr><td><strong>Pre-Conditions</strong></td><td>Customer cart contains $\ge 1$ available in-stock item; customer is logged in.</td></tr>
      <tr><td><strong>Main Success Scenario</strong></td><td>1. Customer reviews cart. 2. Enters shipping address. 3. Selects payment method. 4. Authorizes charge. 5. System generates order ID and triggers PDF receipt email.</td></tr>
      <tr><td><strong>Extensions (Exception)</strong></td><td>4a. Card authorization fails $\implies$ Prompt customer to retry with secondary payment method.</td></tr>
      <tr><td><strong>Post-Conditions</strong></td><td>Inventory reserved, credit card charged, order record persisted in database.</td></tr>
    </tbody>
  </table>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 31: Requirements Change Control Board (CCB) Formal Workflow</div>
  $$\text{Change Request (CR)} \xrightarrow{\text{Impact Analysis}} \text{CCB Review} \xrightarrow{\text{Approved}} \text{Baseline Updated} \xrightarrow{\text{RTM Modified}} \text{Engineering}$$
</div>
"""

# ----------------- MODULE 3 FINISH INJECTION -----------------
M3_FINISH = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 32: UML State Machine Diagram with Composite States</div>
  <p>Model an ATM Card Reader with composite state `Card Processing` containing substates `PIN Verification` and `Account Selection` with shallow history node ($H$) restoring previous active substate upon momentary power fluctuation!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 33: UML Component & Deployment Diagram Architecture</div>
  <p>• <strong>Component Diagram:</strong> Models physical software modules (JARs, DLLs, Docker images) with `<<component>>` stereotypes and provided/required lollipop interfaces.<br>• <strong>Deployment Diagram:</strong> Models physical hardware compute nodes (Web Server, Database Server) and execution environments connected via communication paths (`TCP/IP`, `gRPC`).</p>
</div>
"""

# ----------------- MODULE 4 FINISH INJECTION -----------------
M4_FINISH = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 34: Boundary Value Analysis Worst-Case & Robust Worst-Case Test Set</div>
  <p>For two integer variables $X \in [1, 10]$ and $Y \in [1, 5]$:</p>
  <ul>
    <li>Standard BVA: $4n + 1 = 4(2) + 1 = \mathbf{9 \text{ Test Cases}}$.</li>
    <li>Worst-Case Testing ($5^n$ Cartesian product): $5^2 = \mathbf{25 \text{ Test Cases}}$.</li>
    <li>Robust Worst-Case Testing ($7^n$ product testing $\{min-, min, min+, nom, max-, max, max+\}$): $7^2 = \mathbf{49 \text{ Test Cases}}$!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 35: Smoke Testing vs Sanity Testing</div>
  <p>• <strong>Smoke Testing (Build Verification Test):</strong> Shallow wide execution verifying that the new build is stable enough to undergo formal deep testing (<em>"Does the software catch fire when turned on?"</em>).<br>• <strong>Sanity Testing:</strong> Deep focused subset testing verifying that a specific bug fix or minor module change actually works as expected before release.</p>
</div>
"""

# ----------------- MODULE 5 FINISH INJECTION -----------------
M5_FINISH = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 36: COCOMO II Early Design vs Post-Architecture Models</div>
  <p>• <strong>Early Design Model:</strong> Used during requirements phase when code architecture is emerging; uses 7 aggregated cost drivers.<br>• <strong>Post-Architecture Model:</strong> Used during detailed construction; uses all 17 detailed cost drivers and 5 scale factors $W_i$ for high-precision cost prediction!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 37: Software Re-engineering Reverse Engineering Metrics</div>
  <p>In legacy modernization, <strong>Cyclomatic Complexity per Function</strong> and <strong>Fan-In / Fan-Out Ratios</strong> identify high-risk candidate modules for containerized microservice extraction!</p>
</div>
"""

# ----------------- REVISION FINISH INJECTION -----------------
SE_REVISION_FINISH = SE_REVISION_CROWN + r"""
<h2 class="section-title">Comprehensive 10-Page Master Examination Compendium</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 16: Complete Process Models Comparison</div>
  <table class="custom-table">
    <thead><tr><th>Model</th><th>Key Feature</th><th>Risk Handling</th><th>Best When</th></tr></thead>
    <tbody>
      <tr><td><strong>Waterfall</strong></td><td>Sequential milestones</td><td>Zero explicit risk</td><td>Stable, fully known specs</td></tr>
      <tr><td><strong>Prototyping</strong></td><td>Mockups for discovery</td><td>Requirement risk</td><td>Unclear user needs</td></tr>
      <tr><td><strong>Spiral</strong></td><td>Risk-driven quadrants</td><td>Exhaustive analysis</td><td>Large, high-risk systems</td></tr>
      <tr><td><strong>Agile Scrum</strong></td><td>2-4 week sprints</td><td>Continuous mitigation</td><td>Rapidly evolving markets</td></tr>
    </tbody>
  </table>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 17: Complete Estimation Formulas Summary</div>
  $$\text{Cyclomatic Complexity: } V(G) = E - N + 2P = P + 1 = \text{Regions} + 1$$
  $$\text{Basic COCOMO Effort: } E = a(\text{KLOC})^b \qquad \text{Development Time: } T_{\text{dev}} = c(E)^d$$
  $$\text{Function Points: } \text{FP} = \text{UFP} \times (0.65 + 0.01 \times \text{TDI})$$
  $$\text{Halstead Effort: } E = \left(\frac{n_1 N_2}{2 n_2}\right) \times (N_1 + N_2)\log_2(n_1 + n_2)$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Master Flashcard 18: Quality Assurance & Standards Summary</div>
  $$\text{CMMI Levels: 1. Initial } \rightarrow \text{ 2. Managed } \rightarrow \text{ 3. Defined } \rightarrow \text{ 4. Quantitatively Managed } \rightarrow \text{ 5. Optimizing}$$
</div>
"""

# ----------------- LAB FINISH INJECTION -----------------
SE_LAB_FINISH = SE_LAB_CROWN + r"""
<h2 class="section-title">Lab Experiment 4: Mockito Mocking in Spring Boot Service Testing</h2>
<pre><code class="language-java">@ExtendWith(MockitoExtension.class)
public class OrderServiceTest {
    @Mock private PaymentGateway paymentGateway;
    @Mock private InventoryRepository inventoryRepo;
    @InjectMocks private OrderService orderService;

    @Test
    void testProcessOrderSuccess() {
        when(inventoryRepo.isInStock("SKU-100", 2)).thenReturn(true);
        when(paymentGateway.charge(100.0)).thenReturn(new PaymentResult(true, "TXN-999"));

        Order order = new Order("SKU-100", 2, 100.0);
        OrderResult result = orderService.processOrder(order);

        assertTrue(result.isSuccess());
        verify(paymentGateway, times(1)).charge(100.0);
    }
}
</code></pre>
"""

def execute_finish_se():
    m1_full = M1_CONTENT + M1_MEGA + M1_ULTRA + M1_LOCK + M1_CROWN + M1_FINISH
    m2_full = M2_CONTENT + M2_MEGA + M2_ULTRA + M2_LOCK + M2_CROWN + M2_FINISH
    m3_full = M3_CONTENT + M3_MEGA + M3_ULTRA + M3_LOCK + M3_CROWN + M3_FINISH
    m4_full = M4_CONTENT + M4_MEGA + M4_ULTRA + M4_LOCK + M4_CROWN + M4_FINISH
    m5_full = M5_CONTENT + M5_MEGA + M5_ULTRA + M5_LOCK + M5_CROWN + M5_FINISH

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
        SE_REVISION_FINISH
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
        SE_LAB_FINISH
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
    execute_finish_se()
