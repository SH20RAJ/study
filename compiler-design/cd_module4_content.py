# Compiler Design Module 4 Exhaustive Master Content (Topics 27 to 35)
CD_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Control Flow, Backpatching & Runtime Environments — 9-Topic Master Guide</div>
  <div class="toc-grid">
    <div><strong>Topic 27:</strong> Intermediate Code for Boolean Expressions (Short-Circuit Evaluation)</div>
    <div><strong>Topic 28:</strong> Control Flow Translation (`if-then`, `if-then-else`, `while`, `for`, `switch`)</div>
    <div><strong>Topic 29:</strong> Backpatching Mechanics (`makelist`, `merge`, `backpatch`, `truelist`, `falselist`)</div>
    <div><strong>Topic 30:</strong> Translation of Forward & Backward Jump Control Structures</div>
    <div><strong>Topic 31:</strong> Translation of Procedure Calls & Returns (`param`, `call`, `return`)</div>
    <div><strong>Topic 32:</strong> Runtime Storage Organization (Code, Static, Heap & Call Stack)</div>
    <div><strong>Topic 33:</strong> Activation Records Anatomy (The 7 P-R-C-A-S-L-T Frame Fields)</div>
    <div><strong>Topic 34:</strong> Storage Allocation Strategies (Static, Stack & Heap Allocation)</div>
    <div><strong>Topic 35:</strong> Access to Non-Local Variables (Access Links vs. Displays Technique)</div>
  </div>
</div>

<h2 class="section-title">Topic 27 & 28: Boolean Expressions & Control Flow Translation</h2>

<p>
  In programming languages, <strong>Boolean Expressions</strong> serve two fundamentally distinct operational purposes:
</p>
<ol>
  <li><strong>Numerical Value Representation:</strong> Computing explicit logical truth values stored into boolean variables (e.g., `flag = (a > b)` where `flag` evaluates to integer `1` or `0`).</li>
  <li><strong>Flow-of-Control Branching:</strong> Governing the conditional execution trajectory in decision and looping statements (e.g., `if (a > b) ...` or `while (x <= y) ...`).</li>
</ol>

<div class="callout callout-info">
  <div class="callout-title">Short-Circuit Evaluation Semantics</div>
  Compilers generate highly optimized short-circuit conditional code that avoids evaluating redundant subexpressions:
  <ul>
    <li>In an <strong>$\mathbf{OR}$ expression</strong> ($B_1 \ \mathbf{or} \ B_2$): If $B_1$ evaluates to $\mathbf{true}$, the overall expression is immediately known to be $\mathbf{true}$; evaluation of $B_2$ is completely bypassed.</li>
    <li>In an <strong>$\mathbf{AND}$ expression</strong> ($B_1 \ \mathbf{and} \ B_2$): If $B_1$ evaluates to $\mathbf{false}$, the overall expression is immediately known to be $\mathbf{false}$; evaluation of $B_2$ is completely bypassed.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Generating Three-Address Code for Complex Control Flow</div>
  <p><strong>Source Statement:</strong> `if (a < b || c < d && e < f) x = y + 1; else x = y - 1;`</p>
  <pre><code>100: if a < b goto 104     ; Short-circuit OR: if (a < b) is TRUE -> jump directly to true-body
101: if c < d goto 102     ; If (c < d) is TRUE -> must evaluate (e < f)
102: goto 107              ; If (c < d) is FALSE -> short-circuit AND fails -> jump to else-body
103: if e < f goto 104     ; If (e < f) is TRUE -> jump to true-body
104: goto 107              ; If (e < f) is FALSE -> jump to else-body
105: t1 = y + 1            ; True-body statement
106: x = t1
107: goto 110              ; Jump past else-body
108: t2 = y - 1            ; Else-body statement
109: x = t2
110: ...                   ; Next statement</code></pre>
</div>

<h3 class="subsection-title">28.1 Translation of `switch-case` Statements: 3 Compilation Strategies</h3>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Compilation Strategy</th>
      <th style="width: 45%;">Operating Mechanism</th>
      <th>Ideal Scenario & Time Complexity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Linear Comparison Sequence</strong></td>
      <td>Emits sequential `if (E == V1) goto L1; if (E == V2) goto L2; ...`</td>
      <td>Small number of case branches ($\le 4$ cases); $O(n)$ search time.</td>
    </tr>
    <tr>
      <td><strong>2. Jump Table (Direct Indexing)</strong></td>
      <td>Creates a contiguous array of code pointers indexed directly by value $(E - V_{\text{min}})$.</td>
      <td>Dense, tightly clustered case values ($[1, 2, 3, 4, 5]$); $\mathbf{O(1)}$ instant jump time.</td>
    </tr>
    <tr>
      <td><strong>3. Binary Search Tree (Hash Table)</strong></td>
      <td>Emits a balanced binary search decision tree of conditional branches over sorted case values.</td>
      <td>Large, sparse case values ($[10, 500, 10000, 500000]$); $O(\log n)$ search time.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 29 & 30: Backpatching Mechanics in Single-Pass Compilers</h2>

<p>
  In a single-pass compiler, when the code generator emits a conditional or unconditional branch instruction, the <strong>target jump address</strong> is frequently unknown because the target statement has not yet been parsed. <strong>Backpatching</strong> resolves this problem by storing lists of instruction indices requiring branch targets, and filling in (backpatching) the actual statement labels once they become known.
</p>

<div class="formula-card">
  <strong>The 3 Fundamental Backpatching Helper Functions:</strong>
  1. $\mathbf{makelist}(i)$: Constructs a newly initialized list containing exactly one element: the integer index $i$ of a newly emitted branch instruction.
  2. $\mathbf{merge}(p_1, p_2)$: Concatenates two jump index lists $p_1$ and $p_2$, returning a unified combined list pointer.
  3. $\mathbf{backpatch}(p, L)$: Traverses every instruction index stored in list $p$, inserting statement label $L$ as the explicit target jump address.
</div>

<h3 class="subsection-title">29.1 Syntax-Directed Translation Scheme for Boolean Backpatching:</h3>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 28%;">Grammar Production</th>
      <th>Semantic Action Rule for Backpatching</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$B \rightarrow B_1 \ \mathbf{or} \ M \ B_2$</td>
      <td>
        $\text{backpatch}(B_1.\text{falselist}, M.\text{quad})$<br>
        $B.\text{truelist} = \text{merge}(B_1.\text{truelist}, B_2.\text{truelist})$<br>
        $B.\text{falselist} = B_2.\text{falselist}$
      </td>
    </tr>
    <tr>
      <td>$B \rightarrow B_1 \ \mathbf{and} \ M \ B_2$</td>
      <td>
        $\text{backpatch}(B_1.\text{truelist}, M.\text{quad})$<br>
        $B.\text{truelist} = B_2.\text{truelist}$<br>
        $B.\text{falselist} = \text{merge}(B_1.\text{falselist}, B_2.\text{falselist})$
      </td>
    </tr>
    <tr>
      <td>$B \rightarrow \mathbf{not} \ B_1$</td>
      <td>
        $B.\text{truelist} = B_1.\text{falselist}$<br>
        $B.\text{falselist} = B_1.\text{truelist}$
      </td>
    </tr>
    <tr>
      <td>$B \rightarrow (B_1)$</td>
      <td>
        $B.\text{truelist} = B_1.\text{truelist}$<br>
        $B.\text{falselist} = B_1.\text{falselist}$
      </td>
    </tr>
    <tr>
      <td>$B \rightarrow \mathbf{id}_1 \ \mathbf{relop} \ \mathbf{id}_2$</td>
      <td>
        $B.\text{truelist} = \text{makelist}(\text{nextquad})$<br>
        $B.\text{falselist} = \text{makelist}(\text{nextquad} + 1)$<br>
        $\text{emit}(\text{"if "} \mathbf{id}_1.\text{name} \ \mathbf{relop}.\text{op} \ \mathbf{id}_2.\text{name} \ \text{"goto _"})$<br>
        $\text{emit}(\text{"goto _"})$
      </td>
    </tr>
    <tr>
      <td>$M \rightarrow \epsilon$</td>
      <td>
        $M.\text{quad} = \text{nextquad}$
      </td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 31: Translation of Procedure Calls & Parameter Passing</h2>

<p>
  Procedure calls require coordinating data passing, machine state preservation, stack frame allocation, and execution transfer between the <strong>Caller</strong> and <strong>Callee</strong> routines:
</p>

<div class="worked-box">
  <div class="worked-title">Three-Address Code Sequence for Procedure Call `result = compute_sum(a + 10, b * 2)`</div>
  <pre><code>t1 = a + 10
param t1           ; Push actual argument 1 onto parameter list
t2 = b * 2
param t2           ; Push actual argument 2 onto parameter list
call compute_sum, 2 ; Transfer control to procedure compute_sum (2 parameters)
result = retval    ; Retrieve return value from CPU return register</code></pre>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Parameter Passing Method</th>
      <th style="width: 45%;">Operating Mechanism</th>
      <th>Key Semantic Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Call-by-Value (C, Java Primitives)</strong></td>
      <td>Actual argument expression is evaluated and a local copy of the r-value is passed into the callee's stack frame.</td>
      <td>Modifications inside the callee have zero effect on the caller's variable.</td>
    </tr>
    <tr>
      <td><strong>2. Call-by-Reference (C++ `&`, Fortran)</strong></td>
      <td>The l-value (memory address) of the actual argument is passed directly.</td>
      <td>Changes made to the formal parameter immediately mutate the caller's actual variable.</td>
    </tr>
    <tr>
      <td><strong>3. Call-by-Restore / Copy-In Copy-Out</strong></td>
      <td>Actual value is copied in at function entry; final value is copied back out to caller's variable upon function return.</td>
      <td>Behaves like call-by-reference except in cases of variable aliasing.</td>
    </tr>
    <tr>
      <td><strong>4. Call-by-Name (Algol 60)</strong></td>
      <td>The actual argument expression is substituted textually into the callee body as a parameterless function (called a <strong>Thunk</strong>).</td>
      <td>Re-evaluates the argument expression every single time the formal parameter is accessed.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 32 & 33: Runtime Storage Organization & Activation Records</h2>

<p>
  The operating system allocates a continuous block of virtual memory to the executing process, organized into four canonical logical memory segments:
</p>

<div class="diagram-container">
  <svg width="100%" height="90" viewBox="0 0 740 90" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="20" width="150" height="50" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
    <text x="105" y="42" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">Code / Text Segment</text>
    <text x="105" y="56" font-family="Plus Jakarta Sans" font-size="9" fill="#64748b" text-anchor="middle">Read-Only Instructions</text>

    <rect x="190" y="20" width="160" height="50" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="270" y="42" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Static / Global Data</text>
    <text x="270" y="56" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Fixed Compile-Time Data</text>

    <rect x="360" y="20" width="160" height="50" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="440" y="42" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Heap Segment</text>
    <text x="440" y="56" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Grows Downward ($\downarrow$)</text>

    <rect x="530" y="20" width="180" height="50" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="620" y="42" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#581c87" text-anchor="middle">Call Stack (Stack Frames)</text>
    <text x="620" y="56" font-family="Plus Jakarta Sans" font-size="9" fill="#9333ea" text-anchor="middle">Grows Upward ($\uparrow$)</text>
  </svg>
  <div class="diagram-caption">Figure 4.1: Canonical Process Virtual Memory Runtime Layout</div>
</div>

<h3 class="subsection-title">33.1 Exhaustive Anatomy of an Activation Record (Stack Frame):</h3>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Activation Record Field</th>
      <th style="width: 45%;">Internal Purpose & Operational Contents</th>
      <th>Managing Party</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Actual Parameters</strong></td><td>Holds argument values passed from the caller to the callee.</td><td>Caller Routine</td></tr>
    <tr><td><strong>2. Returned Value</strong></td><td>Reserved memory cell where the callee writes the function return result.</td><td>Callee Routine</td></tr>
    <tr><td><strong>3. Control Link (Dynamic Link)</strong></td><td>Pointer pointing to the base address of the <strong>caller's activation record</strong>. Used to restore caller's stack frame upon return.</td><td>Callee Routine</td></tr>
    <tr><td><strong>4. Access Link (Static Link)</strong></td><td>Pointer pointing to the activation record of the <strong>lexical enclosing parent</strong>. Used to resolve non-local variable references.</td><td>Callee Routine</td></tr>
    <tr><td><strong>5. Saved Machine Status</strong></td><td>Preserves CPU Program Counter (PC), CPU registers, stack base pointers, and condition flags prior to procedure invocation.</td><td>Callee Routine</td></tr>
    <tr><td><strong>6. Local Variables</strong></td><td>Stores local scalar variables and fixed-size arrays declared within the procedure body.</td><td>Callee Routine</td></tr>
    <tr><td><strong>7. Temporaries</strong></td><td>Holds intermediate values generated during expression evaluation, array address offsets, and register spills.</td><td>Callee Routine</td></tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: The 7 Fields of an Activation Record (P-R-C-A-S-L-T)</div>
  <strong>P</strong>arameters $\rightarrow$ <strong>R</strong>eturned value $\rightarrow$ <strong>C</strong>ontrol link $\rightarrow$ <strong>A</strong>ccess link $\rightarrow$ <strong>S</strong>aved status $\rightarrow$ <strong>L</strong>ocal data $\rightarrow$ <strong>T</strong>emporaries
</div>

<h2 class="section-title">Topic 34 & 35: Storage Allocation & Non-Local Data Access (Displays)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Storage Strategy</th>
      <th style="width: 45%;">Operating Mechanism</th>
      <th>Advantages & Critical Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Static Allocation</strong></td>
      <td>All memory addresses for all variables and procedures are permanently fixed at compile time (Fortran 77).</td>
      <td>Zero runtime allocation overhead; cannot support recursion or dynamic data structures.</td>
    </tr>
    <tr>
      <td><strong>2. Stack Allocation</strong></td>
      <td>Stack frames are pushed onto the call stack upon procedure call and popped upon procedure return (LIFO).</td>
      <td>Supports unbounded recursion; local variable lifetimes strictly bounded by function lifetime.</td>
    </tr>
    <tr>
      <td><strong>3. Heap Allocation</strong></td>
      <td>Dynamically allocated in arbitrary order (`malloc`/`new`) and reclaimed via explicit `free` or Garbage Collection.</td>
      <td>Enables dynamic data structures (trees, graphs); incurs memory fragmentation and allocation overhead.</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-warning">
  <div class="callout-title">Non-Local Variable Access: Static Links vs. Displays Array Technique</div>
  <ul>
    <li><strong>Access Links (Static Links):</strong> Chained pointer traversal. Accessing a non-local variable defined $k$ lexical nesting levels away requires dereferencing $k$ successive pointers ($O(k)$ time complexity).</li>
    <li><strong>Displays Array:</strong> An auxiliary global array of pointers `d[0..max_depth]` where `d[i]` directly points to the most recently active activation record at lexical nesting depth $i$. Provides guaranteed $\mathbf{O(1)}$ instant access to any non-local variable at any nesting depth!</li>
  </ul>
</div>

<h2 class="section-title">🧠 M4 Active Recall & 10-Question University Exam Master Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain Backpatching with complete Syntax-Directed Translation Scheme for a `while (B) do S` loop. (10 Marks)</div>
  <div class="qa-a">
    <strong>Production:</strong> $S \rightarrow \mathbf{while} \ M_1 \ B \ \mathbf{do} \ M_2 \ S_1$<br>
    <strong>Semantic Action Rules:</strong><br>
    $$\text{backpatch}(S_1.\text{nextlist}, M_1.\text{quad}); \quad \text{// Loop body branches back to condition}$$
    $$\text{backpatch}(B.\text{truelist}, M_2.\text{quad}); \quad \text{// True condition branches into loop body}$$
    $$S.\text{nextlist} = B.\text{falselist}; \quad \text{// False condition exits while loop}$$
    $$\text{emit}(\text{"goto "} M_1.\text{quad}); \quad \text{// Emit unconditional loop back-edge}$$
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Draw and explain the complete anatomy of an Activation Record (Stack Frame) with all 7 fields. (10 Marks)</div>
  <div class="qa-a">
    An Activation Record manages the execution state of a procedure instance. The 7 standard fields are:<br>
    1. <strong>Actual Parameters:</strong> Arguments passed into the procedure.<br>
    2. <strong>Returned Value:</strong> Result returned to caller.<br>
    3. <strong>Control Link (Dynamic Link):</strong> Pointer to caller's activation record for stack unwinding.<br>
    4. <strong>Access Link (Static Link):</strong> Pointer to enclosing static scope for non-local variables.<br>
    5. <strong>Saved Machine Status:</strong> Saved Program Counter, CPU registers, and status flags.<br>
    6. <strong>Local Data:</strong> Local variables declared in procedure body.<br>
    7. <strong>Temporaries:</strong> Temporary evaluation cells for complex expressions.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Compare Call-by-Value, Call-by-Reference, and Call-by-Name parameter passing methods with code examples. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Call-by-Value:</strong> R-value copied to local parameter. Changes inside callee do not affect caller.<br>
    • <strong>Call-by-Reference:</strong> L-value (address) passed directly. Changes inside callee immediately mutate caller's variable.<br>
    • <strong>Call-by-Name:</strong> Argument substituted textually as a parameterless Thunk function. Re-evaluated upon every access.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q4. How does the Displays array technique achieve O(1) access to non-local variables compared to static links? (8 Marks)</div>
  <div class="qa-a">
    Static links require traversing a linked list of $k$ parent pointers ($O(k)$ time). The <strong>Displays</strong> technique maintains a global array `d[i]` pointing directly to the active frame at lexical depth $i$. Any non-local variable at depth $i$ is accessed in single-step dereference `d[i]->offset`, achieving guaranteed $\mathbf{O(1)}$ lookup time!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q5. Explain the Caller and Callee Calling Sequences and register saving conventions in x86-64 / MIPS. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Caller Calling Sequence:</strong> (1) Evaluates actual arguments; (2) Pushes caller-saved registers; (3) Emits `param` instructions; (4) Emits `call` which pushes return address.<br>
    • <strong>Callee Prologue:</strong> (1) Saves old frame pointer (`push rbp`); (2) Sets new frame pointer (`mov rbp, rsp`); (3) Allocates stack space for local variables (`sub rsp, framesize`); (4) Saves callee-saved registers.<br>
    • <strong>Callee Epilogue:</strong> (1) Writes return value to RAX register; (2) Restores callee-saved registers; (3) Restores stack pointer (`mov rsp, rbp; pop rbp`); (4) Emits `ret`.
  </div>
</div>
<h2 class="section-title">Topic 35.2: Comprehensive Worked Control Flow & Runtime Numerical Traces</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 1: Complete Three-Address Code for Nested While Loop</div>
  <p><strong>Source Statement:</strong></p>
  <pre><code>while (i < 10 && j > 0) {
    if (a[i] == b[j]) {
        x = x + 1;
    } else {
        y = y + 1;
    }
    i = i + 1;
    j = j - 1;
}</code></pre>
  <p><strong>Generated Three-Address Code:</strong></p>
  <pre><code>100: if i < 10 goto 102
101: goto 120              ; Exit loop if (i < 10) is False
102: if j > 0 goto 104     ; Check second condition
103: goto 120              ; Exit loop if (j > 0) is False
104: t1 = i * 4            ; Array offset a[i]
105: t2 = a[t1]
106: t3 = j * 4            ; Array offset b[j]
107: t4 = b[t3]
108: if t2 == t4 goto 111
109: goto 114              ; Branch to else-body
110: goto 114
111: t5 = x + 1            ; True-body: x = x + 1
112: x = t5
113: goto 116
114: t6 = y + 1            ; Else-body: y = y + 1
115: y = t6
116: t7 = i + 1            ; Loop step: i = i + 1
117: i = t7
118: t8 = j - 1            ; Loop step: j = j - 1
119: j = t8
120: goto 100              ; Loop back-edge to condition
121: ...                   ; Next statement</code></pre>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 2: Displays Array Non-Local Variable Access Execution Trace</div>
  <p>Consider lexical nesting levels: `Main` (Depth 1) $\rightarrow$ `Procedure P` (Depth 2) $\rightarrow$ `Procedure Q` (Depth 3).</p>
  <p><strong>Displays Array Structure:</strong></p>
  <ul>
    <li>`d[1]` points to active Activation Record of `Main`</li>
    <li>`d[2]` points to active Activation Record of `Procedure P`</li>
    <li>`d[3]` points to active Activation Record of `Procedure Q`</li>
  </ul>
  <p>When `Procedure Q` references variable `x` declared in `Main` (at offset 16 from `Main`'s FP):</p>
  $$\text{Memory Target Address} = \mathbf{d[1] + 16} \quad (\text{Direct } \mathbf{O(1)} \text{ Instant Lookup!})$$
  <p>When `Procedure Q` calls `Procedure R` at depth 2, the old `d[2]` pointer is saved in `R`'s frame and `d[2]` is updated to point to `R`. Upon return, `d[2]` is restored to `P`.</p>
</div>

<div class="qa-card">
  <div class="qa-q">Q6. Compare Static, Stack, and Heap Memory Allocation strategies across 5 dimensions. (10 Marks)</div>
  <div class="qa-a">
    1. <strong>Allocation Timing:</strong> Static is fixed at compile-time; Stack occurs upon function entry (LIFO); Heap occurs on dynamic programmer request (`malloc`).<br>
    2. <strong>Recursion Support:</strong> Static cannot support recursion; Stack handles unbounded recursion seamlessly; Heap supports dynamic object graph structures.<br>
    3. <strong>Data Lifetime:</strong> Static persists for entire program run; Stack is strictly bounded by function return; Heap persists until explicit `free` or Garbage Collection.<br>
    4. <strong>Overhead:</strong> Static has zero runtime overhead; Stack has minimal pointer adjustment (`sub rsp, framesize`); Heap incurs memory fragmentation and allocator search costs.<br>
    5. <strong>Deallocation:</strong> Static is reclaimed on program termination; Stack automatically pops on return; Heap requires explicit deallocation or Garbage Collection.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q7. Explain the Control Link (Dynamic Link) vs. Access Link (Static Link) in Activation Records. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Control Link (Dynamic Link):</strong> Points to the base address of the <strong>caller's activation record</strong>. It reflects the dynamic call history and is used to restore the caller's stack frame pointer upon function return.<br>
    • <strong>Access Link (Static Link):</strong> Points to the activation record of the <strong>lexical enclosing parent procedure</strong> in the source code. It reflects static lexical nesting and is used to resolve non-local variable references at runtime.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q8. Explain Short-Circuit Boolean Evaluation with code generation templates for `if (B) S1 else S2`. (8 Marks)</div>
  <div class="qa-a">
    Short-circuit evaluation stops evaluating boolean expressions as soon as the final truth value is determined.<br>
    <strong>Template for `if (B) S1 else S2`:</strong><br>
    1. Translate boolean condition $B$, generating `B.truelist` and `B.falselist`.<br>
    2. $\text{backpatch}(B.\text{truelist}, \text{label}(S_1))$.<br>
    3. $\text{backpatch}(B.\text{falselist}, \text{label}(S_2))$.<br>
    4. Emit unconditional `goto` at the end of $S_1$ to jump past $S_2$.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q9. How are `switch-case` statements compiled into Three-Address Code? Compare Jump Tables vs. Binary Search Trees. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Linear Comparison Sequence:</strong> Emits sequential `if (E == V) goto L` for $\le 4$ cases ($O(n)$ time).<br>
    • <strong>Jump Table (Direct Array Indexing):</strong> Creates an array of branch targets indexed by $(E - V_{\text{min}})$ for dense integer ranges ($O(1)$ time).<br>
    • <strong>Binary Search Decision Tree:</strong> Emits a balanced binary search comparison tree for large, sparse case values ($O(\log n)$ time).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q10. Explain the Garbage Collection Mark-and-Sweep algorithm for Heap Memory Management. (8 Marks)</div>
  <div class="qa-a">
    The <strong>Mark-and-Sweep</strong> algorithm reclaims unreachable dynamic heap memory in 2 phases:<br>
    1. <strong>Mark Phase:</strong> Starts from Root Set (global variables, stack pointers, CPU registers) and performs a Graph Traversal (DFS/BFS), setting a `marked = true` bit on all reachable heap objects.<br>
    2. <strong>Sweep Phase:</strong> Linearly scans the entire heap space. Unmarked blocks are added to the Free List for future allocation; marked blocks have their mark bits cleared for the next cycle!
  </div>
</div>
<h2 class="section-title">Topic 35.3: Advanced Runtime Memory Management & Parameter Passing Traces</h2>

<p>
  In modern runtime environments, memory allocation and procedure execution depend heavily on the target hardware architecture, CPU calling conventions (such as System V AMD64 ABI), and memory management strategies.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Memory Arena</th>
      <th style="width: 35%;">Hardware Characteristics</th>
      <th style="width: 25%;">Growth Direction</th>
      <th>Management Protocol</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Code / Text</strong></td><td>Read-only, executable pages mapped directly from executable binary.</td><td>Static fixed bounds</td><td>Operating System kernel memory pager.</td></tr>
    <tr><td><strong>Static / Data</strong></td><td>Read-write, global and static variables initialized at compile time.</td><td>Static fixed bounds</td><td>Operating System loader initialization.</td></tr>
    <tr><td><strong>Heap Segment</strong></td><td>Dynamic memory allocated via system calls (`sbrk`, `mmap`).</td><td>Grows Upward ($\uparrow$)</td><td>`malloc`/`free` allocator with Buddy System.</td></tr>
    <tr><td><strong>Call Stack</strong></td><td>LIFO stack frames allocated and freed on function entry and exit.</td><td>Grows Downward ($\downarrow$)</td><td>Hardware Stack Pointer (`rsp`) & Frame Pointer (`rbp`).</td></tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Complete Calling Sequence Machine Code Flow</div>
  <p>Consider a function call `result = calculate(arg1, arg2)` on x86-64 Architecture:</p>
  <pre><code>; 1. CALLER SEQUENCE:
MOV RDI, [rbp - 8]     ; Place actual argument 1 into 1st argument register RDI
MOV RSI, [rbp - 16]    ; Place actual argument 2 into 2nd argument register RSI
CALL calculate         ; Pushes return address (RIP) to stack, jumps to calculate

; 2. CALLEE PROLOGUE:
calculate:
PUSH RBP               ; Save dynamic control link (caller's base pointer)
MOV RBP, RSP           ; Establish new stack frame base pointer
SUB RSP, 32            ; Allocate 32 bytes on stack for local variables and temporaries

; 3. CALLEE BODY & EPILOGUE:
; ... execute procedure instructions ...
MOV RAX, [rbp - 4]     ; Write return value into RAX register
MOV RSP, RBP           ; Deallocate local frame variables
POP RBP                ; Restore caller's base pointer (control link)
RET                    ; Pops return address from stack into RIP register

; 4. CALLER RESUMPTION:
MOV [rbp - 24], RAX    ; Store returned value from RAX into variable result</code></pre>
</div>
<h2 class="section-title">Topic 35.4: Comprehensive Calling Conventions & Dynamic Heap Allocators</h2>

<p>
  A <strong>Calling Convention</strong> defines the low-level binary contract between caller and callee subroutines. It specifies how parameters are passed (registers vs. stack), how return values are delivered, which CPU registers must be preserved across calls (callee-saved vs. caller-saved), and who cleans up the parameter stack space.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Calling Convention</th>
      <th style="width: 38%;">Parameter Passing Mechanism</th>
      <th style="width: 20%;">Stack Cleanup Responsibility</th>
      <th>Representative Platforms</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>cdecl (Standard C)</strong></td>
      <td>All parameters pushed onto stack right-to-left.</td>
      <td><strong>Caller</strong> cleans stack (`add rsp, N`).</td>
      <td>x86 32-bit Linux / Windows C compilers.</td>
    </tr>
    <tr>
      <td><strong>stdcall</strong></td>
      <td>All parameters pushed onto stack right-to-left.</td>
      <td><strong>Callee</strong> cleans stack (`ret N`).</td>
      <td>Windows Win32 API functions.</td>
    </tr>
    <tr>
      <td><strong>fastcall</strong></td>
      <td>First 2 arguments passed in `ECX`, `EDX`; remainder on stack.</td>
      <td><strong>Callee</strong> cleans stack.</td>
      <td>Performance-critical x86 libraries.</td>
    </tr>
    <tr>
      <td><strong>System V AMD64 ABI</strong></td>
      <td>First 6 integer/pointer args in `RDI`, `RSI`, `RDX`, `RCX`, `R8`, `R9`; floats in `XMM0..7`.</td>
      <td><strong>Caller</strong> cleans stack frame.</td>
      <td>x86-64 Linux, macOS, FreeBSD, GCC, Clang.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Buddy System Dynamic Memory Allocation & Merging</div>
  <p>Suppose a runtime heap starts with a single continuous block of size <strong>1024 KB</strong> (addressed from 0 to 1023). Trace allocations and deallocations:</p>
  <ol>
    <li><strong>Request A (Alloc 70 KB):</strong> Smallest power of 2 is $128\text{ KB}$. The $1024\text{ KB}$ block splits into two $512\text{ KB}$ buddies $\rightarrow$ split to $256\text{ KB}$ $\rightarrow$ split to two $128\text{ KB}$ blocks. Block $[0..127]$ is allocated to $A$.</li>
    <li><strong>Request B (Alloc 200 KB):</strong> Smallest power of 2 is $256\text{ KB}$. Block $[256..511]$ is allocated to $B$.</li>
    <li><strong>Request C (Alloc 110 KB):</strong> Smallest power of 2 is $128\text{ KB}$. Remaining buddy block $[128..255]$ is allocated to $C$.</li>
    <li><strong>Free A (Releases $[0..127]$):</strong> Block $[0..127]$ is marked free. Its buddy $[128..255]$ is currently allocated to $C$, so they cannot merge yet.</li>
    <li><strong>Free C (Releases $[128..255]$):</strong> Both buddies $[0..127]$ and $[128..255]$ are now free! They coalesce instantly into a unified $256\text{ KB}$ block $[0..255]$. This new block's buddy $[256..511]$ is occupied by $B$, so coalescing halts.</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: Backpatching Execution Trace for `for` Loop with `break`</div>
  <p><strong>Source Statement:</strong> `for (i = 0; i < 100; i++) { if (a[i] == 0) break; sum += a[i]; }`</p>
  <pre><code>100: i = 0                 ; Initialization
101: if i < 100 goto 103   ; Loop condition
102: goto 112              ; falselist: exits for loop
103: t1 = i * 4            ; Array address offset a[i]
104: t2 = a[t1]
105: if t2 == 0 goto 112   ; break statement: jumps directly to exit label 112
106: goto 107
107: t3 = i * 4
108: t4 = a[t3]
109: sum = sum + t4        ; Loop body
110: i = i + 1             ; Step increment
111: goto 101              ; Back-edge to condition check
112: ...                   ; Target of backpatch(falselist + break_list, 112)</code></pre>
</div>
<h2 class="section-title">Topic 35.5: Object-Oriented Runtime Layout & Virtual Method Tables (Vtables)</h2>

<p>
  In object-oriented languages (such as C++, Java, and C#), member methods may be dynamically overridden in derived subclasses (polymorphism). The compiler realizes <strong>Dynamic Dispatch</strong> via an auxiliary data structure called a <strong>Virtual Method Table (Vtable)</strong>.
</p>

<div class="diagram-container">
  <svg width="100%" height="85" viewBox="0 0 740 85" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="15" width="200" height="55" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="130" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Object Instance in Heap</text>
    <text x="130" y="52" font-family="Plus Jakarta Sans" font-size="9.5" fill="#2563eb" text-anchor="middle">vptr (Offset 0) | Field x | Field y</text>

    <path d="M 230 42 L 310 42" stroke="#0284c7" stroke-width="2"/>

    <rect x="315" y="15" width="230" height="55" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="430" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Vtable in Read-Only Data</text>
    <text x="430" y="52" font-family="Plus Jakarta Sans" font-size="9.5" fill="#16a34a" text-anchor="middle">&Derived::foo() | &Derived::bar()</text>

    <path d="M 545 42 L 610 42" stroke="#0284c7" stroke-width="2"/>

    <rect x="615" y="15" width="105" height="55" rx="6" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="667" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#581c87" text-anchor="middle">Method Code</text>
    <text x="667" y="52" font-family="Plus Jakarta Sans" font-size="9.5" fill="#9333ea" text-anchor="middle">Binary Text</text>
  </svg>
  <div class="diagram-caption">Figure 4.2: Object Instance Memory Layout with Virtual Method Table Pointer (`vptr`)</div>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Dynamic Dispatch Assembly Code Generation</div>
  <p>Consider a polymorphic method call `obj->draw()` where `draw()` is at virtual table index 1 ($8\text{ bytes}$ offset):</p>
  <pre><code>MOV RDI, [rbp - 8]     ; Load obj pointer into 1st argument register RDI (the 'this' pointer)
MOV RAX, [RDI]         ; Dereference obj to fetch its Virtual Table Pointer (vptr)
MOV RAX, [RAX + 8]     ; Fetch address of draw() from Vtable slot 1
CALL RAX               ; Indirect procedure call to the concrete method implementation!</code></pre>
  <p><em>Complexity:</em> Dynamic dispatch executes in guaranteed $\mathbf{O(1)}$ time with only 2 memory dereferences!</p>
</div>

"""
