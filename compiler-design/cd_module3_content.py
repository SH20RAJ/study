# Compiler Design Module 3 Exhaustive Content (9 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions

CD_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Semantic Analysis & Intermediate Code — Complete 9-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> Introduction to Semantic Analysis (Static vs Dynamic Checks)</div>
    <div><strong>Topic 2:</strong> Syntax-Directed Definitions (SDD Semantic Rules)</div>
    <div><strong>Topic 3:</strong> Syntax-Directed Translation Schemes (SDTS Actions)</div>
    <div><strong>Topic 4:</strong> SDTS for Declaration Processing & Symbol Tables</div>
    <div><strong>Topic 5:</strong> Three Address Code (Quadruples, Triples, Indirect Triples)</div>
    <div><strong>Topic 6:</strong> Types of Attributes (Synthesized vs. Inherited)</div>
    <div><strong>Topic 7:</strong> Type Checking for Expressions (Equivalence & Coercion)</div>
    <div><strong>Topic 8:</strong> Intermediate Code Generation for Assignment Statements</div>
    <div><strong>Topic 9:</strong> Translation of Multi-Dimensional Array References</div>
  </div>
</div>

<h2 class="section-title">Topic 1: Introduction to Semantic Analysis</h2>
<p>
  <strong>Semantic Analysis</strong> verifies that the syntax tree conforms to the semantic rules of the language. While syntax ensures correct grammatical structure, semantics verifies logical validity:
</p>
<ul>
  <li><strong>Static Semantic Checks (Compile-Time):</strong> Type consistency, variable declared before use, scope resolution, identifier uniqueness.</li>
  <li><strong>Dynamic Semantic Checks (Run-Time):</strong> Division by zero, array out-of-bounds, null pointer dereferencing.</li>
</ul>

<h2 class="section-title">Topic 2 – 4: SDD, SDTS & Declaration Processing</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">Syntax-Directed Definition (SDD)</th>
      <th>Syntax-Directed Translation Scheme (SDTS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Representation</strong></td>
      <td>Context-Free Grammar + Semantic Rules associated with productions.</td>
      <td>Context-Free Grammar with semantic action code embedded inside productions `{ ... }`.</td>
    </tr>
    <tr>
      <td><strong>Execution Timing</strong></td>
      <td>Specifies <em>what</em> value to compute (order determined by Dependency Graph topological sort).</td>
      <td>Specifies <em>when</em> and in what exact sequence actions execute during parsing.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step SDTS: Processing Declarations `int a, b, c;`</div>
  <pre><code>D -> T { L.in = T.type } L
T -> int { T.type = integer }
T -> float { T.type = real }
L -> { L1.in = L.in } L1, id { enter(id.name, L.in) }
L -> id { enter(id.name, L.in) }</code></pre>
  <p><em>Uses inherited attribute $L.\text{in}$ to propagate base type down to all declared identifier names.</em></p>
</div>

<h2 class="section-title">Topic 5: Three Address Code (TAC) Representations</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">TAC Form</th>
      <th style="width: 45%;">Internal Data Fields</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Quadruples</strong></td>
      <td>`(op, arg1, arg2, result)` with explicit temporary names (`t1`, `t2`).</td>
      <td>Easy to reorder and optimize; consumes extra memory for names.</td>
    </tr>
    <tr>
      <td><strong>2. Triples</strong></td>
      <td>`(op, arg1, arg2)` where intermediate results are referenced by index `(0)`.</td>
      <td>Space-efficient; moving instructions requires updating all dependent indices.</td>
    </tr>
    <tr>
      <td><strong>3. Indirect Triples</strong></td>
      <td>Array of pointers to separate triple structures.</td>
      <td>Optimizers reorder instructions by swapping array pointers without modifying triples.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 6 & 7: Types of Attributes & Type Checking</h2>

<h3 class="subsection-title">1. Synthesized vs. Inherited Attributes:</h3>
<ul>
  <li><strong>Synthesized Attributes:</strong> Computed strictly from children nodes in parse tree ($A.s = f(Y_1.a, \dots, Y_k.a)$). Evaluated bottom-up in LR parsing.</li>
  <li><strong>Inherited Attributes:</strong> Computed from parent and/or left sibling nodes ($Y_j.i = f(A.a, Y_1.a, \dots, Y_{j-1}.a)$). Evaluated top-down.</li>
</ul>

<h3 class="subsection-title">2. Type Conversions & Equivalence:</h3>
<ul>
  <li><strong>Name Equivalence:</strong> Two types are equal if and only if they share the exact same named identifier.</li>
  <li><strong>Structural Equivalence:</strong> Two types are equal if they have identical internal field layouts and primitive types.</li>
  <li><strong>Widening (Coercion):</strong> `int` $\rightarrow$ `float` (implicit precision preservation).</li>
  <li><strong>Narrowing (Casting):</strong> `float` $\rightarrow$ `int` (explicit potential precision loss).</li>
</ul>

<h2 class="section-title">Topic 8 & 9: Intermediate Code Generation for Arrays & Assignments</h2>

<div class="formula-card">
  <strong>1. 1D Array Reference Address Formula:</strong>
  $$\text{Address}(A[i]) = \text{base} + (i - \text{low}) \times w$$
</div>

<div class="formula-card">
  <strong>2. 2D Array Reference Address Formula (Row-Major Order):</strong>
  $$\text{Address}(A[i_1, i_2]) = \text{base} + \Big( (i_1 - \text{low}_1) \times n_2 + (i_2 - \text{low}_2) \Big) \times w$$
  Where $n_2 = \text{high}_2 - \text{low}_2 + 1$ is the number of columns, and $w$ is element byte width.
</div>

<div class="formula-card">
  <strong>3. General $N$-Dimensional Row-Major Linear Offset:</strong>
  $$\text{Offset} = \Big( \dots \big( (i_1 \cdot d_2 + i_2) \cdot d_3 + i_3 \big) \dots \Big) \cdot d_k + i_k$$
  $$\text{Address} = \text{base} + \text{Offset} \times w$$
</div>

<h2 class="section-title">🧠 M3 Active Recall & Exam-Important Question Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Write Quadruples and Triples for statement `a = b * - c + b * - c`. (8 Marks)</div>
  <div class="qa-a">
    <strong>Quadruples:</strong><br>
    (0) `uminus, c, -, t1`<br>
    (1) `*, b, t1, t2`<br>
    (2) `uminus, c, -, t3`<br>
    (3) `*, b, t3, t4`<br>
    (4) `+, t2, t4, t5`<br>
    (5) `=, t5, -, a`<br><br>
    <strong>Triples:</strong><br>
    (0) `uminus, c, -`<br>
    (1) `*, b, (0)`<br>
    (2) `uminus, c, -`<br>
    (3) `*, b, (2)`<br>
    (4) `+, (1), (3)`<br>
    (5) `assign, a, (4)`
  </div>
</div>
"""
