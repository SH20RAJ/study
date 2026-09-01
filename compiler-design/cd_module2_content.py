# Compiler Design Module 2 Exhaustive Content (12-14 Pages Target)

CD_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Syntax Analysis & Parsing Algorithms — Complete Syllabus Topics</div>
  <div class="toc-grid">
    <div>1. Role of the Parser & Context-Free Grammars (CFG)</div>
    <div>2. Ambiguity Elimination & Grammar Transformations</div>
    <div>3. Left Recursion Elimination (Immediate & Indirect Algorithms)</div>
    <div>4. Left Factoring Algorithm for Common Prefixes</div>
    <div>5. FIRST and FOLLOW Sets Formal Formulations & Step-by-Step Traces</div>
    <div>6. LL(1) Top-Down Predictive Parser Table & Stack Parsing Walkthrough</div>
    <div>7. Bottom-Up Shift-Reduce Parsing & Handle Pruning</div>
    <div>8. LR(0) Canonical Collection of Items & SLR(1) Parsing Tables</div>
    <div>9. Canonical LR (CLR(1)) with Lookahead & LALR(1) State Merging</div>
    <div>10. Parsing Conflicts (Shift/Reduce, Reduce/Reduce) & Error Recovery</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Context-Free Grammars & Ambiguity</h2>
<p>
  A <strong>Context-Free Grammar (CFG)</strong> is formally defined as a 4-tuple $G = (V, T, P, S)$:
</p>
<ul>
  <li>$V$: Finite set of Non-Terminal characters (variables representing syntactic categories).</li>
  <li>$T$: Finite set of Terminal characters (tokens returned by lexical analyzer).</li>
  <li>$P$: Finite set of Production rules of the form $A \rightarrow \alpha$, where $A \in V$ and $\alpha \in (V \cup T)^*$.</li>
  <li>$S \in V$: The designated Start Symbol.</li>
</ul>

<h3 class="subsection-title">Grammar Ambiguity:</h3>
<p>
  A grammar $G$ is <strong>ambiguous</strong> if there exists at least one string $w \in L(G)$ that has two or more distinct parse trees (or equivalently, two distinct leftmost derivations).
</p>
<p>
  Classic example: The Dangling-Else Grammar:
</p>
$$\text{stmt} \rightarrow \mathbf{if} \ \text{expr} \ \mathbf{then} \ \text{stmt} \mid \mathbf{if} \ \text{expr} \ \mathbf{then} \ \text{stmt} \ \mathbf{else} \ \text{stmt} \mid \mathbf{other}$$
<p>
  Resolved by disambiguating the grammar into `matched_stmt` and `unmatched_stmt`, matching each `else` with the closest unmatched `then`.
</p>



<h2 class="section-title">Topic 3 & 4: Grammar Transformations (Left Recursion & Left Factoring)</h2>

<h3 class="subsection-title">1. Immediate Left Recursion Elimination:</h3>
<p>
  A production $A \rightarrow A\alpha \mid \beta$ (where $\beta$ does not start with $A$) causes top-down parsers to loop infinitely. It is eliminated by introducing a new non-terminal $A'$:
</p>
$$A \rightarrow \beta A', \qquad A' \rightarrow \alpha A' \mid \epsilon$$

<h3 class="subsection-title">2. General Left Recursion Elimination Algorithm:</h3>
<ol>
  <li>Arrange non-terminals in some arbitrary ordering: $A_1, A_2, \dots, A_n$.</li>
  <li>For $i = 1$ to $n$:
    <ul>
      <li>For $j = 1$ to $i-1$: Replace each production $A_i \rightarrow A_j \gamma$ with $A_i \rightarrow \delta_1 \gamma \mid \delta_2 \gamma \mid \dots \mid \delta_k \gamma$, where $A_j \rightarrow \delta_1 \mid \delta_2 \mid \dots \mid \delta_k$ are the current $A_j$ productions.</li>
      <li>Eliminate immediate left recursion among the $A_i$ productions.</li>
    </ul>
  </li>
</ol>

<h3 class="subsection-title">3. Left Factoring Algorithm (Removing Common Prefixes):</h3>
<p>
  When two productions for $A$ share a common prefix ($A \rightarrow \alpha\beta_1 \mid \alpha\beta_2$), the parser cannot determine which branch to choose based on one lookahead token. Left factoring extracts the common prefix:
</p>
$$A \rightarrow \alpha A', \qquad A' \rightarrow \beta_1 \mid \beta_2$$



<h2 class="section-title">Topic 5: Formal Formulations of FIRST and FOLLOW</h2>

<div class="callout callout-info">
  <div class="callout-title">Formal Mathematical Definitions</div>
  <strong>$\text{FIRST}(\alpha)$:</strong> Set of all terminals that begin strings derived from $\alpha$. If $\alpha \xrightarrow{*} \epsilon$, then $\epsilon \in \text{FIRST}(\alpha)$.<br>
  <strong>$\text{FOLLOW}(A)$:</strong> Set of all terminals $a$ that can appear immediately to the right of non-terminal $A$ in some sentential form ($S \xrightarrow{*} \alpha A a \beta$). If $A$ is the rightmost symbol in a derivation, the input end-marker $\$$ is in $\text{FOLLOW}(A)$.
</div>

<h3 class="subsection-title">Rules for Computing FIRST:</h3>
<ol>
  <li>If $X$ is a terminal, $\text{FIRST}(X) = \{X\}$.</li>
  <li>If $X \rightarrow \epsilon$ is a production, add $\epsilon$ to $\text{FIRST}(X)$.</li>
  <li>If $X \rightarrow Y_1 Y_2 \dots Y_k$ is a production:
    <ul>
      <li>Add all non-$\epsilon$ symbols from $\text{FIRST}(Y_1)$ to $\text{FIRST}(X)$.</li>
      <li>If $\epsilon \in \text{FIRST}(Y_1)$, add all non-$\epsilon$ symbols from $\text{FIRST}(Y_2)$ to $\text{FIRST}(X)$, and so forth, until some $Y_i$ does not contain $\epsilon$.</li>
      <li>If all $Y_1, \dots, Y_k$ contain $\epsilon$, add $\epsilon$ to $\text{FIRST}(X)$.</li>
    </ul>
  </li>
</ol>

<h3 class="subsection-title">Rules for Computing FOLLOW:</h3>
<ol>
  <li>Place $\$$ in $\text{FOLLOW}(S)$, where $S$ is the start symbol.</li>
  <li>If there is a production $A \rightarrow \alpha B \beta$, everything in $\text{FIRST}(\beta)$ except $\epsilon$ is in $\text{FOLLOW}(B)$.</li>
  <li>If there is a production $A \rightarrow \alpha B$, or $A \rightarrow \alpha B \beta$ where $\text{FIRST}(\beta)$ contains $\epsilon$, everything in $\text{FOLLOW}(A)$ is in $\text{FOLLOW}(B)$.</li>
</ol>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Arithmetic Grammar FIRST & FOLLOW</div>
  <p><strong>Grammar ($G$):</strong></p>
  <ul>
    <li>$E \rightarrow T E'$</li>
    <li>$E' \rightarrow + T E' \mid \epsilon$</li>
    <li>$T \rightarrow F T'$</li>
    <li>$T' \rightarrow * F T' \mid \epsilon$</li>
    <li>$F \rightarrow ( E ) \mid \mathbf{id}$</li>
  </ul>
  <p><strong>Computed Sets:</strong></p>
  <table class="custom-table">
    <thead>
      <tr><th>Non-Terminal</th><th>$\text{FIRST}$ Set</th><th>$\text{FOLLOW}$ Set</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>E</strong></td><td>$\{(, \mathbf{id}\}$</td><td>$\{), \$\}$</td></tr>
      <tr><td><strong>E'</strong></td><td>$\{+, \epsilon\}$</td><td>$\{), \$\}$</td></tr>
      <tr><td><strong>T</strong></td><td>$\{(, \mathbf{id}\}$</td><td>$\{+, ), \$\}$</td></tr>
      <tr><td><strong>T'</strong></td><td>$\{*, \epsilon\}$</td><td>$\{+, ), \$\}$</td></tr>
      <tr><td><strong>F</strong></td><td>$\{(, \mathbf{id}\}$</td><td>$\{*, +, ), \$\}$</td></tr>
    </tbody>
  </table>
</div>



<h2 class="section-title">Topic 6: Top-Down LL(1) Predictive Parsing</h2>

<p>
  An <strong>LL(1) Parser</strong> scans input from Left-to-right, produces a Leftmost derivation, using 1 lookahead token.
</p>
<div class="callout callout-info">
  <div class="callout-title">LL(1) Grammatical Condition</div>
  A grammar $G$ is $LL(1)$ if and only if for every pair of productions $A \rightarrow \alpha \mid \beta$:
  <ol>
    <li>$\text{FIRST}(\alpha) \cap \text{FIRST}(\beta) = \emptyset$.</li>
    <li>If $\epsilon \in \text{FIRST}(\alpha)$, then $\text{FIRST}(\beta) \cap \text{FOLLOW}(A) = \emptyset$.</li>
  </ol>
</div>

<h3 class="subsection-title">Complete LL(1) Parsing Table:</h3>
<table class="custom-table">
  <thead>
    <tr><th>Non-Terminal</th><th>$\mathbf{id}$</th><th>$+$</th><th>$*$</th><th>$($</th><th>$)$</th><th>$\$$</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>E</strong></td><td>$E \rightarrow T E'$</td><td></td><td></td><td>$E \rightarrow T E'$</td><td></td><td></td></tr>
    <tr><td><strong>E'</strong></td><td></td><td>$E' \rightarrow + T E'$</td><td></td><td></td><td>$E' \rightarrow \epsilon$</td><td>$E' \rightarrow \epsilon$</td></tr>
    <tr><td><strong>T</strong></td><td>$T \rightarrow F T'$</td><td></td><td></td><td>$T \rightarrow F T'$</td><td></td><td></td></tr>
    <tr><td><strong>T'</strong></td><td></td><td>$T' \rightarrow \epsilon$</td><td>$T' \rightarrow * F T'$</td><td></td><td>$T' \rightarrow \epsilon$</td><td>$T' \rightarrow \epsilon$</td></tr>
    <tr><td><strong>F</strong></td><td>$F \rightarrow \mathbf{id}$</td><td></td><td></td><td>$F \rightarrow ( E )$</td><td></td><td></td></tr>
  </tbody>
</table>



<h2 class="section-title">Topics 7 – 9: Bottom-Up LR Parsing Landscape</h2>

<p>
  <strong>LR Parsers</strong> (Left-to-right scan, Rightmost derivation in reverse) are the most powerful deterministic shift-reduce parsing engines.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Parser Class</th>
      <th style="width: 25%;">Item Structure</th>
      <th style="width: 25%;">Reduce Action Decision</th>
      <th>State Complexity & Power</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. LR(0)</strong></td>
      <td>$[A \rightarrow \alpha \cdot \beta]$</td>
      <td>Reduce across all columns unconditionally.</td>
      <td>Fewest states; weak; fails on almost all programming grammars.</td>
    </tr>
    <tr>
      <td><strong>2. SLR(1)</strong></td>
      <td>$[A \rightarrow \alpha \cdot \beta]$</td>
      <td>Reduce $A \rightarrow \alpha$ only on input symbols $a \in \text{FOLLOW}(A)$.</td>
      <td>Same number of states as LR(0); resolves many Shift/Reduce conflicts.</td>
    </tr>
    <tr>
      <td><strong>3. CLR(1)</strong></td>
      <td>$[A \rightarrow \alpha \cdot \beta, \ a]$ (with Lookahead $a$)</td>
      <td>Reduce $A \rightarrow \alpha$ only on exact lookahead symbol $a$.</td>
      <td>Most powerful deterministic class; massive number of states (thousands).</td>
    </tr>
    <tr>
      <td><strong>4. LALR(1)</strong></td>
      <td>Merged LR(1) items with identical core $LR(0)$ components.</td>
      <td>Reduce on merged lookahead sets.</td>
      <td>Same number of states as SLR(1); nearly the parsing power of CLR(1); used in Yacc/Bison.</td>
    </tr>
  </tbody>
</table>



<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module II)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Prove why an ambiguous grammar can never be LL(1) or LR(1). (8 Marks)</div>
  <div class="qa-a">
    <strong>Proof:</strong> An ambiguous grammar generates at least two distinct parse trees for some string $w$.<br>
    1. In an <strong>LL(1) parser</strong>, this ambiguity manifests as multiple production entries in the same parsing table cell $M[A, a]$, violating the single-entry requirement of deterministic LL(1) tables.<br>
    2. In an <strong>LR(1) parser</strong>, the two distinct derivations create either a <strong>Shift/Reduce conflict</strong> (where the parser cannot decide whether to shift or reduce) or a <strong>Reduce/Reduce conflict</strong> (where the parser cannot decide which of two distinct productions to reduce by). Thus, ambiguous grammars can never be parsed deterministically by LL(1) or LR(1).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain the difference between SLR(1) and LALR(1) parsers. (6 Marks)</div>
  <div class="qa-a">
    Both SLR(1) and LALR(1) parsers have the exact same number of states (identical to the LR(0) state machine). However, they differ in how they decide reduction actions:<br>
    - <strong>SLR(1):</strong> Places reduce actions for $A \rightarrow \alpha$ in all columns corresponding to $\text{FOLLOW}(A)$. $\text{FOLLOW}(A)$ is a global set that includes symbols that may never legally follow $A$ in that specific context.<br>
    - <strong>LALR(1):</strong> Computes specific context-sensitive lookahead sets during item propagation, placing reduce actions only on valid lookaheads. As a result, LALR(1) eliminates many false Shift/Reduce and Reduce/Reduce conflicts present in SLR(1).
  </div>
</div>
"""
