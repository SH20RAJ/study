# Software Engineering Module 2 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

SE_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Requirements Engineering, Analysis Modeling & Structured Specification</div>
  <div class="toc-grid">
    <div>1. Requirements Engineering Process (Elicitation, Analysis, Specification, Validation)</div>
    <div>2. Functional Requirements vs. Non-Functional Requirements (FURPS+ Model)</div>
    <div>3. IEEE 830 Standard Format for Software Requirements Specification (SRS)</div>
    <div>4. Characteristics of High-Quality SRS Documents (Traceable, Unambiguous, Verifiable)</div>
    <div>5. Use Case Modeling: Actors, Use Cases, `<<include>>` vs. `<<extend>>` Relationships</div>
    <div>6. Structured Analysis: Data Flow Diagrams (DFD) — 4 Core Geometric Notations</div>
    <div>7. DFD Leveling Hierarchy: Context Diagram (Level 0), Level 1 & Level 2 Explosions</div>
    <div>8. DFD Balancing Invariants & Common Modeling Errors (Black Holes, Miracles, Gray Holes)</div>
    <div>9. Data Dictionary Architecture: BNF Metadata Syntax & Composite Data Elements</div>
    <div>10. Entity-Relationship (ER) Modeling: Entities, Attributes, Cardinalities & Keys</div>
    <div>11. Decision Tables & Structured English for Complex Business Logic Modeling</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 2 – 4: Requirements Engineering & The IEEE 830 SRS Standard</h2>

<p>
  A <strong>Software Requirements Specification (SRS)</strong> is a formal contract between the client and the development organization describing the complete functional behavior and operational constraints of the system.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">SRS Section (IEEE 830)</th>
      <th style="width: 45%;">Mandatory Content & Description</th>
      <th>Key Invariants & Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Introduction</strong></td>
      <td>Purpose of the system, project scope, definitions, acronyms, and references.</td>
      <td>Sets project boundary; prevents scope creep.</td>
    </tr>
    <tr>
      <td><strong>2. Overall Description</strong></td>
      <td>Product perspective, user classes, operating environment, design constraints, assumptions.</td>
      <td>Provides high-level context without dictating low-level implementation details.</td>
    </tr>
    <tr>
      <td><strong>3. Specific Requirements</strong></td>
      <td>Detailed Functional Requirements, External Interface Requirements (UI, HW, SW), Non-Functional Requirements (Performance, Security, Reliability).</td>
      <td>Must be 100% <strong>Unambiguous, Complete, Consistent, Verifiable (Testable), and Traceable</strong>.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 6 – 8: Data Flow Diagrams (DFD) & Balancing Rules</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">DFD Symbol</th>
      <th style="width: 25%;">DeMarco & Yourdon</th>
      <th style="width: 25%;">Gane & Sarson</th>
      <th>Functional Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Process</strong></td><td>Circle (Bubble)</td><td>Rounded Rectangle</td><td>Transforms input data flows into output data flows.</td></tr>
    <tr><td><strong>Data Flow</strong></td><td>Directed Arrow</td><td>Directed Arrow</td><td>Pipeline along which packets of data travel.</td></tr>
    <tr><td><strong>Data Store</strong></td><td>Two Parallel Lines</td><td>Open Rectangle</td><td>Repository of data at rest (files, DB tables).</td></tr>
    <tr><td><strong>External Entity</strong></td><td>Rectangle</td><td>Shaded Rectangle</td><td>Source or Sink of data outside system boundary.</td></tr>
  </tbody>
</table>

<div class="callout callout-warning">
  <div class="callout-title">DFD Balancing & Consistency Invariants</div>
  <ul>
    <li><strong>Conservation of Data:</strong> A process cannot output data that was not present in or computable from its input data.</li>
    <li><strong>Black Hole Error:</strong> A process that has inputs but zero outputs.</li>
    <li><strong>Miracle Error:</strong> A process that generates outputs with zero inputs.</li>
    <li><strong>Gray Hole Error:</strong> A process where outputs require data not supplied by its inputs.</li>
    <li><strong>Level Balancing:</strong> All input data flows and output data flows entering/leaving a parent process bubble in DFD Level $N$ must exactly match the external data flows in its child Level $N+1$ diagram.</li>
  </ul>
</div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module II)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Differentiate between `<<include>>` and `<<extend>>` relationships in Use Case Diagrams with examples. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>`<<include>>` (Mandatory Shared Behavior):</strong> The base use case unconditionally and explicitly invokes the included use case every single time it executes. Used to factor out common repeated subroutines.<br>
       <em>Example:</em> `Withdraw Cash` $\xrightarrow{<<include>>}$ `Authenticate User PIN`.<br>
    2. <strong>`<<extend>>` (Optional / Conditional Behavior):</strong> The extending use case executes only if a specific extension condition holds true at designated extension points in the base use case. The base use case is completely functional on its own without knowing about the extension.<br>
       <em>Example:</em> `Calculate Premium` $\xleftarrow{<<extend>>}$ `Apply Senior Citizen Discount` (only if $\text{age} \ge 60$).
  </div>
</div>
"""
