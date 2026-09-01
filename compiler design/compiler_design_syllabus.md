# 🏛️ Compiler Design (CS24301 & CS24302) — Complete Syllabus & Study Guide

> **Academic Program:** B.Tech in Computer Science & Engineering  
> **Scheme:** NEP Scheme (2024–25) | BIT Mesra  
> **Semester:** 5th Semester  
> **Theory Course:** `CS24301` — **3.0 Credits**  
> **Lab Course:** `CS24302` — **1.5 Credits**  
> **Total Credits:** **4.5 Credits**

---

## 📌 Table of Contents
1. [Course Overview & Learning Outcomes](#-course-overview--learning-outcomes)
2. [Theory Syllabus: CS24301 (Module I – V)](#-theory-syllabus-cs24301)
   - [Module I: Lexical Analysis](#module-i--lexical-analysis)
   - [Module II: Syntax Analysis](#module-ii--syntax-analysis)
   - [Module III: Semantic Analysis & Intermediate Code Generation](#module-iii--semantic-analysis--intermediate-code-generation)
   - [Module IV: Intermediate Code Generation & Runtime Environment](#module-iv--intermediate-code-generation--runtime-environment)
   - [Module V: Code Generation & Optimization](#module-v--code-generation--optimization)
3. [Lab Syllabus: CS24302 (Practical Implementation)](#-compiler-design-lab-cs24302)
   - [Lab Modules I – V](#lab-module-breakdown)
4. [Standard Reference Books & Recommended Reading](#-recommended-textbooks--reference-materials)
5. [Key Exam Topics & High-Yield Questions](#-high-yield-exam-topics--question-bank)
6. [Interactive Progress Tracker](#-interactive-study-tracker)

---

## 🎯 Course Overview & Learning Outcomes

A compiler translates high-level programming language code into machine-executable or assembly code. This course covers the end-to-end compilation pipeline spanning analysis (front-end) and synthesis (back-end).

```mermaid
flowchart LR
    subgraph FrontEnd["Front End (Analysis)"]
        Source[Source Program] --> LA[Lexical Analyzer]
        LA -->|Tokens| SA[Syntax Analyzer / Parser]
        SA -->|Parse Tree / AST| SemA[Semantic Analyzer]
        SemA -->|Decorated AST| ICG[Intermediate Code Generator]
    end

    subgraph BackEnd["Back End (Synthesis)"]
        ICG -->|Intermediate Code (TAC)| Opt[Code Optimizer]
        Opt -->|Optimized TAC| CG[Code Generator]
        CG --> Target[Target Machine Code]
    end

    SymbolTable[(Symbol Table)] <---> LA
    SymbolTable <---> SA
    SymbolTable <---> SemA
    SymbolTable <---> ICG
    SymbolTable <---> Opt
    SymbolTable <---> CG

    ErrorHandler[Error Handling] <---> FrontEnd
    ErrorHandler <---> BackEnd
```

---

## 📖 Theory Syllabus: CS24301

### Module I – Lexical Analysis
*Focus: Tokenization, regular languages, finite automata, and direct DFA construction.*

- [ ] **Introduction to Compilers & Language Processors:**
  - Cousins of the Compiler: Preprocessor, Compiler, Assembler, Linker, Loader
  - Structure & Phases of a Compiler (Analysis vs. Synthesis; Front-End vs. Back-End)
  - Compiler-construction tools (Lex/Flex, Yacc/Bison)
- [ ] **Role of Lexical Analyzer:**
  - Tokens, Patterns, and Lexemes
  - Attributes for tokens
  - Lexical errors and recovery strategies
- [ ] **Input Buffering:**
  - Buffer pairs and Sentinel characters
- [ ] **Specification & Recognition of Tokens:**
  - Regular Expressions (RE) & Regular Definitions
  - Transition Diagrams and Finite Automata (NFA & DFA)
  - Thompson’s Construction (RE to NFA)
  - Subset Construction Algorithm (NFA to DFA)
  - DFA State Minimization (Hopcroft’s Algorithm)
- [ ] **Direct DFA Construction from Regular Expressions:**
  - Augmented Regular Expressions $(r)\#$
  - Syntax Tree representations
  - Functions: `nullable(n)`, `firstpos(n)`, `lastpos(n)`, `followpos(i)`
  - Direct DFA state construction algorithm

---

### Module II – Syntax Analysis
*Focus: Context-Free Grammars, top-down predictive parsing, bottom-up shift-reduce parsing, and LR family parsers.*

- [ ] **Introduction to Syntax Analysis:**
  - Role of the Parser and Context-Free Grammars (CFG)
  - Derivations (Leftmost & Rightmost), Parse Trees, Ambiguity
- [ ] **Grammar Transformations:**
  - Elimination of Left Recursion (Immediate and Non-immediate)
  - Left Factoring
  - Ambiguity resolution
- [ ] **Top-Down Parsing:**
  - Recursive Descent Parsing (with backtracking)
  - Non-Recursive Predictive Parsing (Table-Driven)
  - Computation of $\text{FIRST}(\alpha)$ and $\text{FOLLOW}(A)$ sets
  - Construction of $\text{LL}(1)$ Parsing Tables
  - Properties of $\text{LL}(1)$ Grammars & Conflict detection
- [ ] **Bottom-Up Parsing:**
  - Shift-Reduce Parsing and Handle Pruning
  - Viable Prefixes and Model of an LR Parser
- [ ] **The LR Parser Family:**
  - $\text{LR}(0)$ Items and Canonical Collection of $\text{LR}(0)$ Items
  - $\text{SLR}(1)$ Parsing Table Construction
  - $\text{LR}(1)$ Items and Canonical $\text{LR}(1)$ ($\text{CLR}$) Parsing Tables
  - $\text{LALR}(1)$ Parsing Table Construction (Merging core states)
  - Comparison of parser power: $\text{LL}(1) < \text{SLR}(1) < \text{LALR}(1) < \text{CLR}(1)$
- [ ] **Parsing Conflicts & Error Handling:**
  - Shift/Reduce (S/R) and Reduce/Reduce (R/R) conflicts
  - Using Ambiguous Grammars with Precedence and Associativity declarations
  - Syntax Error Detection, Reporting, and Recovery (Panic Mode, Phrase-Level Recovery, Error Productions)

---

### Module III – Semantic Analysis & Intermediate Code Generation
*Focus: Syntax-Directed Definitions, Type Checking, and Intermediate Representations.*

- [ ] **Introduction to Semantic Analysis:**
  - Static vs. Dynamic Checking
  - Role of Symbol Table in Semantic Checking
- [ ] **Syntax-Directed Definitions (SDD):**
  - Attributes: Synthesized vs. Inherited Attributes
  - S-Attributed Definitions (Evaluated during bottom-up parsing)
  - L-Attributed Definitions (Evaluated in depth-first top-down order)
  - Dependency Graphs and Evaluation Orders
- [ ] **Syntax-Directed Translation Schemes (SDTS):**
  - Embedding semantic actions within production rules
  - Implementation of SDTS using top-down and bottom-up parsers
  - SDTS for Declarations (type propagation, memory offset calculation)
- [ ] **Type Systems & Type Checking:**
  - Type expressions, type equivalences (Structural vs. Name equivalence)
  - Type checking and coercion in expressions
- [ ] **Intermediate Representations (IR):**
  - High-level vs. Low-level IR (AST, DAGs, Postfix notation)
  - Three Address Code (TAC) representations:
    1. **Quadruples** `(op, arg1, arg2, result)`
    2. **Triples** `(op, arg1, arg2)`
    3. **Indirect Triples** (Array of pointers to triples)
- [ ] **Translation of Expressions & Arrays:**
  - TAC generation for arithmetic assignment statements
  - Address calculations for 1D, 2D, and Multi-dimensional Arrays:
    - Row-major order address formula: $\text{Base} + ((i - \text{low}_1) \times n_2 + (j - \text{low}_2)) \times w$
    - Column-major order address formula: $\text{Base} + ((j - \text{low}_2) \times n_1 + (i - \text{low}_1)) \times w$

---

### Module IV – Intermediate Code Generation & Runtime Environment
*Focus: Control-flow translation, boolean expressions, backpatching, procedure calls, and storage allocation.*

- [ ] **Boolean Expressions Translation:**
  - Numerical / Bitwise evaluation (evaluating boolean values as `0` or `1`)
  - Flow-of-control / Short-circuit evaluation (using jumps)
- [ ] **Translation of Control Flow Constructs:**
  - `if-then`, `if-then-else`, `while-do`, `do-while`, `for` loops, `switch-case`
- [ ] **Backpatching Technique:**
  - Resolution of Forward and Backward Jumps in a single pass
  - Synthesized attributes: `truelist`, `falselist`, `nextlist`
  - Operations: `makelist(i)`, `merge(p1, p2)`, `backpatch(p, i)`
- [ ] **Translation of Procedures & Function Calls:**
  - Intermediate code generation for function calls (`param x`, `call p, n`)
  - Intermediate code generation for return statements
- [ ] **Runtime Storage Organization:**
  - Memory Layout: Code / Text segment, Static Data, Heap (Dynamic allocation), Stack (Call frames)
- [ ] **Activation Records (Stack Frames):**
  - Contents: Return value, Actual parameters, Control link (Dynamic link), Access link (Static link), Saved machine status, Local data, Temporaries
  - Parameter passing mechanisms: Call-by-Value, Call-by-Reference, Call-by-Name, Call-by-Value-Result
  - Storage allocation strategies: Static, Stack-based, Heap-based

---

### Module V – Code Generation & Optimization
*Focus: Basic blocks, control flow graphs, machine-independent optimizations, and target code emission.*

- [ ] **Basic Blocks & Flow Graphs:**
  - Algorithm to identify Leader instructions
  - Partitioning TAC into Basic Blocks
  - Construction of Control Flow Graphs (CFG)
  - Loops in CFG (Dominators, Natural loops, Reducible flow graphs)
- [ ] **Directed Acyclic Graph (DAG) Representation:**
  - Constructing DAG for basic blocks
  - DAG-based local optimizations:
    - Local Common Subexpression Elimination
    - Dead Code Elimination
    - Renaming of temporary variables
    - Algebraic identities & Strength reduction
- [ ] **Machine-Independent Code Optimization:**
  - **Global Common Subexpression Elimination**
  - **Constant Folding** (Compile-time evaluation of constant expressions)
  - **Constant Propagation** (Replacing variables with known constant values)
  - **Dead Code & Unreachable Code Elimination**
  - **Loop Optimizations:**
    - Loop-Invariant Code Motion (Code hoisting)
    - Induction Variable Elimination
    - Loop Unrolling & Loop Jamming (Fusion)
- [ ] **Dataflow Analysis Overview:**
  - Reaching definitions, Available expressions, Live variable analysis
- [ ] **Target Code Generation:**
  - Addresses of code and data in target assembly
  - Simple code generator algorithm using register and address descriptors
  - Register Allocation & Assignment (Graph coloring heuristics)
  - Peephole Optimization techniques (Redundant load/store elimination, unreachable code, flow-of-control optimizations)

---

## 🧪 Compiler Design Lab: CS24302

| Module | Lab Objectives & Practical Tasks |
| :--- | :--- |
| **Lab Module I** | **Compiler Toolchain & Lexical Analysis**<br>• Study GCC/LLVM compiler options and internal pass dumps (`-fdump-tree-all`, `-S`, `-O0`, `-O2`, `-O3`).<br>• Compare generated assembly with and without optimization.<br>• Performance benchmarking of compiled code under varying inputs.<br>• Implement a custom Lexical Analyzer in C/C++ (recognizing keywords, identifiers, literals, operators, and strip comments).<br>• Study regular expression ordering and action routines. |
| **Lab Module II** | **Syntax Analysis with Lex (Flex) & Yacc (Bison)**<br>• Write CFGs for variable declarations, scalar assignments, and array references.<br>• Design ambiguous vs. unambiguous grammars in Yacc.<br>• Write `.l` (Lex) and `.y` (Yacc) specifications and integrate them.<br>• Generate LALR(1) parser using Yacc (`y.tab.c`, `y.tab.h`) and inspect parser tables (`y.output`).<br>• Implement desk calculators and syntax validators for C-subset statements. |
| **Lab Module III** | **Semantic Analysis & Intermediate Code Generation**<br>• Build a Symbol Table using Hash Maps / Trees to manage identifier scope and type attributes.<br>• Implement semantic type checking for arithmetic and boolean expressions.<br>• Generate Three Address Code (TAC) in Quadruple/Triple format using Yacc actions.<br>• Implement Backpatching routines for boolean expressions and control structures (`if`, `while`). |
| **Lab Module IV** | **Runtime Environment Simulation**<br>• Simulate Stack Frame (Activation Record) management for nested function calls.<br>• Implement parameter passing and return address mechanics. |
| **Lab Module V** | **Code Optimization Implementations**<br>• Implement Basic Block partitioning from TAC input.<br>• Implement DAG-based local common subexpression elimination.<br>• Implement Constant Folding and Constant Propagation algorithms.<br>• Implement Unreachable Code & Dead Code Elimination passes. |

---

## 📚 Recommended Textbooks & Reference Materials

### Standard Textbooks
1. **"Compilers: Principles, Techniques, and Tools" (The Dragon Book)**  
   *Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman* — Pearson Education (2nd Edition).  
   *(Primary text covering all modules from Lexical Analysis to Code Generation).*
2. **"Engineering a Compiler"**  
   *Keith D. Cooper & Linda Torczon* — Morgan Kaufmann / Elsevier.  
   *(Excellent modern reference for IL representations, optimization passes, and register allocation).*
3. **"Compiler Construction: Principles and Practice"**  
   *Kenneth C. Louden* — Cengage Learning.  
   *(Great for practical Lex & Yacc parser construction).*

### Supplementary Tools & Frameworks
- **Lexer/Parser Generators:** `flex` (Fast Lexical Analyzer), `bison` (GNU Parser Generator)
- **Production Compilers:** `gcc` / `g++`, `clang` / `llvm`

---

## 🌟 High-Yield Exam Topics & Question Bank

### Top Numerical & Algorithmic Problems
1. **Direct RE to DFA Construction:** Compute `nullable`, `firstpos`, `lastpos`, and `followpos` table for a given regex (e.g., $(a|b)^*abb\#$) and construct the resulting DFA.
2. **DFA State Minimization:** Minimize a given DFA using equivalence partitioning.
3. **LL(1) Parser Table:** Given a grammar, eliminate left recursion, perform left factoring, calculate $\text{FIRST}$ & $\text{FOLLOW}$ sets, build the $\text{LL}(1)$ table, and prove whether the grammar is $\text{LL}(1)$.
4. **LR Parsing Tables:**
   - Construct Canonical Collection of $\text{LR}(0)$ items $\rightarrow$ Build $\text{SLR}(1)$ parsing table $\rightarrow$ Identify conflicts.
   - Construct $\text{LR}(1)$ canonical items $\rightarrow$ Build $\text{CLR}(1)$ / $\text{LALR}(1)$ parsing tables.
5. **Array Address Calculation:** Derive the intermediate 3-address code instructions for accessing 2D array elements (e.g., `A[i][j] = B[i][j] + C[i][j]`) in Row-Major / Column-Major form.
6. **Three Address Code Representations:** Represent arithmetic expressions into Quadruples, Triples, and Indirect Triples.
7. **Basic Blocks & DAG Optimization:** Given a block of TAC, identify leader statements, partition into basic blocks, draw the CFG, construct the DAG, and produce optimized TAC.

### Critical Theoretical Questions
- Explain the phases of compiler design with an example showing code transformations at each phase.
- Differentiate between **Synthesized** and **Inherited** attributes with illustrative SDDs.
- Explain **Backpatching** with SDT rules for `while` and `if-else` constructs.
- Detail the structure of an **Activation Record** and explain dynamic vs. static links.
- Compare parameter passing techniques: Call-by-value vs. Call-by-reference vs. Call-by-name.
- Describe Loop Optimizations: Code Motion, Induction Variable Elimination, Loop Unrolling.

---

## 📊 Interactive Study Tracker

| Module | Core Concept | Topics Count | Status |
| :---: | :--- | :---: | :---: |
| **M1** | Lexical Analysis, Tokens, Buffer Pairs, Thompson's Construction, Direct RE $\rightarrow$ DFA | 7 | ⬜ Not Started |
| **M2** | CFG, Left Recursion/Factoring, LL(1) Parsing, SLR(1), CLR(1), LALR(1), Conflicts & Errors | 10 | ⬜ Not Started |
| **M3** | SDD (S-attr vs L-attr), SDTS, Symbol Tables, Type Systems, TAC (Quadruples/Triples), Arrays | 9 | ⬜ Not Started |
| **M4** | Boolean Expressions (Short-circuit), Control Flow Translation, Backpatching, Activation Records | 9 | ⬜ Not Started |
| **M5** | Basic Blocks, CFG, DAG Optimization, Constant Folding/Prop, Loop Invariant Code Motion, Peep-hole | 12 | ⬜ Not Started |
| **LAB** | Lex/Flex, Yacc/Bison, GCC Pass Dumps, Symbol Table, TAC Generation, Optimization Passes | 43 Tasks | ⬜ Not Started |

---
*Created for B.Tech 5th Semester CSE — Compiler Design (CS24301 & CS24302).*
