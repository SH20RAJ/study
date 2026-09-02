# Compiler Design Module 5 Exhaustive Content (12 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions

CD_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Code Generation & Optimization — Complete 12-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> Addresses of Code and Data in Assembly Code</div>
    <div><strong>Topic 2:</strong> Correlation of Assembly Code with Source Code</div>
    <div><strong>Topic 3:</strong> Construction of Basic Blocks (3 Leader Rules)</div>
    <div><strong>Topic 4:</strong> Control Flow Graph (CFG Nodes & Edges)</div>
    <div><strong>Topic 5:</strong> Machine-Independent Local Optimizations</div>
    <div><strong>Topic 6:</strong> Machine-Independent Global Optimizations</div>
    <div><strong>Topic 7:</strong> Unreachable Code Elimination</div>
    <div><strong>Topic 8:</strong> Constant Folding Optimization</div>
    <div><strong>Topic 9:</strong> Constant Propagation Optimization</div>
    <div><strong>Topic 10:</strong> Loop-Invariant Code Motion (Hoisting)</div>
    <div><strong>Topic 11:</strong> Common Subexpression Elimination (CSE)</div>
    <div><strong>Topic 12:</strong> Dead Code Elimination</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Assembly Code Addresses & Source Correlation</h2>
<p>
  The final code generator translates intermediate three-address representations into target machine instructions (assembly). The compiler maintains a strict correspondence between source language abstractions, intermediate variables, and physical hardware addresses:
</p>
<pre><code>Source Code: x = a + b;
        ↓
Intermediate: t1 = a + b; x = t1;
        ↓
Assembly:     MOV R1, a ; ADD R1, b ; MOV x, R1</code></pre>
<ul>
  <li><strong>Symbolic Address Mapping:</strong> Source identifiers are assigned relative stack frame offsets or static data segment addresses.</li>
  <li><strong>Source-Level Debugging:</strong> Line number tables and DWARF metadata allow debuggers (GDB) to map assembly crash addresses directly to source code lines.</li>
</ul>

<h2 class="section-title">Topic 3 & 4: Construction of Basic Blocks & Control Flow Graphs (CFG)</h2>

<div class="callout callout-info">
  <div class="callout-title">Algorithm: Partitioning Three-Address Code into Basic Blocks (3 Leader Rules)</div>
  <p><strong>Step 1: Identify Leaders (First instruction of a basic block):</strong></p>
  <ol>
    <li>The first three-address instruction of the intermediate code is a Leader.</li>
    <li>Any instruction that is the target of a conditional or unconditional jump (`goto L`) is a Leader.</li>
    <li>Any instruction that immediately follows a conditional or unconditional jump is a Leader.</li>
  </ol>
  <p><strong>Step 2: Form Basic Blocks:</strong></p>
  <p>For each Leader, its Basic Block consists of the Leader and all subsequent instructions up to (but not including) the next Leader or the end of the program.</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Basic Block Partitioning Trace</div>
  <pre><code>(1)  a = b + c       <-- Leader (Rule 1: First instruction)
(2)  if a < d goto 5
(3)  x = y + z       <-- Leader (Rule 3: Follows conditional jump at line 2)
(4)  goto 6
(5)  x = 0           <-- Leader (Rule 2: Target of goto 5 in line 2)
(6)  print x         <-- Leader (Rule 2: Target of goto 6 in line 4)</code></pre>
  <p><strong>Resulting Basic Blocks:</strong></p>
  <ul>
    <li><strong>Block $B_1$:</strong> Instructions (1) and (2)</li>
    <li><strong>Block $B_2$:</strong> Instructions (3) and (4)</li>
    <li><strong>Block $B_3$:</strong> Instruction (5)</li>
    <li><strong>Block $B_4$:</strong> Instruction (6)</li>
  </ul>
</div>

<h2 class="section-title">Topic 5 & 6: Local vs. Global Optimizations</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Scope</th>
      <th style="width: 45%;">Operating Domain & Algorithms</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Local Optimization</strong></td>
      <td>Operates strictly within a <strong>single basic block</strong> (straight-line code without branches). Analyzed via Directed Acyclic Graphs (DAG).</td>
      <td>Fast, linear time complexity; requires zero data-flow analysis equations across blocks.</td>
    </tr>
    <tr>
      <td><strong>Global Optimization</strong></td>
      <td>Operates across <strong>multiple basic blocks</strong> throughout the entire Control Flow Graph (CFG). Uses iterative Data-Flow Analysis equations.</td>
      <td>Achieves massive performance gains across loops and procedures; higher compile-time cost.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 7 – 12: Principal Machine-Independent Optimizations</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Optimization Pass</th>
      <th style="width: 40%;">Transformation Rule</th>
      <th>Before $\rightarrow$ After Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>7. Unreachable Code Elimination</strong></td>
      <td>Deletes basic blocks and instructions that have zero incoming edges in the CFG.</td>
      <td>`return x; y = 10;` $\rightarrow$ `return x;`</td>
    </tr>
    <tr>
      <td><strong>8. Constant Folding</strong></td>
      <td>Evaluates operations on compile-time constants upfront at compile time.</td>
      <td>`x = 10 * 20 + 4` $\rightarrow$ `x = 204`</td>
    </tr>
    <tr>
      <td><strong>9. Constant Propagation</strong></td>
      <td>Substitutes known constant variable values into subsequent expressions.</td>
      <td>`pi = 3.14; r = 2; a = pi * r;` $\rightarrow$ `a = 3.14 * 2;`</td>
    </tr>
    <tr>
      <td><strong>10. Loop-Invariant Code Motion</strong></td>
      <td>Hoists computations that evaluate to the exact same value in every loop iteration outside the loop header.</td>
      <td>`while (i < n) { x = a * b; i++; }` $\rightarrow$ `x = a * b; while (i < n) { i++; }`</td>
    </tr>
    <tr>
      <td><strong>11. Common Subexpression Elimination (CSE)</strong></td>
      <td>Eliminates redundant re-evaluations of expressions whose operand values have not changed.</td>
      <td>`t1 = a + b; ...; t2 = a + b;` $\rightarrow$ `t2 = t1;`</td>
    </tr>
    <tr>
      <td><strong>12. Dead Code Elimination</strong></td>
      <td>Removes assignments whose computed values are never subsequently read or used anywhere in the program.</td>
      <td>`x = 10; x = 20; print(x);` $\rightarrow$ `x = 20; print(x);`</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M5 Active Recall & Exam-Important Question Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Differentiate between Unreachable Code and Dead Code with code examples. (6 Marks)</div>
  <div class="qa-a">
    - <strong>Unreachable Code:</strong> Code that can <em>never be executed</em> at runtime because no control flow path can ever reach it (e.g., instructions following an unconditional `return` or `goto` without a label):<br>
      `return 5; x = 10;` $\rightarrow$ `x = 10` is unreachable.<br>
    - <strong>Dead Code:</strong> Code that <em>is executed</em>, but its computation is useless because the computed value is never referenced by any subsequent instruction:<br>
      `x = a + b; x = 20; print(x);` $\rightarrow$ `x = a + b` executes, but is completely dead because `x` is immediately overwritten before being read.
  </div>
</div>
"""
