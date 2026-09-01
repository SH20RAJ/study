# 🏛️ Compiler Design (CS24301) — Module 1: Lexical Analysis
**B.Tech Computer Science & Engineering (NEP Scheme) | BIT Mesra**

---

## 📌 Table of Contents
1. [Introduction to Language Processing Systems & Compilers](#1-introduction-to-language-processing-systems--compilers)
   - [1.1 Language Processors & Cousins of the Compiler](#11-language-processors--cousins-of-the-compiler)
   - [1.2 Compiler vs. Interpreter](#12-compiler-vs-interpreter)
   - [1.3 Structure & Phases of a Compiler](#13-structure--phases-of-a-compiler)
   - [1.4 Trace of Compilation: A Concrete Example](#14-trace-of-compilation-a-concrete-example)
   - [1.5 Compiler-Construction Tools](#15-compiler-construction-tools)
2. [Role and Mechanics of the Lexical Analyzer](#2-role-and-mechanics-of-the-lexical-analyzer)
   - [2.1 Lexical Analyzer Interface with Parser](#21-lexical-analyzer-interface-with-parser)
   - [2.2 Tokens, Patterns, and Lexemes](#22-tokens-patterns-and-lexemes)
   - [2.3 Attributes for Tokens](#23-attributes-for-tokens)
   - [2.4 Lexical Errors & Error Recovery Strategies](#24-lexical-errors--error-recovery-strategies)
3. [Input Buffering Techniques](#3-input-buffering-techniques)
   - [3.1 Motivation & Single-Character I/O Bottlenecks](#31-motivation--single-character-io-bottlenecks)
   - [3.2 Buffer Pairs Scheme](#32-buffer-pairs-scheme)
   - [3.3 Sentinel Characters Strategy](#33-sentinel-characters-strategy)
4. [Specification & Recognition of Tokens](#4-specification--recognition-of-tokens)
   - [4.1 Formal Language Preliminaries](#41-formal-language-preliminaries)
   - [4.2 Regular Expressions & Regular Definitions](#42-regular-expressions--regular-definitions)
   - [4.3 Finite Automata: NFA vs. DFA](#43-finite-automata-nfa-vs-dfa)
   - [4.4 Thompson's Construction Algorithm (RE $\rightarrow$ NFA)](#44-thompsons-construction-algorithm-re--nfa)
   - [4.5 Subset Construction Algorithm (NFA $\rightarrow$ DFA)](#45-subset-construction-algorithm-nfa--dfa)
   - [4.6 DFA State Minimization (Hopcroft's Partitioning Algorithm)](#46-dfa-state-minimization-hopcrofts-partitioning-algorithm)
5. [Direct DFA Construction from Regular Expressions (Syntax Tree Method)](#5-direct-dfa-construction-from-regular-expressions-syntax-tree-method)
   - [5.1 Augmented Regular Expressions & Syntax Trees](#51-augmented-regular-expressions--syntax-trees)
   - [5.2 Formal Functions: `nullable`, `firstpos`, `lastpos`, and `followpos`](#52-formal-functions-nullable-firstpos-lastpos-and-followpos)
   - [5.3 Direct DFA Construction Algorithm](#53-direct-dfa-construction-algorithm)
   - [5.4 Solved Master Numerical Walkthrough 1: $(a|b)^*abb\#$](#54-solved-master-numerical-walkthrough-1-abb)
   - [5.5 Solved Master Numerical Walkthrough 2: $(a|b)^*a(a|b)\#$](#55-solved-master-numerical-walkthrough-2-aab)
6. [High-Yield Exam Question Bank & Solved Numerical Problems](#6-high-yield-exam-question-bank--solved-numerical-problems)
7. [Quick Revision Formula Sheet & Exam Pitfalls](#7-quick-revision-formula-sheet--exam-pitfalls)

---

## 1. Introduction to Language Processing Systems & Compilers

A **compiler** is a specialized computer program that translates a source program written in a high-level programming language (such as C, C++, Java, or Rust) into an equivalent target program written in a low-level language (such as assembly language or machine code), while diagnosing and reporting any syntactic or semantic errors present in the source program.

```
+----------------+      +------------+      +----------------+
| Source Program | ---> |  COMPILER  | ---> | Target Program |
+----------------+      +------------+      +----------------+
                              |
                              v
                      [ Error Messages ]
```

---

### 1.1 Language Processors & Cousins of the Compiler

A compiler rarely operates in total isolation. In modern operating environments, the compiler forms the central engine of an integrated **Language Processing System**:

```
[ Source Program (.c / .cpp) ]
              |
              v
     +-----------------+
     |  PREPROCESSOR   |  <-- Handles #include, #define, macro expansions, conditional compilation
     +-----------------+
              |
              v [ Modified / Pure Source Code (.i) ]
     +-----------------+
     |    COMPILER     |  <-- Translates pure source code into assembly language
     +-----------------+
              |
              v [ Assembly Code (.s / .asm) ]
     +-----------------+
     |    ASSEMBLER    |  <-- Translates assembly mnemonics into relocatable machine code
     +-----------------+
              |
              v [ Relocatable Object Code (.o / .obj) ]
     +-----------------+
     | LINKER / LOADER |  <-- Resolves external symbols/libraries; loads into physical memory
     +-----------------+
              |
              v
[ Absolute Machine Code / Executable (.exe / .out / ELF) ]
```

#### The Cousins of the Compiler in Detail:

1. **Preprocessor:**
   - **Function:** Operates on the raw source file prior to translation. It strips comments, expands macros (e.g., `#define PI 3.14159`), includes referenced header files (e.g., `#include <stdio.h>`), and evaluates conditional compilation directives (`#ifdef`, `#ifndef`).
   - **Output:** Modified (pure) high-level source code.

2. **Compiler:**
   - **Function:** Performs end-to-end analysis of the pure source program (lexical, syntactic, and semantic checking) and synthesizes target assembly code.
   - **Output:** Assembly code (`.s`).

3. **Assembler:**
   - **Function:** Translates assembly language mnemonics (e.g., `MOV`, `ADD`, `JMP`) into binary machine instructions, allocating relative memory offsets for variables and labels.
   - **Output:** Relocatable object code (`.o` or `.obj`).

4. **Linker (Linkage Editor):**
   - **Function:** Modern programs are divided into multiple modules and utilize precompiled standard libraries (e.g., `printf` in `libc`). The linker resolves external memory references between different object files, combines multiple relocatable object files into a single unified binary, and calculates absolute/relative memory offsets.
   - **Output:** Executable target program (e.g., ELF on Linux, PE on Windows).

5. **Loader:**
   - **Function:** The operating system component that reads executable machine code from secondary storage (SSD/HDD), allocates primary memory (RAM), initializes registers, sets up stack and heap segments, and jumps to the entry point (`main()`) to commence execution.

---

### 1.2 Compiler vs. Interpreter

Language processors generally fall into two broad execution paradigms:

| Metric / Parameter | Compiler | Interpreter |
| :--- | :--- | :--- |
| **Basic Mechanism** | Translates the entire source program into machine code in one unified process before execution. | Translates and executes the source program statement-by-statement (line-by-line) at runtime. |
| **Intermediate Object Code** | Generates standalone machine/object code (`.exe`, `.o`). | Does **not** produce an independent target object file. |
| **Execution Speed** | Much faster runtime execution since compilation is done beforehand. | Slower runtime execution due to continuous interpretation overhead. |
| **Memory Requirement** | Requires substantial memory during compilation; target binary runs with minimal overhead. | Requires interpreter to reside in memory continuously during runtime. |
| **Error Diagnostics** | Reports all syntactic and semantic errors after scanning the entire source code. | Stops execution at the very first erroneous line encountered. |
| **Debugging Convenience** | Harder to debug runtime state directly without dedicated debug symbols (`gdb`). | Easier interactive debugging and rapid prototyping. |
| **Examples** | C, C++, Rust, Go, Fortran. | Python, Ruby, PHP, JavaScript, Perl. |

> **Hybrid Approach (e.g., Java, C#/.NET):**
> Java source code (`.java`) is first compiled by `javac` into intermediate, platform-independent **Bytecode** (`.class`). The Java Virtual Machine (JVM) then interprets this bytecode or employs a **Just-In-Time (JIT) Compiler** to compile hot execution paths directly into native machine instructions at runtime.

---

### 1.3 Structure & Phases of a Compiler

The compilation process is logically divided into two primary super-phases:
1. **Analysis Phase (Front-End):** Analyzes the source program, breaks it down into constituent parts, checks grammar/semantics, and builds an intermediate representation. It is **machine-independent** and language-dependent.
2. **Synthesis Phase (Back-End):** Takes the intermediate representation and constructs the target machine code, optimizing for register usage, instruction pipelining, and memory efficiency. It is **machine-dependent** and language-independent.

```
                           +------------------------+
                           |     Source Program     |
                           +------------------------+
                                       |
                                       v
                           +------------------------+
 [PHASE 1: FRONT-END] ---> |    Lexical Analyzer    | <---+
                           +------------------------+     |
                                       | Token Stream     |
                                       v                  |
 [PHASE 2: FRONT-END] ---> |    Syntax Analyzer     | <---+
                           +------------------------+     |
                                       | Parse Tree / AST |
                                       v                  |
 [PHASE 3: FRONT-END] ---> |   Semantic Analyzer    | <---+
                           +------------------------+     |
                                       | Decorated AST    |    +--------------------+
                                       v                  |    |                    |
 [PHASE 4: FRONT-END] ---> | Intermediate Code Gen  | <---+--->|    SYMBOL TABLE    |
                           +------------------------+     |    |     MANAGEMENT     |
                                       | 3-Address Code   |    |                    |
                                       v                  |    +--------------------+
 [PHASE 5: BACK-END]  ---> |     Code Optimizer     | <---+             ^
                           +------------------------+     |             |
                                       | Optimized 3AC    |             v
                                       v                  |    +--------------------+
 [PHASE 6: BACK-END]  ---> |     Code Generator     | <---+--->|   ERROR HANDLING   |
                           +------------------------+     |    |      ROUTINES      |
                                       |                  |    +--------------------+
                                       v                  |
                           +------------------------+     |
                           |  Target Machine Code   | <---+
                           +------------------------+
```

#### Detailed Breakdown of the 6 Phases:

1. **Phase 1: Lexical Analysis (Scanning):**
   - Reads the raw input character stream from left to right.
   - Groups characters into meaningful character sequences called **lexemes**.
   - Produces a stream of output **tokens** of the form `<token-name, attribute-value>`.
   - Strips whitespace, tabs, newlines, and comments.

2. **Phase 2: Syntax Analysis (Parsing):**
   - Imposes a hierarchical grammatical structure on the token stream using a Context-Free Grammar (CFG).
   - Produces a **Parse Tree** or **Abstract Syntax Tree (AST)**.
   - Verifies whether the tokens obey the language syntax rules and reports syntax errors.

3. **Phase 3: Semantic Analysis (Type Checking):**
   - Uses the syntax tree and the symbol table to check the source program for semantic consistency with the language definition.
   - Performs **Type Checking** (e.g., verifying operands are compatible with operators).
   - Performs **Type Coercion** (automatic type conversions, such as converting an integer to a floating-point number).

4. **Phase 4: Intermediate Code Generation (ICG):**
   - Translates the decorated AST into an explicit, low-level or medium-level machine-independent intermediate representation (IR), most commonly **Three-Address Code (TAC)**.
   - TAC instructions have at most one operator on the right-hand side, forcing the compiler to generate explicit temporary variables.

5. **Phase 5: Code Optimization:**
   - Transforms the intermediate code to make it faster, shorter, and consume less power/memory without altering program semantics.
   - Techniques include: Constant Folding, Constant Propagation, Common Subexpression Elimination, Dead Code Elimination, and Loop-Invariant Code Motion.

6. **Phase 6: Target Code Generation:**
   - Maps the intermediate instructions into target machine assembly or binary instructions.
   - Involves crucial tasks: **Instruction Selection**, **Register Allocation & Assignment**, and memory offset resolution.

#### Supporting Subsystems:
- **Symbol Table:** A centralized data structure (usually a hash table) maintaining records for each identifier (variable name, function name, array name) along with attributes like data type, memory offset, scope level, line number, and function parameter signatures.
- **Error Handler:** Invoked when flaws are detected during any phase. Ensures meaningful error messages with line numbers are reported and attempts error recovery to allow compilation to proceed.

---

### 1.4 Trace of Compilation: A Concrete Example

Consider the high-level assignment statement:
$$\text{position} = \text{initial} + \text{rate} * 60$$

Let us trace its transformation through every phase of the compiler:

```
[SOURCE STATEMENT]: position = initial + rate * 60
                         |
                         v
[PHASE 1: LEXICAL ANALYZER]
  Tokens: <id, 1> <=> <id, 2> <+> <id, 3> <*> <int_const, 60>
  (Symbol Table updated: 1->position, 2->initial, 3->rate)
                         |
                         v
[PHASE 2: SYNTAX ANALYZER (PARSER)]
  Constructs Syntax Tree:
            =
          /   \
      <id,1>   +
             /   \
         <id,2>   *
                /   \
            <id,3>   60
                         |
                         v
[PHASE 3: SEMANTIC ANALYZER]
  (Detects 60 is integer, but 'rate' is float -> inserts inttofloat type conversion)
            =
          /   \
      <id,1>   +
             /   \
         <id,2>   *
                /   \
            <id,3>  inttofloat
                        |
                        60
                         |
                         v
[PHASE 4: INTERMEDIATE CODE GENERATOR (3AC)]
  t1 = inttofloat(60)
  t2 = id3 * t1
  t3 = id2 + t2
  id1 = t3
                         |
                         v
[PHASE 5: CODE OPTIMIZER]
  (Constant folding converts 60 to 60.0 directly at compile time; eliminates temporary t3)
  t1 = id3 * 60.0
  id1 = id2 + t1
                         |
                         v
[PHASE 6: TARGET CODE GENERATOR (Target Assembly)]
  LDF   R2, id3           ; Load 'rate' into float register R2
  MULF  R2, R2, #60.0     ; R2 = R2 * 60.0
  LDF   R1, id2           ; Load 'initial' into float register R1
  ADDF  R1, R1, R2        ; R1 = R1 + R2
  STF   id1, R1           ; Store result into 'position'
```

---

### 1.5 Compiler-Construction Tools

Modern compiler writers use specialized, highly automated software tools to generate compiler phases:

1. **Scanner Generators (e.g., Lex, Flex):** Produce lexical analyzers from regular expression specifications.
2. **Parser Generators (e.g., Yacc, Bison, ANTLR):** Produce syntax analyzers from context-free grammar specifications (LALR(1), LL(k)).
3. **Syntax-Directed Translation Engines:** Traverse parse trees to produce intermediate code based on associated semantic action rules.
4. **Automatic Code Generators:** Translate intermediate code into target machine code using pattern-matching tree-rewriting rules.
5. **Dataflow Analysis Engines:** Facilitate complex code optimization routines (reaching definitions, live variables, available expressions).

---

## 2. Role and Mechanics of the Lexical Analyzer

The **Lexical Analyzer (Scanner)** is the first phase of a compiler. Its primary duty is to read the source program's input stream of individual characters, translate them into a sequence of meaningful tokens, and deliver them to the parser on demand.

```
                  +------------------+
                  |  Source Program  |
                  +------------------+
                            | (Character Stream)
                            v
+--------+   getNextToken()   +------------------+   Symbol Table
| Parser | <================= | Lexical Analyzer | <=============> [ Symbol Table ]
+--------+       Token        +------------------+
```

### Additional Secondary Tasks of the Lexical Analyzer:
1. **Stripping Comments and Whitespace:** Eliminates unnecessary blanks, tabs, newline characters, and source comments (`// ...` or `/* ... */`).
2. **Correlating Error Messages:** Tracks line numbers and column numbers to output pinpointed compiler error messages (e.g., `Error at line 42: invalid identifier`).
3. **Macro Expansion:** In some compilers, handles simple macro replacements.
4. **Case Normalization:** Converts uppercase to lowercase in case-insensitive languages.

---

### 2.2 Tokens, Patterns, and Lexemes

These three terms are foundational in compiler design and must be clearly distinguished:

```
+-----------------------------------------------------------------------------------+
| TERM     | DEFINITION                                                             |
+----------+------------------------------------------------------------------------+
| TOKEN    | An abstract terminal symbol used by the parser (e.g., id, if, number). |
| PATTERN  | The formal rule / regular expression describing the set of lexemes.    |
| LEXEME   | The concrete, actual string of source characters matching the pattern. |
+-----------------------------------------------------------------------------------+
```

#### Detailed Comparison Table with Concrete Examples:

| Category | Token Name | Informal / Formal Pattern | Example Matching Lexemes |
| :--- | :--- | :--- | :--- |
| **Keyword** | `IF`, `ELSE`, `WHILE` | Literal character sequences: `if`, `else`, `while` | `if`, `else`, `while` |
| **Relational Op** | `RELOP` | `< \| <= \| == \| <> \| > \| >=` | `<`, `<=`, `==`, `<>`, `>`, `>=` |
| **Identifier** | `ID` | `letter (letter \| digit)*` | `count`, `x`, `total_sum`, `temp2` |
| **Integer Literal**| `INT_CONST` | `digit+` | `0`, `42`, `1024`, `999` |
| **Float Literal**  | `FLOAT_CONST` | `digit+ . digit+ (E [+-]? digit+)?` | `3.14159`, `0.5`, `6.02E23` |
| **String Literal** | `STR_CONST` | `" ( [^"\\] \| \\. )* "` | `"Hello, World!"`, `"Result = %d\n"` |
| **Punctuation**   | `SEMICOLON`, `COMMA`| Literal `;` or `,` | `;`, `,` |

---

### 2.3 Attributes for Tokens

When more than one lexeme can match a single token pattern (such as the token `ID` matching variable names `count`, `sum`, or `rate`), the parser cannot rely solely on the token name. The lexical analyzer must supply an **attribute value** to unambiguously identify the lexeme:

$$\text{Token Structure: } \langle \text{Token Name}, \text{Attribute Value} \rangle$$

- For keywords (e.g., `while`), the token name `WHILE` is sufficient; no attribute value is required.
- For identifiers (`ID`), the attribute value is a **pointer to the Symbol Table entry** where details of the identifier (spelling, type, memory location) are stored.
- For constants (`INT_CONST`), the attribute value is the literal numeric value or a pointer to a constant table.

```
Example: E = M * C ** 2
Tokens emitted:
  < ID, ptr_to_symbol_table("E") >
  < ASSIGN_OP >
  < ID, ptr_to_symbol_table("M") >
  < MULT_OP >
  < ID, ptr_to_symbol_table("C") >
  < EXPON_OP >
  < INT_CONST, 2 >
```

---

### 2.4 Lexical Errors & Error Recovery Strategies

A **lexical error** occurs when the scanner encounters a character sequence that cannot be matched to any defined token pattern.

**Examples of Lexical Errors:**
- An unrecognized character: `x = 10 $ 5;` (the `$` symbol is not part of the language alphabet).
- Misspelled keyword: `whlie (x > 0)` (if treated strictly as an unrecognized keyword).
- Unclosed string literal: `"Hello World;` (missing closing quote before EOF).

#### Error Recovery Strategies Employed by the Scanner:
1. **Panic Mode Recovery:** Discard successive characters from the input stream until the scanner reaches a well-known delimiter (such as a whitespace or semicolon) where scanning can cleanly resume.
2. **Deleting Extraneous Characters:** If an illegal character appears (e.g., `x = 10 $ 5;`), remove `$` and continue tokenizing.
3. **Inserting a Missing Character:** If a delimiter or quote is missing, insert the expected character.
4. **Replacing an Incorrect Character:** Replace an invalid character with an adjacent valid candidate.
5. **Transposing Adjacent Characters:** Swap two adjacent characters (e.g., correcting `hte` to `the` or `>=` typed incorrectly).

---

## 3. Input Buffering Techniques

### 3.1 Motivation & Single-Character I/O Bottlenecks
Source code files are stored on secondary disk drives. Reading the source code character-by-character using system-level I/O calls (`getc()`) incurs massive operating system interrupt overhead.

To maximize throughput, the compiler uses **block buffering**: large blocks of characters (typically 4096 bytes, matching disk block sizes) are loaded into RAM in a single system read call.

---

### 3.2 Buffer Pairs Scheme

To look ahead and recognize tokens (such as determining whether `<` is followed by `=` to form `<=`, or followed by a letter to form just `<`), the scanner must frequently look ahead past the current character.

The **Buffer Pairs** scheme uses two matching buffers of size $N$ (e.g., $N = 4096$ bytes):

```
Buffer 1 (Size N)                   Buffer 2 (Size N)
+---+---+---+---+---+---+---+---+   +---+---+---+---+---+---+---+---+
| c | o | u | n | t |   | = |   |   | 1 | 0 | ; |   |   |   |   |   |
+---+---+---+---+---+---+---+---+   +---+---+---+---+---+---+---+---+
  ^                   ^
  |                   |
lexeme_beginning    forward
```

- **Pointers:**
  1. `lexeme_beginning`: Points to the start of the current lexeme being recognized.
  2. `forward`: Scans ahead until a pattern match is confirmed.
- **Buffer Reload Cycle:**
  - If `forward` moves past the end of Buffer 1, Buffer 2 is read into from the source file, and `forward` wraps around to the start of Buffer 2.
  - If `forward` moves past the end of Buffer 2, Buffer 1 is reloaded, and `forward` wraps around to Buffer 1.

---

### 3.3 Sentinel Characters Strategy

Without optimization, every time `forward` is advanced, the scanner must execute **two conditional tests**:
1. Check if `forward` has reached the end of the current buffer (to trigger reload).
2. Check what character `*forward` actually is (to match token pattern).

```c
// Standard Unoptimized Loop: 2 tests per character!
if (forward >= buffer_end) {
    reload_buffer();
    forward = buffer_start;
}
c = *forward++;
process_char(c);
```

#### The Sentinel Solution:
We place a special non-source sentinel character, **`EOF`**, at the very end of each buffer half:

```
Buffer 1 (Size N + 1)                 Buffer 2 (Size N + 1)
+---+---+---+---+---+---+---+-----+   +---+---+---+---+---+---+---+-----+
| c | o | u | n | t |   | = | EOF |   | 1 | 0 | ; |   |   |   |   | EOF |
+---+---+---+---+---+---+---+-----+   +---+---+---+---+---+---+---+-----+
                              ^
                              | (Sentinel EOF triggers buffer boundary handling)
```

Now, the inner loop requires **only ONE test** per character in the common case:

```c
// Optimized Sentinel Loop: ONLY 1 test per character!
switch (*forward++) {
    case EOF:
        if (forward is at end of Buffer 1) {
            reload Buffer 2;
            forward = start of Buffer 2;
        } else if (forward is at end of Buffer 2) {
            reload Buffer 1;
            forward = start of Buffer 1;
        } else {
            // Truly the end of the source file
            terminate_lexical_analysis();
        }
        break;
    
    // Normal character handling continues here...
    case '+': ...
    case '*': ...
}
```

> **Performance Gain:** For a 100,000-character source file, sentinels eliminate 100,000 pointer-boundary comparisons, dramatically boosting scanner throughput.

---

## 4. Specification & Recognition of Tokens

### 4.1 Formal Language Preliminaries

1. **Alphabet ($\Sigma$):** A finite, non-empty set of symbols.
   - Example: $\Sigma = \{0, 1\}$ (Binary), $\Sigma = \{a, b, \dots, z\}$ (English lowercase).
2. **String (Word):** A finite sequence of symbols chosen from $\Sigma$.
   - **Empty String ($\epsilon$):** The string of length zero ($|\epsilon| = 0$).
   - **String Length ($|s|$):** Number of symbol occurrences in $s$ (e.g., $|banana| = 6$).
3. **String Terms & Operations:**
   - **Prefix:** Any leading characters of $s$. (Prefixes of $abc$: $\epsilon, a, ab, abc$).
   - **Suffix:** Any trailing characters of $s$. (Suffixes of $abc$: $\epsilon, c, bc, abc$).
   - **Substring:** Deleting any prefix and suffix. (Substrings of $abc$: $\epsilon, a, b, c, ab, bc, abc$).
   - **Proper Prefix / Suffix / Substring:** Any prefix / suffix / substring of $s$ that is **not** equal to $\epsilon$ and not equal to $s$ itself.
   - **Subsequence:** Any string formed by deleting zero or more characters from $s$ without changing the order of remaining characters. (Subsequences of $abc$: $\epsilon, a, b, c, ab, ac, bc, abc$).
   - **Concatenation ($xy$):** Appending $y$ after $x$. If $x = dog$ and $y = house$, $xy = doghouse$.
   - **Exponentiation ($s^k$):** $s^0 = \epsilon$, $s^1 = s$, $s^2 = ss$, $s^k = s s^{k-1}$.
4. **Language ($L$):** Any set of strings over a fixed alphabet $\Sigma$.
   - **Kleene Closure ($L^*$):** $L^* = \bigcup_{i=0}^{\infty} L^i = L^0 \cup L^1 \cup L^2 \cup \dots$ (includes $\epsilon$).
   - **Positive Closure ($L^+$):** $L^+ = \bigcup_{i=1}^{\infty} L^i = L^1 \cup L^2 \cup \dots = L L^*$.

---

### 4.2 Regular Expressions & Regular Definitions

**Regular Expressions (RE)** are declarative formulas used to specify the patterns of tokens.

#### Formal Recursive Definition:
1. **Base Cases:**
   - $\epsilon$ is an RE denoting language $L(\epsilon) = \{\epsilon\}$.
   - If $a \in \Sigma$, then $a$ is an RE denoting language $L(a) = \{a\}$.
2. **Inductive Steps:** If $r$ and $s$ are REs denoting languages $L(r)$ and $L(s)$:
   - **Alternation / Union ($r | s$):** Denotes $L(r) \cup L(s)$.
   - **Concatenation ($rs$):** Denotes $L(r) L(s) = \{xy \mid x \in L(r), y \in L(s)\}$.
   - **Kleene Closure ($r^*$):** Denotes $(L(r))^*$.
   - **Parentheses ($(r)$):** Enforces grouping precedence without altering the language.

#### Algebraic Laws of Regular Expressions:

| Law Name | Algebraic Identity |
| :--- | :--- |
| **Commutativity of Union** | $r \| s = s \| r$ |
| **Associativity of Union** | $r \| (s \| t) = (r \| s) \| t$ |
| **Associativity of Concatenation** | $r(st) = (rs)t$ |
| **Distributivity of Concatenation over Union** | $r(s \| t) = rs \| rt \quad \text{and} \quad (s \| t)r = sr \| tr$ |
| **Identity for Union** | $r \| \emptyset = r$ |
| **Identity for Concatenation** | $r\epsilon = \epsilon r = r$ |
| **Idempotence of Union** | $r \| r = r$ |
| **Kleene Star Properties** | $(r^*)^* = r^*, \quad r^* = (r \| \epsilon)^*, \quad r^* = \epsilon \| r r^*$ |

#### Shorthand Extensions:
- $r^+ = r r^*$ (One or more occurrences).
- $r? = r | \epsilon$ (Zero or one occurrence / Optional).
- Character Classes: `[a-z]` $\equiv a | b | \dots | z$, `[0-9]` $\equiv 0 | 1 | \dots | 9$.

#### Regular Definitions:
A **Regular Definition** is a sequence of definitions of the form:
$$d_1 \rightarrow r_1, \quad d_2 \rightarrow r_2, \quad \dots, \quad d_n \rightarrow r_n$$
where each $d_i$ is a distinct new name, and each $r_i$ is a regular expression over $\Sigma \cup \{d_1, d_2, \dots, d_{i-1}\}$.

```
Example: Regular Definitions for C-like Identifiers & Numbers
  letter_    -> [A-Za-z_]
  digit      -> [0-9]
  id         -> letter_ ( letter_ | digit )*
  digits     -> digit+
  optional_fraction -> ( . digits )?
  optional_exponent -> ( (E | e) [+-]? digits )?
  number     -> digits optional_fraction optional_exponent
```

---

### 4.3 Finite Automata: NFA vs. DFA

Tokens specified by regular expressions are recognized at runtime using **Finite Automata**.

#### Non-Deterministic Finite Automaton (NFA):
A 5-tuple $M = (Q, \Sigma, \delta, q_0, F)$ where:
1. $Q$: Finite set of states.
2. $\Sigma$: Finite set of input symbols.
3. $\delta$: State transition function mapping $Q \times (\Sigma \cup \{\epsilon\}) \rightarrow 2^Q$ (power set of $Q$).
4. $q_0 \in Q$: Start state.
5. $F \subseteq Q$: Set of accepting (final) states.

#### Deterministic Finite Automaton (DFA):
A 5-tuple $M = (Q, \Sigma, \delta, q_0, F)$ where:
1. $Q, \Sigma, q_0, F$ have the same definitions as above.
2. $\delta$: State transition function mapping $Q \times \Sigma \rightarrow Q$ (exactly **one** destination state for each input symbol; **no** $\epsilon$-transitions).

#### NFA vs. DFA Comprehensive Comparison:

| Feature / Metric | Non-Deterministic Finite Automata (NFA) | Deterministic Finite Automata (DFA) |
| :--- | :--- | :--- |
| **$\epsilon$-Transitions** | Allowed ($\epsilon$-moves without reading input). | Strictly **prohibited**. |
| **Transitions per Symbol** | Multiple possible next states for a single symbol. | Exactly **one** unique next state for each symbol. |
| **State Space Size** | Smaller number of states (typically $\approx |r|$). | Can have up to $2^{|Q|}$ states in worst-case. |
| **Execution Speed** | Slower (requires backtracking or tracking sets). | Extremely fast: $O(1)$ per character via table lookup. |
| **Implementation Complexity**| Harder to implement directly in software. | Trivial to implement using a 2D transition table array. |
| **Usage in Compilers** | Intermediate model during regex compilation. | The standard engine executing the scanner. |

---

### 4.4 Thompson's Construction Algorithm (RE $\rightarrow$ NFA)

**Ken Thompson's Algorithm** systematically converts any regular expression $r$ into an equivalent NFA $N(r)$ by structural induction.

#### Invariants Maintained by Thompson's Construction:
1. $N(r)$ has exactly **one** start state and **one** accepting state.
2. No transitions enter the start state.
3. No transitions leave the accepting state.
4. Each state has at most two outgoing $\epsilon$-transitions and at most one outgoing symbol transition.

#### Construction Rules:

1. **Base Case 1: For $\epsilon$**
```
   (start) ---> (( i )) --- epsilon ---> ((( f )))
```

2. **Base Case 2: For symbol $a \in \Sigma$**
```
   (start) ---> (( i )) ------- a ------> ((( f )))
```

3. **Inductive Rule 1: Alternation / Union ($r_1 | r_2$)**
```
                    +-- epsilon --> [ N(r_1) ] -- epsilon --+
                    |                                       |
                    |                                       v
   (start) ---> (( i ))                                  ((( f )))
                    |                                       ^
                    |                                       |
                    +-- epsilon --> [ N(r_2) ] -- epsilon --+
```

4. **Inductive Rule 2: Concatenation ($r_1 r_2$)**
```
   (start) ---> [ N(r_1) ] -- (merge accept of r1 with start of r2) --> [ N(r_2) ] ---> ((( f )))
```

5. **Inductive Rule 3: Kleene Closure ($r^*$)**
```
                    +------------------ epsilon ------------------+
                    |                                             |
                    v                                             |
   (start) ---> (( i )) -- epsilon --> [ N(r) ] -- epsilon --> ((( f )))
                    |                     ^
                    |                     |
                    +------ epsilon ------+ (loopback)
```

---

### 4.5 Subset Construction Algorithm (NFA $\rightarrow$ DFA)

Since DFAs are fast and deterministic, we convert the NFA produced by Thompson's construction into an equivalent DFA using the **Subset Construction Algorithm** (also known as the Powerset Construction).

#### Mathematical Auxiliary Operations:

1. **$\epsilon\text{-closure}(s)$:** The set of all NFA states reachable from state $s$ along paths consisting solely of $\epsilon$-transitions (always includes $s$ itself).
2. **$\epsilon\text{-closure}(T)$:** For a set of states $T$:
   $$\epsilon\text{-closure}(T) = \bigcup_{s \in T} \epsilon\text{-closure}(s)$$
3. **$\text{move}(T, a)$:** The set of all NFA states to which there is an actual transition on input symbol $a$ from some state $s \in T$:
   $$\text{move}(T, a) = \{ u \mid \text{there exists } s \in T \text{ such that } s \xrightarrow{a} u \}$$

#### The Complete Subset Construction Algorithm:

```
Input:  An NFA N = (Q_N, Sigma, delta_N, q0, F_N)
Output: An equivalent DFA D = (Q_D, Sigma, delta_D, s0, F_D)

1. s0 = epsilon-closure({q0})
2. Q_D = { s0 }  (unmarked)
3. while (there is an unmarked state T in Q_D) do:
     mark T
     for each input symbol a in Sigma do:
       U = epsilon-closure(move(T, a))
       if U is not empty then:
         if U is not in Q_D then:
           add U as an unmarked state to Q_D
         delta_D(T, a) = U
       end if
     end for
   end while
4. F_D = { T in Q_D | T contains at least one state s in F_N }
```

---

### 4.6 DFA State Minimization (Hopcroft's Partitioning Algorithm)

A DFA generated by the subset construction algorithm may contain redundant, equivalent states. **Hopcroft's Algorithm** finds the unique minimal-state DFA accepting the exact same language by partitioning states into equivalence classes.

#### Concept of State Equivalence:
Two states $p$ and $q$ are **equivalent** ($p \equiv q$) if and only if for all possible input strings $w \in \Sigma^*$, the transitions $\hat{\delta}(p, w)$ and $\hat{\delta}(q, w)$ both land in accepting states or both land in non-accepting states. If there exists any string $w$ that distinguishes them, $p$ and $q$ are **distinguishable**.

#### The Equivalence Partitioning Algorithm:

1. **Initial Partition ($P_0$):**
   Divide all states $Q$ into two groups: accepting states and non-accepting states:
   $$P_0 = \{ F, \quad Q \setminus F \}$$
2. **Iterative Refinement ($P_{k} \rightarrow P_{k+1}$):**
   For each group $G \in P_k$:
   - Split $G$ into subgroups such that two states $s, t \in G$ remain in the same subgroup if and only if for every input symbol $a \in \Sigma$, $\delta(s, a)$ and $\delta(t, a)$ transition into states belonging to the **same group in $P_k$**.
   - If a state transitions to a different group on symbol $a$, it is split into a new separate subgroup.
3. **Termination:**
   Repeat until $P_{k+1} = P_k$ (no further partition splits occur).
4. **Constructing Minimal DFA:**
   - Each final group in the partition becomes a single state in the minimized DFA.
   - If a group contains the original start state $q_0$, that group is the new start state.
   - If a group contains an accepting state, that group is an accepting state.

---

## 5. Direct DFA Construction from Regular Expressions (Syntax Tree Method)

### 5.1 Augmented Regular Expressions & Syntax Trees

Rather than converting $\text{RE} \xrightarrow{\text{Thompson}} \text{NFA} \xrightarrow{\text{Subset}} \text{DFA} \xrightarrow{\text{Hopcroft}} \text{Min-DFA}$, the **Syntax Tree Method** directly constructs a DFA from a regular expression in a single pass.

#### 1. Augmenting the Regular Expression:
Append a unique right-end marker symbol **`#`** to the regular expression:
$$(r) \implies (r)\#$$
The endmarker $\#$ plays a crucial role: an input string is accepted if and only if the automaton matches the endmarker symbol $\#$.

#### 2. Building the Syntax Tree:
- Leaf nodes represent input alphabet symbols $a \in \Sigma$, $\epsilon$, or the endmarker $\#$.
- Interior nodes represent regular expression operators:
  - **Cat-node (`•` or `cat`):** Binary concatenation.
  - **Or-node (`|` or `or`):** Binary alternation / union.
  - **Star-node (`*`):** Unary Kleene closure.
- Each leaf corresponding to an alphabet symbol or $\#$ is assigned a unique **integer position** ($1, 2, \dots, n$) from left to right. ($\epsilon$ leaves are not assigned positions).

---

### 5.2 Formal Functions: `nullable`, `firstpos`, `lastpos`, and `followpos`

For each node $n$ in the syntax tree, we define four core functions:

```
+---------------------------------------------------------------------------------------------------+
| FUNCTION     | RETURN TYPE      | INTUITIVE MEANING                                               |
+--------------+------------------+-----------------------------------------------------------------+
| nullable(n)  | Boolean          | True iff the subtree rooted at n can generate the string \epsilon.|
| firstpos(n)  | Set of Positions | Set of positions that can match the 1st character of a string   |
|              |                  | generated by the subtree rooted at n.                           |
| lastpos(n)   | Set of Positions | Set of positions that can match the last character of a string  |
|              |                  | generated by the subtree rooted at n.                           |
| followpos(i) | Set of Positions | Set of positions j that can immediately follow position i in    |
|              |                  | some string generated by the augmented regex (r)#.              |
+---------------------------------------------------------------------------------------------------+
```

#### Computation Rules for `nullable`, `firstpos`, and `lastpos`:

| Node Type $n$ | $\text{nullable}(n)$ | $\text{firstpos}(n)$ | $\text{lastpos}(n)$ |
| :--- | :--- | :--- | :--- |
| **Leaf $\epsilon$** | `true` | $\emptyset$ | $\emptyset$ |
| **Leaf position $i$** | `false` | $\{i\}$ | $\{i\}$ |
| **Or-node: $c_1 \mid c_2$** | $\text{nullable}(c_1) \lor \text{nullable}(c_2)$ | $\text{firstpos}(c_1) \cup \text{firstpos}(c_2)$ | $\text{lastpos}(c_1) \cup \text{lastpos}(c_2)$ |
| **Cat-node: $c_1 \cdot c_2$** | $\text{nullable}(c_1) \land \text{nullable}(c_2)$ | $\begin{cases} \text{firstpos}(c_1) \cup \text{firstpos}(c_2) & \text{if } \text{nullable}(c_1) \\ \text{firstpos}(c_1) & \text{otherwise} \end{cases}$ | $\begin{cases} \text{lastpos}(c_1) \cup \text{lastpos}(c_2) & \text{if } \text{nullable}(c_2) \\ \text{lastpos}(c_2) & \text{otherwise} \end{cases}$ |
| **Star-node: $c_1^*$** | `true` | $\text{firstpos}(c_1)$ | $\text{lastpos}(c_1)$ |

#### Two Rules for Calculating `followpos(i)`:

`followpos` is computed by walking the syntax tree and applying two specific rules:

1. **Rule 1 (Cat-node $n = c_1 \cdot c_2$):**
   For every position $i \in \text{lastpos}(c_1)$:
   $$\text{followpos}(i) = \text{followpos}(i) \cup \text{firstpos}(c_2)$$

2. **Rule 2 (Star-node $n = c_1^*$):**
   For every position $i \in \text{lastpos}(c_1)$:
   $$\text{followpos}(i) = \text{followpos}(i) \cup \text{firstpos}(c_1)$$

---

### 5.3 Direct DFA Construction Algorithm

```
Input:  An augmented regular expression (r)#
Output: A DFA D = (Dstates, Sigma, Dtran, s0, F)

1. Construct the syntax tree for (r)#.
2. Compute nullable, firstpos, and lastpos for all tree nodes.
3. Compute followpos(i) for all leaf positions i.
4. s0 = firstpos(root)
5. Dstates = { s0 }  (unmarked)
6. while (there is an unmarked state U in Dstates) do:
     mark U
     for each input symbol a in Sigma do:
       let S_a = { p in U | leaf p is labeled with symbol a }
       U_a = Union_{p in S_a} followpos(p)
       if U_a is not empty then:
         if U_a is not in Dstates then:
           add U_a as an unmarked state to Dstates
         Dtran(U, a) = U_a
       end if
     end for
   end while
7. F = { U in Dstates | U contains the position corresponding to endmarker # }
```

---

### 5.4 Solved Master Numerical Walkthrough 1: $(a|b)^*abb\#$

Let us construct the DFA directly for:
$$r = (a \mid b)^* a b b \#$$

#### Step 1: Number the Leaves of the Syntax Tree
1. Leaf 1: $a$
2. Leaf 2: $b$
3. Leaf 3: $a$
4. Leaf 4: $b$
5. Leaf 5: $b$
6. Leaf 6: $\#$

#### Step 2: Syntax Tree Structure & Node Calculations

```
                                 cat_5 (root)
                                /            \
                           cat_4              #(6)
                          /     \
                     cat_3       b(5)
                    /     \
               cat_2       b(4)
              /     \
          star_1     a(3)
            |
           or_1
          /    \
        a(1)   b(2)
```

#### Node-by-Node Evaluation Table:

| Node | Expression Represented | `nullable` | `firstpos` | `lastpos` |
| :---: | :--- | :---: | :---: | :---: |
| $1$ | Leaf $a$ | `false` | $\{1\}$ | $\{1\}$ |
| $2$ | Leaf $b$ | `false` | $\{2\}$ | $\{2\}$ |
| $\text{or}_1$ | $a \mid b$ | `false` | $\{1, 2\}$ | $\{1, 2\}$ |
| $\text{star}_1$| $(a \mid b)^*$ | `true` | $\{1, 2\}$ | $\{1, 2\}$ |
| $3$ | Leaf $a$ | `false` | $\{3\}$ | $\{3\}$ |
| $\text{cat}_2$| $(a \mid b)^* a$ | `false` | $\{1, 2, 3\}$ | $\{3\}$ |
| $4$ | Leaf $b$ | `false` | $\{4\}$ | $\{4\}$ |
| $\text{cat}_3$| $(a \mid b)^* a b$ | `false` | $\{1, 2, 3\}$ | $\{4\}$ |
| $5$ | Leaf $b$ | `false` | $\{5\}$ | $\{5\}$ |
| $\text{cat}_4$| $(a \mid b)^* a b b$ | `false` | $\{1, 2, 3\}$ | $\{5\}$ |
| $6$ | Leaf $\#$ | `false` | $\{6\}$ | $\{6\}$ |
| $\text{cat}_5$ (Root) | $(a \mid b)^* a b b \#$ | `false` | $\{1, 2, 3\}$ | $\{6\}$ |

---

#### Step 3: Compute `followpos(i)` Table

- **From $\text{star}_1$ ($n = c_1^*$, where $\text{lastpos}(c_1) = \{1, 2\}$ and $\text{firstpos}(c_1) = \{1, 2\}$):**
  - $\text{followpos}(1) = \{1, 2\}$
  - $\text{followpos}(2) = \{1, 2\}$
- **From $\text{cat}_2$ ($c_1 = \text{star}_1, c_2 = 3$):**
  - For $i \in \text{lastpos}(\text{star}_1) = \{1, 2\}$:
  - $\text{followpos}(1) = \text{followpos}(1) \cup \{3\} = \{1, 2, 3\}$
  - $\text{followpos}(2) = \text{followpos}(2) \cup \{3\} = \{1, 2, 3\}$
- **From $\text{cat}_3$ ($c_1 = \text{cat}_2, c_2 = 4$):**
  - For $i \in \text{lastpos}(\text{cat}_2) = \{3\}$:
  - $\text{followpos}(3) = \{4\}$
- **From $\text{cat}_4$ ($c_1 = \text{cat}_3, c_2 = 5$):**
  - For $i \in \text{lastpos}(\text{cat}_3) = \{4\}$:
  - $\text{followpos}(4) = \{5\}$
- **From $\text{cat}_5$ ($c_1 = \text{cat}_4, c_2 = 6$):**
  - For $i \in \text{lastpos}(\text{cat}_4) = \{5\}$:
  - $\text{followpos}(5) = \{6\}$

#### Summary `followpos` Table:

| Node Position $i$ | Symbol at $i$ | $\text{followpos}(i)$ |
| :---: | :---: | :--- |
| **1** | $a$ | $\{1, 2, 3\}$ |
| **2** | $b$ | $\{1, 2, 3\}$ |
| **3** | $a$ | $\{4\}$ |
| **4** | $b$ | $\{5\}$ |
| **5** | $b$ | $\{6\}$ |
| **6** | $\#$ | $\emptyset$ |

---

#### Step 4: DFA State Computation

- **Start State $A = \text{firstpos}(\text{root}) = \{1, 2, 3\}$**
- **From State $A = \{1, 2, 3\}$:**
  - On $a$ (positions $\{1, 3\}$):
    $$\text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3\} \cup \{4\} = \{1, 2, 3, 4\} \implies \textbf{State } B$$
  - On $b$ (position $\{2\}$):
    $$\text{followpos}(2) = \{1, 2, 3\} \implies \textbf{State } A$$
- **From State $B = \{1, 2, 3, 4\}$:**
  - On $a$ (positions $\{1, 3\}$):
    $$\text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3, 4\} \implies \textbf{State } B$$
  - On $b$ (positions $\{2, 4\}$):
    $$\text{followpos}(2) \cup \text{followpos}(4) = \{1, 2, 3\} \cup \{5\} = \{1, 2, 3, 5\} \implies \textbf{State } C$$
- **From State $C = \{1, 2, 3, 5\}$:**
  - On $a$ (positions $\{1, 3\}$):
    $$\text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3, 4\} \implies \textbf{State } B$$
  - On $b$ (positions $\{2, 5\}$):
    $$\text{followpos}(2) \cup \text{followpos}(5) = \{1, 2, 3\} \cup \{6\} = \{1, 2, 3, 6\} \implies \textbf{State } D$$
- **From State $D = \{1, 2, 3, 6\}$ (Accepting State because $6 \in D$):**
  - On $a$ (positions $\{1, 3\}$):
    $$\text{followpos}(1) \cup \text{followpos}(3) = \{1, 2, 3, 4\} \implies \textbf{State } B$$
  - On $b$ (position $\{2\}$):
    $$\text{followpos}(2) = \{1, 2, 3\} \implies \textbf{State } A$$

---

#### Step 5: Final DFA Transition Table

| DFA State | NFA Positions Set | Transition on $a$ | Transition on $b$ | Is Accepting? |
| :---: | :---: | :---: | :---: | :---: |
| $\rightarrow \mathbf{A}$ | $\{1, 2, 3\}$ | $\mathbf{B}$ | $\mathbf{A}$ | No |
| $\mathbf{B}$ | $\{1, 2, 3, 4\}$ | $\mathbf{B}$ | $\mathbf{C}$ | No |
| $\mathbf{C}$ | $\{1, 2, 3, 5\}$ | $\mathbf{B}$ | $\mathbf{D}$ | No |
| $* \mathbf{D}$ | $\{1, 2, 3, 6\}$ | $\mathbf{B}$ | $\mathbf{A}$ | **Yes** (Contains 6) |

---

### 5.5 Solved Master Numerical Walkthrough 2: $(a|b)^*a(a|b)\#$

Let us construct the DFA for the language of strings over $\{a, b\}$ whose **second-to-last symbol is $a$**.
$$r = (a \mid b)^* a (a \mid b) \#$$

#### Position Assignments:
- Leaf 1: $a$, Leaf 2: $b$ (under star)
- Leaf 3: $a$
- Leaf 4: $a$, Leaf 5: $b$ (under second or)
- Leaf 6: $\#$

#### Calculated `followpos` Values:
- $\text{followpos}(1) = \{1, 2, 3\}$
- $\text{followpos}(2) = \{1, 2, 3\}$
- $\text{followpos}(3) = \{4, 5\}$
- $\text{followpos}(4) = \{6\}$
- $\text{followpos}(5) = \{6\}$
- $\text{followpos}(6) = \emptyset$

#### State Discovery:
- $\text{Start } S_0 = \text{firstpos}(\text{root}) = \{1, 2, 3\}$
- $S_0 \xrightarrow{a} \{1, 2, 3, 4, 5\} = S_1$
- $S_0 \xrightarrow{b} \{1, 2, 3\} = S_0$
- $S_1 \xrightarrow{a} \{1, 2, 3, 4, 5, 6\} = S_2$
- $S_1 \xrightarrow{b} \{1, 2, 3, 6\} = S_3$
- $S_2 \xrightarrow{a} \{1, 2, 3, 4, 5, 6\} = S_2$
- $S_2 \xrightarrow{b} \{1, 2, 3, 6\} = S_3$
- $S_3 \xrightarrow{a} \{1, 2, 3, 4, 5\} = S_1$
- $S_3 \xrightarrow{b} \{1, 2, 3\} = S_0$

#### Resulting 4-State DFA Transition Table:

| State | Position Set | On $a$ | On $b$ | Final? |
| :---: | :---: | :---: | :---: | :---: |
| $\rightarrow S_0$ | $\{1, 2, 3\}$ | $S_1$ | $S_0$ | No |
| $S_1$ | $\{1, 2, 3, 4, 5\}$ | $S_2$ | $S_3$ | No |
| $* S_2$ | $\{1, 2, 3, 4, 5, 6\}$ | $S_2$ | $S_3$ | **Yes** |
| $* S_3$ | $\{1, 2, 3, 6\}$ | $S_1$ | $S_0$ | **Yes** |

---

## 6. High-Yield Exam Question Bank & Solved Numerical Problems

### ❓ Question 1: Explain the Cousins of a Compiler with a neat block diagram.
**Answer Summary:**
A compiler operates as part of an integrated language processing toolchain comprising:
1. **Preprocessor:** Strips comments, expands `#define` macros, handles `#include` header files.
2. **Compiler:** Translates pure source code to assembly code (`.s`).
3. **Assembler:** Translates assembly mnemonics into relocatable machine code (`.o`).
4. **Linker:** Resolves cross-file symbol references and static library dependencies.
5. **Loader:** Allocates memory, sets up call stacks/heaps, and loads executable machine instructions into RAM for execution.

---

### ❓ Question 2: Differentiate between a Token, Pattern, and Lexeme with two distinct examples.
**Answer Summary:**
- **Token:** Abstract terminal symbol delivered to parser (e.g., `<ID>`, `<NUM>`, `<RELOP>`).
- **Pattern:** Regular expression description matching the lexeme class (e.g., `letter(letter|digit)*`).
- **Lexeme:** The actual concrete substring in source code matching the pattern (e.g., `totalScore`, `3.1415`).

---

### ❓ Question 3: Explain Input Buffering using Buffer Pairs and Sentinels.
**Answer Summary:**
- Two buffers of size $N$ loaded via single block-read operations.
- Pointers `lexeme_beginning` and `forward` manage character scanning.
- **Sentinel character (`EOF`)** is placed at the end of each buffer half to reduce checking overhead from two conditional tests per character (`forward >= limit` and `*forward == EOF`) to a single test in the main scanning loop.

---

### ❓ Question 4: Minimize the following DFA using Equivalence Partitioning:
States: $\{q_0, q_1, q_2, q_3, q_4\}$, Start: $q_0$, Accept: $\{q_4\}$
Transitions:
- $\delta(q_0, a) = q_1, \delta(q_0, b) = q_2$
- $\delta(q_1, a) = q_1, \delta(q_1, b) = q_3$
- $\delta(q_2, a) = q_1, \delta(q_2, b) = q_2$
- $\delta(q_3, a) = q_1, \delta(q_3, b) = q_4$
- $\delta(q_4, a) = q_1, \delta(q_4, b) = q_2$

#### Step-by-Step Solution:
1. **Initial Partition $P_0$:**
   $$G_1 = \{q_0, q_1, q_2, q_3\} \quad (\text{Non-accepting}), \quad G_2 = \{q_4\} \quad (\text{Accepting})$$
2. **Refine $G_1$ under $a$ and $b$:**
   - For input $a$: All states in $G_1$ transition to $q_1 \in G_1$. (No split on $a$).
   - For input $b$:
     - $\delta(q_0, b) = q_2 \in G_1$
     - $\delta(q_1, b) = q_3 \in G_1$
     - $\delta(q_2, b) = q_2 \in G_1$
     - $\delta(q_3, b) = q_4 \in \mathbf{G_2}$  $\implies q_3$ transitions out of $G_1$!
   - Therefore, $G_1$ splits into $\{q_0, q_1, q_2\}$ and $\{q_3\}$.
   $$P_1 = \{ \{q_0, q_1, q_2\}, \{q_3\}, \{q_4\} \}$$
3. **Refine $\{q_0, q_1, q_2\}$ in $P_1$:**
   - On $a$: All transition to $q_1 \in \{q_0, q_1, q_2\}$.
   - On $b$:
     - $\delta(q_0, b) = q_2 \in \{q_0, q_1, q_2\}$
     - $\delta(q_1, b) = q_3 \in \mathbf{\{q_3\}}$ $\implies q_1$ transitions to a different group!
     - $\delta(q_2, b) = q_2 \in \{q_0, q_1, q_2\}$
   - Split $\{q_0, q_1, q_2\}$ into $\{q_0, q_2\}$ and $\{q_1\}$.
   $$P_2 = \{ \{q_0, q_2\}, \{q_1\}, \{q_3\}, \{q_4\} \}$$
4. **Check $\{q_0, q_2\}$ in $P_2$:**
   - On $a$: $\delta(q_0, a) = q_1, \delta(q_2, a) = q_1$ (Same group $\{q_1\}$).
   - On $b$: $\delta(q_0, b) = q_2, \delta(q_2, b) = q_2$ (Same group $\{q_0, q_2\}$).
   - No further splits.
5. **Final Minimal States:**
   - State $[0, 2] = \{q_0, q_2\}$ (Start)
   - State $[1] = \{q_1\}$
   - State $[3] = \{q_3\}$
   - State $[4] = \{q_4\}$ (Accepting)

---

## 7. Quick Revision Formula Sheet & Exam Pitfalls

### ⚡ Direct DFA Formula Cheat Sheet

| AST Node ($n$) | $\text{nullable}(n)$ | $\text{firstpos}(n)$ | $\text{lastpos}(n)$ |
| :--- | :---: | :---: | :---: |
| Leaf $\epsilon$ | `true` | $\emptyset$ | $\emptyset$ |
| Leaf $i$ | `false` | $\{i\}$ | $\{i\}$ |
| $c_1 \mid c_2$ | $\text{nullable}(c_1) \lor \text{nullable}(c_2)$ | $\text{firstpos}(c_1) \cup \text{firstpos}(c_2)$ | $\text{lastpos}(c_1) \cup \text{lastpos}(c_2)$ |
| $c_1 \cdot c_2$ | $\text{nullable}(c_1) \land \text{nullable}(c_2)$ | $\text{if } \text{nullable}(c_1) \text{ then } \text{firstpos}(c_1) \cup \text{firstpos}(c_2) \text{ else } \text{firstpos}(c_1)$ | $\text{if } \text{nullable}(c_2) \text{ then } \text{lastpos}(c_1) \cup \text{lastpos}(c_2) \text{ else } \text{lastpos}(c_2)$ |
| $c_1^*$ | `true` | $\text{firstpos}(c_1)$ | $\text{lastpos}(c_1)$ |

### ⚠️ Top 5 Common Exam Mistakes to Avoid:
1. **Forgetting to augment $(r)\#$:** Always append $\#$ before building the syntax tree for direct DFA construction.
2. **Confusing Token vs Lexeme:** Token is the abstract class name (`ID`), lexeme is the literal character sequence (`count`).
3. **Missing $\text{lastpos}$ in Cat-node $\text{followpos}$ rule:** In $c_1 \cdot c_2$, $\text{firstpos}(c_2)$ is added to $\text{followpos}(i)$ for all $i \in \text{lastpos}(c_1)$.
4. **DFA Accepting States:** A DFA state is accepting if and only if it contains the position of the endmarker $\#$.
5. **Sentinel Efficiency:** Sentinels save comparisons by placing `EOF` at buffer boundaries, reducing inner loop branch checks from two to one.

---
*Created for B.Tech CSE 5th Semester — Compiler Design (CS24301).*
