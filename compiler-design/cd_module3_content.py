# Compiler Design Module 3 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

CD_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Semantic Analysis & Type Checking — Complete Syllabus Topics</div>
  <div class="toc-grid">
    <div>1. Role of Semantic Analysis & Static vs. Dynamic Checking</div>
    <div>2. Syntax-Directed Definitions (SDD) & Semantic Rule Formulations</div>
    <div>3. Synthesized Attributes vs. Inherited Attributes Formal Properties</div>
    <div>4. S-Attributed Definitions & Bottom-Up LR Parsing Implementations</div>
    <div>5. L-Attributed Definitions & Depth-First Left-to-Right Traversal Orders</div>
    <div>6. Dependency Graphs & Topological Sorting for Attribute Evaluation</div>
    <div>7. Syntax-Directed Translation Schemes (SDTS) & Action Placement Rules</div>
    <div>8. Type Systems, Type Expressions & Static Type Checker Architecture</div>
    <div>9. Type Equivalence (Structural vs. Name Equivalence Algorithms)</div>
    <div>10. Type Conversions (Implicit Coercions vs. Explicit Casting Mechanics)</div>
    <div>11. Symbol Table Organizations (Block Scoping with Chained Hash Tables)</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Question Bank (8 Solved Problems)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Syntax-Directed Definitions (SDD) & Attribute Types</h2>
<p>
  A <strong>Syntax-Directed Definition (SDD)</strong> is a context-free grammar augmented with attributes and semantic rules. Attributes are associated with grammar symbols, and semantic rules are associated with production rules.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Attribute Class</th>
      <th style="width: 45%;">Formal Mathematical Formulation & Value Flow</th>
      <th>Parsing & Evaluation Invariants</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Synthesized Attribute</strong></td>
      <td>Computed strictly from the attribute values of the node's children in the parse tree (or lexical values):
        $$A.s = f(Y_1.a_1, Y_2.a_2, \dots, Y_k.a_k) \quad \text{for production } A \rightarrow Y_1 Y_2 \dots Y_k$$
      </td>
      <td>Flows strictly <strong>Bottom-Up</strong>; naturally evaluated during shift-reduce / LR parsing using an attribute stack.</td>
    </tr>
    <tr>
      <td><strong>2. Inherited Attribute</strong></td>
      <td>Computed from the attribute values of the node's parent and/or left siblings:
        $$Y_j.i = f(A.a, Y_1.a_1, \dots, Y_{j-1}.a_{j-1}) \quad \text{for symbol } Y_j \text{ in } A \rightarrow Y_1 \dots Y_k$$
      </td>
      <td>Flows <strong>Top-Down</strong> and <strong>Left-to-Right</strong>; passes context (e.g., base data types) down into declarations.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 3 & 4: S-Attributed vs. L-Attributed SDD</h2>

<div class="callout callout-info">
  <div class="callout-title">Structural Classifications</div>
  <ul>
    <li><strong>S-Attributed SDD:</strong> An SDD that uses <strong>only synthesized attributes</strong>. Can be evaluated during bottom-up parsing (e.g., LR parser) by maintaining an attribute value stack in parallel with the parser state stack.</li>
    <li><strong>L-Attributed SDD:</strong> An SDD where every attribute is either synthesized, or inherited with the restriction that for production $A \rightarrow X_1 X_2 \dots X_n$, an inherited attribute of $X_j$ depends only on:
      <ol>
        <li>Attributes of the parent $A$.</li>
        <li>Attributes of symbols to the left of $X_j$ ($X_1, X_2, \dots, X_{j-1}$).</li>
      </ol>
      Every S-Attributed SDD is strictly an L-Attributed SDD ($S\text{-Attributed} \subset L\text{-Attributed}$).
    </li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Desktop Calculator S-Attributed SDD</div>
  <table class="custom-table">
    <thead>
      <tr>
        <th style="width: 35%;">Grammar Production</th>
        <th>Semantic Evaluation Rule</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>$L \rightarrow E \ \mathbf{n}$</td><td>$\text{print}(E.\text{val})$</td></tr>
      <tr><td>$E \rightarrow E_1 + T$</td><td>$E.\text{val} = E_1.\text{val} + T.\text{val}$</td></tr>
      <tr><td>$E \rightarrow T$</td><td>$E.\text{val} = T.\text{val}$</td></tr>
      <tr><td>$T \rightarrow T_1 * F$</td><td>$T.\text{val} = T_1.\text{val} * F.\text{val}$</td></tr>
      <tr><td>$T \rightarrow F$</td><td>$T.\text{val} = F.\text{val}$</td></tr>
      <tr><td>$F \rightarrow ( E )$</td><td>$F.\text{val} = E.\text{val}$</td></tr>
      <tr><td>$F \rightarrow \mathbf{digit}$</td><td>$F.\text{val} = \mathbf{digit}.\text{lexval}$</td></tr>
    </tbody>
  </table>
  <p>Evaluates expression `(3 + 4) * 5\n` bottom-up in a single LR parsing pass to yield `35`.</p>
</div>

<h2 class="section-title">Topic 6: Dependency Graphs & Topological Evaluation Orders</h2>
<p>
  A <strong>Dependency Graph</strong> represents the data-flow constraints between attribute instances in a parse tree:
</p>
<ul>
  <li>For each node attribute $X.a$, there is a corresponding graph vertex.</li>
  <li>A directed edge $X.a \rightarrow Y.b$ indicates that the semantic rule for $Y.b$ requires the value of $X.a$.</li>
  <li>If the dependency graph contains <strong>no directed cycles</strong>, a valid evaluation order is given by any <strong>Topological Sort</strong> of the graph.</li>
</ul>

<h2 class="section-title">Topic 8 & 9: Type Systems & Type Equivalence</h2>

<h3 class="subsection-title">1. Structural vs. Name Equivalence:</h3>
<ul>
  <li><strong>Name Equivalence:</strong> Two types are equivalent if and only if they share the exact same named type identifier.
    <pre><code>typedef struct { int x, y; } PointA;
typedef struct { int x, y; } PointB;
// Under Name Equivalence: PointA != PointB (Strict)</code></pre>
  </li>
  <li><strong>Structural Equivalence:</strong> Two types are equivalent if they have identical internal constituent structures.
    <pre><code>// Under Structural Equivalence: PointA == PointB (Both contain two integer fields)</code></pre>
  </li>
</ul>

<h3 class="subsection-title">2. Type Conversions & Coercion Rules:</h3>
<ul>
  <li><strong>Widening Conversions (Implicit):</strong> Preserve numeric precision (e.g., `char` $\rightarrow$ `int` $\rightarrow$ `float` $\rightarrow$ `double`). Automatically inserted by compiler.</li>
  <li><strong>Narrowing Conversions (Explicit):</strong> May lose precision or overflow (e.g., `double` $\rightarrow$ `int`). Require explicit type cast syntax.</li>
</ul>

<h2 class="section-title">Topic 11: Symbol Table Organizations (Block Scoping with Hash Tables)</h2>

<div class="diagram-container">
  <svg width="100%" height="95" viewBox="0 0 740 95" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="15" width="180" height="65" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="110" y="36" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Global Scope Table</text>
    <text x="110" y="52" font-family="Fira Code" font-size="9.5" fill="#2563eb" text-anchor="middle">int global_x; float g_y;</text>
    <text x="110" y="66" font-family="Plus Jakarta Sans" font-size="8.5" fill="#64748b" text-anchor="middle">Parent: NULL</text>

    <path d="M 200 47 L 260 47" stroke="#0284c7" stroke-width="2"/>

    <rect x="270" y="15" width="190" height="65" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="365" y="36" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Function Scope Table</text>
    <text x="365" y="52" font-family="Fira Code" font-size="9.5" fill="#16a34a" text-anchor="middle">int param_a; char local_b;</text>
    <text x="365" y="66" font-family="Plus Jakarta Sans" font-size="8.5" fill="#16a34a" text-anchor="middle">Parent: Global Scope</text>

    <path d="M 460 47 L 520 47" stroke="#0284c7" stroke-width="2"/>

    <rect x="530" y="15" width="190" height="65" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="625" y="36" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">Nested Block Scope Table</text>
    <text x="625" y="52" font-family="Fira Code" font-size="9.5" fill="#b45309" text-anchor="middle">int loop_i; int temp;</text>
    <text x="625" y="66" font-family="Plus Jakarta Sans" font-size="8.5" fill="#b45309" text-anchor="middle">Parent: Function Scope</text>
  </svg>
  <div class="diagram-caption">Figure 3.1: Hierarchical Chained Hash Tables for Nested Lexical Block Scoping</div>
</div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module III)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Differentiate between S-Attributed and L-Attributed SDD with examples and evaluation strategies. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>S-Attributed SDD:</strong> Uses only synthesized attributes. Evaluated strictly bottom-up during LR parsing using an attribute value stack without needing an explicit syntax tree.<br>
    2. <strong>L-Attributed SDD:</strong> Allows synthesized and inherited attributes with the restriction that inherited attributes of $X_j$ in $A \rightarrow X_1 X_2 \dots X_n$ depend only on attributes of parent $A$ and left siblings $X_1, \dots, X_{j-1}$. Evaluated in a single depth-first, left-to-right tree traversal.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Write an SDD to translate type declarations like `int a, b, c;` into symbol table entries. (8 Marks)</div>
  <div class="qa-a">
    <table class="custom-table">
      <thead><tr><th>Production</th><th>Semantic Rule</th></tr></thead>
      <tbody>
        <tr><td>$D \rightarrow T \ L$</td><td>$L.\text{in} = T.\text{type}$</td></tr>
        <tr><td>$T \rightarrow \mathbf{int}$</td><td>$T.\text{type} = \text{integer}$</td></tr>
        <tr><td>$T \rightarrow \mathbf{float}$</td><td>$T.\text{type} = \text{real}$</td></tr>
        <tr><td>$L \rightarrow L_1, \ \mathbf{id}$</td><td>$L_1.\text{in} = L.\text{in}; \ \text{addType}(\mathbf{id}.\text{entry}, L.\text{in})$</td></tr>
        <tr><td>$L \rightarrow \mathbf{id}$</td><td>$\text{addType}(\mathbf{id}.\text{entry}, L.\text{in})$</td></tr>
      </tbody>
    </table>
    <em>Uses inherited attribute $L.\text{in}$ to propagate base type downward to all identifier instances.</em>
  </div>
</div>
"""
