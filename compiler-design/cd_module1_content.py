# Compiler Design Module 1 Exhaustive Content (7 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions

CD_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Lexical Analysis — Complete 7-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> Introduction to Compilers & Its Cousins (P-I-C-A-L)</div>
    <div><strong>Topic 2:</strong> Structure of a Compiler (Phases, Symbol Table, Errors)</div>
    <div><strong>Topic 3:</strong> Lexical Analyzer (Token, Lexeme, Pattern Triad)</div>
    <div><strong>Topic 4:</strong> Input Buffering (Two-Buffer Scheme, Sentinels)</div>
    <div><strong>Topic 5:</strong> Specification of Tokens (Regular Expressions & Operators)</div>
    <div><strong>Topic 6:</strong> Recognition of Tokens (Transition Diagrams & DFA)</div>
    <div><strong>Topic 7:</strong> DFA Directly from Regular Expressions (FLF Rules)</div>
    <div><strong>Exam Prep:</strong> Active Recall Check & Exam-Important Questions</div>
  </div>
</div>

<h2 class="section-title">Topic 1: Introduction to Compilers and its Cousins</h2>

<h3 class="subsection-title">1. What is a Compiler?</h3>
<p>
  A <strong>compiler</strong> is a specialized software program that translates a source program written in a high-level language into an equivalent target program, usually in machine code or assembly language.
</p>
<pre><code>High-Level Language (C, C++, Java) ---> [ COMPILER ] ---> Target Machine / Assembly Code</code></pre>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Parameter</th>
      <th style="width: 37%;">Compiler</th>
      <th>Interpreter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Translation Mode</strong></td>
      <td>Translates the entire source program into target machine code before execution.</td>
      <td>Translates and executes the source program statement-by-statement at runtime.</td>
    </tr>
    <tr>
      <td><strong>Execution Speed</strong></td>
      <td>Very fast target execution once compiled (standalone binary).</td>
      <td>Slower execution due to continuous interpretation overhead.</td>
    </tr>
    <tr>
      <td><strong>Memory Requirement</strong></td>
      <td>Generates intermediate object files; requires memory for full compilation.</td>
      <td>Minimal initial memory; does not produce a standalone object binary.</td>
    </tr>
    <tr>
      <td><strong>Error Reporting</strong></td>
      <td>Reports all syntactic & semantic errors after full program scan.</td>
      <td>Halts execution at the very first line containing an error.</td>
    </tr>
  </tbody>
</table>

<h3 class="subsection-title">2. Cousins of the Compiler (Language Processing Ecosystem):</h3>
<ul>
  <li><strong>1. Preprocessor:</strong> Handles source-level directives before compilation (e.g., `#include`, `#define` macro expansion, file inclusion, conditional compilation `#ifdef`).</li>
  <li><strong>2. Assembler:</strong> Translates human-readable assembly mnemonics (e.g., `MOV R1, R2`) into relocatable binary machine code.</li>
  <li><strong>3. Linker:</strong> Resolves external cross-file symbol references and links external precompiled library binaries into a single executable module.</li>
  <li><strong>4. Loader:</strong> Dynamically loads the executable binary into physical RAM, allocates stack/heap segments, adjusts relocatable memory addresses, and initializes the CPU Program Counter (PC).</li>
</ul>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: P-I-C-A-L</div>
  <strong>P</strong>reprocessor $\rightarrow$ <strong>C</strong>ompiler $\rightarrow$ <strong>A</strong>ssembler $\rightarrow$ <strong>L</strong>inker $\rightarrow$ <strong>L</strong>oader
</div>

<h2 class="section-title">Topic 2: Structure of a Compiler (Front End vs. Back End)</h2>

<div class="diagram-container">
  <svg width="100%" height="85" viewBox="0 0 740 85" xmlns="http://www.w3.org/2000/svg">
    <rect x="15" y="15" width="130" height="55" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="80" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">1. Lexical Analysis</text>
    <text x="80" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Character -> Tokens</text>

    <path d="M 145 42 L 165 42" stroke="#0284c7" stroke-width="2"/>

    <rect x="170" y="15" width="130" height="55" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="235" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">2. Syntax Analysis</text>
    <text x="235" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Parse Tree Generation</text>

    <path d="M 300 42 L 320 42" stroke="#0284c7" stroke-width="2"/>

    <rect x="325" y="15" width="130" height="55" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="390" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">3. Semantic Analysis</text>
    <text x="390" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Type Checking & SDD</text>

    <path d="M 455 42 L 475 42" stroke="#0284c7" stroke-width="2"/>

    <rect x="480" y="15" width="120" height="55" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="540" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">4. Intermediate Code</text>
    <text x="540" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Three-Address Code</text>

    <path d="M 600 42 L 615 42" stroke="#0284c7" stroke-width="2"/>

    <rect x="620" y="15" width="105" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="672" y="38" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#92400e" text-anchor="middle">5. Code Gen & Opt</text>
    <text x="672" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#b45309" text-anchor="middle">Assembly Target</text>
  </svg>
  <div class="diagram-caption">Figure 1.1: The 6 Classical Phases of Compilation with Symbol Table & Error Handler Support</div>
</div>

<h3 class="subsection-title">Cross-Phase Supporting Components:</h3>
<ol>
  <li><strong>Symbol Table Management:</strong> A centralized data structure (e.g., chained hash table) storing variable and function identifiers, data types, memory offsets, scope levels, and register assignments.</li>
  <li><strong>Error Detection & Handling:</strong> Detects lexical errors (invalid characters), syntax errors (mismatched parentheses), and semantic errors (type mismatches) and provides recovery mechanisms to continue parsing without crashing.</li>
</ol>

<h2 class="section-title">Topic 3: Lexical Analyzer (Tokens, Lexemes, Patterns)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Concept</th>
      <th style="width: 35%;">Definition</th>
      <th>Concrete Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Token</strong></td>
      <td>An abstract syntactic category/class passed to the parser.</td>
      <td>`IDENTIFIER`, `NUMBER`, `ASSIGN_OP`, `KEYWORD`</td>
    </tr>
    <tr>
      <td><strong>Lexeme</strong></td>
      <td>The actual concrete sequence of characters in the source code matching a pattern.</td>
      <td>`count`, `100`, `=`, `while`</td>
    </tr>
    <tr>
      <td><strong>Pattern</strong></td>
      <td>The formal grammar/regular expression rule describing valid lexemes.</td>
      <td>`letter(letter|digit)*`, `[0-9]+`</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Example: Lexical Tokenization Breakdown for `count = 25;`</div>
  <table class="custom-table">
    <thead><tr><th>Lexeme</th><th>Token Name</th><th>Attribute Value (Symbol Table Pointer / Numeric Constant)</th></tr></thead>
    <tbody>
      <tr><td>`count`</td><td>`IDENTIFIER`</td><td>Pointer to Symbol Table entry for `count`</td></tr>
      <tr><td>`=`</td><td>`ASSIGN_OP`</td><td>None</td></tr>
      <tr><td>`25`</td><td>`NUMBER`</td><td>Integer value `25`</td></tr>
      <tr><td>`;`</td><td>`SEMICOLON`</td><td>None</td></tr>
    </tbody>
  </table>
</div>

<h2 class="section-title">Topic 4: Input Buffering (Two-Buffer Scheme & Sentinels)</h2>

<p>
  Reading one character at a time directly from secondary storage causes severe I/O bottlenecks. Lexical analyzers use an <strong>Input Buffering</strong> scheme with block reads:
</p>

<div class="diagram-container">
  <svg width="100%" height="90" viewBox="0 0 740 90" xmlns="http://www.w3.org/2000/svg">
    <rect x="50" y="20" width="300" height="40" fill="#f8fafc" stroke="#64748b" stroke-width="1.5"/>
    <text x="200" y="45" font-family="Fira Code" font-size="11" fill="#334155" text-anchor="middle">| c | o | u | n | t |   | = |   | eof |</text>
    <text x="200" y="15" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">Buffer 1 (Size N)</text>

    <rect x="390" y="20" width="300" height="40" fill="#f8fafc" stroke="#64748b" stroke-width="1.5"/>
    <text x="540" y="45" font-family="Fira Code" font-size="11" fill="#334155" text-anchor="middle">| 2 | 5 | ; |   |   |   |   |   | eof |</text>
    <text x="540" y="15" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">Buffer 2 (Size N)</text>

    <path d="M 70 75 L 70 62" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="70" y="87" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#dc2626" text-anchor="middle">lexemeBegin</text>

    <path d="M 175 75 L 175 62" stroke="#16a34a" stroke-width="2"/>
    <text x="175" y="87" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#16a34a" text-anchor="middle">forward</text>
  </svg>
  <div class="diagram-caption">Figure 1.2: Two-Buffer Scheme with lexemeBegin and forward pointers & eof Sentinels</div>
</div>

<ul>
  <li><strong>`lexemeBegin` Pointer:</strong> Marks the start of the current lexeme being recognized.</li>
  <li><strong>`forward` Pointer:</strong> Scans ahead one character at a time until a token boundary is identified.</li>
  <li><strong>Sentinels (`eof`):</strong> Appending an `eof` character at the end of each buffer reduces two boundary tests per character (end of buffer check + EOF check) down to a single test.</li>
</ul>

<h2 class="section-title">Topic 5 & 6: Specification & Recognition of Tokens</h2>

<div class="callout callout-info">
  <div class="callout-title">Regular Expression Operators & Precedence</div>
  <ol>
    <li><strong>Kleene Star ($*$):</strong> Zero or more repetitions (Highest Precedence).</li>
    <li><strong>Concatenation:</strong> Sequence of symbols (Medium Precedence).</li>
    <li><strong>Alternation ($|$):</strong> Logical OR / choice (Lowest Precedence).</li>
  </ol>
</div>

<h2 class="section-title">Topic 7: DFA Directly from Regular Expressions (Direct Method)</h2>

<p>
  The Direct Method constructs a minimal DFA directly from an augmented regular expression $(r)\#$ without generating an intermediate Thompson NFA.
</p>

<div class="callout callout-warning">
  <div class="callout-title">The 4 Fundamental Functions: `nullable`, `firstpos`, `lastpos`, `followpos`</div>
  <table class="custom-table">
    <thead>
      <tr>
        <th style="width: 20%;">Node Type $n$</th>
        <th style="width: 20%;">`nullable(n)`</th>
        <th style="width: 30%;">`firstpos(n)`</th>
        <th>`lastpos(n)`</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Leaf $\epsilon$</strong></td>
        <td>$\text{true}$</td>
        <td>$\emptyset$</td>
        <td>$\emptyset$</td>
      </tr>
      <tr>
        <td><strong>Leaf Position $i$</strong></td>
        <td>$\text{false}$</td>
        <td>$\{i\}$</td>
        <td>$\{i\}$</td>
      </tr>
      <tr>
        <td><strong>OR: $c_1 \mid c_2$</strong></td>
        <td>`nullable(c1) || nullable(c2)`</td>
        <td>$\text{firstpos}(c_1) \cup \text{firstpos}(c_2)$</td>
        <td>$\text{lastpos}(c_1) \cup \text{lastpos}(c_2)$</td>
      </tr>
      <tr>
        <td><strong>Cat: $c_1 \cdot c_2$</strong></td>
        <td>`nullable(c1) && nullable(c2)`</td>
        <td>$\text{if nullable}(c_1) \text{ then } \text{firstpos}(c_1) \cup \text{firstpos}(c_2) \text{ else } \text{firstpos}(c_1)$</td>
        <td>$\text{if nullable}(c_2) \text{ then } \text{lastpos}(c_1) \cup \text{lastpos}(c_2) \text{ else } \text{lastpos}(c_2)$</td>
      </tr>
      <tr>
        <td><strong>Star: $c_1^*$</strong></td>
        <td>$\text{true}$</td>
        <td>$\text{firstpos}(c_1)$</td>
        <td>$\text{lastpos}(c_1)$</td>
      </tr>
    </tbody>
  </table>
  <p><strong>`followpos(i)` Invariant Rules:</strong></p>
  <ol>
    <li>For Cat node $n = c_1 \cdot c_2$: For every position $i \in \text{lastpos}(c_1)$, $\text{followpos}(i) = \text{followpos}(i) \cup \text{firstpos}(c_2)$.</li>
    <li>For Star node $n = c_1^*$: For every position $i \in \text{lastpos}(c_1)$, $\text{followpos}(i) = \text{followpos}(i) \cup \text{firstpos}(c_1)$.</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Direct DFA Construction for $(a \mid b)^* a b b \#$</div>
  <p><strong>Step 1: Assign Position Indices:</strong> $(a_1 \mid b_2)^* \cdot a_3 \cdot b_4 \cdot b_5 \cdot \#_6$</p>
  <p><strong>Step 2: Compute `followpos` Table:</strong></p>
  <table class="custom-table">
    <thead><tr><th>Node Position $i$</th><th>Symbol</th><th>`followpos(i)`</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>$a$</td><td>$\{1, 2, 3\}$</td></tr>
      <tr><td>2</td><td>$b$</td><td>$\{1, 2, 3\}$</td></tr>
      <tr><td>3</td><td>$a$</td><td>$\{4\}$</td></tr>
      <tr><td>4</td><td>$b$</td><td>$\{5\}$</td></tr>
      <tr><td>5</td><td>$b$</td><td>$\{6\}$</td></tr>
      <tr><td>6</td><td>$\#$</td><td>$\emptyset$</td></tr>
    </tbody>
  </table>
  <p><strong>Step 3: DFA States & Transitions:</strong></p>
  <ul>
    <li>$S_0 = \text{firstpos}(\text{root}) = \{1, 2, 3\}$</li>
    <li>$\delta(S_0, a) = \text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3, 4\} = S_1$</li>
    <li>$\delta(S_0, b) = \text{followpos}(2) = \{1, 2, 3\} = S_0$</li>
    <li>$\delta(S_1, a) = \text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3, 4\} = S_1$</li>
    <li>$\delta(S_1, b) = \text{followpos}(2) \cup \text{followpos}(4) = \{1, 2, 3, 5\} = S_2$</li>
    <li>$\delta(S_2, b) = \text{followpos}(2) \cup \text{followpos}(5) = \{1, 2, 3, 6\} = S_3 \ (\text{Accepting, since } 6 \in S_3)$</li>
  </ul>
</div>

<h2 class="section-title">🧠 M1 Active Recall & Exam-Important Question Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the 6 phases of a compiler with a neat translation diagram for the statement `position = initial + rate * 60`. (10 Marks)</div>
  <div class="qa-a">
    1. <strong>Lexical Analysis:</strong> Produces token stream: $\langle \mathbf{id}_1 \rangle \ \langle = \rangle \ \langle \mathbf{id}_2 \rangle \ \langle + \rangle \ \langle \mathbf{id}_3 \rangle \ \langle * \rangle \ \langle \mathbf{60} \rangle$.<br>
    2. <strong>Syntax Analysis:</strong> Builds parse tree showing operator precedence ($*$ over $+$).<br>
    3. <strong>Semantic Analysis:</strong> Checks types and inserts `inttofloat(60)` conversion.<br>
    4. <strong>Intermediate Code Generation:</strong> Emits Three-Address Code:<br>
       `t1 = inttofloat(60); t2 = id3 * t1; t3 = id2 + t2; id1 = t3`<br>
    5. <strong>Code Optimization:</strong> Constant propagation & strength reduction: `t1 = id3 * 60.0; id1 = id2 + t1`<br>
    6. <strong>Code Generation:</strong> Emits target assembly: `LDF R2, id3; MULF R2, #60.0; ADDF R2, id2; STF id1, R2`.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain the Two-Buffer scheme and the role of Sentinels in input buffering. (8 Marks)</div>
  <div class="qa-a">
    - <strong>Two-Buffer Scheme:</strong> Uses two contiguous blocks of size $N$ in memory. While the scanner processes characters in Buffer 1 using `lexemeBegin` and `forward` pointers, Buffer 2 can be asynchronously filled via a single system I/O read call.<br>
    - <strong>Role of Sentinels:</strong> Without sentinels, testing every character requires two comparisons: (1) `if (forward == buffer_end)` and (2) test character. Placing an `eof` sentinel at the end of each buffer reduces this to a single check: only when an `eof` character is encountered does the scanner check whether it has reached a buffer boundary or the genuine end of the source file.
  </div>
</div>
"""
