# Compiler Design Module 4 Exhaustive Content (12-14 Pages Target)

CD_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Intermediate Code Generation & Runtime Environments — Complete Topics</div>
  <div class="toc-grid">
    <div>1. Intermediate Representations (Syntax Trees, DAG, Postfix, TAC)</div>
    <div>2. Three-Address Code (TAC) Representations: Quadruples, Triples, Indirect Triples</div>
    <div>3. Translation of Expressions & Type Coercion TAC</div>
    <div>4. Multi-Dimensional Array Addressing (Row-Major vs Column-Major Proofs)</div>
    <div>5. Boolean Expressions Translation & Short-Circuit Evaluation</div>
    <div>6. Backpatching Techniques (`makelist`, `merge`, `backpatch`)</div>
    <div>7. Runtime Storage Organization & Activation Records (Stack Frames)</div>
    <div>8. Storage Allocation Strategies (Static, Stack, Heap)</div>
    <div>9. Access Links & Displays for Nested Block Scopes</div>
    <div>10. Parameter Passing Mechanisms & Garbage Collection</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Three-Address Code (TAC) Representations</h2>
<p>
  <strong>Three-Address Code (TAC)</strong> is a linear intermediate representation where each instruction has at most one operator on the right-hand side:
</p>
$$x = y \ \mathbf{op} \ z$$

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Representation</th>
      <th style="width: 45%;">Internal Data Structure & Fields</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Quadruples</strong></td>
      <td>Four fields: `(op, arg1, arg2, result)`. Explicit temporary names (e.g., `t1`, `t2`) are stored in `result`.</td>
      <td>Easy to reorder during code optimization; requires extra memory for temporary names.</td>
    </tr>
    <tr>
      <td><strong>2. Triples</strong></td>
      <td>Three fields: `(op, arg1, arg2)`. Results of operations are referred to by their instruction index position (e.g., `(0)`, `(1)`).</td>
      <td>Space efficient; moving or inserting instructions requires updating all index references.</td>
    </tr>
    <tr>
      <td><strong>3. Indirect Triples</strong></td>
      <td>Uses an array of pointers to separate triple structures.</td>
      <td>Optimizers can reorder instructions by simply swapping pointers in the array without touching the underlying triples.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Quadruples, Triples & Indirect Triples for `a = b * - c + b * - c`</div>
  <p><strong>Step 1: Generate Three-Address Code:</strong></p>
  <pre><code>(0) t1 = uminus c
(1) t2 = b * t1
(2) t3 = uminus c
(3) t4 = b * t3
(4) t5 = t2 + t4
(5) a = t5</code></pre>

  <p><strong>Step 2: Quadruple Representation:</strong></p>
  <table class="custom-table">
    <tr><th>#</th><th>op</th><th>arg1</th><th>arg2</th><th>result</th></tr>
    <tr><td>0</td><td>uminus</td><td>c</td><td>-</td><td>t1</td></tr>
    <tr><td>1</td><td>*</td><td>b</td><td>t1</td><td>t2</td></tr>
    <tr><td>2</td><td>uminus</td><td>c</td><td>-</td><td>t3</td></tr>
    <tr><td>3</td><td>*</td><td>b</td><td>t3</td><td>t4</td></tr>
    <tr><td>4</td><td>+</td><td>t2</td><td>t4</td><td>t5</td></tr>
    <tr><td>5</td><td>=</td><td>t5</td><td>-</td><td>a</td></tr>
  </table>

  <p><strong>Step 3: Triple Representation:</strong></p>
  <table class="custom-table">
    <tr><th>#</th><th>op</th><th>arg1</th><th>arg2</th></tr>
    <tr><td>(0)</td><td>uminus</td><td>c</td><td>-</td></tr>
    <tr><td>(1)</td><td>*</td><td>b</td><td>(0)</td></tr>
    <tr><td>(2)</td><td>uminus</td><td>c</td><td>-</td></tr>
    <tr><td>(3)</td><td>*</td><td>b</td><td>(2)</td></tr>
    <tr><td>(4)</td><td>+</td><td>(1)</td><td>(3)</td></tr>
    <tr><td>(5)</td><td>assign</td><td>a</td><td>(4)</td></tr>
  </table>
</div>



<h2 class="section-title">Topic 4: Multi-Dimensional Array Addressing Formulations</h2>

<div class="formula-card">
  <strong>1. 1D Array Address Formula:</strong>
  $$\text{Address}(A[i]) = \text{base} + (i - \text{low}) \times w$$
  Where $\text{base}$ is the start memory address, $\text{low}$ is lower index bound (typically 0 or 1), and $w$ is byte width per element.
</div>

<div class="formula-card">
  <strong>2. 2D Array Address Formula (Row-Major Order — C / C++ / Java):</strong>
  $$\text{Address}(A[i_1, i_2]) = \text{base} + \Big( (i_1 - \text{low}_1) \times n_2 + (i_2 - \text{low}_2) \Big) \times w$$
  Where $n_2 = \text{high}_2 - \text{low}_2 + 1$ is the number of elements in each row.
</div>

<div class="formula-card">
  <strong>3. 2D Array Address Formula (Column-Major Order — FORTRAN / MATLAB):</strong>
  $$\text{Address}(A[i_1, i_2]) = \text{base} + \Big( (i_2 - \text{low}_2) \times n_1 + (i_1 - \text{low}_1) \Big) \times w$$
  Where $n_1 = \text{high}_1 - \text{low}_1 + 1$ is the number of elements in each column.
</div>



<h2 class="section-title">Topic 5 & 6: Backpatching in Boolean Expressions</h2>

<p>
  <strong>Backpatching</strong> is a single-pass technique for generating intermediate code for control flow and boolean expressions without leaving unresolved forward jump target addresses.
</p>
<ul>
  <li><strong>`makelist(i)`:</strong> Creates a new list containing only jump instruction index $i$.</li>
  <li><strong>`merge(p1, p2)`:</strong> Concatenates two jump target lists $p_1$ and $p_2$.</li>
  <li><strong>`backpatch(p, i)`:</strong> Inserts target instruction label $i$ as the jump destination into all instructions indexed in list $p$.</li>
</ul>



<h2 class="section-title">Topics 7 – 9: Runtime Storage Organization & Activation Records</h2>

<p>
  During program execution, the operating system allocates a contiguous block of memory divided into 4 major logical segments:
</p>
<ol>
  <li><strong>Code Segment (Text):</strong> Read-only region holding compiled target machine instructions.</li>
  <li><strong>Static / Global Segment:</strong> Holds global variables, static constants, and compiler metadata fixed at compile time.</li>
  <li><strong>Call Stack:</strong> Grows downward dynamically; stores <strong>Activation Records (Stack Frames)</strong> for function invocations.</li>
  <li><strong>Heap:</strong> Grows upward dynamically; handles explicit dynamic memory allocation (`malloc`, `free`, `new`).</li>
</ol>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Activation Record Field</th>
      <th>Functional Purpose in Procedure Call / Return</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Actual Parameters</strong></td><td>Arguments passed by the caller to the callee.</td></tr>
    <tr><td><strong>Returned Values</strong></td><td>Space for return data passed back to caller.</td></tr>
    <tr><td><strong>Control Link (Dynamic Link)</strong></td><td>Points to caller's activation record; used to restore caller's stack frame on return.</td></tr>
    <tr><td><strong>Access Link (Static Link)</strong></td><td>Points to activation record of the statically enclosing lexical scope; used to access non-local variables.</td></tr>
    <tr><td><strong>Saved Machine Status</strong></td><td>Program counter (PC), CPU registers, and status flags saved before function call.</td></tr>
    <tr><td><strong>Local Data</strong></td><td>Local automatic variables allocated within the function.</td></tr>
    <tr><td><strong>Temporaries</strong></td><td>Temporary values generated during expression evaluation.</td></tr>
  </tbody>
</table>



<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module IV)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Compare Quadruples, Triples, and Indirect Triples with examples. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Quadruples:</strong> Explicit 4-field structures `(op, arg1, arg2, res)` where temporary names (`t1`) are explicitly stated. Highly flexible for compiler optimization reordering, but uses more memory.<br>
    2. <strong>Triples:</strong> 3-field structures `(op, arg1, arg2)` where intermediate results are referenced by instruction array indices `(0)`. Memory compact, but relocating code requires patching all dependent instruction references.<br>
    3. <strong>Indirect Triples:</strong> Stores pointers to triple structures in an array. Allows optimizers to reorder and eliminate code simply by modifying pointer positions without touching underlying triple records.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain Call-by-Value, Call-by-Reference, and Call-by-Name parameter passing. (6 Marks)</div>
  <div class="qa-a">
    - <strong>Call-by-Value:</strong> Actual parameter expression is evaluated and a local copy of the value is passed to the callee. Changes inside the function do not affect the caller's variable.<br>
    - <strong>Call-by-Reference:</strong> Memory address (pointer) of the actual parameter is passed. Any modification inside the function directly modifies caller's variable.<br>
    - <strong>Call-by-Name (Algol 60):</strong> The parameter is not evaluated upfront; instead, the parameter text is literally substituted into the function body (evaluated lazily via thunks every time it is referenced).
  </div>
</div>
"""
