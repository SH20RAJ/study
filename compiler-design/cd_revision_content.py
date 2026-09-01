# Compiler Design 10-Page Master Revision Exhaustive Content (CS24301)

CD_REVISION_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title">⚡ 10-Page Master Quick Revision — Compiler Design (CS24301)</div>
  <div class="toc-grid">
    <div>Page 1: 6 Compiler Phases & Running Translation Trace</div>
    <div>Page 2: Lexical Analysis, Thompson RE to NFA & Subset Construction</div>
    <div>Page 3: Hopcroft's DFA Minimization & Input Buffering Sentinels</div>
    <div>Page 4: CFG Transformations: Left Recursion & Left Factoring</div>
    <div>Page 5: FIRST & FOLLOW Formal Sets & LL(1) Table Construction</div>
    <div>Page 6: LR Parser Hierarchy: LR(0), SLR(1), CLR(1), LALR(1)</div>
    <div>Page 7: S-Attributed vs L-Attributed SDD & Dependency Graphs</div>
    <div>Page 8: Three-Address Code (Quadruples/Triples) & Array Addressing</div>
    <div>Page 9: Runtime Activation Records, Stack Frames & Scoping Links</div>
    <div>Page 10: Basic Blocks, CFG, DAG, Data-Flow Equations & BIT Mesra PYQs</div>
  </div>
</div>

<h2 class="section-title">⚡ Master Formula, Algorithm & Grammar Cheat Sheet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Topic / Concept</th>
      <th style="width: 45%;">Core Mathematical Formulation / Rule</th>
      <th>Key Exam Insight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Immediate Left Recursion</strong></td>
      <td>$$A \rightarrow A\alpha \mid \beta \implies A \rightarrow \beta A', \quad A' \rightarrow \alpha A' \mid \epsilon$$</td>
      <td>Eliminates infinite loops in top-down parsers.</td>
    </tr>
    <tr>
      <td><strong>Left Factoring</strong></td>
      <td>$$A \rightarrow \alpha \beta_1 \mid \alpha \beta_2 \implies A \rightarrow \alpha A', \quad A' \rightarrow \beta_1 \mid \beta_2$$</td>
      <td>Defers decision until lookahead is clear.</td>
    </tr>
    <tr>
      <td><strong>2D Array (Row-Major)</strong></td>
      <td>$$\text{Addr}(A[i_1, i_2]) = \text{base} + \Big( (i_1 - l_1)n_2 + (i_2 - l_2) \Big) \times w$$</td>
      <td>Standard in C / C++ / Java.</td>
    </tr>
    <tr>
      <td><strong>2D Array (Column-Major)</strong></td>
      <td>$$\text{Addr}(A[i_1, i_2]) = \text{base} + \Big( (i_2 - l_2)n_1 + (i_1 - l_1) \Big) \times w$$</td>
      <td>Standard in FORTRAN / MATLAB.</td>
    </tr>
    <tr>
      <td><strong>Reaching Definitions</strong></td>
      <td>$$\text{OUT}[B] = \text{GEN}[B] \cup (\text{IN}[B] \setminus \text{KILL}[B])$$</td>
      <td>Forward data-flow; confluence by $\cup$.</td>
    </tr>
    <tr>
      <td><strong>Available Expressions</strong></td>
      <td>$$\text{OUT}[B] = e\_\text{GEN}[B] \cup (\text{IN}[B] \setminus e\_\text{KILL}[B])$$</td>
      <td>Forward data-flow; confluence by $\cap$.</td>
    </tr>
    <tr>
      <td><strong>Live Variables</strong></td>
      <td>$$\text{IN}[B] = \text{USE}[B] \cup (\text{OUT}[B] \setminus \text{DEF}[B])$$</td>
      <td>Backward data-flow; confluence by $\cup$.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2 class="section-title">🔥 Top 10 High-Yield BIT Mesra Exam Questions & Answers</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Trace the 6 phases of a compiler for the statement `a = b + c * 50`. (10 Marks)</div>
  <div class="qa-a">
    1. <strong>Lexical:</strong> `id1 = id2 + id3 * 50`<br>
    2. <strong>Syntax:</strong> Parse tree with `*` subtree evaluated before `+`<br>
    3. <strong>Semantic:</strong> Type conversion `inttofloat(50)` injected<br>
    4. <strong>ICG (TAC):</strong> `t1 = inttofloat(50); t2 = id3 * t1; t3 = id2 + t2; id1 = t3`<br>
    5. <strong>Optimization:</strong> `t1 = id3 * 50.0; id1 = id2 + t1`<br>
    6. <strong>Code Gen:</strong> Emits target machine assembly with CPU registers.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Compare LL(1), SLR(1), CLR(1), and LALR(1) parsers. (8 Marks)</div>
  <div class="qa-a">
    - <strong>LL(1):</strong> Top-down predictive parser using 1 lookahead; cannot handle left recursive grammars.<br>
    - <strong>SLR(1):</strong> Simple LR bottom-up parser using LR(0) items; places reduce actions in $\text{FOLLOW}(A)$.<br>
    - <strong>CLR(1):</strong> Canonical LR parser using LR(1) items with specific lookaheads; largest number of states.<br>
    - <strong>LALR(1):</strong> Merges CLR(1) states having identical LR(0) cores; same number of states as SLR(1) with near CLR(1) power.
  </div>
</div>
"""
