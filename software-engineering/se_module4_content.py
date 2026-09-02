# Software Engineering Module 4 Exhaustive Content (16 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

SE_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Verification, Validation & Testing — Complete 16-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 40:</strong> Verification ("Are We Building the Product Right?")</div>
    <div><strong>Topic 41:</strong> Validation ("Are We Building the Right Product?")</div>
    <div><strong>Topic 42:</strong> V&V Planning & Test Strategy Life Cycle</div>
    <div><strong>Topic 43:</strong> Software Inspection (Fagan Formal Defect Reviews)</div>
    <div><strong>Topic 44:</strong> Static Analysis (Control Flow, Data Flow & Linters)</div>
    <div><strong>Topic 45:</strong> Software Testing Foundations & Defect Taxonomies</div>
    <div><strong>Topic 46:</strong> Testing Functions & Test Harness Design</div>
    <div><strong>Topic 47:</strong> Test Case Design (Formal Test Case Artifact Structure)</div>
    <div><strong>Topic 48:</strong> White-Box Testing (Statement & Branch Coverage)</div>
    <div><strong>Topic 49:</strong> Black-Box Testing (Equivalence Partitioning & BVA)</div>
    <div><strong>Topic 50:</strong> Basis Path Testing & McCabe's Cyclomatic Complexity</div>
    <div><strong>Topic 51:</strong> Control Structure Testing (Condition & Loop Testing)</div>
    <div><strong>Topic 52:</strong> Unit Testing (Stubs, Drivers & Test Doubles)</div>
    <div><strong>Topic 53:</strong> Integration Testing (Top-Down, Bottom-Up, Sandwich)</div>
    <div><strong>Topic 54:</strong> System Testing (Stress, Load, Recovery & Acceptance)</div>
    <div><strong>Topic 55:</strong> Software Reliability & Availability (MTBF, MTTF, MTTR)</div>
  </div>
</div>

<h2 class="section-title">Topic 40 – 44: Verification vs. Validation & Static Quality Techniques</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Parameter</th>
      <th style="width: 37%;">Verification (Static Quality Assurance)</th>
      <th>Validation (Dynamic Quality Control)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Boehm's Question</strong></td><td><strong>"Are we building the product right?"</strong></td><td><strong>"Are we building the right product?"</strong></td></tr>
    <tr><td><strong>Execution</strong></td><td>Static evaluation <em>without executing code</em> (Inspections, Walkthroughs, Linters).</td><td>Dynamic execution of software using actual test cases.</td></tr>
    <tr><td><strong>Target Evaluation</strong></td><td>Verifies whether design/code conforms to SRS specifications.</td><td>Validates whether the operational system satisfies actual user needs.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 48 & 49: White-Box vs. Black-Box Testing Methodologies</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">Black-Box Testing (Functional)</th>
      <th>White-Box Testing (Structural / Glass-Box)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Knowledge Needed</strong></td><td>Zero internal code knowledge; tests external inputs vs. expected outputs.</td><td>Full knowledge of source code logic, branches, loops, and data structures.</td></tr>
    <tr><td><strong>Primary Techniques</strong></td><td>• <strong>Equivalence Partitioning (EP):</strong> Divides inputs into valid/invalid equivalence classes.<br>• <strong>Boundary Value Analysis (BVA):</strong> Tests boundaries ($\text{min}, \text{min}+1, \text{nominal}, \text{max}-1, \text{max}$).</td><td>• Statement Coverage, Branch Coverage, Condition Coverage.<br>• <strong>Basis Path Testing</strong> via Control Flow Graphs (CFG).</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 50: Basis Path Testing & McCabe's Cyclomatic Complexity</h2>

<div class="formula-card">
  <strong>McCabe's Cyclomatic Complexity $V(G)$ Formulations (McCabe, 1976):</strong>
  1. From Edges ($E$) and Nodes ($N$): $\mathbf{V(G) = E - N + 2}$
  2. From Predicate / Decision Nodes ($P$): $\mathbf{V(G) = P + 1}$
  3. From Enclosed Regions ($R$): $\mathbf{V(G) = R}$
  <em>Significance:</em> $V(G)$ defines the exact number of linearly independent execution paths required to achieve $100\%$ branch coverage!
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Cyclomatic Complexity & Independent Paths</div>
  <pre><code>int find_max(int a, int b, int c) {
    int max = a;            // Node 1
    if (b > max)            // Node 2 (Predicate)
        max = b;            // Node 3
    if (c > max)            // Node 4 (Predicate)
        max = c;            // Node 5
    return max;             // Node 6
}</code></pre>
  <p><strong>Graph Analysis:</strong> Nodes $N = 6$, Edges $E = 7$, Predicates $P = 2$ (Nodes 2 and 4).</p>
  <p>$$V(G) = E - N + 2 = 7 - 6 + 2 = \mathbf{3} \quad (\text{or } P + 1 = 2 + 1 = \mathbf{3})$$</p>
  <p><strong>Set of 3 Linearly Independent Paths:</strong></p>
  <ul>
    <li><strong>Path 1:</strong> $1 \rightarrow 2 \rightarrow 4 \rightarrow 6$ (Test: $a=10, b=5, c=2$)</li>
    <li><strong>Path 2:</strong> $1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 6$ (Test: $a=5, b=10, c=2$)</li>
    <li><strong>Path 3:</strong> $1 \rightarrow 2 \rightarrow 4 \rightarrow 5 \rightarrow 6$ (Test: $a=5, b=2, c=10$)</li>
  </ul>
</div>

<h2 class="section-title">Topic 52 – 55: Levels of Testing & Software Reliability</h2>

<div class="formula-card">
  <strong>Software Reliability & Availability Formulas:</strong>
  $$\text{Mean Time Between Failures (MTBF)} = \text{Mean Time To Failure (MTTF)} + \text{Mean Time To Repair (MTTR)}$$
  $$\mathbf{\text{Availability } (A) = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}}}$$
</div>

<h2 class="section-title">🧠 M4 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain Top-Down vs. Bottom-Up Integration Testing. Define Stubs and Drivers with diagrams. (10 Marks)</div>
  <div class="qa-a">
    - <strong>Top-Down Integration:</strong> Modules are integrated from top to bottom of the control hierarchy. Subordinate modules not yet developed are simulated using <strong>Stubs</strong> (dummy subroutines called by the tested module).<br>
    - <strong>Bottom-Up Integration:</strong> Low-level worker modules are tested first. Superordinate modules not yet developed are simulated using <strong>Drivers</strong> (test harnesses that invoke the module and display results).<br>
    - <strong>Sandwich (Hybrid) Integration:</strong> Combines top-down for top layers and bottom-up for low-level utility libraries, minimizing stub/driver development overhead.
  </div>
</div>
"""
