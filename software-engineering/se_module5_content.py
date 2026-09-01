# Software Engineering Module 5 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

SE_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Software Testing Strategies, Quality Assurance & Maintenance</div>
  <div class="toc-grid">
    <div>1. Verification vs. Validation (Boehm: "Building product right" vs. "Building right product")</div>
    <div>2. Black-Box Testing: Equivalence Class Partitioning (ECP) & Boundary Value Analysis (BVA)</div>
    <div>3. White-Box (Structural) Testing: Control Flow Graphs (CFG) & Logic Path Coverage</div>
    <div>4. McCabe's Cyclomatic Complexity ($V(G) = E - N + 2P = P + 1$) & Independent Basis Paths</div>
    <div>5. Advanced Structural Coverage: Branch, Condition, Multiple Condition & MC/DC</div>
    <div>6. Testing Levels Hierarchy: Unit Testing (Stubs & Drivers), Integration & System Testing</div>
    <div>7. Integration Strategies: Big-Bang, Top-Down (Depth/Breadth-First) vs. Bottom-Up Sandwich</div>
    <div>8. Acceptance Testing (Alpha vs. Beta Testing) & Regression Testing Test-Suite Minimization</div>
    <div>9. Mutation Testing: Generating Mutants, Killed Mutants ($D$) & Mutation Score ($\text{MS}$)</div>
    <div>10. Software Quality Assurance: ISO 9126, McCall's Quality Factors & CMMI 5 Levels</div>
    <div>11. Software Maintenance: 4 Classical Categories (Corrective, Adaptive, Perfective, Preventive)</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 2: Black-Box (Functional) Testing Techniques</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Testing Method</th>
      <th style="width: 45%;">Test Case Derivation Principle</th>
      <th>Example for Input Range $[1, 100]$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Equivalence Class Partitioning (ECP)</strong></td>
      <td>Divides input domain into valid and invalid equivalence classes. One test case is selected to represent each class.</td>
      <td>• Valid Class: $[1, 100]$ (e.g., $50$)<br>• Invalid Class 1: $< 1$ (e.g., $-5$)<br>• Invalid Class 2: $> 100$ (e.g., $150$)</td>
    </tr>
    <tr>
      <td><strong>2. Boundary Value Analysis (BVA)</strong></td>
      <td>Selects test cases at the extreme boundaries and just inside/outside boundaries ($Min, Min+, Nom, Max-, Max$).</td>
      <td>Test values: $1$ (Min), $2$ (Min+), $50$ (Nom), $99$ (Max-), $100$ (Max), plus invalid boundaries $0$ and $101$.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 3 & 4: White-Box Testing & McCabe's Cyclomatic Complexity</h2>

<div class="formula-card">
  <strong>McCabe's Cyclomatic Complexity ($V(G)$) Formulas:</strong>
  Let $G$ be the Control Flow Graph of a program:
  1. <strong>Formula 1 (Edges & Nodes):</strong>
     $$V(G) = E - N + 2P$$
     Where $E$ is number of flow graph edges, $N$ is number of nodes, and $P$ is number of connected components ($P=1$ for single programs).
  2. <strong>Formula 2 (Predicate Nodes):</strong>
     $$V(G) = P + 1$$
     Where $P$ is the number of binary decision/conditional predicate nodes (`if`, `while`, `for`).
  3. <strong>Formula 3 (Enclosed Regions):</strong>
     $$V(G) = \text{Number of Enclosed Planar Regions} + 1 \text{ (Outer Region)}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Cyclomatic Complexity & Basis Paths Calculation</div>
  <p><strong>Code Snippet:</strong></p>
  <pre><code>1: if (a > 10) {
2:     if (b < 20)
3:         x = 1;
4:     else
5:         x = 2;
6: } else {
7:     x = 3;
8: }
9: return x;</code></pre>
  <ol>
    <li><strong>Predicate Nodes ($P$):</strong> Two conditional tests (Node 1: `a > 10`, Node 2: `b < 20`).</li>
    <li><strong>Cyclomatic Complexity:</strong> $V(G) = P + 1 = 2 + 1 = \mathbf{3}$.</li>
    <li><strong>3 Linearly Independent Basis Paths:</strong>
      - <em>Path 1:</em> $1 \rightarrow 6 \rightarrow 7 \rightarrow 9$ (Condition 1 is False).
      - <em>Path 2:</em> $1 \rightarrow 2 \rightarrow 3 \rightarrow 9$ (Condition 1 is True, Condition 2 is True).
      - <em>Path 3:</em> $1 \rightarrow 2 \rightarrow 5 \rightarrow 9$ (Condition 1 is True, Condition 2 is False).
    </li>
  </ol>
</div>

<h2 class="section-title">Topic 9: Mutation Testing & Quality Evaluation</h2>

<div class="formula-card">
  <strong>Mutation Score ($\text{MS}$) Formula:</strong>
  $$\text{Mutation Score } (\text{MS}) = \frac{D}{T - E} \times 100\%$$
  Where $T$ is total generated mutants, $D$ is number of killed (detected) mutants, and $E$ is number of equivalent mutants (mutants that have identical functional behavior to original program).
</div>

<h2 class="section-title">Topic 11: Software Maintenance Categories</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Maintenance Type</th>
      <th style="width: 45%;">Purpose & Triggering Factor</th>
      <th>Typical Effort Share</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Corrective</strong></td><td>Fixing residual latent software defects and bugs discovered in production.</td><td>$\approx 20\%$</td></tr>
    <tr><td><strong>2. Adaptive</strong></td><td>Modifying software to accommodate changes in external environment (new OS, hardware upgrade, legal regulations).</td><td>$\approx 25\%$</td></tr>
    <tr><td><strong>3. Perfective</strong></td><td>Enhancing software functionality, improving performance, and optimizing code maintainability based on user requests.</td><td>$\approx 50\%$ (Dominant)</td></tr>
    <tr><td><strong>4. Preventive</strong></td><td>Refactoring and restructuring code to forestall future potential failures (Software Re-engineering).</td><td>$\approx 5\%$</td></tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module V)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Compare Stubs and Drivers in Integration Testing with diagrams. (8 Marks)</div>
  <div class="qa-a">
    - <strong>Driver:</strong> A dummy calling program written to invoke and pass test data to the module under test. Used extensively in <strong>Bottom-Up Integration Testing</strong> where high-level parent control modules have not yet been developed.<br>
    - <strong>Stub:</strong> A dummy called subroutine that simulates the interface and returns dummy values for sub-modules invoked by the module under test. Used extensively in <strong>Top-Down Integration Testing</strong> where low-level worker modules have not yet been developed.
  </div>
</div>
"""
