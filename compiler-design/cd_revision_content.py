# Compiler Design 10-Page Master Revision (CS24301)
CD_REVISION_EXHAUSTIVE = r"""

    <div class="toc-box">
      <div class="toc-title">⚡ 10-Page Master Quick Revision — Compiler Design (CS24301)</div>
      <div class="toc-grid">
        <div>Page 1: 47-Topic Master Syllabus Progress Checklist (Modules I – V)</div>
        <div>Page 2: The Tier-S High-Yield Core Topic Ranking & Exam Strategy</div>
        <div>Page 3: Lexical Analysis: Phases of Compiler, Input Buffering & Regular Expressions</div>
        <div>Page 4: Direct DFA Construction: Nullable, Firstpos, Lastpos & Followpos Rules</div>
        <div>Page 5: Context-Free Grammars, Left Recursion Elimination & Left Factoring</div>
        <div>Page 6: Top-Down LL(1) Parsing: FIRST & FOLLOW Inductive Math & Table Construction</div>
        <div>Page 7: Bottom-Up LR Parsing Hierarchy: LR(0), SLR(1), CLR(1) & LALR(1)</div>
        <div>Page 8: Semantic Analysis & SDD: S-Attributed vs. L-Attributed Definitions</div>
        <div>Page 9: Intermediate Code: 3AC, Quadruples, Triples & Multi-Dimensional Array Offsets</div>
        <div>Page 10: Code Generation & Optimization: Basic Blocks, CFG, DAG, Data-Flow & Peephole</div>
      </div>
    </div>

    <h2 class="section-title" style="margin-top: 0;">Page 1: Complete 47-Topic Master Syllabus Progress Checklist</h2>
    <div class="callout callout-info">
      <div class="callout-title">CS24301 Compiler Design — All 47 Topics Verified & Mastered</div>
      <table class="custom-table" style="font-size: 10px;">
        <thead><tr><th>Module</th><th>Topic #</th><th>Topic Name</th><th>Key Focus</th></tr></thead>
        <tbody>
          <tr><td rowspan="7"><strong>M1: Lexical (7)</strong></td><td>1</td><td>Introduction & Cousins (P-I-C-A-L)</td><td>Preprocessor, Compiler, Assembler, Linker, Loader</td></tr>
          <tr><td>2</td><td>Structure of Compiler (6 Phases)</td><td>Analysis front-end vs. Synthesis back-end</td></tr>
          <tr><td>3</td><td>The Lexical Analyzer</td><td>Token, Lexeme, Pattern & Error Recovery</td></tr>
          <tr><td>4</td><td>Input Buffering Strategies</td><td>Two-Buffer Scheme & Sentinel Optimizations</td></tr>
          <tr><td>5</td><td>Specification of Tokens</td><td>Regular Expressions & Algebraic Properties</td></tr>
          <tr><td>6</td><td>Recognition of Tokens</td><td>Transition Diagrams & Finite Automata</td></tr>
          <tr><td>7</td><td>Direct DFA Construction</td><td>Nullable, Firstpos, Lastpos, Followpos</td></tr>

          <tr><td rowspan="10"><strong>M2: Syntax (10)</strong></td><td>8</td><td>Introduction & CFG Grammars</td><td>Grammar Formal 4-tuple & Ambiguity Proofs</td></tr>
          <tr><td>9</td><td>Grammar Transformations</td><td>Left Recursion Elimination & Left Factoring</td></tr>
          <tr><td>10</td><td>Recursive Top-Down Parsers</td><td>Recursive Descent Parsing & Backtracking</td></tr>
          <tr><td>11</td><td>Non-Recursive Top-Down</td><td>Stack-driven LL(1) Parsing Table Model</td></tr>
          <tr><td>12</td><td>LL(1) Parser Design</td><td>FIRST & FOLLOW Math + Table Construction</td></tr>
          <tr><td>13</td><td>Bottom-Up Shift-Reduce</td><td>Handles, Handle Pruning & Viable Prefixes</td></tr>
          <tr><td>14</td><td>Variants of LR Parsers</td><td>LR(0), SLR(1), CLR(1), LALR(1) Hierarchy</td></tr>
          <tr><td>15</td><td>Parsing Conflict Handling</td><td>Shift-Reduce & Reduce-Reduce Disambiguation</td></tr>
          <tr><td>16</td><td>Syntax Error Detection</td><td>Panic-Mode & Phrase-Level Recovery</td></tr>
          <tr><td>17</td><td>Syntax Error Reporting</td><td>Error Productions & Diagnostic Compilers</td></tr>

          <tr><td rowspan="9"><strong>M3: Semantics (9)</strong></td><td>18</td><td>Semantic Analysis Overview</td><td>Static vs. Dynamic Semantic Checks</td></tr>
          <tr><td>19</td><td>Syntax-Directed Definitions</td><td>SDD Attribute Grammars & Dependency Graphs</td></tr>
          <tr><td>20</td><td>SDTS Translation Schemes</td><td>Embedded Semantic Actions in Productions</td></tr>
          <tr><td>21</td><td>SDTS for Declarations</td><td>Type Propagation & Scoped Symbol Tables</td></tr>
          <tr><td>22</td><td>Three-Address Code (TAC)</td><td>Quadruples, Triples & Indirect Triples</td></tr>
          <tr><td>23</td><td>Types of Attributes</td><td>S-Attributed vs. L-Attributed Definitions</td></tr>
          <tr><td>24</td><td>Type Checking</td><td>Name vs. Structural Equivalence & Coercion</td></tr>
          <tr><td>25</td><td>ICG for Assignments</td><td>Scalar Arithmetic & Temporary Allocation</td></tr>
          <tr><td>26</td><td>Multi-D Array Translation</td><td>Row/Col Major Linear Offset Derivations</td></tr>

          <tr><td rowspan="9"><strong>M4: Runtime (9)</strong></td><td>27</td><td>Boolean Expression ICG</td><td>Short-Circuit Boolean Evaluation Semantics</td></tr>
          <tr><td>28</td><td>Control Flow Translation</td><td>`if-else`, `while`, `for`, `switch-case` Jumps</td></tr>
          <tr><td>29</td><td>Backpatching Mechanics</td><td>`makelist`, `merge`, `backpatch` Operations</td></tr>
          <tr><td>30</td><td>Forward & Backward Jumps</td><td>Jump Labels & Control Flow Synthesis</td></tr>
          <tr><td>31</td><td>Procedure Calls & Returns</td><td>`param`, `call`, `return` & Parameter Modes</td></tr>
          <tr><td>32</td><td>Runtime Storage Layout</td><td>Code, Static, Heap & Call Stack Organization</td></tr>
          <tr><td>33</td><td>Activation Records (Stack)</td><td>7 P-R-C-A-S-L-T Frame Fields & Memory Map</td></tr>
          <tr><td>34</td><td>Storage Allocation Rules</td><td>Static vs. Stack vs. Heap Allocation</td></tr>
          <tr><td>35</td><td>Non-Local Data Access</td><td>Static Links Chain vs. Displays Array</td></tr>

          <tr><td rowspan="12"><strong>M5: Opt & CG (12)</strong></td><td>36</td><td>Code Generator Design</td><td>Instruction Selection & Target Architecture</td></tr>
          <tr><td>37</td><td>Target Language Costs</td><td>Instruction Costs & Target Addressing Modes</td></tr>
          <tr><td>38</td><td>Addresses in Target Code</td><td>Static Offsets & Stack Frame Relocation</td></tr>
          <tr><td>39</td><td>Basic Block Construction</td><td>The 3 Classical Leader Identification Rules</td></tr>
          <tr><td>40</td><td>Control Flow Graphs (CFG)</td><td>Basic Block Graph, Dominators & Loops</td></tr>
          <tr><td>41</td><td>Next-Use & Liveness</td><td>Variable Liveness inside Basic Blocks</td></tr>
          <tr><td>42</td><td>Register Allocation</td><td>Chaitin-Briggs Graph Coloring Algorithm</td></tr>
          <tr><td>43</td><td>Directed Acyclic Graphs</td><td>DAG Construction for Local Block Optimization</td></tr>
          <tr><td>44</td><td>Data-Flow Frameworks</td><td>Reaching Definitions, Available Expressions</td></tr>
          <tr><td>45</td><td>Loop Optimizations</td><td>Loop Invariant Code Motion & Strength Red.</td></tr>
          <tr><td>46</td><td>Peephole Optimization</td><td>Sliding Window Redundant Instruction Removal</td></tr>
          <tr><td>47</td><td>Simple Code Generation</td><td>Register & Address Descriptors (`getReg`)</td></tr>
        </tbody>
      </table>
    </div>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 2: The Tier-S High-Yield Core Topic Ranking & Exam Strategy</h2>
    <table class="custom-table">
      <thead><tr><th>Rank</th><th>Core Exam Topic</th><th>Module</th><th>Frequency & Yield</th><th>Essential Mathematical Formula / Rule</th></tr></thead>
      <tbody>
        <tr><td><strong>⭐ 1</strong></td><td>Direct DFA Construction</td><td>M1</td><td>100% Exam Probability (10M)</td><td>$\text{followpos}(i)$ on Syntax Tree Cat/Star nodes; $\text{DTran}[S, a] = \bigcup_{p \in S} \text{followpos}(p)$</td></tr>
        <tr><td><strong>⭐ 2</strong></td><td>Left Recursion Elimination</td><td>M2</td><td>100% Exam Probability (5M)</td><td>$A \rightarrow A\alpha \mid \beta \implies A \rightarrow \beta A', \ A' \rightarrow \alpha A' \mid \epsilon$</td></tr>
        <tr><td><strong>⭐ 3</strong></td><td>LL(1) Parser Construction</td><td>M2</td><td>100% Exam Probability (10M)</td><td>$\text{FIRST}(\alpha)$ and $\text{FOLLOW}(A)$ calculation tables + Parsing Table $M[A, a]$</td></tr>
        <tr><td><strong>⭐ 4</strong></td><td>LR Parsing Power Hierarchy</td><td>M2</td><td>100% Exam Probability (8M)</td><td>$\text{LR}(0) \subset \text{SLR}(1) \subset \text{LALR}(1) \subset \text{CLR}(1)$; LALR(1) merges core states</td></tr>
        <tr><td><strong>⭐ 5</strong></td><td>S- vs. L-Attributed SDD</td><td>M3</td><td>100% Exam Probability (8M)</td><td>Synthesized attributes (Bottom-Up LR) vs. Inherited left-to-right attributes (Top-Down LL)</td></tr>
        <tr><td><strong>⭐ 6</strong></td><td>Multi-Dimensional Array Offsets</td><td>M3</td><td>100% Exam Probability (10M)</td><td>Row-Major: $\text{Address} = \text{base} + [(i_1 - l_1) \cdot n_2 + (i_2 - l_2)] \cdot w$</td></tr>
        <tr><td><strong>⭐ 7</strong></td><td>Backpatching Control Flow</td><td>M4</td><td>100% Exam Probability (10M)</td><td>$\text{makelist}(i), \text{merge}(p_1, p_2), \text{backpatch}(p, \text{label})$ for boolean expressions</td></tr>
        <tr><td><strong>⭐ 8</strong></td><td>Activation Record (Stack Frame)</td><td>M4</td><td>100% Exam Probability (8M)</td><td>The 7 Fields: Parameters, Return value, Control link, Access link, Saved status, Local data, Temporaries</td></tr>
        <tr><td><strong>⭐ 9</strong></td><td>Basic Block Leader Rules</td><td>M5</td><td>100% Exam Probability (6M)</td><td>1. First instruction; 2. Target of branch; 3. Instruction immediately following branch</td></tr>
        <tr><td><strong>⭐ 10</strong></td><td>Data-Flow Reaching Definitions</td><td>M5</td><td>100% Exam Probability (10M)</td><td>$\text{IN}[B] = \bigcup_{P \in \text{Pred}} \text{OUT}[P], \quad \text{OUT}[B] = \text{GEN}[B] \cup (\text{IN}[B] - \text{KILL}[B])$</td></tr>
      </tbody>
    </table>

    <div class="callout callout-info">
      <div class="callout-title">Master Strategic Examination Execution Protocol</div>
      1. <strong>Section A (2 Marks):</strong> Target definitions: Token vs Lexeme, Compiler vs Interpreter, S- vs L-attributed, Static vs Dynamic scoping.<br>
      2. <strong>Section B (5 Marks):</strong> Short derivations: Left recursion elimination, Left factoring, Intermediate code triples/quadruples, Peephole rules.<br>
      3. <strong>Section C (10–14 Marks):</strong> Full numericals: Direct DFA from RE, LL(1) Table & Stack simulation, LR parsing DFA item sets, 3D Array memory calculations, Reaching Definitions data-flow convergence!
    </div>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 3: Module I — Lexical Analysis & Compiler Architecture</h2>
    <div class="formula-card">
      <strong>The 6 Compiler Phases & Memory Flow:</strong><br>
      1. <strong>Lexical Analysis:</strong> Characters $\rightarrow$ Tokens. (DFA / Input Buffering).<br>
      2. <strong>Syntax Analysis:</strong> Tokens $\rightarrow$ Parse Tree / AST. (CFG / LL & LR Parsers).<br>
      3. <strong>Semantic Analysis:</strong> AST $\rightarrow$ Decorated AST. (Type Checking & SDD).<br>
      4. <strong>Intermediate Code Gen:</strong> Decorated AST $\rightarrow$ Three-Address Code (TAC).<br>
      5. <strong>Code Optimization:</strong> TAC $\rightarrow$ Optimized TAC (CFG, Data-Flow & Loops).<br>
      6. <strong>Target Code Gen:</strong> Optimized TAC $\rightarrow$ Target Assembly / Binary.
    </div>

    <table class="custom-table">
      <thead><tr><th>Concept</th><th>Formal Definition</th><th>Example</th></tr></thead>
      <tbody>
        <tr><td><strong>Token</strong></td><td>Abstract syntactic terminal symbol category.</td><td>`IDENTIFIER`, `NUMBER`, `KW_IF`</td></tr>
        <tr><td><strong>Lexeme</strong></td><td>Concrete source code character sequence matching pattern.</td><td>`"total_count"`, `"120"`, `"if"`</td></tr>
        <tr><td><strong>Pattern</strong></td><td>Formal regular expression grammar rule for lexeme.</td><td>`[a-zA-Z_][a-zA-Z0-9_]*`</td></tr>
      </tbody>
    </table>

    <div class="callout callout-info">
      <div class="callout-title">Input Buffering & Sentinel Optimization</div>
      • Naive buffering checks for buffer end AND current character (2 checks/char).<br>
      • Placing `eof` Sentinels at the end of each 4096-byte half-buffer reduces this to <strong>1 check/char</strong> in the common case!
    </div>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 4: Module I — Direct Construction of DFA from Regular Expressions</h2>
    <div class="formula-card">
      <strong>The 4 Positional Syntax-Tree Functions:</strong><br>
      • $\mathbf{\text{nullable}(n)}$: Subexpression at node $n$ can generate $\epsilon$.<br>
      • $\mathbf{\text{firstpos}(n)}$: Leaf positions matching first character of strings in $L(n)$.<br>
      • $\mathbf{\text{lastpos}(n)}$: Leaf positions matching last character of strings in $L(n)$.<br>
      • $\mathbf{\text{followpos}(i)}$: Positions $j$ that can immediately follow position $i$.
    </div>
    <table class="custom-table">
      <thead><tr><th>Node $n$</th><th>$\text{nullable}(n)$</th><th>$\text{firstpos}(n)$</th><th>$\text{lastpos}(n)$</th></tr></thead>
      <tbody>
        <tr><td>Leaf $\epsilon$</td><td>$\text{true}$</td><td>$\emptyset$</td><td>$\emptyset$</td></tr>
        <tr><td>Leaf pos $i$</td><td>$\text{false}$</td><td>$\{i\}$</td><td>$\{i\}$</td></tr>
        <tr><td>$c_1 \mid c_2$</td><td>$\text{null}(c_1) \vee \text{null}(c_2)$</td><td>$\text{firstpos}(c_1) \cup \text{firstpos}(c_2)$</td><td>$\text{lastpos}(c_1) \cup \text{lastpos}(c_2)$</td></tr>
        <tr><td>$c_1 \cdot c_2$</td><td>$\text{null}(c_1) \wedge \text{null}(c_2)$</td><td>$\text{if } \text{null}(c_1) \text{ then } \text{firstpos}(c_1) \cup \text{firstpos}(c_2) \text{ else } \text{firstpos}(c_1)$</td><td>$\text{if } \text{null}(c_2) \text{ then } \text{lastpos}(c_1) \cup \text{lastpos}(c_2) \text{ else } \text{lastpos}(c_2)$</td></tr>
        <tr><td>$c_1^*$</td><td>$\text{true}$</td><td>$\text{firstpos}(c_1)$</td><td>$\text{lastpos}(c_1)$</td></tr>
      </tbody>
    </table>
    <div class="callout callout-info">
      <div class="callout-title">Hopcroft DFA Minimization Algorithm</div>
      Initialize $P = \{F, S - F\}$. Repeatedly split groups $G$ on input $a \in \Sigma$ until no further partitions can be made. Merges all equivalent states in $O(n \log n)$ time!
    </div>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 5: Module II — Context-Free Grammars & Top-Down LL(1) Parsing</h2>
    <div class="formula-card">
      <strong>Grammar Transformation Formulas:</strong><br>
      1. <strong>Immediate Left Recursion:</strong> $A \rightarrow A\alpha \mid \beta \implies \mathbf{A \rightarrow \beta A', \quad A' \rightarrow \alpha A' \mid \epsilon}$<br>
      2. <strong>Left Factoring:</strong> $A \rightarrow \alpha \beta_1 \mid \alpha \beta_2 \mid \gamma \implies \mathbf{A \rightarrow \alpha A' \mid \gamma, \quad A' \rightarrow \beta_1 \mid \beta_2}$
    </div>
    <div class="callout callout-info">
      <div class="callout-title">Condition for LL(1) Grammar</div>
      A grammar $G$ is LL(1) if and only if for every pair of productions $A \rightarrow \alpha \mid \beta$:<br>
      1. $\text{FIRST}(\alpha) \cap \text{FIRST}(\beta) = \emptyset$<br>
      2. If $\alpha \Rightarrow^* \epsilon$, then $\text{FIRST}(\beta) \cap \text{FOLLOW}(A) = \emptyset$.
    </div>
    <div class="worked-box">
      <div class="worked-title">FIRST and FOLLOW Rules Reference</div>
      • $\text{FIRST}(X)$: Terminals starting strings derived from $X$. Include $\epsilon$ if $X \Rightarrow^* \epsilon$.<br>
      • $\text{FOLLOW}(A)$: Terminals appearing immediately to right of $A$ in some sentential form. Always include $\$$ in $\text{FOLLOW}(S)$.
    </div>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 6: Module II — Bottom-Up LR Parsing Hierarchy</h2>
    <table class="custom-table">
      <thead><tr><th>Parser</th><th>Item Format</th><th>Reduction Rule</th><th>States</th><th>Power</th></tr></thead>
      <tbody>
        <tr><td><strong>LR(0)</strong></td><td>$[A \rightarrow \alpha \cdot \beta]$</td><td>Placed in ALL terminal columns</td><td>$K$</td><td>Weakest</td></tr>
        <tr><td><strong>SLR(1)</strong></td><td>$[A \rightarrow \alpha \cdot \beta]$</td><td>Placed ONLY in $\text{FOLLOW}(A)$ columns</td><td>$K$</td><td>Moderate</td></tr>
        <tr><td><strong>CLR(1)</strong></td><td>$[A \rightarrow \alpha \cdot \beta, a]$</td><td>Placed ONLY for exact lookahead $a$</td><td>$5\times\text{ to }10\times K$</td><td>Most Powerful</td></tr>
        <tr><td><strong>LALR(1)</strong></td><td>Merged $[A \rightarrow \alpha \cdot \beta, a \mid b]$</td><td>Merges CLR(1) states with identical LR(0) cores</td><td>$K$</td><td>Industry Standard</td></tr>
      </tbody>
    </table>
    <div class="callout callout-warning">
      <div class="callout-title">Shift-Reduce vs Reduce-Reduce Conflicts</div>
      • <strong>Shift-Reduce:</strong> Parser cannot decide whether to shift token or reduce handle (resolve by favoring Shift).<br>
      • <strong>Reduce-Reduce:</strong> Parser cannot decide between two productions to reduce by (grammar flaw).
    </div>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 7: Module III — Semantic Analysis, SDD & Type Checking</h2>
    <table class="custom-table">
      <thead><tr><th>Dimension</th><th>S-Attributed Definitions</th><th>L-Attributed Definitions</th></tr></thead>
      <tbody>
        <tr><td><strong>Attributes Used</strong></td><td>Synthesized attributes ONLY</td><td>Synthesized AND Inherited attributes</td></tr>
        <tr><td><strong>Information Flow</strong></td><td>Strictly Bottom-Up (Children $\rightarrow$ Parent)</td><td>Top-Down & Left-to-Right between siblings</td></tr>
        <tr><td><strong>Evaluation Traversal</strong></td><td>Post-Order Traversal</td><td>Pre-Order / Depth-First Traversal</td></tr>
        <tr><td><strong>Parsing Engine</strong></td><td>Evaluated on-the-fly during Bottom-Up LR reductions</td><td>Natural match for Top-Down LL recursive descent</td></tr>
      </tbody>
    </table>
    <div class="formula-card">
      <strong>Type Systems & Structural Equivalence:</strong><br>
      • <strong>Name Equivalence:</strong> Types are identical only if declared under identical names.<br>
      • <strong>Structural Equivalence:</strong> Types are identical if internal memory layouts, fields, and sizes match.
    </div>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 8: Module III — Multi-Dimensional Array Offsets & Three-Address Code</h2>
    <div class="formula-card">
      <strong>Multi-Dimensional Array Address Formulas:</strong><br>
      • <strong>1D Array:</strong> $\text{Address}(A[i]) = \text{base} + (i - \text{low}) \cdot w$<br>
      • <strong>2D Row-Major:</strong> $\text{Address}(A[i, j]) = \text{base} + \big[ (i - l_1) \cdot n_2 + (j - l_2) \big] \cdot w$<br>
      • <strong>2D Column-Major:</strong> $\text{Address}(A[i, j]) = \text{base} + \big[ (j - l_2) \cdot n_1 + (i - l_1) \big] \cdot w$<br>
      • <strong>3D Row-Major:</strong> $\text{Address}(A[i, j, k]) = \text{base} + \Big[ \big( (i - l_1) \cdot n_2 + (j - l_2) \big) \cdot n_3 + (k - l_3) \Big] \cdot w$
    </div>

    <table class="custom-table">
      <thead><tr><th>TAC Representation</th><th>Record Structure</th><th>Key Advantage</th></tr></thead>
      <tbody>
        <tr><td><strong>Quadruples</strong></td><td>`(op, arg1, arg2, result)`</td><td>Free reordering during optimization passes</td></tr>
        <tr><td><strong>Triples</strong></td><td>`(op, arg1, arg2)`</td><td>Saves memory; no temporary variable names</td></tr>
        <tr><td><strong>Indirect Triples</strong></td><td>Array of pointers $\rightarrow$ Triples</td><td>Optimal reordering without altering triple memory</td></tr>
      </tbody>
    </table>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 9: Module IV — Control Flow, Backpatching & Runtime Environments</h2>
    <div class="formula-card">
      <strong>The 3 Backpatching Functions:</strong><br>
      1. $\mathbf{\text{makelist}(i)}$: Creates a new list containing instruction index $i$.<br>
      2. $\mathbf{\text{merge}(p_1, p_2)}$: Concatenates two jump target lists.<br>
      3. $\mathbf{\text{backpatch}(p, L)}$: Inserts label $L$ into all instructions indexed in list $p$.
    </div>

    <div class="callout callout-info">
      <div class="callout-title">The 7 Activation Record Fields (P-R-C-A-S-L-T)</div>
      <strong>P</strong>arameters $\rightarrow$ <strong>R</strong>eturn value $\rightarrow$ <strong>C</strong>ontrol link $\rightarrow$ <strong>A</strong>ccess link $\rightarrow$ <strong>S</strong>aved machine status $\rightarrow$ <strong>L</strong>ocal data $\rightarrow$ <strong>T</strong>emporaries.
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">Non-Local Variable Access</div>
      • <strong>Static Links:</strong> Linked pointer traversal ($O(k)$ time for depth $k$).<br>
      • <strong>Displays Array:</strong> Global array `d[depth]` providing guaranteed $\mathbf{O(1)}$ instant access!
    </div>
    <div class='page-break'></div>
    <h2 class="section-title" style="margin-top: 0;">Page 10: Module V — Code Optimization & Target Code Generation</h2>
    <div class="formula-card">
      <strong>Basic Block Leader Rules:</strong><br>
      1. The first instruction of the TAC sequence is a Leader.<br>
      2. Any instruction that is the target of a jump is a Leader.<br>
      3. Any instruction immediately following a jump is a Leader.
    </div>

    <div class="formula-card">
      <strong>Data-Flow Equations for Reaching Definitions:</strong><br>
      $$\mathbf{\text{IN}[B] = \bigcup_{P \in \text{Pred}[B]} \text{OUT}[P]}$$
      $$\mathbf{\text{OUT}[B] = \text{GEN}[B] \cup (\text{IN}[B] - \text{KILL}[B])}$$
    </div>

    <table class="custom-table">
      <thead><tr><th>Optimization Pass</th><th>Mechanism</th><th>Before $\rightarrow$ After</th></tr></thead>
      <tbody>
        <tr><td><strong>Constant Folding</strong></td><td>Compile-time arithmetic</td><td>`x = 10 * 20` $\rightarrow$ `x = 200`</td></tr>
        <tr><td><strong>Constant Propagation</strong></td><td>Propagating constant values</td><td>`x = 10; y = x + 5;` $\rightarrow$ `y = 15;`</td></tr>
        <tr><td><strong>Loop-Invariant Motion</strong></td><td>Hoisting out of loops</td><td>Statements independent of loop variables moved to pre-header</td></tr>
        <tr><td><strong>Strength Reduction</strong></td><td>Cheaper operations</td><td>Replacing multiplication $i * 4$ with pointer additions or shifts</td></tr>
        <tr><td><strong>Dead Code Elimination</strong></td><td>Removing unused writes</td><td>Deleting computations whose values are never read</td></tr>
      </tbody>
    </table>
    
"""
