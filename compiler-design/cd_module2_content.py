# Compiler Design Module 2 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

CD_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Syntax Analysis & Parsing Algorithms — Complete Syllabus Topics</div>
  <div class="toc-grid">
    <div>1. Role of Parser & Context-Free Grammars (CFG) Mathematical Formulations</div>
    <div>2. Parse Trees, Derivations (Leftmost & Rightmost) & Ambiguity Proofs</div>
    <div>3. Left Recursion Elimination (Immediate & Indirect Grammatical Algorithms)</div>
    <div>4. Left Factoring Algorithm for Common Prefixes</div>
    <div>5. FIRST and FOLLOW Sets Formal Inductive Formulations & Traces</div>
    <div>6. LL(1) Top-Down Predictive Parsing Table Construction & Stack Simulations</div>
    <div>7. Bottom-Up Shift-Reduce Parsing Principles & Handle Pruning Theorems</div>
    <div>8. LR(0) Canonical Collection of Items & SLR(1) Parsing Table Formulations</div>
    <div>9. Canonical LR (CLR(1)) Items with Lookaheads & LALR(1) State Merging</div>
    <div>10. Parsing Conflicts (Shift/Reduce, Reduce/Reduce) & Ambiguity Resolutions</div>
    <div>11. Syntax Error Detection & Recovery Strategies (Panic Mode & Phrase Level)</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Question Bank (8 Solved Problems)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Context-Free Grammars, Derivations & Ambiguity</h2>
<p>
  A <strong>Context-Free Grammar (CFG)</strong> is formally defined as a 4-tuple $G = (V, T, P, S)$:
</p>
<ul>
  <li>$V$: Finite set of Non-Terminal characters (syntactic variables).</li>
  <li>$T$: Finite set of Terminal characters (token types returned by lexical analyzer).</li>
  <li>$P$: Finite set of Production rules of the form $A \rightarrow \alpha$, where $A \in V$ and $\alpha \in (V \cup T)^*$.</li>
  <li>$S \in V$: The designated Start Symbol.</li>
</ul>

<h3 class="subsection-title">1. Derivations & Parse Trees:</h3>
<ul>
  <li><strong>Leftmost Derivation (LMD):</strong> At each derivation step, the leftmost non-terminal is replaced by the body of one of its productions ($\alpha \xRightarrow[lm]{} \beta$).</li>
  <li><strong>Rightmost Derivation (RMD / Canonical Derivation):</strong> At each step, the rightmost non-terminal is replaced ($\alpha \xRightarrow[rm]{} \beta$). Bottom-up parsers reconstruct the reverse of a rightmost derivation ($RMD^R$).</li>
  <li><strong>Parse Tree:</strong> A graphical representation of a derivation where the root is start symbol $S$, interior nodes are non-terminals, and leaves are terminals or $\epsilon$, read left-to-right to yield the input sentence.</li>
</ul>

<div class="callout callout-warning">
  <div class="callout-title">Formal Definition of Grammar Ambiguity</div>
  A grammar $G$ is <strong>ambiguous</strong> if there exists at least one string $w \in L(G)$ that has <strong>two or more distinct parse trees</strong> (or equivalently, two distinct leftmost derivations). Ambiguity makes deterministic parsing impossible unless resolved by disambiguating rules.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Classic Problem: Disambiguating the Dangling-Else Grammar</div>
  <p><strong>Ambiguous Grammar:</strong></p>
  $$\text{stmt} \rightarrow \mathbf{if} \ \text{expr} \ \mathbf{then} \ \text{stmt} \mid \mathbf{if} \ \text{expr} \ \mathbf{then} \ \text{stmt} \ \mathbf{else} \ \text{stmt} \mid \mathbf{other}$$
  <p>For input `if E1 then if E2 then S1 else S2`, the `else` clause can be attached to the first or second `if`.</p>
  <p><strong>Unambiguous Disambiguated Grammar:</strong></p>
  <pre><code>stmt          -> matched_stmt | open_stmt
matched_stmt  -> if expr then matched_stmt else matched_stmt | other
open_stmt     -> if expr then stmt
               | if expr then matched_stmt else open_stmt</code></pre>
  <p>Enforces that every `else` matches the closest preceding unmatched `then`.</p>
</div>

<h2 class="section-title">Topic 3 & 4: Grammar Transformations (Left Recursion & Left Factoring)</h2>

<h3 class="subsection-title">1. Immediate Left Recursion Elimination:</h3>
<p>
  A production of the form $A \rightarrow A\alpha \mid \beta$ causes top-down predictive parsers to loop infinitely. It is eliminated by introducing a new non-terminal $A'$:
</p>
$$A \rightarrow \beta A', \qquad A' \rightarrow \alpha A' \mid \epsilon$$

<h3 class="subsection-title">2. General Left Recursion Elimination Algorithm (Handling Indirect Recursion):</h3>
<ol>
  <li>Order non-terminals in an arbitrary sequence: $A_1, A_2, \dots, A_n$.</li>
  <li>For $i = 1$ to $n$:
    <ul>
      <li>For $j = 1$ to $i-1$: Replace each production of the form $A_i \rightarrow A_j \gamma$ by $A_i \rightarrow \delta_1 \gamma \mid \delta_2 \gamma \mid \dots \mid \delta_k \gamma$, where $A_j \rightarrow \delta_1 \mid \delta_2 \mid \dots \mid \delta_k$ are the current $A_j$ rules.</li>
      <li>Eliminate immediate left recursion among the $A_i$ productions.</li>
    </ul>
  </li>
</ol>

<h3 class="subsection-title">3. Left Factoring Algorithm (Removing Common Prefixes):</h3>
<p>
  When two productions for $A$ share a common prefix ($A \rightarrow \alpha\beta_1 \mid \alpha\beta_2$), the parser cannot determine which rule to apply with 1 lookahead token. Left factoring delays the decision:
</p>
$$A \rightarrow \alpha A', \qquad A' \rightarrow \beta_1 \mid \beta_2$$

<h2 class="section-title">Topic 5: Formal Formulations of FIRST and FOLLOW Sets</h2>

<div class="callout callout-info">
  <div class="callout-title">Mathematical Definitions</div>
  <ul>
    <li><strong>$\text{FIRST}(\alpha)$:</strong> Set of all terminals that appear as the first symbol in strings derived from $\alpha$. If $\alpha \xrightarrow{*} \epsilon$, then $\epsilon \in \text{FIRST}(\alpha)$.</li>
    <li><strong>$\text{FOLLOW}(A)$:</strong> Set of all terminals $a$ that can appear immediately to the right of non-terminal $A$ in some sentential form ($S \xrightarrow{*} \alpha A a \beta$). If $A$ is the rightmost symbol in a derivation, the input end-marker $\$$ is in $\text{FOLLOW}(A)$.</li>
  </ul>
</div>

<h3 class="subsection-title">Formal Rules for Computing FIRST:</h3>
<ol>
  <li>If $X$ is a terminal, $\text{FIRST}(X) = \{X\}$.</li>
  <li>If $X \rightarrow \epsilon$ is a production, add $\epsilon$ to $\text{FIRST}(X)$.</li>
  <li>If $X \rightarrow Y_1 Y_2 \dots Y_k$ is a production:
    <ul>
      <li>Add all non-$\epsilon$ symbols of $\text{FIRST}(Y_1)$ to $\text{FIRST}(X)$.</li>
      <li>If $\epsilon \in \text{FIRST}(Y_1)$, add non-$\epsilon$ symbols of $\text{FIRST}(Y_2)$, continuing until some $Y_i$ does not contain $\epsilon$.</li>
      <li>If all $Y_1, \dots, Y_k$ contain $\epsilon$, add $\epsilon$ to $\text{FIRST}(X)$.</li>
    </ul>
  </li>
</ol>

<h3 class="subsection-title">Formal Rules for Computing FOLLOW:</h3>
<ol>
  <li>Place $\$$ in $\text{FOLLOW}(S)$, where $S$ is the grammar start symbol.</li>
  <li>If there is a production $A \rightarrow \alpha B \beta$, everything in $\text{FIRST}(\beta)$ except $\epsilon$ is in $\text{FOLLOW}(B)$.</li>
  <li>If there is a production $A \rightarrow \alpha B$, or $A \rightarrow \alpha B \beta$ where $\text{FIRST}(\beta)$ contains $\epsilon$, everything in $\text{FOLLOW}(A)$ is in $\text{FOLLOW}(B)$.</li>
</ol>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Arithmetic Grammar FIRST & FOLLOW</div>
  <p><strong>Transformed Arithmetic Grammar ($G$):</strong></p>
  <ul>
    <li>$E \rightarrow T E'$</li>
    <li>$E' \rightarrow + T E' \mid \epsilon$</li>
    <li>$T \rightarrow F T'$</li>
    <li>$T' \rightarrow * F T' \mid \epsilon$</li>
    <li>$F \rightarrow ( E ) \mid \mathbf{id}$</li>
  </ul>

  <table class="custom-table">
    <thead>
      <tr>
        <th style="width: 20%;">Non-Terminal</th>
        <th style="width: 35%;">$\text{FIRST}$ Set</th>
        <th>$\text{FOLLOW}$ Set</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>E</strong></td>
        <td>$\{(, \ \mathbf{id}\}$</td>
        <td>$\{), \ \$\}$</td>
      </tr>
      <tr>
        <td><strong>E'</strong></td>
        <td>$\{+, \ \epsilon\}$</td>
        <td>$\{), \ \$\}$</td>
      </tr>
      <tr>
        <td><strong>T</strong></td>
        <td>$\{(, \ \mathbf{id}\}$</td>
        <td>$\{+, \ ), \ \$\}$</td>
      </tr>
      <tr>
        <td><strong>T'</strong></td>
        <td>$\{*, \ \epsilon\}$</td>
        <td>$\{+, \ ), \ \$\}$</td>
      </tr>
      <tr>
        <td><strong>F</strong></td>
        <td>$\{(, \ \mathbf{id}\}$</td>
        <td>$\{*, \ +, \ ), \ \$\}$</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 class="section-title">Topic 6: Top-Down LL(1) Predictive Parsing</h2>

<p>
  An <strong>LL(1) Parser</strong> scans input from <strong>L</strong>eft-to-right, produces a <strong>L</strong>eftmost derivation, using <strong>1</strong> token of lookahead without backtracking.
</p>

<div class="callout callout-info">
  <div class="callout-title">Formal Condition for an LL(1) Grammar</div>
  A context-free grammar $G$ is $LL(1)$ if and only if for every pair of productions $A \rightarrow \alpha \mid \beta$:
  <ol>
    <li>$\text{FIRST}(\alpha) \cap \text{FIRST}(\beta) = \emptyset$.</li>
    <li>If $\epsilon \in \text{FIRST}(\alpha)$, then $\text{FIRST}(\beta) \cap \text{FOLLOW}(A) = \emptyset$.</li>
  </ol>
</div>

<h3 class="subsection-title">Complete LL(1) Parsing Table $M[A, a]$:</h3>
<table class="custom-table">
  <thead>
    <tr>
      <th>Non-Terminal</th>
      <th>$\mathbf{id}$</th>
      <th>$+$</th>
      <th>$*$</th>
      <th>$($</th>
      <th>$)$</th>
      <th>$\$$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>E</strong></td>
      <td>$E \rightarrow T E'$</td>
      <td></td>
      <td></td>
      <td>$E \rightarrow T E'$</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><strong>E'</strong></td>
      <td></td>
      <td>$E' \rightarrow + T E'$</td>
      <td></td>
      <td></td>
      <td>$E' \rightarrow \epsilon$</td>
      <td>$E' \rightarrow \epsilon$</td>
    </tr>
    <tr>
      <td><strong>T</strong></td>
      <td>$T \rightarrow F T'$</td>
      <td></td>
      <td></td>
      <td>$T \rightarrow F T'$</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><strong>T'</strong></td>
      <td></td>
      <td>$T' \rightarrow \epsilon$</td>
      <td>$T' \rightarrow * F T'$</td>
      <td></td>
      <td>$T' \rightarrow \epsilon$</td>
      <td>$T' \rightarrow \epsilon$</td>
    </tr>
    <tr>
      <td><strong>F</strong></td>
      <td>$F \rightarrow \mathbf{id}$</td>
      <td></td>
      <td></td>
      <td>$F \rightarrow ( E )$</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
<p><em>Since no cell contains multiple production rules, the grammar is strictly $LL(1)$.</em></p>

<h2 class="section-title">Topics 7 – 9: Bottom-Up LR Parsing Hierarchy</h2>

<p>
  <strong>LR Parsers</strong> (Left-to-right scan, Rightmost derivation in reverse) are the most general deterministic shift-reduce parsing engines.
</p>

<div class="diagram-container">
  <svg width="100%" height="75" viewBox="0 0 740 75" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="18" width="130" height="40" rx="6" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="85" y="42" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">LR(0) Parser</text>

    <text x="175" y="43" font-family="Plus Jakarta Sans" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">⊂</text>

    <rect x="200" y="18" width="130" height="40" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="265" y="42" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1d4ed8" text-anchor="middle">SLR(1) Parser</text>

    <text x="355" y="43" font-family="Plus Jakarta Sans" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">⊂</text>

    <rect x="380" y="18" width="140" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
    <text x="450" y="42" font-family="Plus Jakarta Sans" font-size="11" font-weight="800" fill="#92400e" text-anchor="middle">LALR(1) Parser</text>

    <text x="545" y="43" font-family="Plus Jakarta Sans" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">⊂</text>

    <rect x="570" y="18" width="150" height="40" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
    <text x="645" y="42" font-family="Plus Jakarta Sans" font-size="11" font-weight="800" fill="#14532d" text-anchor="middle">Canonical LR(1)</text>
  </svg>
  <div class="diagram-caption">Figure 2.1: Relative Grammatical Expressive Power of LR Parser Classes</div>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 15%;">Parser Class</th>
      <th style="width: 25%;">Item Representation</th>
      <th style="width: 35%;">Reduce Action Decision Logic</th>
      <th>State Complexity & Practical Use</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. LR(0)</strong></td>
      <td>$[A \rightarrow \alpha \cdot \beta]$</td>
      <td>Reduce $A \rightarrow \alpha$ across all columns in row unconditionally.</td>
      <td>Fewest states; very weak; fails on almost all programming grammars.</td>
    </tr>
    <tr>
      <td><strong>2. SLR(1)</strong></td>
      <td>$[A \rightarrow \alpha \cdot \beta]$</td>
      <td>Reduce $A \rightarrow \alpha$ only on input terminal $a \in \text{FOLLOW}(A)$.</td>
      <td>Same states as LR(0); resolves many simple shift/reduce conflicts.</td>
    </tr>
    <tr>
      <td><strong>3. CLR(1)</strong></td>
      <td>$[A \rightarrow \alpha \cdot \beta, \ a]$ (with explicit lookahead $a$)</td>
      <td>Reduce $A \rightarrow \alpha$ only on exact lookahead terminal $a$.</td>
      <td>Most powerful deterministic class; massive state explosion (thousands of states).</td>
    </tr>
    <tr>
      <td><strong>4. LALR(1)</strong></td>
      <td>Merged LR(1) items having identical LR(0) core items.</td>
      <td>Reduce on merged lookahead terminal sets.</td>
      <td>Same number of states as SLR(1); nearly CLR(1) parsing power; standard in Yacc/Bison.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 10 & 11: Parsing Conflicts & Error Recovery</h2>

<h3 class="subsection-title">1. Bottom-Up Parsing Conflicts:</h3>
<ul>
  <li><strong>Shift/Reduce (S/R) Conflict:</strong> The parser state cannot decide whether to shift the next input symbol onto the stack or reduce the current top-of-stack handle by a production rule.</li>
  <li><strong>Reduce/Reduce (R/R) Conflict:</strong> The parser state recognizes two or more distinct completed handles simultaneously and cannot decide which production to reduce by (indicates severe grammatical ambiguity).</li>
</ul>

<h3 class="subsection-title">2. Error Recovery Modes:</h3>
<ul>
  <li><strong>Panic-Mode Recovery:</strong> The parser discards incoming tokens until a designated synchronizing token (e.g., `;`, `}`) is encountered, then pops stack symbols until parsing can safely resume. Simple and guaranteed to avoid infinite loops.</li>
  <li><strong>Phrase-Level Recovery:</strong> Replaces an erroneous prefix with a valid correction (e.g., replacing comma with semicolon).</li>
  <li><strong>Error Productions:</strong> Language designers augment the grammar with common anticipated developer errors to emit detailed diagnostic messages.</li>
</ul>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module II)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Prove why an ambiguous grammar can never be LL(1) or LR(1). (8 Marks)</div>
  <div class="qa-a">
    <strong>Proof:</strong> An ambiguous grammar generates at least two distinct parse trees for some valid string $w$.<br>
    1. In an <strong>LL(1) parser</strong>, this ambiguity manifests as multiple production entries in the same parsing table cell $M[A, a]$, violating the single-entry requirement of deterministic LL(1) tables.<br>
    2. In an <strong>LR(1) parser</strong>, the two distinct derivations create either a <strong>Shift/Reduce conflict</strong> (where the parser cannot decide whether to shift or reduce) or a <strong>Reduce/Reduce conflict</strong> (where the parser cannot decide which of two distinct productions to reduce by). Thus, ambiguous grammars can never be parsed deterministically by LL(1) or LR(1).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain the difference between SLR(1) and LALR(1) parsers. Can merging states introduce Shift/Reduce conflicts in LALR(1)? (10 Marks)</div>
  <div class="qa-a">
    - <strong>SLR(1):</strong> Uses LR(0) items and makes reduction decisions based on the global $\text{FOLLOW}(A)$ set, which often includes symbols that cannot legally appear in that specific context.<br>
    - <strong>LALR(1):</strong> Merges CLR(1) states having identical LR(0) cores while unioning their lookahead sets. Reduction is guided by exact propagated lookaheads.<br>
    - <strong>Theorem on Conflicts:</strong> Merging LR(1) states with identical cores <strong>CANNOT introduce new Shift/Reduce conflicts</strong> (because shift decisions depend solely on the core item's symbol after the dot). However, merging <strong>CAN introduce new Reduce/Reduce conflicts</strong> if two distinct productions have overlapping lookaheads after merging.
  </div>
</div>
"""
