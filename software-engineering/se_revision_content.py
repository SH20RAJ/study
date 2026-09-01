# Software Engineering 10-Page Master Revision Exhaustive Content (CS24309)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

SE_REVISION_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title">⚡ 10-Page Master Quick Revision — Software Engineering (CS24309)</div>
  <div class="toc-grid">
    <div>Page 1: Process Models: Waterfall, V-Model, Prototyping & Spiral 4 Quadrants</div>
    <div>Page 2: Agile & Scrum: Roles, Ceremonies, Artifacts & Burndown Metrics</div>
    <div>Page 3: Requirements Engineering: IEEE 830 SRS Standard & DFD Leveling Rules</div>
    <div>Page 4: Software Design: Cohesion & Coupling Hierarchies (Best to Worst)</div>
    <div>Page 5: Object-Oriented Principles: SOLID Architecture & GoF Design Patterns</div>
    <div>Page 6: Software Metrics: Albrecht Function Points (FP) Domain Weights</div>
    <div>Page 7: Boehm's COCOMO I: Organic, Semi-Detached & Embedded Cost Equations</div>
    <div>Page 8: Project Scheduling: PERT 3-Point Estimate ($T_e$) & CPM Float Calculation</div>
    <div>Page 9: Software Testing: Equivalence Partitioning, BVA & Cyclomatic Complexity ($V(G)$)</div>
    <div>Page 10: Integration Testing: Stubs vs. Drivers, Mutation Score & 4 Maintenance Types</div>
  </div>
</div>

<h2 class="section-title">⚡ Master Formula, Estimation & Metric Cheat Sheet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Metric / Model</th>
      <th style="width: 45%;">Core Mathematical Formulation / Rule</th>
      <th>Key Exam Takeaway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Function Point (FP)</strong></td>
      <td>$$\text{FP} = \text{UFC} \times \left(0.65 + 0.01 \times \sum_{i=1}^{14} F_i\right)$$</td>
      <td>Independent of programming language; measures functionality from user perspective.</td>
    </tr>
    <tr>
      <td><strong>Basic COCOMO Effort</strong></td>
      <td>$$E = a \cdot (\text{KLOC})^b, \quad T_{\text{dev}} = c \cdot (E)^d$$</td>
      <td>Organic ($a=2.4, b=1.05$), Semi-Detached ($a=3.0, b=1.12$), Embedded ($a=3.6, b=1.20$).</td>
    </tr>
    <tr>
      <td><strong>PERT Expected Duration</strong></td>
      <td>$$T_e = \frac{a + 4m + b}{6}, \quad \sigma^2 = \left(\frac{b - a}{6}\right)^2$$</td>
      <td>Weights most likely estimate ($m$) 4 times higher than optimistic ($a$) and pessimistic ($b$).</td>
    </tr>
    <tr>
      <td><strong>Cyclomatic Complexity</strong></td>
      <td>$$V(G) = E - N + 2P = P + 1 = \text{Enclosed Regions} + 1$$</td>
      <td>Specifies upper bound on number of test cases needed for branch coverage.</td>
    </tr>
    <tr>
      <td><strong>Mutation Score ($\text{MS}$)</strong></td>
      <td>$$\text{MS} = \frac{D}{T - E} \times 100\%$$</td>
      <td>Measures test suite adequacy; $D$ is killed mutants, $E$ is equivalent mutants.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🔥 Top 10 High-Yield BIT Mesra Exam Questions & Solutions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Given a program with 14 edges and 10 nodes, compute its McCabe's Cyclomatic Complexity and state its significance. (6 Marks)</div>
  <div class="qa-a">
    $$V(G) = E - N + 2P = 14 - 10 + 2(1) = \mathbf{6}$$
    <strong>Significance:</strong> The program contains exactly 6 linearly independent execution paths. A minimum of 6 distinct test cases is mathematically necessary and sufficient to guarantee 100% basis path (branch) test coverage.
  </div>
</div>
"""
