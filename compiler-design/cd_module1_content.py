# Compiler Design Module 1 Exhaustive Content (12-14 Pages Target)

CD_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Lexical Analysis & Automata Theory — Complete Syllabus Topics</div>
  <div class="toc-grid">
    <div>1. Language Processors (Compiler, Interpreter, Assembler, Preprocessor)</div>
    <div>2. 6 Phases of Compiler Architecture with End-to-End Running Example</div>
    <div>3. Compiler Front-End vs Back-End & Pass Structures</div>
    <div>4. Lexical Analysis Role, Tokens, Patterns & Lexemes</div>
    <div>5. Input Buffering (Two-Buffer Scheme & Sentinels)</div>
    <div>6. Regular Expressions & Regular Definitions for Programming Tokens</div>
    <div>7. Thompson's Construction Algorithm (RE to NFA Step-by-Step)</div>
    <div>8. Subset Construction Algorithm (NFA to DFA Transition Table)</div>
    <div>9. Hopcroft's DFA State Minimization Algorithm (Equivalence Partitioning)</div>
    <div>10. Lex & Flex Lexical Analyzer Generator Specifications</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 3: Language Processing Systems & Compiler Architecture</h2>
<p>
  A <strong>Compiler</strong> is a sophisticated system software that translates a computer program written in a high-level source language (e.g., C, C++, Java) into an equivalent target program in low-level machine code or assembly language, while detecting and reporting diagnostic errors.
</p>

<div class="diagram-container">
  <svg width="100%" height="80" viewBox="0 0 740 80" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="20" width="100" height="40" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="60" y="44" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#1e40af" text-anchor="middle">Preprocessor</text>

    <path d="M 110 40 L 135 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="140" y="15" width="115" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
    <text x="197" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="800" fill="#92400e" text-anchor="middle">Compiler</text>
    <text x="197" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#b45309" text-anchor="middle">Front + Back End</text>

    <path d="M 260 40 L 285 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="290" y="20" width="100" height="40" rx="6" fill="#f0fdf4" stroke="#22c55e"/>
    <text x="340" y="44" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#14532d" text-anchor="middle">Assembler</text>

    <path d="M 395 40 L 420 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="425" y="20" width="135" height="40" rx="6" fill="#faf5ff" stroke="#a855f7"/>
    <text x="492" y="44" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#581c87" text-anchor="middle">Linker / Loader</text>

    <path d="M 565 40 L 590 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="595" y="20" width="135" height="40" rx="6" fill="#ccfbf1" stroke="#0f766e"/>
    <text x="662" y="44" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#0f766e" text-anchor="middle">Target Machine Code</text>
  </svg>
  <div class="diagram-caption">Figure 1.1: Context of a Compiler in Language Processing Pipeline</div>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">System Tool</th>
      <th style="width: 25%;">Input $\rightarrow$ Output</th>
      <th>Primary Responsibilities & Core Functions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Preprocessor</strong></td>
      <td>Raw Source Code $\rightarrow$ Pure Source Code</td>
      <td>Macro expansion (`#define`), file inclusion (`#include`), conditional compilation (`#ifdef`), stripping comments.</td>
    </tr>
    <tr>
      <td><strong>2. Compiler</strong></td>
      <td>Pure Source Code $\rightarrow$ Target Assembly</td>
      <td>Translates high-level syntax into assembly language, performs type checking, syntax validation, intermediate code generation, and optimization.</td>
    </tr>
    <tr>
      <td><strong>3. Assembler</strong></td>
      <td>Assembly Code $\rightarrow$ Relocatable Object Code</td>
      <td>Translates mnemonic assembly instructions into binary machine opcodes and resolves memory offsets.</td>
    </tr>
    <tr>
      <td><strong>4. Linker / Loader</strong></td>
      <td>Object Files + Libs $\rightarrow$ Absolute Executable</td>
      <td><strong>Linker:</strong> Resolves external cross-file symbol references and library routines.<br><strong>Loader:</strong> Loads executable binary into primary RAM, sets up stack/heap memory spaces, and initializes CPU instruction pointer.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2 class="section-title">Topic 2: The 6 Phases of a Compiler (End-to-End Walkthrough)</h2>

<p>
  A compiler operates as a sequence of distinct analytical and synthesis phases. Every phase transforms the source program from one intermediate representation to another, interacting continuously with the <strong>Symbol Table</strong> and <strong>Error Handler</strong>.
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Running Example: Step-by-Step Translation of Statement `position = initial + rate * 60`</div>
  <ol>
    <li><strong>Phase 1: Lexical Analysis (Scanning):</strong>
      <p>Reads raw input character stream and converts into a stream of tokens:</p>
      $$\langle \mathbf{id}, 1 \rangle \ \langle \mathbf{=} \rangle \ \langle \mathbf{id}, 2 \rangle \ \langle \mathbf{+} \rangle \ \langle \mathbf{id}, 3 \rangle \ \langle \mathbf{*} \rangle \ \langle \mathbf{num}, 60 \rangle$$
      <p>Symbol table stores: `1: position (float)`, `2: initial (float)`, `3: rate (float)`.</p>
    </li>
    <li><strong>Phase 2: Syntax Analysis (Parsing):</strong>
      <p>Constructs a hierarchical Syntax Tree enforcing operator precedence ($*$ over $+$):</p>
      <pre><code>      =
     / \
  id1   +
       / \
    id2   *
         / \
      id3  60</code></pre>
    </li>
    <li><strong>Phase 3: Semantic Analysis (Type Checking):</strong>
      <p>Checks static semantic rules, ensuring operand type compatibility. Inserts implicit type conversion node $\text{inttofloat}(60)$:</p>
      <pre><code>      =
     / \
  id1   +
       / \
    id2   *
         / \
      id3  inttofloat(60)</code></pre>
    </li>
    <li><strong>Phase 4: Intermediate Code Generation (ICG):</strong>
      <p>Generates machine-independent Three-Address Code (TAC) with at most one operator per instruction:</p>
      <pre><code>t1 = inttofloat(60)
t2 = id3 * t1
t3 = id2 + t2
id1 = t3</code></pre>
    </li>
    <li><strong>Phase 5: Code Optimization:</strong>
      <p>Performs compile-time constant folding and eliminates temporary variables:</p>
      <pre><code>t1 = id3 * 60.0    -- Constant folded: inttofloat(60) -> 60.0
id1 = id2 + t1</code></pre>
    </li>
    <li><strong>Phase 6: Code Generation (Target Assembly):</strong>
      <p>Emits target machine instructions using hardware CPU registers (`R1`, `R2`):</p>
      <pre><code>LDF   R2, id3      ; Load float rate into R2
MULF  R2, #60.0    ; Multiply R2 by float literal 60.0
LDF   R1, id2      ; Load float initial into R1
ADDF  R1, R2       ; Add R2 to R1
STF   id1, R1      ; Store result into memory position</code></pre>
    </li>
  </ol>
</div>

<div class="page-break"></div>

<h2 class="section-title">Topic 4 & 5: Lexical Analysis & Input Buffering</h2>

<h3 class="subsection-title">1. Fundamental Terminology:</h3>
<ul>
  <li><strong>Token:</strong> An abstract terminal category returned to the parser (e.g., `id`, `num`, `if`, `while`, `assign_op`).</li>
  <li><strong>Pattern:</strong> A formal grammatical specification (regular expression) describing the set of strings representing a token (e.g., `[a-zA-Z_][a-zA-Z0-9_]*`).</li>
  <li><strong>Lexeme:</strong> The concrete sequence of source characters matching the pattern (e.g., `counter_variable`, `1024`, `==`).</li>
</ul>

<h3 class="subsection-title">2. Input Buffering (Two-Buffer Scheme with Sentinels):</h3>
<p>
  Reading one character at a time using direct system calls incurs massive operating system overhead. A <strong>Two-Buffer Scheme</strong> uses two $N$-byte blocks (typically $N=4096$ bytes matching disk blocks) managed by two pointers:
</p>
<ul>
  <li><strong>`lexemeBegin` Pointer:</strong> Marks the beginning of the current token being recognized.</li>
  <li><strong>`forward` Pointer:</strong> Advances ahead character by character until a token pattern boundary is identified.</li>
  <li><strong>Sentinels (`EOF`):</strong> Appending an `EOF` marker at the end of each buffer half avoids making two comparisons per character (one for buffer boundary and one for character matching), accelerating lexer throughput by over $200\%$.</li>
</ul>

<div class="page-break"></div>

<h2 class="section-title">Topic 7: Thompson's Construction Algorithm (RE $\rightarrow$ NFA)</h2>

<p>
  <strong>Thompson's Construction</strong> converts any Regular Expression $r$ into an equivalent Non-Deterministic Finite Automaton ($N(r)$) with $\epsilon$-transitions in linear time $O(|r|)$:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">RE Operation</th>
      <th style="width: 45%;">Thompson's Structural Composition</th>
      <th>Key Structural Invariants</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Basic Symbol ($a$)</strong></td>
      <td>$\text{Start} \xrightarrow{a} \text{Accept}$ (2 states, 1 transition)</td>
      <td>Exactly 1 start state and 1 accept state.</td>
    </tr>
    <tr>
      <td><strong>2. Concatenation ($r_1 r_2$)</strong></td>
      <td>Accept state of $N(r_1)$ merged with start state of $N(r_2)$.</td>
      <td>Flows directly from $N(r_1)$ into $N(r_2)$.</td>
    </tr>
    <tr>
      <td><strong>3. Union / Alternation ($r_1 \mid r_2$)</strong></td>
      <td>New start state branching via $\epsilon$ to $N(r_1)$ and $N(r_2)$; both accept states transition via $\epsilon$ to a new single accept state.</td>
      <td>4 new $\epsilon$-transitions introduced.</td>
    </tr>
    <tr>
      <td><strong>4. Kleene Closure ($r^*$)</strong></td>
      <td>New start state branches via $\epsilon$ to $N(r)$ and bypasses $N(r)$ to accept state; accept state loops back via $\epsilon$ to start of $N(r)$.</td>
      <td>Handles zero or multiple repetitions.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2 class="section-title">Topic 8: Subset Construction Algorithm (NFA $\rightarrow$ DFA)</h2>

<p>
  A Deterministic Finite Automaton (DFA) contains no $\epsilon$-transitions and has at most one outgoing transition per input symbol from any state.
</p>

<div class="callout callout-info">
  <div class="callout-title">Core Operations in Subset Construction</div>
  <ul>
    <li><strong>$\epsilon\text{-closure}(s)$:</strong> Set of all NFA states reachable from state $s$ taking only $\epsilon$-transitions.</li>
    <li><strong>$\epsilon\text{-closure}(T)$:</strong> $\bigcup_{s \in T} \epsilon\text{-closure}(s)$ for a set of states $T$.</li>
    <li><strong>$\text{move}(T, a)$:</strong> Set of all NFA states reachable from any state in $T$ on input symbol $a$.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Convert $(a \mid b)^*abb$ to DFA via Subset Construction</div>
  <p><strong>NFA States:</strong> $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Accept state: $\{10\}$.</p>
  <p><strong>Step 1: Compute Initial DFA State $A = \epsilon\text{-closure}(0) = \{0, 1, 2, 4, 7\}$.</strong></p>
  <p><strong>Step 2: Compute Transitions for DFA States ($D\text{-Tran}$ Table):</strong></p>
  <table class="custom-table">
    <thead>
      <tr><th>DFA State</th><th>NFA State Subset</th><th>Input 'a'</th><th>Input 'b'</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>A</strong> (Start)</td><td>{0, 1, 2, 4, 7}</td><td>B = {1, 2, 3, 4, 6, 7, 8}</td><td>C = {1, 2, 4, 5, 6, 7}</td></tr>
      <tr><td><strong>B</strong></td><td>{1, 2, 3, 4, 6, 7, 8}</td><td>B = {1, 2, 3, 4, 6, 7, 8}</td><td>D = {1, 2, 4, 5, 6, 7, 9}</td></tr>
      <tr><td><strong>C</strong></td><td>{1, 2, 4, 5, 6, 7}</td><td>B = {1, 2, 3, 4, 6, 7, 8}</td><td>C = {1, 2, 4, 5, 6, 7}</td></tr>
      <tr><td><strong>D</strong></td><td>{1, 2, 4, 5, 6, 7, 9}</td><td>B = {1, 2, 3, 4, 6, 7, 8}</td><td>E = {1, 2, 4, 5, 6, 7, 10}</td></tr>
      <tr><td><strong>E*</strong> (Accept)</td><td>{1, 2, 4, 5, 6, 7, 10}</td><td>B = {1, 2, 3, 4, 6, 7, 8}</td><td>C = {1, 2, 4, 5, 6, 7}</td></tr>
    </tbody>
  </table>
</div>

<div class="page-break"></div>

<h2 class="section-title">Topic 9: Hopcroft's DFA Minimization Algorithm</h2>

<p>
  <strong>Hopcroft's Algorithm</strong> finds the unique minimal DFA by iteratively partitioning the set of all DFA states $S$ into disjoint equivalence classes based on behavioral distinguishability:
</p>
<ol>
  <li><strong>Initial Partition ($P_0$):</strong> Divide states into two groups: Accept states ($F$) and Non-Accept states ($S \setminus F$).
    $$P_0 = \{ F, \ S \setminus F \}$$
  </li>
  <li><strong>Refinement Step:</strong> For each group $G \in P$ and each input symbol $a \in \Sigma$, if $\text{move}(s, a)$ for states in $G$ leads into different partitions, split $G$ into sub-partitions.</li>
  <li><strong>Termination:</strong> Repeat refinement until no partition can be further split ($P_{k+1} = P_k$).</li>
  <li><strong>State Compression:</strong> Replace each final partition group with a single representative state in the minimal DFA.</li>
</ol>

<div class="page-break"></div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module I)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the role of Lexical Analyzer and why it is separated from the Parser. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Simplicity of Compiler Design:</strong> Separating lexical scanning from grammatical parsing simplifies both phases. The parser deals with clean token streams rather than raw character-level whitespace, newlines, and comments.<br>
    2. <strong>Compiler Efficiency:</strong> Specialized high-speed buffering techniques can be applied to the lexical scanner. Over 70% of compilation time is spent reading source characters.<br>
    3. <strong>Portability:</strong> Character-set idiosyncrasies (ASCII, UTF-8, Unicode) are isolated strictly inside the lexical phase, making the parser platform-independent.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. State the difference between Compiler and Interpreter across 5 engineering parameters. (6 Marks)</div>
  <div class="qa-a">
    1. <strong>Translation Mechanism:</strong> Compiler translates entire source code into native machine code before execution; Interpreter translates and executes line-by-line at runtime.<br>
    2. <strong>Execution Speed:</strong> Compiled machine code executes 10–50x faster than interpreted bytecode.<br>
    3. <strong>Memory Usage:</strong> Compiler requires memory for object code storage; Interpreter requires memory for runtime engine.<br>
    4. <strong>Error Reporting:</strong> Compiler reports all syntax/semantic errors collectively during compilation; Interpreter stops at the first runtime error encountered.<br>
    5. <strong>Examples:</strong> C, C++, Rust (Compiled); Python, Ruby, PHP (Interpreted).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Describe the structure and working of Lex/Flex tool. (6 Marks)</div>
  <div class="qa-a">
    A Lex program consists of 3 distinct sections separated by `%%` delimiters:<br>
    1. <strong>Definitions Section:</strong> Header includes, declarations, and regular definitions (e.g., `digit [0-9]`).<br>
    2. <strong>Rules Section:</strong> Pairs of regular expressions and corresponding C action code (e.g., `{digit}+ { return NUM; }`).<br>
    3. <strong>User Subroutines Section:</strong> Auxiliary C functions including `main()` and `yywrap()`.<br>
    Lex compiles the specification into a fast transition table-driven DFA scanner named `yylex()`.
  </div>
</div>
"""
