# Compiler Design Module 3 Exhaustive Content (10-12 Pages Target)

CD_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Semantic Analysis & Type Checking — Complete Syllabus Topics</div>
  <div class="toc-grid">
    <div>1. Syntax-Directed Definitions (SDD) & Semantic Rules</div>
    <div>2. Synthesized Attributes vs. Inherited Attributes</div>
    <div>3. S-Attributed Definitions & Bottom-Up Evaluation</div>
    <div>4. L-Attributed Definitions & Top-Down Evaluation Orders</div>
    <div>5. Dependency Graphs & Topological Sorting for Attribute Evaluation</div>
    <div>6. Syntax-Directed Translation Schemes (SDTS) & Action Placement</div>
    <div>7. Static Type Checking & Type Systems</div>
    <div>8. Type Expressions, Type Equivalence (Structural vs Name)</div>
    <div>9. Type Conversions (Implicit Coercion vs Explicit Casting)</div>
    <div>10. Symbol Table Organizations (Hash Tables with Scope Chaining)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Syntax-Directed Definitions (SDD) & Attributes</h2>
<p>
  A <strong>Syntax-Directed Definition (SDD)</strong> is a context-free grammar together with attributes and semantic rules. Attributes are associated with grammar symbols, and rules are associated with productions.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Attribute Class</th>
      <th style="width: 45%;">Definition & Value Flow Direction</th>
      <th>Key Evaluation Properties</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Synthesized Attribute</strong></td>
      <td>Computed from the attribute values of the node's children in the parse tree (or lexical values).
        $$A.s = f(Y_1.a_1, Y_2.a_2, \dots, Y_k.a_k)$$
      </td>
      <td>Flows strictly <strong>Bottom-Up</strong>; naturally evaluated during LR parsing.</td>
    </tr>
    <tr>
      <td><strong>2. Inherited Attribute</strong></td>
      <td>Computed from the attribute values of the node's parent and/or siblings.
        $$Y_j.i = f(A.a, Y_1.a_1, \dots, Y_{j-1}.a_{j-1})$$
      </td>
      <td>Flows <strong>Top-Down</strong> and <strong>Left-to-Right</strong>; passes context (e.g., data type declarations) downward.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2 class="section-title">Topic 3 & 4: S-Attributed vs. L-Attributed SDD</h2>

<div class="callout callout-info">
  <div class="callout-title">Structural Classifications</div>
  <ul>
    <li><strong>S-Attributed SDD:</strong> An SDD that uses <strong>only synthesized attributes</strong>. Can be evaluated during bottom-up parsing (e.g., LR parser) by maintaining an attribute stack in parallel with the parse stack.</li>
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
      <tr><th>Production</th><th>Semantic Rule</th></tr>
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
  <p>Evaluates $(3 + 4) * 5\mathbf{n} \implies \mathbf{35}$ bottom-up in a single pass.</p>
</div>

<div class="page-break"></div>

<h2 class="section-title">Topic 7 & 8: Type Checking & Type Systems</h2>

<p>
  A <strong>Type Checker</strong> verifies that the type of a construct matches that expected by its context (e.g., the modulo operator `%` requires integer operands in C).
</p>

<h3 class="subsection-title">1. Structural vs. Name Equivalence:</h3>
<ul>
  <li><strong>Name Equivalence:</strong> Two types are equivalent if and only if they share the exact same type name identifier (Strict, fast to check).</li>
  <li><strong>Structural Equivalence:</strong> Two types are equivalent if they have identical internal structures (e.g., record fields with identical names and types in the same order).</li>
</ul>

<h3 class="subsection-title">2. Type Conversions:</h3>
<ul>
  <li><strong>Implicit Coercion:</strong> Automatically performed by compiler (e.g., widening an `int` to `float` during addition `2 + 3.5`).</li>
  <li><strong>Explicit Casting:</strong> Programmed explicitly by the developer (e.g., `(int) x`).</li>
</ul>

<div class="page-break"></div>

<h2 class="section-title">Topic 10: Symbol Table Organization</h2>

<p>
  The <strong>Symbol Table</strong> is a critical data structure containing record entries for every user-defined identifier in the source program, storing name, type, memory offset, scope level, and parameter signatures.
</p>

<div class="diagram-container">
  <svg width="100%" height="90" viewBox="0 0 740 90" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="15" width="160" height="60" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="100" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Global Scope Table</text>
    <text x="100" y="55" font-family="Fira Code" font-size="9.5" fill="#2563eb" text-anchor="middle">int x, float y</text>

    <path d="M 180 45 L 250 45" stroke="#0284c7" stroke-width="2"/>

    <rect x="260" y="15" width="180" height="60" rx="6" fill="#f0fdf4" stroke="#22c55e"/>
    <text x="350" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Function Scope Table</text>
    <text x="350" y="55" font-family="Fira Code" font-size="9.5" fill="#16a34a" text-anchor="middle">int a, int b, parent -> Global</text>

    <path d="M 440 45 L 510 45" stroke="#0284c7" stroke-width="2"/>

    <rect x="520" y="15" width="180" height="60" rx="6" fill="#fef3c7" stroke="#d97706"/>
    <text x="610" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">Block Scope Table</text>
    <text x="610" y="55" font-family="Fira Code" font-size="9.5" fill="#b45309" text-anchor="middle">int i, parent -> Func</text>
  </svg>
  <div class="diagram-caption">Figure 3.1: Hierarchical Block-Structured Scope Chaining</div>
</div>

<div class="page-break"></div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module III)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Differentiate between S-Attributed and L-Attributed SDD with syntax-directed rules. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>S-Attributed SDD:</strong> Uses only synthesized attributes. Can be evaluated during bottom-up parsing using an attribute stack without creating an explicit parse tree.<br>
    2. <strong>L-Attributed SDD:</strong> Allows both synthesized and inherited attributes, but inherited attributes of symbol $X_j$ in $A \rightarrow X_1 X_2 \dots X_n$ are restricted to depend only on attributes of parent $A$ and left siblings $X_1, \dots, X_{j-1}$. Can be evaluated in a single depth-first, left-to-right parse tree traversal.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. How is dynamic block scoping implemented in a symbol table? (6 Marks)</div>
  <div class="qa-a">
    Block scoping is implemented using a <strong>Stack of Hash Tables</strong> or a chained tree of symbol tables. When entering a new block `{`, a new empty hash table is created and pushed onto the scope stack, with a pointer pointing to its enclosing parent scope table. Symbol lookups search from the current top-of-stack table upwards along parent pointers. When exiting a block `}`, its table is popped and deallocated.
  </div>
</div>
"""
