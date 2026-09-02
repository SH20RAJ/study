# Compiler Design 10-Page Master Revision Exhaustive Content (CS24301)
# Contains the full 47-Topic Checklist, Master Differences Cards & Spaced Repetition Protocol

CD_REVISION_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title">⚡ 10-Page Master Quick Revision — Compiler Design (CS24301)</div>
  <div class="toc-grid">
    <div>Page 1: 47-Topic Master Syllabus Progress Checklist (Modules I – V)</div>
    <div>Page 2: The 6 Classical Compiler Phases & P-I-C-A-L Translation Pipeline</div>
    <div>Page 3: Lexical Analysis: Token/Lexeme/Pattern & Direct DFA $(r)\#$ Math</div>
    <div>Page 4: Syntax Analysis: Left Recursion, Left Factoring & LL(1) Table Rules</div>
    <div>Page 5: LR Parsing Family Hierarchy: LR(0), SLR(1), CLR(1) & LALR(1)</div>
    <div>Page 6: Semantic Analysis: SDD vs. SDTS, Synthesized vs. Inherited Types</div>
    <div>Page 7: Intermediate Code: Quadruples, Triples & Multidimensional Array Math</div>
    <div>Page 8: Runtime Storage: Memory Segments & Activation Record (P-R-C-A-S-L-T)</div>
    <div>Page 9: Code Optimization: 3 Leader Rules, CFG & 6 Principal Machine-Independent Passes</div>
    <div>Page 10: Top 10 High-Frequency Exam-Important Conceptual Differences & Solutions</div>
  </div>
</div>

<h2 class="section-title">📋 The Complete 47-Topic Syllabus Master Checklist</h2>

<div class="callout callout-info">
  <div class="callout-title">47 / 47 Syllabus Topics Complete</div>
  <table class="custom-table" style="font-size: 10px;">
    <thead><tr><th>Module</th><th>Topic #</th><th>Topic Name</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td rowspan="7"><strong>M1: Lexical Analysis (7)</strong></td><td>1</td><td>Introduction to Compilers and its Cousins (P-I-C-A-L)</td><td>✅ Complete</td></tr>
      <tr><td>2</td><td>Structure of a Compiler (Front End vs. Back End, 6 Phases)</td><td>✅ Complete</td></tr>
      <tr><td>3</td><td>Lexical Analyzer (Token, Lexeme, Pattern)</td><td>✅ Complete</td></tr>
      <tr><td>4</td><td>Input Buffering (Two-Buffer Scheme, Sentinels)</td><td>✅ Complete</td></tr>
      <tr><td>5</td><td>Specification of Tokens (Regular Expressions & Operators)</td><td>✅ Complete</td></tr>
      <tr><td>6</td><td>Recognition of Tokens (Transition Diagrams & DFAs)</td><td>✅ Complete</td></tr>
      <tr><td>7</td><td>DFA Directly from Regular Expressions (FLF Rules)</td><td>✅ Complete</td></tr>

      <tr><td rowspan="10"><strong>M2: Syntax Analysis (10)</strong></td><td>8</td><td>Introduction to Syntax Analysis & CFG Grammars</td><td>✅ Complete</td></tr>
      <tr><td>9</td><td>Grammar Rewriting (Left Recursion & Left Factoring)</td><td>✅ Complete</td></tr>
      <tr><td>10</td><td>Recursive Top-Down Parsers (Recursive Descent)</td><td>✅ Complete</td></tr>
      <tr><td>11</td><td>Non-Recursive Top-Down Parsers (Predictive Parsing)</td><td>✅ Complete</td></tr>
      <tr><td>12</td><td>Design of LL(1) Parser (FIRST & FOLLOW Inductive Rules)</td><td>✅ Complete</td></tr>
      <tr><td>13</td><td>Bottom-Up Parsers (Shift-Reduce Parsing & Handle Pruning)</td><td>✅ Complete</td></tr>
      <tr><td>14</td><td>Variants of LR Parsers (LR(0), SLR(1), CLR(1), LALR(1))</td><td>✅ Complete</td></tr>
      <tr><td>15</td><td>Handling Parsing Conflicts (Shift-Reduce & Reduce-Reduce)</td><td>✅ Complete</td></tr>
      <tr><td>16</td><td>Detection of Syntax Errors (Panic-Mode & Phrase-Level)</td><td>✅ Complete</td></tr>
      <tr><td>17</td><td>Reporting of Syntax Errors & Diagnostics</td><td>✅ Complete</td></tr>

      <tr><td rowspan="9"><strong>M3: Semantic Analysis (9)</strong></td><td>18</td><td>Introduction to Semantic Analysis & Static Checks</td><td>✅ Complete</td></tr>
      <tr><td>19</td><td>Syntax-Directed Definitions (SDD Semantic Rules)</td><td>✅ Complete</td></tr>
      <tr><td>20</td><td>Syntax-Directed Translation Schemes (SDTS Actions)</td><td>✅ Complete</td></tr>
      <tr><td>21</td><td>SDTS for Declaration Processing & Symbol Tables</td><td>✅ Complete</td></tr>
      <tr><td>22</td><td>Three Address Code (Quadruples, Triples, Indirect Triples)</td><td>✅ Complete</td></tr>
      <tr><td>23</td><td>Types of Attributes (Synthesized vs. Inherited)</td><td>✅ Complete</td></tr>
      <tr><td>24</td><td>Type Checking for Expressions (Equivalence & Coercion)</td><td>✅ Complete</td></tr>
      <tr><td>25</td><td>Intermediate Code Generation for Assignment Statements</td><td>✅ Complete</td></tr>
      <tr><td>26</td><td>Translation of Multi-Dimensional Array References</td><td>✅ Complete</td></tr>

      <tr><td rowspan="9"><strong>M4: Intermediate & Runtime (9)</strong></td><td>27</td><td>Complete Evaluation of Boolean Expressions</td><td>✅ Complete</td></tr>
      <tr><td>28</td><td>Partial Evaluation (Short-Circuit) of Boolean Expressions</td><td>✅ Complete</td></tr>
      <tr><td>29</td><td>Translation of Control Flow Constructs (`if-else`, `while`)</td><td>✅ Complete</td></tr>
      <tr><td>30</td><td>Resolution of Forward Jumps & Backpatching</td><td>✅ Complete</td></tr>
      <tr><td>31</td><td>Resolution of Backward Jumps in Loops</td><td>✅ Complete</td></tr>
      <tr><td>32</td><td>Translation of Function Calls (`param`, `call`)</td><td>✅ Complete</td></tr>
      <tr><td>33</td><td>Translation of Function Returns & Caller Restoration</td><td>✅ Complete</td></tr>
      <tr><td>34</td><td>Memory Layout of Code and Data (Text, Static, Heap, Stack)</td><td>✅ Complete</td></tr>
      <tr><td>35</td><td>Activation Records (Stack Frame Anatomy: P-R-C-A-S-L-T)</td><td>✅ Complete</td></tr>

      <tr><td rowspan="12"><strong>M5: Optimization & Code Gen (12)</strong></td><td>36</td><td>Addresses of Code and Data in Assembly Code</td><td>✅ Complete</td></tr>
      <tr><td>37</td><td>Correlation of Assembly Code with Source Code</td><td>✅ Complete</td></tr>
      <tr><td>38</td><td>Construction of Basic Blocks (3 Leader Rules)</td><td>✅ Complete</td></tr>
      <tr><td>39</td><td>Control Flow Graph (CFG Nodes & Edges)</td><td>✅ Complete</td></tr>
      <tr><td>40</td><td>Machine-Independent Local Optimizations</td><td>✅ Complete</td></tr>
      <tr><td>41</td><td>Machine-Independent Global Optimizations</td><td>✅ Complete</td></tr>
      <tr><td>42</td><td>Unreachable Code Elimination</td><td>✅ Complete</td></tr>
      <tr><td>43</td><td>Constant Folding Optimization</td><td>✅ Complete</td></tr>
      <tr><td>44</td><td>Constant Propagation Optimization</td><td>✅ Complete</td></tr>
      <tr><td>45</td><td>Loop-Invariant Code Motion (Hoisting)</td><td>✅ Complete</td></tr>
      <tr><td>46</td><td>Common Subexpression Elimination (CSE)</td><td>✅ Complete</td></tr>
      <tr><td>47</td><td>Dead Code Elimination</td><td>✅ Complete</td></tr>
    </tbody>
  </table>
</div>

<h2 class="section-title">🧠 Master Conceptual Differences Flashcards</h2>

<table class="custom-table">
  <thead><tr><th>Concept Pair</th><th>Core Distinction & Memory Cue</th></tr></thead>
  <tbody>
    <tr><td><strong>Token vs. Lexeme vs. Pattern</strong></td><td>`Token` = Abstract Category; `Lexeme` = Concrete characters in code; `Pattern` = Regex rule.</td></tr>
    <tr><td><strong>Compiler vs. Interpreter</strong></td><td>`Compiler` = Translates entire program to binary upfront; `Interpreter` = Translates & executes line-by-line.</td></tr>
    <tr><td><strong>Syntax vs. Semantics</strong></td><td>`Syntax` = Grammatical structure (Parse tree); `Semantics` = Logical meaning & type consistency.</td></tr>
    <tr><td><strong>SDD vs. SDTS</strong></td><td>`SDD` = High-level attribute grammar + semantic rules; `SDTS` = Grammar with explicit action code `{...}` embedded.</td></tr>
    <tr><td><strong>Synthesized vs. Inherited</strong></td><td>`Synthesized` = Computed from children (Bottom-up); `Inherited` = Passed from parent/siblings (Top-down).</td></tr>
    <tr><td><strong>Quadruple vs. Triple</strong></td><td>`Quadruple` = Explicit `(op, arg1, arg2, result)`; `Triple` = Implicit index reference `(op, arg1, arg2)`.</td></tr>
    <tr><td><strong>Control Link vs. Access Link</strong></td><td>`Control Link` = Points to dynamic caller frame; `Access Link` = Points to static lexical enclosing scope.</td></tr>
    <tr><td><strong>Constant Folding vs. Propagation</strong></td><td>`Folding` = Evaluates `3 + 4 -> 7`; `Propagation` = Substitutes variable `x=7; y=x+2 -> y=7+2`.</td></tr>
    <tr><td><strong>Unreachable vs. Dead Code</strong></td><td>`Unreachable` = Can never execute (no path); `Dead` = Executes, but result is never used.</td></tr>
  </tbody>
</table>
"""
