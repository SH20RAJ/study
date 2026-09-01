# Compiler Design Module 5 Exhaustive Content (12-14 Pages Target)

CD_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Code Optimization & Target Code Generation — Complete Syllabus Topics</div>
  <div class="toc-grid">
    <div>1. Principal Sources of Optimization (Machine-Independent)</div>
    <div>2. Basic Blocks Partitioning Algorithm & Control Flow Graphs (CFG)</div>
    <div>3. Directed Acyclic Graphs (DAG) Representation for Basic Blocks</div>
    <div>4. Local vs. Global Code Optimization Techniques</div>
    <div>5. Loop Optimizations (Loop Invariant Code Motion, Strength Reduction, Unrolling)</div>
    <div>6. Dominators, Natural Loops & Reducible Flow Graphs</div>
    <div>7. Data-Flow Analysis Equations (Reaching Definitions & Available Expressions)</div>
    <div>8. Live Variable Analysis & Dead Code Elimination</div>
    <div>9. Target Code Generation Issues & Register Allocation by Graph Coloring</div>
    <div>10. Peephole Optimization Techniques (Redundant Load/Store, Algebraic Identities)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 4: Principal Sources of Code Optimization</h2>
<p>
  Code optimization transforms intermediate or target code to run faster, consume less memory, or use less power, while strictly preserving program semantics.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Optimization Technique</th>
      <th style="width: 45%;">Mechanisms & Transformations</th>
      <th>Before $\rightarrow$ After Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Constant Folding</strong></td>
      <td>Evaluating operations on compile-time constants upfront.</td>
      <td>`x = 3 + 4 * 2` $\rightarrow$ `x = 11`</td>
    </tr>
    <tr>
      <td><strong>2. Constant Propagation</strong></td>
      <td>Replacing variables holding known constant values with the constant.</td>
      <td>`pi = 3.14; r = 2; area = pi * r * r` $\rightarrow$ `area = 3.14 * 2 * 2`</td>
    </tr>
    <tr>
      <td><strong>3. Common Subexpression Elimination</strong></td>
      <td>Reusing previously computed values instead of re-evaluating identical expressions.</td>
      <td>`t1 = a + b; ... ; t2 = a + b` $\rightarrow$ `t2 = t1`</td>
    </tr>
    <tr>
      <td><strong>4. Dead Code Elimination</strong></td>
      <td>Removing instructions whose results are never read by subsequent code or unreachable blocks.</td>
      <td>`if (0) { do_something(); }` $\rightarrow$ `/* Removed */`</td>
    </tr>
    <tr>
      <td><strong>5. Strength Reduction</strong></td>
      <td>Replacing expensive operations (e.g., multiplication) with cheaper equivalents (addition, bit-shift).</td>
      <td>`x = y * 8` $\rightarrow$ `x = y << 3`</td>
    </tr>
    <tr>
      <td><strong>6. Loop Invariant Code Motion</strong></td>
      <td>Hoisting computations that evaluate to the same value in every loop iteration outside the loop header.</td>
      <td>`while (i < n) { x = a + b; i++; }` $\rightarrow$ `x = a + b; while (i < n) { i++; }`</td>
    </tr>
  </tbody>
</table>



<h2 class="section-title">Topic 2: Basic Blocks & Control Flow Graphs (CFG)</h2>

<div class="callout callout-info">
  <div class="callout-title">Algorithm: Partitioning Three-Address Code into Basic Blocks</div>
  <p><strong>Step 1: Identify the Leaders (first instructions of basic blocks):</strong></p>
  <ol>
    <li>The first Three-Address instruction of the intermediate code is a Leader.</li>
    <li>Any instruction that is the target of a conditional or unconditional jump (`goto L`) is a Leader.</li>
    <li>Any instruction that immediately follows a conditional or unconditional jump is a Leader.</li>
  </ol>
  <p><strong>Step 2: Construct Basic Blocks:</strong></p>
  <p>For each Leader, its Basic Block consists of the Leader and all subsequent instructions up to, but not including, the next Leader or the end of the program.</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Basic Block Partitioning on Dot Product Code</div>
  <p><strong>Three-Address Code:</strong></p>
  <pre><code>(1)  prod = 0          <-- Leader (Rule 1: First instruction)
(2)  i = 1
(3)  t1 = 4 * i        <-- Leader (Rule 2: Target of goto (3) in line 9)
(4)  t2 = a[t1]
(5)  t3 = 4 * i
(6)  t4 = b[t3]
(7)  t5 = t2 * t4
(8)  prod = prod + t5
(9)  i = i + 1
(10) if i <= 20 goto (3)
(11) print(prod)       <-- Leader (Rule 3: Follows conditional jump at line 10)</code></pre>
  <p><strong>Resulting Basic Blocks:</strong></p>
  <ul>
    <li><strong>Block $B_1$:</strong> Instructions (1) to (2).</li>
    <li><strong>Block $B_2$ (Loop Body):</strong> Instructions (3) to (10).</li>
    <li><strong>Block $B_3$:</strong> Instruction (11).</li>
  </ul>
</div>



<h2 class="section-title">Topic 3: Directed Acyclic Graphs (DAG) for Basic Blocks</h2>

<p>
  A <strong>DAG (Directed Acyclic Graph)</strong> is an efficient representation for basic blocks that makes local common subexpression elimination, dead code elimination, and array dependency tracking straightforward:
</p>
<ul>
  <li>Leaves correspond to initial values of variables or constants.</li>
  <li>Interior nodes correspond to operators.</li>
  <li>Nodes have labels attached showing current identifier names having that computed value.</li>
</ul>



<h2 class="section-title">Topic 7 & 8: Data-Flow Analysis Frameworks</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Framework</th>
      <th style="width: 45%;">Data-Flow Transfer Equations</th>
      <th>Direction & Confluence Operator</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Reaching Definitions</strong></td>
      <td>$$\text{OUT}[B] = \text{GEN}[B] \cup (\text{IN}[B] \setminus \text{KILL}[B])$$
          $$\text{IN}[B] = \bigcup_{P \in \text{Pred}(B)} \text{OUT}[P]$$</td>
      <td>Forward Data-Flow; Union ($\cup$) confluence.</td>
    </tr>
    <tr>
      <td><strong>2. Available Expressions</strong></td>
      <td>$$\text{OUT}[B] = e\_\text{GEN}[B] \cup (\text{IN}[B] \setminus e\_\text{KILL}[B])$$
          $$\text{IN}[B] = \bigcap_{P \in \text{Pred}(B)} \text{OUT}[P]$$</td>
      <td>Forward Data-Flow; Intersection ($\cap$) confluence.</td>
    </tr>
    <tr>
      <td><strong>3. Live Variable Analysis</strong></td>
      <td>$$\text{IN}[B] = \text{USE}[B] \cup (\text{OUT}[B] \setminus \text{DEF}[B])$$
          $$\text{OUT}[B] = \bigcup_{S \in \text{Succ}(B)} \text{IN}[S]$$</td>
      <td>Backward Data-Flow; Union ($\cup$) confluence.</td>
    </tr>
  </tbody>
</table>



<h2 class="section-title">Topic 9 & 10: Target Code Generation & Peephole Optimization</h2>

<h3 class="subsection-title">1. Register Allocation by Graph Coloring (Chaitin's Algorithm):</h3>
<ol>
  <li>Construct the <strong>Interference Graph</strong> where nodes represent variables/temporaries and edges connect variables that are simultaneously live at the same program point.</li>
  <li>Find a $K$-coloring of the graph, where $K$ is the number of available physical hardware CPU registers. If successful, no two interfering variables share the same register.</li>
  <li>If the graph cannot be $K$-colored, select candidate variables to <strong>spill</strong> into RAM stack slots.</li>
</ol>

<h3 class="subsection-title">2. Peephole Optimization:</h3>
<p>
  A local optimization method that examines a short slide window of target assembly instructions ("peephole") and applies immediate algebraic and redundant instruction eliminations:
</p>
<ul>
  <li><strong>Eliminating Redundant Loads and Stores:</strong>
    <pre><code>MOV R0, a
MOV a, R0     ; Redundant - Eliminated!</code></pre>
  </li>
  <li><strong>Eliminating Unreachable Code:</strong> Instructions immediately following an unconditional jump without a label are deleted.</li>
  <li><strong>Algebraic Simplifications:</strong> Replacing $x + 0 \rightarrow x$, $x * 1 \rightarrow x$, $x * 0 \rightarrow 0$.</li>
</ul>



<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module V)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. State the algorithm to identify Basic Blocks and construct a Control Flow Graph. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Identify Leaders:</strong> (i) First instruction of program, (ii) Target of any jump (`goto`), (iii) Instruction immediately following any jump.<br>
    2. <strong>Construct Blocks:</strong> For each leader, its basic block consists of all instructions up to the next leader or program end.<br>
    3. <strong>Build Control Flow Graph (CFG):</strong> Nodes are the basic blocks. Directed edges $B_i \rightarrow B_j$ exist if control can transfer from $B_i$ to $B_j$ (via conditional/unconditional jump or sequential fall-through).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain Loop Invariant Code Motion and Strength Reduction with code examples. (8 Marks)</div>
  <div class="qa-a">
    - <strong>Loop Invariant Code Motion:</strong> Moves computations whose operand values do not change across loop iterations outside the loop header.<br>
      <em>Example:</em> `for (int i=0; i<n; i++) { a = x + y; b[i] = a * i; }` $\rightarrow$ `a = x + y; for (int i=0; i<n; i++) { b[i] = a * i; }`<br>
    - <strong>Strength Reduction:</strong> Replaces computationally expensive operations (e.g., multiplication inside loops driven by induction variables) with cheaper operations (addition).<br>
      <em>Example:</em> `for (int i=0; i<100; i++) { t = i * 4; }` $\rightarrow$ `t = 0; for (int i=0; i<100; i++) { ... t += 4; }`
  </div>
</div>
"""
