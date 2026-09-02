# Compiler Design Module 4 Exhaustive Content (9 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions

CD_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Intermediate Code & Runtime Environment — Complete 9-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> Complete Evaluation of Boolean Expressions</div>
    <div><strong>Topic 2:</strong> Partial Evaluation (Short-Circuit) of Boolean Expressions</div>
    <div><strong>Topic 3:</strong> Translation of Control Flow Constructs (`if-else`, `while`)</div>
    <div><strong>Topic 4:</strong> Resolution of Forward Jumps & Backpatching Algorithms</div>
    <div><strong>Topic 5:</strong> Resolution of Backward Jumps in Loop Constructs</div>
    <div><strong>Topic 6:</strong> Translation of Function Calls (`param`, `call`, `return_val`)</div>
    <div><strong>Topic 7:</strong> Translation of Function Returns & Caller Restoration</div>
    <div><strong>Topic 8:</strong> Memory Layout of Code and Data (Text, Static, Heap, Stack)</div>
    <div><strong>Topic 9:</strong> Activation Records (Stack Frame Anatomy: P-R-C-A-S-L-T)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Boolean Expressions (Complete vs. Short-Circuit Evaluation)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Evaluation Strategy</th>
      <th style="width: 45%;">Operational Semantics</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Complete Evaluation</strong></td>
      <td>Evaluates all sub-expressions unconditionally before applying logical operators (e.g., bitwise `&` and `|`).</td>
      <td>Evaluates side-effects in all operands; can cause runtime crashes on null-pointer guards (e.g., `p != NULL && p->val == 5`).</td>
    </tr>
    <tr>
      <td><strong>2. Partial Evaluation (Short-Circuit)</strong></td>
      <td>Stops evaluating as soon as the final truth value is guaranteed:<br>
          • In `A && B`: If $A$ is false, $B$ is never evaluated.<br>
          • In `A || B`: If $A$ is true, $B$ is never evaluated.
      </td>
      <td>Highly optimized execution speed; safely handles null-pointer guards and range checks.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 3 – 5: Control Flow Translation & Jump Resolutions</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Three-Address Code for `if (a < b) x = 1; else x = 2;`</div>
  <pre><code>    if a < b goto L1
    goto L2
L1: x = 1
    goto L3
L2: x = 2
L3: /* End of If-Else */</code></pre>
</div>

<h3 class="subsection-title">Backpatching Mechanics (`makelist`, `merge`, `backpatch`):</h3>
<ul>
  <li><strong>Forward Jumps:</strong> Jump targets point to instructions not yet generated. The compiler emits placeholder jumps (`goto ?`) and maintains lists of pending jump instructions.</li>
  <li><strong>Backward Jumps:</strong> Jump targets point to previously emitted labeled instructions (common in loop repeat steps). Target address is immediately known.</li>
  <li><strong>`makelist(i)`:</strong> Creates a new list containing index $i$.</li>
  <li><strong>`merge(p1, p2)`:</strong> Combines two jump lists $p_1$ and $p_2$.</li>
  <li><strong>`backpatch(p, target_label)`:</strong> Fills $target\_label$ as the destination for all jump instructions indexed in list $p$.</li>
</ul>

<h2 class="section-title">Topic 6 & 7: Translation of Function Calls & Returns</h2>

<div class="formula-card">
  <strong>Standard Calling Sequence Three-Address Instructions:</strong>
  For high-level call `x = f(a, b);`:
  <pre><code>param a
param b
call f, 2
t1 = return_value
x = t1</code></pre>
  For function return `return y;`:
  <pre><code>return y</code></pre>
</div>

<h2 class="section-title">Topic 8 & 9: Memory Layout & Activation Records</h2>

<div class="diagram-container">
  <svg width="100%" height="100" viewBox="0 0 740 100" xmlns="http://www.w3.org/2000/svg">
    <rect x="50" y="20" width="130" height="60" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="115" y="45" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Code (Text)</text>
    <text x="115" y="60" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Read-Only Instructions</text>

    <rect x="200" y="20" width="130" height="60" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="265" y="45" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Static / Global</text>
    <text x="265" y="60" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Global Variables</text>

    <rect x="350" y="20" width="160" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="430" y="45" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">Heap Segment (▲)</text>
    <text x="430" y="60" font-family="Plus Jakarta Sans" font-size="9" fill="#b45309" text-anchor="middle">Grows Upward (malloc/new)</text>

    <rect x="530" y="20" width="160" height="60" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="610" y="45" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#581c87" text-anchor="middle">Call Stack (▼)</text>
    <text x="610" y="60" font-family="Plus Jakarta Sans" font-size="9" fill="#9333ea" text-anchor="middle">Grows Downward (Frames)</text>
  </svg>
  <div class="diagram-caption">Figure 4.1: Runtime Memory Address Space Layout</div>
</div>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: Activation Record Anatomy (P-R-C-A-S-L-T)</div>
  <table class="custom-table">
    <thead><tr><th>Field</th><th>Functional Role in Stack Frame</th></tr></thead>
    <tbody>
      <tr><td><strong>P — Parameters</strong></td><td>Actual argument values passed by the caller.</td></tr>
      <tr><td><strong>R — Return Value</strong></td><td>Space allocated to return computation result to caller.</td></tr>
      <tr><td><strong>C — Control Link</strong></td><td>Dynamic link pointing to caller's activation record (restores stack frame on return).</td></tr>
      <tr><td><strong>A — Access Link</strong></td><td>Static link pointing to enclosing lexical scope for resolving non-local variables.</td></tr>
      <tr><td><strong>S — Saved Status</strong></td><td>Saved machine state (Program Counter PC, CPU registers).</td></tr>
      <tr><td><strong>L — Local Variables</strong></td><td>Automatic local variables declared within procedure body.</td></tr>
      <tr><td><strong>T — Temporaries</strong></td><td>Temporary intermediate expression evaluation registers/values.</td></tr>
    </tbody>
  </table>
</div>

<h2 class="section-title">🧠 M4 Active Recall & Exam-Important Question Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the difference between Control Link (Dynamic Link) and Access Link (Static Link) in Activation Records. (8 Marks)</div>
  <div class="qa-a">
    - <strong>Control Link (Dynamic Link):</strong> Points to the activation record of the <em>calling procedure</em> (who called me). It is determined strictly at runtime based on the dynamic execution call stack and is used to restore the caller's stack frame upon return.<br>
    - <strong>Access Link (Static Link):</strong> Points to the activation record of the <em>statically enclosing procedure</em> in the source code text (where was I lexically defined). It is determined at compile time based on lexical block nesting and is used by nested functions to access non-local variables.
  </div>
</div>
"""
