# Compiler Design Module 1 Exhaustive Master Content (Topics 1 to 7)
# Generates 11 to 14 Publication-Grade Pages in Headless Chromium

CD_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Lexical Analysis & Language Translation Systems — 7-Topic Master Syllabus Guide</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> Introduction to Compilers & Language Processing Cousins (P-I-C-A-L)</div>
    <div><strong>Topic 2:</strong> Structure of a Compiler (Analysis Front-End vs. Synthesis Back-End)</div>
    <div><strong>Topic 3:</strong> The Lexical Analyzer (Tokens, Lexemes, Patterns & Error Recovery)</div>
    <div><strong>Topic 4:</strong> Input Buffering Strategies (Two-Buffer Scheme & Sentinel Optimizations)</div>
    <div><strong>Topic 5:</strong> Specification of Tokens (Regular Expressions & Regular Definitions)</div>
    <div><strong>Topic 6:</strong> Recognition of Tokens (Transition Diagrams & Finite Automata)</div>
    <div><strong>Topic 7:</strong> Direct Construction of DFA from RE (Nullable, Firstpos, Lastpos, Followpos)</div>
  </div>
</div>

<h2 class="section-title">Topic 1: Introduction to Compilers & Language Processing Systems</h2>

<p>
  A <strong>Compiler</strong> is a complex computer software system that translates programs written in a high-level source language (such as C, C++, Rust, or Java) into an equivalent low-level target machine language (such as x86-64, ARM assembly, or relocatable binary object code). The fundamental mandate of a compiler is twofold:
</p>
<ol>
  <li><strong>Correctness (Semantic Preservation):</strong> The target machine program must execute with the exact same observable behavior and mathematical semantics as specified by the source code.</li>
  <li><strong>Efficiency (Resource Optimization):</strong> The generated target code must maximize CPU execution throughput, minimize memory footprint, optimize cache utilization, and minimize energy consumption.</li>
</ol>

<div class="diagram-container">
  <svg width="100%" height="85" viewBox="0 0 740 85" xmlns="http://www.w3.org/2000/svg">
    <rect x="15" y="18" width="130" height="50" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="80" y="40" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Source Program</text>
    <text x="80" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">High-Level Syntax</text>

    <path d="M 145 43 L 195 43" stroke="#0284c7" stroke-width="2"/>

    <rect x="200" y="18" width="150" height="50" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="275" y="40" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Compiler System</text>
    <text x="275" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Front-End & Back-End</text>

    <path d="M 350 43 L 400 43" stroke="#0284c7" stroke-width="2"/>

    <rect x="405" y="18" width="150" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="480" y="40" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">Target Program</text>
    <text x="480" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#b45309" text-anchor="middle">Assembly / Object Code</text>

    <path d="M 555 43 L 600 43" stroke="#0284c7" stroke-width="2"/>

    <rect x="605" y="18" width="120" height="50" rx="6" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="665" y="40" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#581c87" text-anchor="middle">Target CPU</text>
    <text x="665" y="54" font-family="Plus Jakarta Sans" font-size="9" fill="#9333ea" text-anchor="middle">Hardware Registers</text>
  </svg>
  <div class="diagram-caption">Figure 1.1: Complete End-to-End Compilation and Hardware Execution Architecture</div>
</div>

<h3 class="subsection-title">1.1 Exhaustive Comparison: Compiler vs. Interpreter vs. Hybrid Systems</h3>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Dimension</th>
      <th style="width: 27%;">Pure Compiler (GCC, Clang, Rustc)</th>
      <th style="width: 27%;">Pure Interpreter (CPython, Ruby)</th>
      <th>Hybrid JIT (JVM HotSpot, V8)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Translation Timing</strong></td>
      <td>Translates the complete codebase into native machine instructions upfront prior to execution.</td>
      <td>Translates and executes instructions statement-by-statement dynamically during runtime.</td>
      <td>Compiles to intermediate bytecode; JIT-compiles hot loops to native machine code at runtime.</td>
    </tr>
    <tr>
      <td><strong>Execution Speed</strong></td>
      <td><strong>Fastest ($1\times$ baseline):</strong> Direct execution on native CPU ALU and registers.</td>
      <td><strong>Slowest ($5\times\text{ to }25\times$ slower):</strong> Software interpretation loop overhead per instruction.</td>
      <td><strong>Near-Native ($1.2\times\text{ to }2\times$):</strong> Profile-guided dynamic native compilation.</td>
    </tr>
    <tr>
      <td><strong>Memory Overhead</strong></td>
      <td>Minimal runtime memory footprint; only the final generated binary resides in memory.</td>
      <td>High memory footprint; the interpreter engine and source AST must both reside in RAM.</td>
      <td>Moderate-to-High; includes JVM/V8 runtime engine, garbage collector, and JIT cache.</td>
    </tr>
    <tr>
      <td><strong>Error Detection</strong></td>
      <td>Detects all lexical, syntactic, and static semantic errors across entire codebase upfront.</td>
      <td>Errors are discovered only when program execution control flow reaches the offending line.</td>
      <td>Detects syntax/type errors during bytecode compilation; runtime exceptions during execution.</td>
    </tr>
    <tr>
      <td><strong>Portability</strong></td>
      <td>Low binary portability; generated binary is tied to specific CPU instruction set architecture (ISA).</td>
      <td>High portability; source script runs on any platform that has the interpreter installed.</td>
      <td><strong>Universal Portability:</strong> "Write Once, Run Anywhere" via standard bytecode execution.</td>
    </tr>
  </tbody>
</table>

<h3 class="subsection-title">1.2 Language Processing Ecosystem ("The Cousins of the Compiler")</h3>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Palace: The P-I-C-A-L Language Transformation Suite</div>
  <strong>P</strong>reprocessor $\longrightarrow$ <strong>I</strong>ntermediate Representation $\longrightarrow$ <strong>C</strong>ompiler $\longrightarrow$ <strong>A</strong>ssembler $\longrightarrow$ <strong>L</strong>inker $\longrightarrow$ <strong>L</strong>oader
</div>

<ol>
  <li><strong>Preprocessor:</strong> Operates as the initial source-to-source text transformation pass prior to compilation:
    <ul>
      <li><em>Macro Expansion:</em> Replaces symbolic macro constants (e.g., `#define BUFFER_SIZE 4096`) with literal values throughout the token stream.</li>
      <li><em>File Inclusion:</em> Replaces header directives (e.g., `#include <stdio.h>`) with the verbatim contents of the header interface file.</li>
      <li><em>Conditional Compilation:</em> Prunes dead code branches guarded by `#ifdef`, `#ifndef`, and `#endif` blocks based on build flags.</li>
      <li><em>Language Extension / Rational Preprocessors:</em> Augments older languages with modern control structures (e.g., Ratfor for Fortran).</li>
    </ul>
  </li>
  <li><strong>Compiler:</strong> Translates preprocessed source code into relocatable assembly language or intermediate representations.</li>
  <li><strong>Assembler:</strong> Translates human-readable symbolic assembly mnemonics (e.g., `MOV [rbp-8], rax`) into relocatable object binary files (`.o`, `.obj`).</li>
  <li><strong>Linker:</strong> Resolves unresolved external symbol references across independent compilation units, binds static libraries (`.a`, `.lib`), and unifies text/data segments into a cohesive executable binary.</li>
  <li><strong>Loader:</strong> Operating system utility that allocates virtual memory pages, copies text and initialized data segments into physical RAM, initializes CPU stack/heap pointers, and sets the Program Counter (PC) to the entry point address (`_start` / `main`).</li>
</ol>

<h2 class="section-title">Topic 2: Structure of a Compiler (The 6 Classical Phases)</h2>

<p>
  A production compiler is divided into two logical sections: the <strong>Analysis Phase (Front-End)</strong>, which is source-language dependent and target-machine independent, and the <strong>Synthesis Phase (Back-End)</strong>, which is target-hardware dependent and source-language independent.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 15%;">Phase #</th>
      <th style="width: 22%;">Compiler Phase</th>
      <th style="width: 25%;">Input $\longrightarrow$ Output</th>
      <th style="width: 23%;">Internal Algorithm</th>
      <th>Key Errors Detected</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Phase 1</strong></td>
      <td><strong>Lexical Analysis (Scanner)</strong></td>
      <td>Character Stream $\longrightarrow$ Token Stream</td>
      <td>Deterministic Finite Automata (DFA), Input Buffering, Regular Expressions</td>
      <td>Illegal characters, invalid identifier prefixes, unclosed string literals.</td>
    </tr>
    <tr>
      <td><strong>Phase 2</strong></td>
      <td><strong>Syntax Analysis (Parser)</strong></td>
      <td>Token Stream $\longrightarrow$ Parse Tree / AST</td>
      <td>Context-Free Grammars, LL(1) Top-Down, LR(1)/LALR(1) Bottom-Up Parsing</td>
      <td>Missing semicolons, mismatched brackets, invalid statement syntax.</td>
    </tr>
    <tr>
      <td><strong>Phase 3</strong></td>
      <td><strong>Semantic Analysis</strong></td>
      <td>AST $\longrightarrow$ Annotated Parse Tree</td>
      <td>Attribute Grammars, Syntax-Directed Definitions, Type Inference Engines</td>
      <td>Type mismatch in assignments, undeclared variables, scope violations.</td>
    </tr>
    <tr>
      <td><strong>Phase 4</strong></td>
      <td><strong>Intermediate Code Generation</strong></td>
      <td>Annotated Tree $\longrightarrow$ Three-Address Code</td>
      <td>Quadruples, Triples, Indirect Triples, Backpatching, AST Linearization</td>
      <td>Invalid jump targets, array bound translation errors.</td>
    </tr>
    <tr>
      <td><strong>Phase 5</strong></td>
      <td><strong>Code Optimization</strong></td>
      <td>TAC $\longrightarrow$ Optimized TAC</td>
      <td>Control Flow Graphs, Basic Block Partitioning, Data-Flow Equations</td>
      <td>Dead code, unreachable basic blocks, redundant subexpressions.</td>
    </tr>
    <tr>
      <td><strong>Phase 6</strong></td>
      <td><strong>Target Code Generation</strong></td>
      <td>Optimized TAC $\longrightarrow$ Target Assembly / Binary</td>
      <td>Instruction Selection, Register Allocation (Graph Coloring), Address Descriptors</td>
      <td>Register spilling, target architecture instruction violations.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete 6-Phase End-to-End Walkthrough of Statement: `total = base + rate * 120`</div>
  <p><strong>Step 1: Lexical Analysis:</strong> Produces token stream and populates Symbol Table:</p>
  $$\langle \text{id}, 1 \rangle \quad \langle = \rangle \quad \langle \text{id}, 2 \rangle \quad \langle + \rangle \quad \langle \text{id}, 3 \rangle \quad \langle * \rangle \quad \langle \text{number}, 120 \rangle$$
  <p><strong>Step 2: Syntax Analysis:</strong> Builds hierarchical Abstract Syntax Tree respecting operator precedence ($* > +$):</p>
  <pre><code>        =
       / \
  id(1)   +
         / \
    id(2)   *
           / \
      id(3)   120</code></pre>
  <p><strong>Step 3: Semantic Analysis:</strong> Performs type checking and inserts explicit type conversion node `inttofloat`:</p>
  <pre><code>        =
       / \
  id(1)   +
         / \
    id(2)   *
           / \
      id(3)   inttofloat(120)</code></pre>
  <p><strong>Step 4: Intermediate Code Generation (Three-Address Code):</strong></p>
  <pre><code>t1 = inttofloat(120)
t2 = id3 * t1
t3 = id2 + t2
id1 = t3</code></pre>
  <p><strong>Step 5: Code Optimization:</strong> Applies Constant Folding and Temporary Variable Reduction:</p>
  <pre><code>t1 = id3 * 120.0     ; Compile-time float conversion
id1 = id2 + t1       ; Direct assignment eliminates t3</code></pre>
  <p><strong>Step 6: Target Code Generation (Target Assembly using registers R1, R2):</strong></p>
  <pre><code>LDF  R2, id3          ; Load floating-point variable id3 into register R2
MULF R2, R2, #120.0    ; Multiply R2 by constant float literal 120.0
LDF  R1, id2          ; Load floating-point variable id2 into register R1
ADDF R1, R1, R2       ; Add R2 into R1
STF  id1, R1          ; Store resulting sum from R1 into memory location id1</code></pre>
</div>

<h2 class="section-title">Topic 3: The Lexical Analyzer (Tokens, Lexemes & Patterns)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Concept</th>
      <th style="width: 45%;">Formal Engineering Definition</th>
      <th>Representative Concrete Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Token</strong></td>
      <td>An abstract grammatical category or terminal symbol used by the parser. Formally defined as an integer ID or pair $\langle \text{token-name}, \text{attribute-value} \rangle$.</td>
      <td>`IDENTIFIER`, `NUMBER_LITERAL`, `KW_IF`, `OP_ASSIGN`, `RELOP`.</td>
    </tr>
    <tr>
      <td><strong>Lexeme</strong></td>
      <td>The concrete, verbatim sequence of characters in the source code matching the pattern for a token.</td>
      <td>`"total"`, `"120"`, `"if"`, `"="`, `"<="`.</td>
    </tr>
    <tr>
      <td><strong>Pattern</strong></td>
      <td>The formal syntactic specification rule (expressed via a Regular Expression) that a lexeme must satisfy.</td>
      <td>`letter (letter | digit)*` for identifiers; `[0-9]+` for integer constants.</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-warning">
  <div class="callout-title">Lexical Error Handling & Recovery Protocols</div>
  When the lexical scanner encounters a character sequence matching zero valid patterns, it executes error recovery:
  <ol>
    <li><strong>Panic Mode Recovery:</strong> Discard successive unmatchable characters until a valid token boundary (whitespace, semicolon) is identified.</li>
    <li><strong>Deleting Extraneous Characters:</strong> Remove an illegal symbol (e.g., transforming `num#ber` to `number`).</li>
    <li><strong>Inserting Missing Characters:</strong> Insert expected delimiters (e.g., supplying missing closing quote in string literal).</li>
    <li><strong>Transposing Adjacent Characters:</strong> Correct common typing slips (e.g., transforming `fi` into `if`).</li>
  </ol>
</div>

<h2 class="section-title">Topic 4: Input Buffering Strategies & The Two-Buffer Scheme</h2>

<p>
  Invoking system calls (`fgetc`, `read`) to process individual characters incurs severe disk I/O performance penalties. Production compilers load source code in <strong>4096-byte blocks</strong> into a unified continuous buffer divided into two halves:
</p>

<div class="diagram-container">
  <svg width="100%" height="90" viewBox="0 0 740 90" xmlns="http://www.w3.org/2000/svg">
    <rect x="50" y="20" width="300" height="45" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="200" y="45" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Buffer 1 (4096 Bytes)</text>
    <rect x="330" y="20" width="20" height="45" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
    <text x="340" y="45" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#991b1b" text-anchor="middle">eof</text>

    <rect x="390" y="20" width="300" height="45" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="540" y="45" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Buffer 2 (4096 Bytes)</text>
    <rect x="670" y="20" width="20" height="45" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
    <text x="680" y="45" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#991b1b" text-anchor="middle">eof</text>

    <path d="M 120 75 L 120 66" stroke="#0284c7" stroke-width="2"/>
    <text x="120" y="86" font-family="Plus Jakarta Sans" font-size="9.5" font-weight="700" fill="#0369a1" text-anchor="middle">lexemeBegin</text>

    <path d="M 230 75 L 230 66" stroke="#0284c7" stroke-width="2"/>
    <text x="230" y="86" font-family="Plus Jakarta Sans" font-size="9.5" font-weight="700" fill="#0369a1" text-anchor="middle">forward</text>
  </svg>
  <div class="diagram-caption">Figure 1.2: Two-Buffer Architecture with Sentinel (`eof`) Optimization</div>
</div>

<h3 class="subsection-title">4.1 Two-Pointer Mechanism:</h3>
<ul>
  <li><strong>`lexemeBegin` Pointer:</strong> Marks the memory address of the first character of the lexeme currently being recognized.</li>
  <li><strong>`forward` Pointer:</strong> Scans ahead through characters until a pattern match or lexical boundary is confirmed.</li>
</ul>

<h3 class="subsection-title">4.2 Sentinel Optimization Algorithm:</h3>
<p>
  In a naive buffer, advancing `forward` requires <strong>two checks per character</strong>: (1) Check if `forward` reached the buffer end, and (2) Test what character is read. By placing a special <strong>Sentinel character (`eof`)</strong> at the end of each buffer half, the algorithm performs only <strong>one test per character</strong> in the common case:
</p>

<pre><code>switch (*forward++) {
    case eof:
        if (forward is at end of Buffer 1) {
            reload Buffer 2;
            forward = beginning of Buffer 2;
        } else if (forward is at end of Buffer 2) {
            reload Buffer 1;
            forward = beginning of Buffer 1;
        } else {
            // True EOF reached: terminate scanning
            terminate_lexical_analysis();
        }
        break;
    case ' ': case '\t': case '\n':
        // Skip whitespace delimiters
        break;
    default:
        // Transition DFA state
        break;
}</code></pre>

<h2 class="section-title">Topic 5 & 6: Specification & Recognition of Tokens</h2>

<div class="formula-card">
  <strong>Formal Regular Expression Algebraic Operators:</strong>
  1. <strong>Alternation (Union):</strong> $r \mid s = L(r) \cup L(s)$
  2. <strong>Concatenation:</strong> $rs = \{ xy \mid x \in L(r), y \in L(s) \}$
  3. <strong>Kleene Closure:</strong> $r^* = \bigcup_{i=0}^\infty L(r)^i$ (Zero or more occurrences, includes $\epsilon$)
  4. <strong>Positive Closure:</strong> $r^+ = r r^* = \bigcup_{i=1}^\infty L(r)^i$ (One or more occurrences)
  5. <strong>Optional:</strong> $r? = r \mid \epsilon$
</div>

<h3 class="subsection-title">Lexical Specification Definitions (Regular Definitions):</h3>
<pre><code>digit       -> [0-9]
digits      -> digit+
letter      -> [a-zA-Z_]
id          -> letter (letter | digit)*
number      -> digits (. digits)? (E [+-]? digits)?
relop       -> < | <= | = | <> | > | >=</code></pre>

<h3 class="subsection-title">6.1 Lex / Flex Lexical Analyzer Generator Architecture</h3>
<p>
  A Lex source file (`lexer.l`) consists of three distinct sections separated by `%%` delimiter lines:
</p>
<pre><code>%{
/* C Declarations Section: Header includes, token definitions, global variables */
#include "y.tab.h"
#include <stdio.h>
int line_num = 1;
%}

/* Regular Definitions Section: Shorthands for complex patterns */
digit       [0-9]
letter      [a-zA-Z_]
id          {letter}({letter}|{digit})*
ws          [ \t]+

%%
/* Translation Rules Section: Pattern-Action pairs */
{ws}            { /* Discard whitespace */ }
"\n"            { line_num++; }
"if"            { return KEYWORD_IF; }
"else"          { return KEYWORD_ELSE; }
{id}            { yylval.str = strdup(yytext); return IDENTIFIER; }
{digit}+        { yylval.val = atoi(yytext); return INTEGER_LITERAL; }
"=="            { return OP_EQ; }
"<="            { return OP_LE; }
"="             { return OP_ASSIGN; }
.               { printf("Lexical Error at line %d: %s\n", line_num, yytext); }

%%
/* User Subroutines Section: Auxiliary C helper functions */
int yywrap() { return 1; }</code></pre>

<h2 class="section-title">Topic 7: Direct Construction of DFA from Regular Expressions</h2>

<p>
  Rather than converting a regular expression to an NFA via Thompson's Construction and then determinizing via Subset Construction ($O(2^n)$ intermediate states), compilers use the <strong>Syntax-Tree Direct Method</strong> (McNaughton-Yamada-Thompson Algorithm).
</p>

<div class="callout callout-info">
  <div class="callout-title">The 4 Fundamental Positional Functions</div>
  Augment regular expression $r$ with unique end-marker `#`: $(r)\#$. Construct syntax tree where each alphabet symbol is a leaf with unique integer position $i$.
  <ul>
    <li><strong>$\text{nullable}(n)$ (Boolean):</strong> Returns true if subexpression rooted at node $n$ can generate the empty string $\epsilon$.</li>
    <li><strong>$\text{firstpos}(n)$ (Set of Positions):</strong> Set of leaf positions that can match the <em>first character</em> of a string generated by the subexpression at node $n$.</li>
    <li><strong>$\text{lastpos}(n)$ (Set of Positions):</strong> Set of leaf positions that can match the <em>last character</em> of a string generated by the subexpression at node $n$.</li>
    <li><strong>$\text{followpos}(i)$ (Set of Positions):</strong> Set of leaf positions $j$ that can immediately follow position $i$ in some valid string in $L((r)\#)$.</li>
  </ul>
</div>

<h3 class="subsection-title">7.1 Inductive Calculation Rules for Node Functions:</h3>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 15%;">Node Type $n$</th>
      <th style="width: 22%;">$\text{nullable}(n)$</th>
      <th style="width: 31%;">$\text{firstpos}(n)$</th>
      <th>$\text{lastpos}(n)$</th>
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
      <td><strong>Leaf position $i$</strong></td>
      <td>$\text{false}$</td>
      <td>$\{i\}$</td>
      <td>$\{i\}$</td>
    </tr>
    <tr>
      <td><strong>Or Node: $c_1 \mid c_2$</strong></td>
      <td>$\text{nullable}(c_1) \vee \text{nullable}(c_2)$</td>
      <td>$\text{firstpos}(c_1) \cup \text{firstpos}(c_2)$</td>
      <td>$\text{lastpos}(c_1) \cup \text{lastpos}(c_2)$</td>
    </tr>
    <tr>
      <td><strong>Cat Node: $c_1 \cdot c_2$</strong></td>
      <td>$\text{nullable}(c_1) \wedge \text{nullable}(c_2)$</td>
      <td>$\begin{cases} \text{firstpos}(c_1) \cup \text{firstpos}(c_2) & \text{if } \text{nullable}(c_1) \\ \text{firstpos}(c_1) & \text{otherwise} \end{cases}$</td>
      <td>$\begin{cases} \text{lastpos}(c_1) \cup \text{lastpos}(c_2) & \text{if } \text{nullable}(c_2) \\ \text{lastpos}(c_2) & \text{otherwise} \end{cases}$</td>
    </tr>
    <tr>
      <td><strong>Star Node: $c_1^*$</strong></td>
      <td>$\text{true}$</td>
      <td>$\text{firstpos}(c_1)$</td>
      <td>$\text{lastpos}(c_1)$</td>
    </tr>
  </tbody>
</table>

<div class="formula-card">
  <strong>The 2 Rules for Computing $\text{followpos}(i)$:</strong>
  1. <strong>Cat Node Rule ($n = c_1 \cdot c_2$):</strong> For every position $i \in \text{lastpos}(c_1)$, add all positions in $\text{firstpos}(c_2)$ to $\text{followpos}(i)$.
  2. <strong>Star Node Rule ($n = c_1^*$):</strong> For every position $i \in \text{lastpos}(c_1)$, add all positions in $\text{firstpos}(c_1)$ to $\text{followpos}(i)$.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Direct DFA for $(a \mid b)^*abb\#$</div>
  <p><strong>Step 1: Leaf Position Assignment:</strong></p>
  $$\text{Expression: } (a_1 \mid b_2)^* \cdot a_3 \cdot b_4 \cdot b_5 \cdot \#_6$$
  <p><strong>Step 2: Followpos Calculation Table:</strong></p>
  <table class="custom-table">
    <thead><tr><th>Node Position $i$</th><th>Symbol</th><th>Computed $\text{followpos}(i)$ Set</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>$a$</td><td>$\{1, 2, 3\}$ (from star node on $(a_1 \mid b_2)$ and concatenation with $a_3$)</td></tr>
      <tr><td>2</td><td>$b$</td><td>$\{1, 2, 3\}$ (from star node on $(a_1 \mid b_2)$ and concatenation with $a_3$)</td></tr>
      <tr><td>3</td><td>$a$</td><td>$\{4\}$ (from concatenation $a_3 \cdot b_4$)</td></tr>
      <tr><td>4</td><td>$b$</td><td>$\{5\}$ (from concatenation $b_4 \cdot b_5$)</td></tr>
      <tr><td>5</td><td>$b$</td><td>$\{6\}$ (from concatenation $b_5 \cdot \#_6$)</td></tr>
      <tr><td>6</td><td>$\#$</td><td>$\emptyset$ (End marker)</td></tr>
    </tbody>
  </table>

  <p><strong>Step 3: DFA State Transitions Computation:</strong></p>
  <ul>
    <li><strong>Start State $A = \text{firstpos}(\text{root}) = \{1, 2, 3\}$:</strong>
      <ul>
        <li>$\text{DTran}[A, a] = \text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3\} \cup \{4\} = \{1, 2, 3, 4\} \implies \mathbf{B}$</li>
        <li>$\text{DTran}[A, b] = \text{followpos}(2) = \{1, 2, 3\} \implies \mathbf{A}$</li>
      </ul>
    </li>
    <li><strong>State $B = \{1, 2, 3, 4\}$:</strong>
      <ul>
        <li>$\text{DTran}[B, a] = \text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3, 4\} \implies \mathbf{B}$</li>
        <li>$\text{DTran}[B, b] = \text{followpos}(2) \cup \text{followpos}(4) = \{1, 2, 3, 5\} \implies \mathbf{C}$</li>
      </ul>
    </li>
    <li><strong>State $C = \{1, 2, 3, 5\}$:</strong>
      <ul>
        <li>$\text{DTran}[C, a] = \text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3, 4\} \implies \mathbf{B}$</li>
        <li>$\text{DTran}[C, b] = \text{followpos}(2) \cup \text{followpos}(5) = \{1, 2, 3, 6\} \implies \mathbf{D} \ (\text{Accepting State!})$</li>
      </ul>
    </li>
    <li><strong>State $D = \{1, 2, 3, 6\}$ (contains position $6 = \#$):</strong>
      <ul>
        <li>$\text{DTran}[D, a] = \text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3, 4\} \implies \mathbf{B}$</li>
        <li>$\text{DTran}[D, b] = \text{followpos}(2) = \{1, 2, 3\} \implies \mathbf{A}$</li>
      </ul>
    </li>
  </ul>

  <p><strong>Step 4: Final DFA Transition Table:</strong></p>
  <table class="custom-table">
    <thead><tr><th>DFA State</th><th>Positions in State</th><th>Input $a$</th><th>Input $b$</th><th>Accepting?</th></tr></thead>
    <tbody>
      <tr><td><strong>$A$ (Start)</strong></td><td>$\{1, 2, 3\}$</td><td>$B$</td><td>$A$</td><td>No</td></tr>
      <tr><td><strong>$B$</strong></td><td>$\{1, 2, 3, 4\}$</td><td>$B$</td><td>$C$</td><td>No</td></tr>
      <tr><td><strong>$C$</strong></td><td>$\{1, 2, 3, 5\}$</td><td>$B$</td><td>$D$</td><td>No</td></tr>
      <tr><td><strong>$D$ (Final)</strong></td><td>$\{1, 2, 3, 6\}$</td><td>$B$</td><td>$A$</td><td><strong>YES (Token Recognized)</strong></td></tr>
    </tbody>
  </table>
</div>

<h3 class="subsection-title">7.2 DFA State Minimization (Hopcroft's Partitioning Algorithm)</h3>
<p>
  Once a DFA is synthesized, it may contain redundant equivalent states. <strong>Hopcroft's Algorithm</strong> computes the unique minimal-state DFA in $O(|V| \log |V|)$ time by iteratively partitioning states:
</p>
<div class="formula-card">
  <strong>Hopcroft Partitioning Procedure:</strong>
  1. Initialize partition $P = \{F, S - F\}$ into Final (Accepting) and Non-Final states.
  2. For each group $G \in P$ and each input symbol $a \in \Sigma$, check if state transitions $\delta(s, a)$ land in different groups of $P$.
  3. If transitions diverge, split $G$ into sub-groups. Repeat until no group in $P$ can be further partitioned (Fixed-Point Convergence).
</div>

<h2 class="section-title">🧠 M1 Active Recall & 10-Question University Exam Master Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the 6 phases of a compiler with an end-to-end trace of statement `a = b + c * 50`. (10 Marks)</div>
  <div class="qa-a">
    <strong>1. Lexical Analysis:</strong> $\langle \text{id}, a \rangle \ \langle = \rangle \ \langle \text{id}, b \rangle \ \langle + \rangle \ \langle \text{id}, c \rangle \ \langle * \rangle \ \langle \text{num}, 50 \rangle$.<br>
    <strong>2. Syntax Analysis:</strong> Generates hierarchical AST with $* > +$.<br>
    <strong>3. Semantic Analysis:</strong> Inserts `inttofloat(50)` for type compatibility.<br>
    <strong>4. Intermediate Code:</strong> Emits TAC: `t1 = inttofloat(50)`, `t2 = c * t1`, `t3 = b + t2`, `a = t3`.<br>
    <strong>5. Code Optimization:</strong> Folds constant: `t1 = c * 50.0`, `a = b + t1`.<br>
    <strong>6. Code Generation:</strong> Generates assembly using registers R1, R2.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Differentiate between Lexeme, Token, and Pattern with 3 concrete examples. (5 Marks)</div>
  <div class="qa-a">
    • <strong>Pattern:</strong> The formal grammatical specification (RE), e.g., `[a-zA-Z_][a-zA-Z0-9_]*`.<br>
    • <strong>Lexeme:</strong> The concrete source character sequence matching the pattern, e.g., `"total_score"`.<br>
    • <strong>Token:</strong> The abstract integer symbol passed to parser, e.g., `IDENTIFIER`.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Why is Input Buffering necessary in lexical analyzers? Explain the Two-Buffer scheme with Sentinels. (8 Marks)</div>
  <div class="qa-a">
    Reading single characters via system calls creates massive disk I/O bottlenecks. The Two-Buffer scheme loads 4096-byte blocks alternately. Sentinels (`eof` markers placed at block boundaries) reduce 2 checks per character down to 1 check in the common case, increasing scanner throughput by over $300\%$.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q4. Construct the Direct DFA for regular expression $(a \mid b)^*a(a \mid b)$ using syntax-tree positions. (10 Marks)</div>
  <div class="qa-a">
    Augment: $(a_1 \mid b_2)^* \cdot a_3 \cdot (a_4 \mid b_5) \cdot \#_6$.<br>
    $\text{firstpos}(\text{root}) = \{1, 2, 3\}$.<br>
    $\text{followpos}(1)=\{1,2,3\}, \text{followpos}(2)=\{1,2,3\}, \text{followpos}(3)=\{4,5\}, \text{followpos}(4)=\{6\}, \text{followpos}(5)=\{6\}$.<br>
    DFA States: $A=\{1,2,3\}, B=\{1,2,3,4,5\}, C=\{1,2,3,6\}, D=\{1,2,3,4,5,6\}$. Accepting states: $C$ and $D$.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q5. Explain the role of the Symbol Table and Error Handler throughout the 6 compiler phases. (8 Marks)</div>
  <div class="qa-a">
    The <strong>Symbol Table</strong> is a shared data structure storing identifier names, types, scopes, memory offsets, and parameter signatures. It is populated by the Lexical/Syntax phases and queried by Semantic/Code Gen phases. The <strong>Error Handler</strong> catches phase-specific errors, recovers state, and emits accurate line numbers and diagnostic messages.
  </div>
</div>
<h2 class="section-title">Topic 7.3: Comprehensive Automata & Theory Worked Examples</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Thompson's NFA Construction for $(a \mid b)^*abb$</div>
  <p><strong>Step 1: Subexpression NFAs:</strong> Construct 2-state NFAs for symbols $a$ and $b$.</p>
  <p><strong>Step 2: Alternation $(a \mid b)$:</strong> Introduce new start and accept states with $\epsilon$-transitions branching to $a$ and $b$.</p>
  <p><strong>Step 3: Kleene Star $(a \mid b)^*$:</strong> Introduce new start/accept states with feedback and bypass $\epsilon$-transitions.</p>
  <p><strong>Step 4: Concatenation:</strong> Chain with sequential NFAs for $a$, $b$, and $b$ to reach final accepting state.</p>
</div>

<div class="qa-card">
  <div class="qa-q">Q6. Compare Compiler and Interpreter across execution speed, memory consumption, error localization, and portability. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Execution Speed:</strong> Compilers generate direct native hardware instructions ($1\times$ baseline); Interpreters interpret instructions line-by-line with interpretation overhead ($5\times\text{ to }20\times$ slower).<br>
    • <strong>Memory:</strong> Compilers require memory only for generated binary during execution; Interpreters require the interpreter runtime engine and source AST to reside in memory.<br>
    • <strong>Error Localization:</strong> Compilers report all syntax/type errors across the entire program before execution; Interpreters report errors dynamically only when control flow reaches the faulting statement.<br>
    • <strong>Portability:</strong> Compilers generate machine-dependent binaries; Interpreters allow source code to run unmodified across any hardware platform.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q7. Explain the Lex/Flex specification file format and internal scanning mechanism with a complete C token scanner example. (10 Marks)</div>
  <div class="qa-a">
    A Lex file contains 3 sections: Declarations (`%{ ... %}`), Translation Rules (`pattern { action }`), and User C Subroutines (`main()`, `yywrap()`). When compiled by `lex`, it emits `lex.yy.c`, which contains `yylex()`. `yylex()` utilizes a deterministic finite automaton transition matrix to match the longest valid prefix of characters against declared patterns, setting `yytext` to the matching string and `yyleng` to its character length.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q8. What are Regular Definitions? Write regular definitions for Unsigned Numbers and Identifiers in Pascal/C. (6 Marks)</div>
  <div class="qa-a">
    A <strong>Regular Definition</strong> is a sequence of definitions of the form: $d_1 \rightarrow r_1, d_2 \rightarrow r_2, \dots, d_n \rightarrow r_n$ where each $r_i$ is a regular expression over $\Sigma \cup \{d_1, \dots, d_{i-1}\}$.<br>
    <pre><code>digit       -> [0-9]
digits      -> digit+
optional_fraction -> (. digits)?
optional_exponent -> (E [+-]? digits)?
num         -> digits optional_fraction optional_exponent
letter_     -> [A-Za-z_]
id          -> letter_ (letter_ | digit)*</code></pre>
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q9. Explain the Hopcroft DFA Minimization algorithm with state partitioning trace for a 5-state DFA. (10 Marks)</div>
  <div class="qa-a">
    Hopcroft's algorithm initializes partition $P = \{F, S - F\}$. It repeatedly selects a group $G$ and an input symbol $a$, checking if $\delta(s, a)$ splits $G$ into states transitioning into different target groups. If so, $G$ is replaced by its split sub-groups. The process terminates when no group can be further partitioned, producing the unique minimal DFA.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q10. Explain Lexical Error Recovery strategies: Panic Mode, Character Deletion, Insertion, and Transposition. (8 Marks)</div>
  <div class="qa-a">
    When no regular expression pattern matches the remaining input prefix:<br>
    1. <strong>Panic Mode:</strong> Scans ahead, discarding invalid characters until a recognizable token boundary (e.g. whitespace, semicolon) is found.<br>
    2. <strong>Character Deletion:</strong> Removes an extraneous unmatchable character from the input stream.<br>
    3. <strong>Character Insertion:</strong> Inserts an expected missing delimiter (such as a closing quote on a single-line string literal).<br>
    4. <strong>Character Transposition:</strong> Swaps two adjacent out-of-order characters to fix common typographical slips (e.g. `teh` $\rightarrow$ `the`).
  </div>
</div>
"""
