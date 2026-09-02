# Compiler Design Module 5 Exhaustive Master Content (Topics 36 to 47)
CD_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Code Optimization & Target Code Generation — 12-Topic Master Guide</div>
  <div class="toc-grid">
    <div><strong>Topic 36:</strong> Issues in the Design of a Code Generator (Target Architecture)</div>
    <div><strong>Topic 37:</strong> Target Language Instruction Selection & Instruction Cost Models</div>
    <div><strong>Topic 38:</strong> Addresses in Target Code (Static & Dynamic Offset Calculations)</div>
    <div><strong>Topic 39:</strong> Basic Blocks Partitioning (The 3 Classical Leader Rules)</div>
    <div><strong>Topic 40:</strong> Control Flow Graphs (CFG Nodes, Edges, Dominators & Natural Loops)</div>
    <div><strong>Topic 41:</strong> Next-Use Information & Liveness Analysis Inside Blocks</div>
    <div><strong>Topic 42:</strong> Register Allocation & Assignment (Chaitin Graph Coloring Algorithm)</div>
    <div><strong>Topic 43:</strong> Directed Acyclic Graphs (DAG) for Local Basic Block Optimization</div>
    <div><strong>Topic 44:</strong> Data-Flow Analysis Frameworks (Reaching Definitions & Live Variables)</div>
    <div><strong>Topic 45:</strong> Loop Optimizations (Loop-Invariant Code Motion & Strength Reduction)</div>
    <div><strong>Topic 46:</strong> Peephole Optimization Techniques (Sliding Window Transformations)</div>
    <div><strong>Topic 47:</strong> Simple Code Generator Algorithm (Register & Address Descriptors)</div>
  </div>
</div>

<h2 class="section-title">Topic 36 – 38: Fundamental Issues in Target Code Generation</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Design Challenge</th>
      <th style="width: 45%;">Engineering Complexity & Tradeoffs</th>
      <th>Compiler Strategy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Instruction Selection</strong></td>
      <td>Mapping uniform Three-Address Code into diverse, irregular target CPU instruction sets (CISC vs. RISC).</td>
      <td>Tree-rewriting and dynamic programming instruction selection algorithms.</td>
    </tr>
    <tr>
      <td><strong>2. Register Allocation</strong></td>
      <td>Registers are the fastest hardware storage ($1\text{ cycle}$) but strictly limited in quantity (e.g., 16 or 32 physical registers).</td>
      <td>NP-Complete <strong>Graph Coloring</strong>; spills excess variables to stack frames.</td>
    </tr>
    <tr>
      <td><strong>3. Evaluation Order</strong></td>
      <td>The sequence in which computations execute dramatically alters the number of registers required.</td>
      <td>Sethi-Ullman algorithm for optimal register labeling of syntax trees.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 39 & 40: Basic Blocks & Control Flow Graphs (CFG)</h2>

<p>
  A <strong>Basic Block</strong> is a maximal sequence of consecutive Three-Address instructions with a <strong>single entry point</strong> (execution enters only at the first instruction) and a <strong>single exit point</strong> (execution leaves only at the last instruction), with zero internal branches or jump targets.
</p>

<div class="callout callout-info">
  <div class="callout-title">The 3 Classical Rules for Leader Identification</div>
  An instruction $i$ is designated a <strong>Leader</strong> if and only if it satisfies at least one condition:
  <ol>
    <li><strong>Rule 1:</strong> The very first instruction of the Three-Address Code sequence is a Leader.</li>
    <li><strong>Rule 2:</strong> Any instruction that is the <strong>target of a conditional or unconditional goto</strong> is a Leader.</li>
    <li><strong>Rule 3:</strong> Any instruction that <strong>immediately follows a conditional or unconditional goto</strong> is a Leader.</li>
  </ol>
  <em>Partitioning:</em> A Basic Block starts at a Leader and extends up to, but not including, the next Leader or the end of the program.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Partitioning TAC into Basic Blocks & Constructing CFG</div>
  <pre><code>(1)  i = 1             ; LEADER (Rule 1: First instruction)
(2)  j = 1
(3)  t1 = 10 * i       ; LEADER (Rule 2: Target of goto 3 at line 11)
(4)  t2 = t1 + j
(5)  t3 = 8 * t2
(6)  t4 = b[t3]
(7)  a[t3] = t4
(8)  j = j + 1
(9)  if j <= 10 goto 3 ; Branch instruction
(10) i = i + 1         ; LEADER (Rule 3: Immediately follows goto 9)
(11) if i <= 10 goto 3 ; Branch instruction
(12) return            ; LEADER (Rule 3: Immediately follows goto 11)</code></pre>

  <p><strong>Identified Basic Blocks:</strong></p>
  <ul>
    <li><strong>$B_1$:</strong> Instructions (1) to (2) [Initialization]</li>
    <li><strong>$B_2$:</strong> Instructions (3) to (9) [Inner loop body]</li>
    <li><strong>$B_3$:</strong> Instructions (10) to (11) [Outer loop step]</li>
    <li><strong>$B_4$:</strong> Instruction (12) [Exit]</li>
  </ul>

  <p><strong>Control Flow Graph Edges:</strong></p>
  $$B_1 \longrightarrow B_2, \quad B_2 \xrightarrow{\text{true}} B_2, \quad B_2 \xrightarrow{\text{false}} B_3, \quad B_3 \xrightarrow{\text{true}} B_2, \quad B_3 \xrightarrow{\text{false}} B_4$$
</div>

<h2 class="section-title">Topic 42: Register Allocation via Graph Coloring (Chaitin-Briggs)</h2>

<div class="formula-card">
  <strong>Kempe's Heuristic for $K$-Register Graph Coloring:</strong>
  1. Construct <strong>Interference Graph</strong> $G=(V, E)$ where nodes represent variable live ranges, and edges connect variables simultaneously live at any program point.
  2. <strong>Simplify Step:</strong> Find a node $v$ with degree $< K$. Remove $v$ from graph and push onto stack $S$.
  3. If all nodes are removed, pop nodes from $S$ one by one and assign available non-conflicting physical registers.
  4. If a stage is reached where all remaining nodes have degree $\ge K$, select a variable to <strong>Spill</strong> to stack memory.
</div>

<h2 class="section-title">Topic 43: Directed Acyclic Graphs (DAG) for Local Optimization</h2>

<p>
  A <strong>Directed Acyclic Graph (DAG)</strong> constructed for a single basic block exposes common subexpressions, eliminates redundant computations, and detects dead code locally.
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step DAG Optimization Example</div>
  <pre><code>// Original Basic Block:
t1 = a + b
t2 = a + b       ; Redundant common subexpression!
t3 = t1 * t2
t4 = c + d
t5 = t3 + t4</code></pre>
  <p><strong>DAG Construction:</strong> Identifies that `t1` and `t2` compute the identical node `+(a, b)`. Replaces `t2` with `t1`.</p>
  <p><strong>Optimized Generated Code:</strong></p>
  <pre><code>t1 = a + b
t3 = t1 * t1      ; Reused t1!
t4 = c + d
t5 = t3 + t4</code></pre>
</div>

<h2 class="section-title">Topic 44 & 45: Principal Global & Loop Optimization Passes</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Optimization Pass</th>
      <th style="width: 45%;">Transformation Mechanism</th>
      <th>Concrete Code Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Constant Folding</strong></td>
      <td>Computes constant operations at compile time rather than generating runtime instructions.</td>
      <td>`x = 3.14159 * 2` $\implies$ `x = 6.28318`</td>
    </tr>
    <tr>
      <td><strong>2. Constant Propagation</strong></td>
      <td>Replaces variable uses with known constant values throughout reaching definitions.</td>
      <td>`x = 10; y = x + 5;` $\implies$ `y = 10 + 5;` $\implies$ `y = 15;`</td>
    </tr>
    <tr>
      <td><strong>3. Loop-Invariant Code Motion</strong></td>
      <td>Hoists statements whose operands do not change during loop iterations into a loop pre-header.</td>
      <td>`while (i < N) { x = a + b; ... }` $\implies$ `x = a + b; while (i < N) { ... }`</td>
    </tr>
    <tr>
      <td><strong>4. Strength Reduction</strong></td>
      <td>Replaces expensive operations (multiplication/division) with equivalent cheaper operations (addition/shifts).</td>
      <td>`for (i=0; i<N; i++) arr[i] = i * 4;` $\implies$ Uses pointer addition `p += 4;` per step.</td>
    </tr>
    <tr>
      <td><strong>5. Dead Code Elimination</strong></td>
      <td>Removes statements computing values that are never subsequently read on any execution path.</td>
      <td>`if (0) { foo(); }` is entirely deleted from the binary.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 46: Peephole Optimization Techniques</h2>

<div class="callout callout-info">
  <div class="callout-title">The 4 Classical Peephole Transformations</div>
  Operates on a small sliding window (typically 2–4 instructions) of target assembly code:
  <ol>
    <li><strong>Eliminating Redundant Load/Store:</strong> `MOV R0, a` immediately followed by `MOV a, R0` (second instruction is deleted).</li>
    <li><strong>Eliminating Unreachable Code:</strong> Instructions immediately following an unconditional `JMP` that lack a jump label are deleted.</li>
    <li><strong>Algebraic Simplifications:</strong> Replaces `x = x + 0` or `x = x * 1` with no-ops; replaces `x = x * 2` with fast shift `SHL R0, 1`.</li>
    <li><strong>Machine Idioms:</strong> Replaces `MOV R0, #0` with single-cycle `XOR R0, R0`.</li>
  </ol>
</div>

<h2 class="section-title">Topic 47: Simple Code Generation Algorithm</h2>

<div class="formula-card">
  <strong>Register Descriptors & Address Descriptors:</strong>
  - <strong>Register Descriptor ($\text{RD}[R]$):</strong> Tracks all variables currently held inside physical register $R$.
  - <strong>Address Descriptor ($\text{AD}[v]$):</strong> Tracks all memory and register locations where current value of variable $v$ can be found.
</div>

<h2 class="section-title">🧠 M5 Active Recall & 10-Question University Exam Master Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the Data-Flow Analysis framework for Reaching Definitions with mathematical equations. (10 Marks)</div>
  <div class="qa-a">
    A definition $d: u = v + w$ <strong>reaches</strong> a point $p$ if there exists an execution path from $d$ to $p$ along which $d$ is not "killed" (redefined).<br>
    <strong>Data-Flow Transfer Equations:</strong><br>
    $$\mathbf{\text{IN}[B] = \bigcup_{P \in \text{Pred}[B]} \text{OUT}[P]}$$
    $$\mathbf{\text{OUT}[B] = \text{GEN}[B] \cup (\text{IN}[B] - \text{KILL}[B])}$$
    Where $\text{GEN}[B]$ is the set of definitions generated inside block $B$, and $\text{KILL}[B]$ is the set of all definitions elsewhere in the program that define the same variables modified in $B$. Solved iteratively to reach maximum fixed-point convergence!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. State the 3 Leader Identification Rules for partitioning Three-Address Code into Basic Blocks. (6 Marks)</div>
  <div class="qa-a">
    1. <strong>Rule 1:</strong> The very first instruction of the Three-Address Code sequence is a Leader.<br>
    2. <strong>Rule 2:</strong> Any instruction that is the target of a conditional or unconditional branch is a Leader.<br>
    3. <strong>Rule 3:</strong> Any instruction that immediately follows a conditional or unconditional branch is a Leader.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Explain Loop-Invariant Code Motion and Induction Variable Elimination with concrete code examples. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Loop-Invariant Code Motion (Hoisting):</strong> Computations inside a loop whose operands never change across iterations are moved outside the loop into a newly created pre-header block.<br>
    • <strong>Induction Variable Elimination:</strong> When two variables $i$ and $j$ change in lockstep inside a loop (e.g., $j = 4 * i$), $j$ can be updated via addition ($j += 4$) and $i$ can be eliminated entirely if it is not used outside the loop.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q4. What is Peephole Optimization? Explain 4 classical peephole optimization techniques. (8 Marks)</div>
  <div class="qa-a">
    Peephole optimization is a local target-code optimization technique that inspects a short sliding window of target instructions (2 to 4 instructions) to perform immediate peephole replacements:<br>
    1. <strong>Redundant Load/Store Elimination:</strong> Deleting redundant `MOV x, R0` immediately after `MOV R0, x`.<br>
    2. <strong>Unreachable Code Elimination:</strong> Deleting instructions following an unconditional `JMP` that lack a target label.<br>
    3. <strong>Flow of Control Optimization:</strong> Replacing jumps to jumps (`JMP L1` where `L1: JMP L2`) with `JMP L2`.<br>
    4. <strong>Algebraic Simplification & Strength Reduction:</strong> Replacing $x = x * 2$ with single-cycle `SHL R0, 1`.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q5. Explain the Chaitin-Briggs Graph Coloring algorithm for Register Allocation. (10 Marks)</div>
  <div class="qa-a">
    Register allocation is formulated as graph $K$-coloring where vertices represent variable live ranges and edges represent simultaneous liveness (interference):<br>
    1. <strong>Build:</strong> Construct interference graph $G=(V, E)$.<br>
    2. <strong>Simplify (Kempe's Heuristic):</strong> Find vertex $v$ with degree $< K$. Remove $v$ and push onto stack $S$.<br>
    3. <strong>Spill:</strong> If all remaining vertices have degree $\ge K$, select a candidate with high spill cost / low frequency to spill to memory.<br>
    4. <strong>Select:</strong> Pop vertices from $S$ and assign non-conflicting colors (registers). If spilled, insert load/store instructions and re-run!
  </div>
</div>
<h2 class="section-title">Topic 47.2: Comprehensive Data-Flow Analysis & Optimization Traces</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 1: Reaching Definitions Iterative Fixed-Point Table Convergence</div>
  <p>Consider Control Flow Graph with 3 Basic Blocks:</p>
  <ul>
    <li><strong>$B_1$:</strong> $d_1: i = 1, \ d_2: j = 1$ $\implies \text{GEN}[B_1] = \{d_1, d_2\}, \ \text{KILL}[B_1] = \{d_3, d_4\}$</li>
    <li><strong>$B_2$:</strong> $d_3: i = i + 1, \ d_4: j = j + 1$ $\implies \text{GEN}[B_2] = \{d_3, d_4\}, \ \text{KILL}[B_2] = \{d_1, d_2\}$</li>
    <li><strong>$B_3$:</strong> $d_5: x = i + j$ $\implies \text{GEN}[B_3] = \{d_5\}, \ \text{KILL}[B_3] = \emptyset$</li>
  </ul>
  <p><strong>Iterative Fixed-Point Convergence Table:</strong></p>
  <table class="custom-table">
    <thead><tr><th>Iteration</th><th>$\text{IN}[B_1]$</th><th>$\text{OUT}[B_1]$</th><th>$\text{IN}[B_2]$</th><th>$\text{OUT}[B_2]$</th><th>$\text{IN}[B_3]$</th><th>$\text{OUT}[B_3]$</th></tr></thead>
    <tbody>
      <tr><td><strong>Init</strong></td><td>$\emptyset$</td><td>$\emptyset$</td><td>$\emptyset$</td><td>$\emptyset$</td><td>$\emptyset$</td><td>$\emptyset$</td></tr>
      <tr><td><strong>Pass 1</strong></td><td>$\emptyset$</td><td>$\{d_1, d_2\}$</td><td>$\{d_1, d_2\}$</td><td>$\{d_3, d_4\}$</td><td>$\{d_3, d_4\}$</td><td>$\{d_3, d_4, d_5\}$</td></tr>
      <tr><td><strong>Pass 2</strong></td><td>$\emptyset$</td><td>$\{d_1, d_2\}$</td><td>$\{d_1, d_2, d_3, d_4\}$</td><td>$\{d_3, d_4\}$</td><td>$\{d_3, d_4\}$</td><td>$\{d_3, d_4, d_5\}$</td></tr>
      <tr><td><strong>Pass 3 (Converged)</strong></td><td>$\emptyset$</td><td>$\{d_1, d_2\}$</td><td>$\{d_1, d_2, d_3, d_4\}$</td><td>$\{d_3, d_4\}$</td><td>$\{d_3, d_4\}$</td><td>$\{d_3, d_4, d_5\}$</td></tr>
    </tbody>
  </table>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 2: Loop-Invariant Code Motion & Induction Variable Strength Reduction</div>
  <p><strong>Unoptimized Source Loop:</strong></p>
  <pre><code>for (i = 0; i < N; i++) {
    x = a + b;           // Loop Invariant!
    arr[i] = i * 4;      // Induction Variable with multiplication!
}</code></pre>
  <p><strong>Optimized Generated Code:</strong></p>
  <pre><code>x = a + b;               // Hoisted to loop pre-header
p = &arr[0];             // Pointer initialization
for (i = 0; i < N; i++) {
    *p = i << 2;         // Strength reduction: replaced mult with fast shift & pointer addition
    p++;
}</code></pre>
</div>

<div class="qa-card">
  <div class="qa-q">Q6. Compare Local Optimization, Loop Optimization, and Global Optimization across scope and algorithms. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Local Optimization:</strong> Operates strictly within a single Basic Block using Directed Acyclic Graphs (DAG) for common subexpression elimination, algebraic identities, and dead code elimination.<br>
    • <strong>Loop Optimization:</strong> Operates on natural loops in the CFG using Loop-Invariant Code Motion (hoisting statements to loop pre-headers), Induction Variable Elimination, and Strength Reduction.<br>
    • <strong>Global Optimization:</strong> Operates across multiple basic blocks throughout the entire CFG using Iterative Data-Flow Analysis (Reaching Definitions, Available Expressions, Live Variable Analysis).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q7. Explain Dominators, Immediate Dominators, and Natural Loops in Control Flow Graphs. (10 Marks)</div>
  <div class="qa-a">
    • <strong>Dominator ($d \ \mathbf{dom} \ n$):</strong> Node $d$ dominates node $n$ if every execution path from the CFG entry node to $n$ must pass through $d$.<br>
    • <strong>Immediate Dominator ($\text{idom}(n)$):</strong> The unique dominator $d$ of $n$ ($d \neq n$) that does not strictly dominate any other strict dominator of $n$. Forming the <strong>Dominator Tree</strong>.<br>
    • <strong>Natural Loop:</strong> A loop characterized by a single loop header $d$ and a <strong>Back-Edge</strong> $n \rightarrow d$ where $d \ \mathbf{dom} \ n$. The natural loop consists of $d$ plus all nodes that can reach $n$ without passing through $d$.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q8. Explain Available Expressions Data-Flow Analysis and Global Common Subexpression Elimination. (8 Marks)</div>
  <div class="qa-a">
    An expression $x + y$ is <strong>Available</strong> at point $p$ if every path from the initial node to $p$ evaluates $x + y$, and neither $x$ nor $y$ is subsequently redefined.<br>
    <strong>Transfer Equations (Must-Analysis / Intersection Meet):</strong><br>
    $$\mathbf{\text{IN}[B] = \bigcap_{P \in \text{Pred}[B]} \text{OUT}[P]}$$
    $$\mathbf{\text{OUT}[B] = \text{GEN}[B] \cup (\text{IN}[B] - \text{KILL}[B])}$$
    Used to eliminate redundant evaluations globally across the entire CFG.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q9. Explain Live Variable Analysis and its role in Dead Code Elimination and Register Allocation. (8 Marks)</div>
  <div class="qa-a">
    A variable $v$ is <strong>Live</strong> at point $p$ if there exists an execution path from $p$ along which $v$ is read before any subsequent redefinition.<br>
    <strong>Transfer Equations (Backward Data-Flow Analysis):</strong><br>
    $$\mathbf{\text{OUT}[B] = \bigcup_{S \in \text{Succ}[B]} \text{IN}[S]}$$
    $$\mathbf{\text{IN}[B] = \text{DEF}[B] \cup (\text{OUT}[B] - \text{USE}[B])}$$
    Variables not live after a statement are dead (allowing assignment removal), and simultaneously live variables define edges in the Register Interference Graph.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q10. Explain the Simple Code Generator algorithm with Register Descriptors and Address Descriptors. (10 Marks)</div>
  <div class="qa-a">
    The simple code generator processes Three-Address instructions $x = y \ \mathbf{op} \ z$ sequentially within a basic block:<br>
    1. Invokes $\mathbf{getReg}(x = y \ \mathbf{op} \ z)$ to determine the optimal physical register $R_y$ for operand $y$.<br>
    2. If $y$ is not already in $R_y$, emits `MOV R_y, y`.<br>
    3. Emits `OP R_y, z` (where $z$ is in a register or memory location).<br>
    4. Updates $\text{RD}[R_y]$ to indicate $R_y$ now contains variable $x$.<br>
    5. Updates $\text{AD}[x]$ to indicate $x$ resides in register $R_y$, and removes $x$ from other descriptors.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q11. Explain Constant Folding vs. Constant Propagation with before and after code traces. (6 Marks)</div>
  <div class="qa-a">
    • <strong>Constant Folding:</strong> Evaluates arithmetic operations on constant literals at compile-time: `x = 10 * 20` $\implies$ `x = 200`.<br>
    • <strong>Constant Propagation:</strong> Replaces variable uses with their statically known constant values throughout the CFG: `x = 10; y = x + 5;` $\implies$ `y = 10 + 5;` $\implies$ `y = 15;`.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q12. Explain the Sethi-Ullman Algorithm for Optimal Instruction Scheduling and Register Labeling. (8 Marks)</div>
  <div class="qa-a">
    The <strong>Sethi-Ullman Algorithm</strong> computes the minimum number of registers required to evaluate an expression tree without spilling to memory:<br>
    1. Leaves (variables) are assigned label `1`; right leaves of binary operations are assigned `0`.<br>
    2. For a binary node with left child label $l_1$ and right child label $l_2$:<br>
       $$\text{Label}(\text{Node}) = \begin{cases} \max(l_1, l_2) & \text{if } l_1 \neq l_2 \\ l_1 + 1 & \text{if } l_1 = l_2 \end{cases}$$
    3. The compiler generates code evaluating the child subtree with the higher label first, minimizing temporary register holding time!
  </div>
</div>
<h2 class="section-title">Topic 47.3: Advanced Register Allocation & Global Data-Flow Frameworks</h2>

<p>
  Register allocation is widely considered one of the most critical optimization passes in modern compilers. Because memory access takes 100–300 CPU clock cycles while register access takes only 1 cycle, maximizing variable residence in registers yields order-of-magnitude execution speedups.
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Step-by-Step Chaitin-Briggs Graph Coloring Trace</div>
  <p>Let variables $A, B, C, D, E$ have the following Interference Graph edges for a target CPU with $K = 2$ physical registers (R1, R2):</p>
  <ul>
    <li>$A$ interferes with $\{B, C\}$ (Degree 2)</li>
    <li>$B$ interferes with $\{A, C, D\}$ (Degree 3)</li>
    <li>$C$ interferes with $\{A, B, E\}$ (Degree 3)</li>
    <li>$D$ interferes with $\{B\}$ (Degree 1)</li>
    <li>$E$ interferes with $\{C\}$ (Degree 1)</li>
  </ul>
  <p><strong>Graph Coloring Execution Trace:</strong></p>
  <ol>
    <li><strong>Step 1:</strong> Node $D$ has degree $1 < 2$. Remove $D$ and push onto stack $S = [D]$.</li>
    <li><strong>Step 2:</strong> Node $E$ has degree $1 < 2$. Remove $E$ and push onto stack $S = [D, E]$.</li>
    <li><strong>Step 3:</strong> Remaining graph nodes: $A$ (degree 2), $B$ (degree 2), $C$ (degree 2). Since all degrees are $\ge 2$, Kempe's heuristic selects $A$ to remove: Stack $S = [D, E, A]$.</li>
    <li><strong>Step 4:</strong> Remaining nodes $B$ and $C$ now have degree 1. Remove $B$: Stack $S = [D, E, A, B]$; Remove $C$: Stack $S = [D, E, A, B, C]$.</li>
    <li><strong>Reconstruction & Color Assignment:</strong>
      <ul>
        <li>Pop $C$: Assign Register **R1**.</li>
        <li>Pop $B$: Assign Register **R2** (since $B$ interferes with $C$).</li>
        <li>Pop $A$: Interferes with $B$ (R2) and $C$ (R1) $\implies$ <strong>Spill $A$ to Stack Memory!</strong></li>
        <li>Pop $E$: Interferes only with $C$ (R1) $\implies$ Assign Register **R2**.</li>
        <li>Pop $D$: Interferes only with $B$ (R2) $\implies$ Assign Register **R1**.</li>
      </ul>
    </li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Dominator Tree & Natural Loop Identification Algorithm</div>
  <p>Consider CFG nodes $1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 2$ (Back-edge $4 \rightarrow 2$):</p>
  <ul>
    <li>Node 1 dominates $\{1, 2, 3, 4\}$</li>
    <li>Node 2 dominates $\{2, 3, 4\}$</li>
    <li>Node 3 dominates $\{3, 4\}$</li>
    <li>Node 4 dominates $\{4\}$</li>
  </ul>
  <p>Because $2 \ \mathbf{dom} \ 4$, the edge $4 \rightarrow 2$ is a <strong>Back-Edge</strong>. The Natural Loop consists of header node $2$ plus all nodes that can reach node $4$ without passing through $2$, yielding loop node set $\{2, 3, 4\}$.</p>
</div>
<h2 class="section-title">Topic 47.4: Advanced Instruction Selection & Available Expressions Worklist</h2>

<p>
  <strong>Instruction Selection</strong> maps the machine-independent Three-Address intermediate code into concrete target processor instructions. The compiler models target CPU instructions as <strong>Tree Patterns (Tiles)</strong> and tiles the intermediate representation Abstract Syntax Tree with minimum cost.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Instruction Selection Technique</th>
      <th style="width: 45%;">Operating Algorithm & Tree Tiling Strategy</th>
      <th>Computational Complexity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Maximal Munch Algorithm</strong></td>
      <td>Greedy top-down pattern matcher: at root of tree, finds the largest matching tile covering the most nodes, emits instruction, and recurses on subtrees.</td>
      <td>Linear Time $O(N)$; produces high-quality RISC and CISC instructions.</td>
    </tr>
    <tr>
      <td><strong>2. Dynamic Programming Tiling</strong></td>
      <td>Bottom-up optimal tiling: computes minimum cost to evaluate each subtree in each hardware register class, then traverses downward to emit instructions.</td>
      <td>Optimal Code in $O(N \cdot |P|)$ time, where $|P|$ is the number of target instruction patterns.</td>
    </tr>
    <tr>
      <td><strong>3. Tree-Rewriting / BURG Systems</strong></td>
      <td>Uses Tree Grammars and Bottom-Up Rewrite Generators to automatically generate table-driven optimal instruction selectors.</td>
      <td>Industry standard in production compilers (GCC, LLVM SelectionDAG).</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Iterative Available Expressions Data-Flow Convergence</div>
  <p>Consider a CFG with 3 basic blocks and expression set $U = \{a+b, \ c*d, \ e-f\}$:</p>
  <ul>
    <li><strong>$B_1$:</strong> Computes $a+b$, defines $x$ $\implies \text{GEN}[B_1] = \{a+b\}, \ \text{KILL}[B_1] = \emptyset$</li>
    <li><strong>$B_2$:</strong> Computes $c*d$, redefines $a$ $\implies \text{GEN}[B_2] = \{c*d\}, \ \text{KILL}[B_2] = \{a+b\}$</li>
    <li><strong>$B_3$:</strong> Computes $e-f$ $\implies \text{GEN}[B_3] = \{e-f\}, \ \text{KILL}[B_3] = \emptyset$</li>
  </ul>
  <p><strong>Available Expressions Iterative Convergence Table (Must-Analysis: $\text{IN}[B] = \bigcap \text{OUT}[P]$):</strong></p>
  <table class="custom-table">
    <thead><tr><th>Iteration</th><th>$\text{IN}[B_1]$</th><th>$\text{OUT}[B_1]$</th><th>$\text{IN}[B_2]$</th><th>$\text{OUT}[B_2]$</th><th>$\text{IN}[B_3]$</th><th>$\text{OUT}[B_3]$</th></tr></thead>
    <tbody>
      <tr><td><strong>Init</strong></td><td>$\emptyset$</td><td>$U$</td><td>$U$</td><td>$U$</td><td>$U$</td><td>$U$</td></tr>
      <tr><td><strong>Pass 1</strong></td><td>$\emptyset$</td><td>$\{a+b\}$</td><td>$\{a+b\}$</td><td>$\{c*d\}$</td><td>$\{c*d\}$</td><td>$\{c*d, e-f\}$</td></tr>
      <tr><td><strong>Pass 2 (Converged)</strong></td><td>$\emptyset$</td><td>$\{a+b\}$</td><td>$\{a+b\}$</td><td>$\{c*d\}$</td><td>$\{c*d\}$</td><td>$\{c*d, e-f\}$</td></tr>
    </tbody>
  </table>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: DAG Construction for 8-Statement Basic Block</div>
  <p><strong>Basic Block Statements:</strong></p>
  <pre><code>(1) a = b + c
(2) d = b + c       ; Common Subexpression: Reuses DAG node +(b, c)
(3) e = a + d
(4) f = b + c       ; Common Subexpression: Reuses DAG node +(b, c)
(5) g = e * f
(6) h = a + d       ; Common Subexpression: Reuses DAG node +(a, d)
(7) i = g - h
(8) x = i</code></pre>
  <p><strong>Optimized Target Code Generated from DAG:</strong></p>
  <pre><code>a = b + c
d = a               ; Copy instead of addition
e = a + a
g = e * a
h = e               ; Copy instead of addition
x = g - e           ; Direct assignment eliminating temporaries f, h, i</code></pre>
</div>
<h2 class="section-title">Topic 47.5: Interprocedural Optimization (IPO) & Whole-Program Compilation</h2>

<p>
  While intraprocedural optimization operates within a single procedure, <strong>Interprocedural Optimization (IPO)</strong> analyzes relationships across the entire call graph of the program.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Interprocedural Pass</th>
      <th style="width: 45%;">Operating Mechanism</th>
      <th>Optimization Impact & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Function Inlining</strong></td>
      <td>Replaces a procedure call site with the verbatim body of the callee, substituting actual parameters for formal variables.</td>
      <td>Eliminates function call overhead ($10\text{ to }30\text{ cycles}$) and enables massive downstream constant propagation; may increase code size.</td>
    </tr>
    <tr>
      <td><strong>2. Interprocedural Constant Propagation (IPCP)</strong></td>
      <td>Tracks constant values passed as arguments across procedure boundaries throughout the Call Graph.</td>
      <td>Specializes procedures for common constant inputs and prunes dead branches globally.</td>
    </tr>
    <tr>
      <td><strong>3. Devirtualization</strong></td>
      <td>Proves via Class Hierarchy Analysis (CHA) that a virtual call site has only one possible target subclass.</td>
      <td>Converts expensive indirect virtual dispatch calls into direct static calls or inlined code!</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Function Inlining & Downstream Optimization Cascade</div>
  <p><strong>Original Code:</strong></p>
  <pre><code>int square(int val) { return val * val; }
int compute() {
    int x = 5;
    return square(x) + 10;
}</code></pre>
  <p><strong>Optimization Cascade Trace:</strong></p>
  <ol>
    <li><strong>Pass 1 (Function Inlining):</strong> Replaces `square(x)` with `(x * x)` $\implies$ `return (x * x) + 10;`</li>
    <li><strong>Pass 2 (Constant Propagation):</strong> Replaces `x` with `5` $\implies$ `return (5 * 5) + 10;`</li>
    <li><strong>Pass 3 (Constant Folding):</strong> Evaluates `5 * 5 = 25` and `25 + 10 = 35` at compile time.</li>
    <li><strong>Final Generated Target Code:</strong> `MOV EAX, 35; RET;` (Zero memory access, zero multiplication, instant return!)</li>
  </ol>
</div>

"""
