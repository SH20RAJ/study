# NLP Module 3 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

NLP_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Syntactic Parsing, Context-Free Grammars & Dependency Structures</div>
  <div class="toc-grid">
    <div>1. Phrase Structure Grammars & Constituency vs. Dependency Syntax Trees</div>
    <div>2. Context-Free Grammars (CFG) for Natural Language Syntax ($G = (V, T, P, S)$)</div>
    <div>3. Structural Ambiguity in Natural Language (Prepositional Phrase & Coordination)</div>
    <div>4. Chomsky Normal Form (CNF) Formal Conversion Rules ($A \rightarrow BC \mid a$)</div>
    <div>5. The CYK (Cocke-Younger-Kasami) Dynamic Programming Parsing Algorithm</div>
    <div>6. Complete Step-by-Step CYK Triangular Table Parsing Trace for "Book the flight"</div>
    <div>7. Probabilistic Context-Free Grammars (PCFG) & Maximum Likelihood Estimation</div>
    <div>8. The Probabilistic CYK (Inside-Outside) Parsing Algorithm for Disambiguation</div>
    <div>9. Dependency Grammar Foundations: Heads, Dependents & Universal Dependencies (UD)</div>
    <div>10. Transition-Based Dependency Parsing (Shift-Reduce, ARC-STANDARD & ARC-EAGER)</div>
    <div>11. Graph-Based Dependency Parsing (Chu-Liu-Edmonds Maximum Spanning Tree)</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 4 & 5: Chomsky Normal Form (CNF) & The CYK Algorithm</h2>

<p>
  A Context-Free Grammar is in <strong>Chomsky Normal Form (CNF)</strong> if every production rule has one of two forms:
</p>
$$A \rightarrow B \ C \quad \text{or} \quad A \rightarrow a$$
<p>Where $A, B, C$ are non-terminals ($B, C \neq S$) and $a$ is a single terminal symbol.</p>

<div class="formula-card">
  <strong>CYK Dynamic Programming Recurrence:</strong>
  Let table entry $P[i, j, A]$ be true if non-terminal $A$ derives substring $w_i \dots w_j$ of length $l = j - i + 1$:
  1. <strong>Base Case (Length $l = 1$):</strong>
     $$P[i, i, A] = \text{true} \quad \text{for all } A \rightarrow w_i \in P$$
  2. <strong>Inductive Step (Length $l = 2 \dots n$):</strong>
     $$P[i, j, A] = \text{true} \iff \exists k \in [i, j-1] \text{ and } A \rightarrow B \ C \in P \text{ such that } P[i, k, B] = \text{true} \land P[k+1, j, C] = \text{true}$$
  <em>Time Complexity: $O(n^3 \cdot |P|)$ where $n$ is sentence length and $|P|$ is number of CNF grammar rules.</em>
</div>

<h2 class="section-title">Topic 9 & 10: Dependency Parsing & Transition Systems</h2>

<p>
  <strong>Dependency Syntax</strong> describes grammatical structure by establishing direct binary asymmetric grammatical relations between words (Heads $\rightarrow$ Dependents), without intermediate phrase nodes:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Transition Action</th>
      <th style="width: 45%;">Stack & Buffer Manipulation</th>
      <th>Dependency Arc Created</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. SHIFT</strong></td>
      <td>Remove first word $w$ from Buffer and push onto Stack.</td>
      <td>None.</td>
    </tr>
    <tr>
      <td><strong>2. LEFT-ARC ($r$)</strong></td>
      <td>Creates dependency arc $s_1 \xleftarrow{r} s_2$ from top of stack $s_1$ to second item $s_2$. Pops $s_2$ from stack.</td>
      <td>$s_1 \rightarrow s_2$ ($s_1$ is Head).</td>
    </tr>
    <tr>
      <td><strong>3. RIGHT-ARC ($r$)</strong></td>
      <td>Creates dependency arc $s_1 \xrightarrow{r} s_2$ from second item $s_1$ to top of stack $s_2$. Pops $s_2$ from stack.</td>
      <td>$s_1 \rightarrow s_2$ ($s_1$ is Head).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module III)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. State the Chomsky Normal Form (CNF) restrictions and explain why CNF is mandatory for the CYK algorithm. (8 Marks)</div>
  <div class="qa-a">
    - <strong>CNF Restrictions:</strong> All productions must strictly be of the form $A \rightarrow BC$ (exactly 2 non-terminals) or $A \rightarrow a$ (exactly 1 terminal). No unit productions ($A \rightarrow B$) or $\epsilon$-productions ($A \rightarrow \epsilon$) are allowed.<br>
    - <strong>Why Mandatory for CYK:</strong> CYK relies on dynamic programming by splitting a substring into exactly two parts ($w[i \dots k]$ and $w[k+1 \dots j]$). Binary branching ($A \rightarrow BC$) guarantees that any subphrase is formed by joining exactly two adjacent subphrases, creating the $O(n^3)$ tabular recurrence.
  </div>
</div>
"""
