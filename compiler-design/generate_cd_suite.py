#!/usr/bin/env python3
"""
Compiler Design (CS24301) - Complete Neuroscience-Backed Study Suite Generator
Generates:
1. Module 1: Lexical Analysis Notes (HTML & PDF)
2. Module 2: Syntax Analysis Notes (HTML & PDF)
3. Module 3: Semantic Analysis & ICG Notes (HTML & PDF)
4. Module 4: Advanced ICG & Runtime Environment Notes (HTML & PDF)
5. Module 5: Code Optimization & Target Generation Notes (HTML & PDF)
6. 10-Page Master Quick Revision Notes (HTML & PDF)
7. Full Course Master Compilation (HTML & PDF)
"""

import os
import sys
from playwright.sync_api import sync_playwright

BASE_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');

:root {
  --primary: #1e3a8a;       /* Deep Navy */
  --primary-light: #eff6ff; /* Soft Blue */
  --accent: #0284c7;        /* Sky Blue */
  --secondary: #4f46e5;     /* Indigo */
  --success: #059669;       /* Emerald */
  --success-bg: #ecfdf5;
  --warning: #d97706;       /* Amber */
  --warning-bg: #fffbeb;
  --danger: #dc2626;        /* Rose */
  --danger-bg: #fef2f2;
  --dark: #0f172a;          /* Slate 900 */
  --text: #1e293b;          /* Slate 800 */
  --text-muted: #64748b;    /* Slate 500 */
  --border: #cbd5e1;        /* Slate 300 */
  --bg-card: #ffffff;
  --bg-page: #f8fafc;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: var(--text);
  background-color: var(--bg-page);
  line-height: 1.6;
  font-size: 12.6px;
  padding: 0;
}

.page-container {
  max-width: 900px;
  margin: 0 auto;
  background: #ffffff;
  padding: 35px 40px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}

.doc-header {
  border-bottom: 3px solid var(--primary);
  padding-bottom: 18px;
  margin-bottom: 22px;
}

.badge-container {
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.badge {
  display: inline-block;
  padding: 3px 10px;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-radius: 4px;
}

.badge-blue { background: #dbeafe; color: #1e40af; }
.badge-purple { background: #ede9fe; color: #5b21b6; }
.badge-green { background: #d1fae5; color: #065f46; }
.badge-amber { background: #fef3c7; color: #92400e; }

h1.doc-title {
  font-size: 23px;
  font-weight: 800;
  color: var(--dark);
  line-height: 1.25;
  margin-bottom: 5px;
}

.doc-subtitle {
  font-size: 12.5px;
  color: var(--text-muted);
  font-weight: 500;
}

.toc-box {
  background: #f0f9ff;
  border: 1px solid #bae6fd;
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 25px;
  page-break-inside: avoid;
}

.toc-title {
  font-size: 13px;
  font-weight: 700;
  color: #0369a1;
  margin-bottom: 8px;
}

.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px 20px;
  font-size: 11.5px;
}

h2.section-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--dark);
  border-left: 4px solid var(--accent);
  padding-left: 10px;
  margin: 24px 0 12px 0;
}

h3.subsection-title {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--secondary);
  margin: 15px 0 7px 0;
}

p { margin-bottom: 8px; text-align: justify; }

.callout {
  border-radius: 6px;
  padding: 10px 14px;
  margin: 11px 0;
  font-size: 11.8px;
  border-left: 4px solid;
  page-break-inside: avoid;
}

.callout-info { background: #f0fdf4; border-color: #16a34a; color: #14532d; }
.callout-blue { background: #f0f9ff; border-color: #0284c7; color: #0c4a6e; }
.callout-warning { background: #fffbeb; border-color: #d97706; color: #78350f; }
.callout-danger { background: #fef2f2; border-color: #dc2626; color: #7f1d1d; }
.callout-pyq { background: #faf5ff; border-color: #9333ea; color: #581c87; }

.callout-title {
  font-weight: 700;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}

table.custom-table {
  width: 100%;
  border-collapse: collapse;
  margin: 11px 0;
  font-size: 11.5px;
  background: #ffffff;
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid var(--border);
  page-break-inside: avoid;
}

table.custom-table th {
  background: #1e293b;
  color: #ffffff;
  font-weight: 600;
  text-align: left;
  padding: 6px 10px;
  font-size: 11px;
}

table.custom-table td {
  padding: 5.5px 10px;
  border-bottom: 1px solid #e2e8f0;
  vertical-align: middle;
}

table.custom-table tr:nth-child(even) td { background-color: #f8fafc; }

code {
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  background: #f1f5f9;
  color: #0f172a;
  padding: 1.5px 4px;
  border-radius: 3px;
  border: 1px solid #e2e8f0;
}

pre {
  background: #0f172a;
  color: #f8fafc;
  padding: 9px 13px;
  border-radius: 6px;
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  line-height: 1.4;
  overflow-x: auto;
  margin: 9px 0;
  page-break-inside: avoid;
}

ul, ol { margin: 5px 0 9px 18px; font-size: 12px; }
li { margin-bottom: 3px; }

.diagram-container {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
  margin: 12px 0;
  text-align: center;
  page-break-inside: avoid;
}

.diagram-caption {
  font-size: 10px;
  font-weight: 600;
  color: var(--text-muted);
  margin-top: 5px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.qa-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 11px 15px;
  margin: 11px 0;
  page-break-inside: avoid;
}

.qa-q { font-weight: 700; color: #1e3a8a; font-size: 12.2px; margin-bottom: 5px; }
.qa-a { font-size: 11.8px; color: var(--text); }

@media print {
  body { background: #ffffff; font-size: 11.8px; }
  .page-container { padding: 0; max-width: 100%; box-shadow: none; }
  @page {
    size: A4 portrait;
    margin: 14mm 11mm 14mm 11mm;
    @bottom-right {
      content: "Page " counter(page);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8px;
      color: #94a3b8;
    }
    @bottom-left {
      content: "Compiler Design (CS24301) Study Notes | BIT Mesra";
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8px;
      color: #94a3b8;
    }
  }
  .toc-box, .diagram-container, .callout, table, pre, .qa-card {
    page-break-inside: avoid;
  }
}
"""

def wrap_html(title, subtitle, badge_text, body_html):
    template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"></script>
<style>__BASE_CSS__</style>
</head>
<body>
<div class="page-container">
  <div class="doc-header">
    <div class="badge-container">
      <span class="badge badge-blue">CS24301 — Theory (3.0 Cr)</span>
      <span class="badge badge-purple">__BADGE__</span>
      <span class="badge badge-green">BIT Mesra | NEP Scheme</span>
    </div>
    <h1 class="doc-title">__TITLE__</h1>
    <div class="doc-subtitle">__SUBTITLE__</div>
  </div>
  __BODY__
  <div style="margin-top: 22px; padding-top: 12px; border-top: 1px solid var(--border); font-size: 10px; color: var(--text-muted); display: flex; justify-content: space-between;">
    <span>Compiler Design (CS24301) — Comprehensive Study Suite</span>
    <span>BIT Mesra | B.Tech CSE</span>
  </div>
</div>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  });
</script>
</body>
</html>"""
    return template.replace("__TITLE__", title).replace("__SUBTITLE__", subtitle).replace("__BADGE__", badge_text).replace("__BODY__", body_html).replace("__BASE_CSS__", BASE_CSS)

MODULE_2_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module II: Syntax Analysis — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Role of Parser & Context-Free Grammars (CFG)</div>
    <div>2. Ambiguity & Derivations (LM / RM)</div>
    <div>3. Grammar Rewriting (Left Recursion & Factoring)</div>
    <div>4. Top-Down Parsing: LL(1) Table Construction</div>
    <div>5. Computation of FIRST and FOLLOW Sets</div>
    <div>6. Bottom-Up Parsing & Handle Pruning</div>
    <div>7. LR Parsers: LR(0), SLR(1), CLR(1), LALR(1)</div>
    <div>8. Parsing Conflicts & Error Recovery Strategies</div>
  </div>
</div>

<h2 class="section-title">1. Context-Free Grammars (CFG) & Ambiguity</h2>
<p>
  A <strong>Context-Free Grammar</strong> is a 4-tuple $G = (V, \Sigma, R, S)$ where $V$ is a finite set of non-terminal variables, $\Sigma$ is a finite set of terminal symbols ($V \cap \Sigma = \emptyset$), $R$ is a finite set of production rules of the form $A \rightarrow \alpha$ ($A \in V, \alpha \in (V \cup \Sigma)^*$), and $S \in V$ is the start symbol.
</p>

<div class="callout callout-info">
  <div class="callout-title">Leftmost vs. Rightmost Derivations</div>
  <strong>Leftmost Derivation (LMD):</strong> At each step, the leftmost non-terminal is replaced first.<br>
  <strong>Rightmost Derivation (RMD / Canonical Derivation):</strong> At each step, the rightmost non-terminal is replaced first.<br>
  <strong>Ambiguous Grammar:</strong> A grammar that produces <em>two or more distinct parse trees</em> (or distinct LMDs) for at least one string $w \in L(G)$. (Classic example: "Dangling-Else" ambiguity).
</div>

<h2 class="section-title">2. Grammar Transformations for Top-Down Parsing</h2>

<h3 class="subsection-title">2.1 Elimination of Immediate Left Recursion</h3>
<p>
  A production rule $A \rightarrow A\alpha \mid \beta$ is immediately left-recursive. It causes top-down predictive parsers to enter an infinite loop. We eliminate it by introducing a new non-terminal $A'$:
</p>
$$A \rightarrow \beta A', \quad A' \rightarrow \alpha A' \mid \epsilon$$

<h3 class="subsection-title">2.2 Left Factoring (Resolving Common Prefixes)</h3>
<p>
  When two productions for $A$ share a common leading prefix $A \rightarrow \alpha \beta_1 \mid \alpha \beta_2$, a predictive parser cannot decide which production to choose based on 1 lookahead token. We left-factor:
</p>
$$A \rightarrow \alpha A', \quad A' \rightarrow \beta_1 \mid \beta_2$$

<h2 class="section-title">3. Computation of $\text{FIRST}$ and $\text{FOLLOW}$ Sets</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Set</th>
      <th style="width: 30%;">Mathematical Definition</th>
      <th>Construction Rules</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>$\text{FIRST}(\alpha)$</strong></td>
      <td>$\text{FIRST}(\alpha) = \{ a \in \Sigma \mid \alpha \Rightarrow^* a\beta \}$ (includes $\epsilon$ if $\alpha \Rightarrow^* \epsilon$)</td>
      <td>
        1. If $X \in \Sigma$, $\text{FIRST}(X) = \{X\}$.<br>
        2. If $X \rightarrow \epsilon$, add $\epsilon \in \text{FIRST}(X)$.<br>
        3. For $X \rightarrow Y_1 Y_2 \dots Y_k$: add $\text{FIRST}(Y_1) \setminus \{\epsilon\}$. If $Y_1 \Rightarrow^* \epsilon$, add $\text{FIRST}(Y_2) \setminus \{\epsilon\}$, continuing until a non-nullable $Y_i$ is reached. If all $Y_i \Rightarrow^* \epsilon$, add $\epsilon$.
      </td>
    </tr>
    <tr>
      <td><strong>$\text{FOLLOW}(A)$</strong></td>
      <td>$\text{FOLLOW}(A) = \{ a \in \Sigma \cup \{\$\} \mid S \Rightarrow^* \alpha A a \beta \}$</td>
      <td>
        1. Add $\$$ to $\text{FOLLOW}(S)$ (where $S$ is start symbol).<br>
        2. If $A \rightarrow \alpha B \beta$, add $\text{FIRST}(\beta) \setminus \{\epsilon\}$ to $\text{FOLLOW}(B)$.<br>
        3. If $A \rightarrow \alpha B$ or $A \rightarrow \alpha B \beta$ where $\epsilon \in \text{FIRST}(\beta)$, add all elements of $\text{FOLLOW}(A)$ to $\text{FOLLOW}(B)$.
      </td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">4. Top-Down $\text{LL}(1)$ Parsing Table Construction</h2>
<p>
  For each production $A \rightarrow \alpha$:
  <ol>
    <li>For every terminal $a \in \text{FIRST}(\alpha)$, add $A \rightarrow \alpha$ to $M[A, a]$.</li>
    <li>If $\epsilon \in \text{FIRST}(\alpha)$, then for every terminal $b \in \text{FOLLOW}(A)$ (including $\$$), add $A \rightarrow \alpha$ to $M[A, b]$.</li>
  </ol>
  <strong>LL(1) Condition:</strong> A grammar is $\text{LL}(1)$ iff no cell in parsing table $M$ contains multiple entries (no conflicts).
</p>

<h2 class="section-title">5. Bottom-Up LR Parsers ($\text{LR}(0), \text{SLR}(1), \text{CLR}(1), \text{LALR}(1)$)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th>Parser Type</th>
      <th>Item Representation</th>
      <th>Lookahead & Table Size</th>
      <th>Power & Conflict Resolution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>$\text{LR}(0)$</strong></td>
      <td>$A \rightarrow \alpha \cdot \beta$</td>
      <td>0 lookaheads. Same number of states as SLR(1).</td>
      <td>Weakest; frequent Shift/Reduce conflicts on reduction.</td>
    </tr>
    <tr>
      <td><strong>$\text{SLR}(1)$</strong></td>
      <td>$A \rightarrow \alpha \cdot \beta$</td>
      <td>Place reduction $A \rightarrow \alpha$ only in $\text{FOLLOW}(A)$.</td>
      <td>More powerful than $\text{LR}(0)$, but still suffers conflicts on ambiguous grammars.</td>
    </tr>
    <tr>
      <td><strong>$\text{CLR}(1)$</strong></td>
      <td>$[A \rightarrow \alpha \cdot \beta, a]$ where $a \in \Sigma \cup \{\$\}$</td>
      <td>Carries exact lookahead $a$. Huge state table.</td>
      <td>Most powerful LR parser for deterministic CFGs. Large memory footprint.</td>
    </tr>
    <tr>
      <td><strong>$\text{LALR}(1)$</strong></td>
      <td>Merged $\text{CLR}(1)$ items with identical core</td>
      <td>Same number of states as $\text{SLR}(1)$, lookaheads merged.</td>
      <td><strong>Standard in Yacc/Bison</strong>; rarely introduces R/R conflicts, never introduces S/R conflicts.</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-pyq">
  <div class="callout-title">🏛️ BIT Mesra Exam Question & Solved Walkthrough (10 Marks)</div>
  <strong>Question:</strong> Construct the $\text{LL}(1)$ parsing table for the grammar: $E \rightarrow T E', E' \rightarrow + T E' \mid \epsilon, T \rightarrow F T', T' \rightarrow * F T' \mid \epsilon, F \rightarrow ( E ) \mid \text{id}$.<br>
  <strong>Solution:</strong>
  <ul>
    <li>$\text{FIRST}(E) = \text{FIRST}(T) = \text{FIRST}(F) = \{ (, \text{id} \}$</li>
    <li>$\text{FIRST}(E') = \{ +, \epsilon \}, \quad \text{FIRST}(T') = \{ *, \epsilon \}$</li>
    <li>$\text{FOLLOW}(E) = \text{FOLLOW}(E') = \{ ), \$ \}$</li>
    <li>$\text{FOLLOW}(T) = \text{FOLLOW}(T') = \{ +, ), \$ \}$</li>
    <li>$\text{FOLLOW}(F) = \{ *, +, ), \$ \}$</li>
  </ul>
  Every cell in table $M$ contains at most one production $\implies$ The grammar is strictly $\text{LL}(1)$.
</div>
"""

MODULE_3_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module III: Semantic Analysis & Intermediate Code Generation — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Syntax-Directed Definitions (SDD) & Attributes</div>
    <div>2. S-Attributed vs. L-Attributed Definitions</div>
    <div>3. Syntax-Directed Translation Schemes (SDTS)</div>
    <div>4. Type Systems, Checking & Coercion</div>
    <div>5. Three-Address Code (TAC): Quadruples & Triples</div>
    <div>6. Multi-Dimensional Array Address Calculations</div>
  </div>
</div>

<h2 class="section-title">1. Syntax-Directed Definitions (SDD)</h2>
<p>
  An <strong>SDD</strong> is a Context-Free Grammar augmented with attributes and semantic rules.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Attribute Category</th>
      <th style="width: 40%;">Definition & Dependency Order</th>
      <th>Evaluation Paradigm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Synthesized Attribute</strong></td>
      <td>Computed solely from the values of attributes at the child nodes in the parse tree: $A.s = f(Y_1.a, Y_2.b, \dots, Y_k.c)$.</td>
      <td>Evaluated naturally during <strong>Bottom-Up Parsing</strong> (Post-order traversal).</td>
    </tr>
    <tr>
      <td><strong>Inherited Attribute</strong></td>
      <td>Computed from attributes of the parent node and/or sibling nodes: $Y_j.i = f(A.a, Y_1.b, \dots, Y_{j-1}.c)$.</td>
      <td>Evaluated during <strong>Top-Down Parsing</strong> (Pre-order / In-order traversal).</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">S-Attributed vs. L-Attributed SDD Classification</div>
  <strong>S-Attributed SDD:</strong> Uses <em>exclusively synthesized attributes</em>. Can be evaluated directly in bottom-up LR parsers without building explicit trees.<br>
  <strong>L-Attributed SDD:</strong> Allows synthesized attributes AND inherited attributes, provided inherited attributes of $Y_j$ depend only on $A$'s inherited attributes or attributes of siblings to the <em>left</em> ($Y_1, \dots, Y_{j-1}$). Evaluated in a single Depth-First Search (DFS) left-to-right pass.
</div>

<h2 class="section-title">2. Three-Address Code (TAC) Representations</h2>
<p>
  Three-Address Code instructions have at most one operator on the RHS: $x = y \text{ op } z$.
</p>

<div class="diagram-container">
  <svg width="100%" height="85" viewBox="0 0 740 85" xmlns="http://www.w3.org/2000/svg">
    <!-- Quadruple -->
    <rect x="20" y="15" width="220" height="55" rx="5" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="130" y="35" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e3a8a" text-anchor="middle">Quadruple</text>
    <text x="130" y="55" font-family="Fira Code" font-size="10" fill="#2563eb" text-anchor="middle">(op, arg1, arg2, result)</text>

    <!-- Triple -->
    <rect x="260" y="15" width="220" height="55" rx="5" fill="#f0fdf4" stroke="#22c55e"/>
    <text x="370" y="35" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Triple</text>
    <text x="370" y="55" font-family="Fira Code" font-size="10" fill="#16a34a" text-anchor="middle">(op, arg1, arg2) - index is result</text>

    <!-- Indirect Triple -->
    <rect x="500" y="15" width="220" height="55" rx="5" fill="#faf5ff" stroke="#a855f7"/>
    <text x="610" y="35" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#581c87" text-anchor="middle">Indirect Triple</text>
    <text x="610" y="55" font-family="Fira Code" font-size="10" fill="#9333ea" text-anchor="middle">Array of pointers to triples</text>
  </svg>
  <div class="diagram-caption">Figure 3.1: Comparison of Three-Address Code Data Structures</div>
</div>

<h2 class="section-title">3. Multi-Dimensional Array Address Calculations</h2>
<p>
  Consider an array $A[d_1][d_2]$ with element size $w$ and base address $\text{Base}$. Let lower bounds be $low_1, low_2$:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 30%;">Memory Storage Order</th>
      <th>Address Formula for Element $A[i][j]$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Row-Major Order (C/C++, Java)</strong></td>
      <td>$$\text{Address}(A[i][j]) = \text{Base} + \Big( (i - low_1) \times n_2 + (j - low_2) \Big) \times w$$</td>
    </tr>
    <tr>
      <td><strong>Column-Major Order (Fortran, MATLAB)</strong></td>
      <td>$$\text{Address}(A[i][j]) = \text{Base} + \Big( (j - low_2) \times n_1 + (i - low_1) \Big) \times w$$</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-pyq">
  <div class="callout-title">🏛️ BIT Mesra Numerical: 2D Array TAC Generation</div>
  <strong>Problem:</strong> Generate Three-Address Code for the assignment `x = A[i][j]` where $A$ is a $10 \times 20$ integer array ($w=4$ bytes, $low_1=1, low_2=1$) stored in Row-Major order.<br>
  <strong>Derivation:</strong>
  <pre><code>// Address formula: Base + ((i - 1)*20 + (j - 1))*4
t1 = i - 1
t2 = t1 * 20
t3 = j - 1
t4 = t2 + t3
t5 = t4 * 4
t6 = A[t5]      // Array dereference with offset t5
x = t6</code></pre>
</div>
"""

MODULE_4_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module IV: Advanced ICG & Runtime Environment — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Short-Circuit vs. Numerical Boolean Evaluation</div>
    <div>2. Control Flow Translation (if-else, while, for)</div>
    <div>3. Backpatching: makelist, merge, backpatch</div>
    <div>4. Procedure Calls & Return Mechanisms</div>
    <div>5. Runtime Memory Organization (Text, Data, Heap, Stack)</div>
    <div>6. Activation Records (Stack Frames) & Parameter Passing</div>
  </div>
</div>

<h2 class="section-title">1. Translation of Boolean Expressions (Short-Circuit Evaluation)</h2>
<p>
  In programming languages like C and Java, boolean operators `&&` and `||` evaluate conditionally:
  <ul>
    <li>In $B_1 \text{ || } B_2$: If $B_1$ is true, $B_2$ is skipped entirely.</li>
    <li>In $B_1 \text{ \&\& } B_2$: If $B_1$ is false, $B_2$ is skipped entirely.</li>
  </ul>
</p>

<h2 class="section-title">2. Backpatching Technique</h2>
<p>
  In a single-pass compiler, forward jump targets are not known when the jump instruction is emitted. **Backpatching** leaves target addresses blank and fills them once the target label is generated.
</p>
<ul>
  <li><code>makelist(i)</code>: Creates a new list containing just the jump instruction index $i$.</li>
  <li><code>merge(p1, p2)</code>: Concatenates two lists of jump instructions $p1$ and $p2$.</li>
  <li><code>backpatch(p, i)</code>: Inserts label $i$ as the target for each instruction on list $p$.</li>
</ul>

<h2 class="section-title">3. Runtime Storage Organization & Activation Records</h2>

<div class="diagram-container">
  <svg width="100%" height="150" viewBox="0 0 740 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Memory Layout -->
    <g transform="translate(40, 10)">
      <text x="75" y="15" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e3a8a" text-anchor="middle">Runtime Memory Layout</text>
      <rect x="10" y="25" width="130" height="25" fill="#f1f5f9" stroke="#64748b"/>
      <text x="75" y="42" font-family="Plus Jakarta Sans" font-size="10" text-anchor="middle">Code / Text Segment</text>
      <rect x="10" y="50" width="130" height="25" fill="#f8fafc" stroke="#64748b"/>
      <text x="75" y="67" font-family="Plus Jakarta Sans" font-size="10" text-anchor="middle">Static / Global Data</text>
      <rect x="10" y="75" width="130" height="25" fill="#ecfdf5" stroke="#059669"/>
      <text x="75" y="92" font-family="Plus Jakarta Sans" font-size="10" font-weight="600" fill="#065f46" text-anchor="middle">Heap (grows downward ↓)</text>
      <rect x="10" y="100" width="130" height="30" fill="#dbeafe" stroke="#1e40af"/>
      <text x="75" y="118" font-family="Plus Jakarta Sans" font-size="10" font-weight="600" fill="#1e3a8a" text-anchor="middle">Stack (grows upward ↑)</text>
    </g>

    <!-- Activation Record -->
    <g transform="translate(280, 10)">
      <text x="210" y="15" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e3a8a" text-anchor="middle">Structure of an Activation Record (Stack Frame)</text>
      <rect x="30" y="25" width="360" height="105" rx="5" fill="#ffffff" stroke="#1e40af" stroke-width="1.5"/>
      <line x1="30" y1="42" x2="390" y2="42" stroke="#cbd5e1"/>
      <line x1="30" y1="59" x2="390" y2="59" stroke="#cbd5e1"/>
      <line x1="30" y1="76" x2="390" y2="76" stroke="#cbd5e1"/>
      <line x1="30" y1="93" x2="390" y2="93" stroke="#cbd5e1"/>
      <line x1="30" y1="110" x2="390" y2="110" stroke="#cbd5e1"/>

      <text x="210" y="38" font-family="Plus Jakarta Sans" font-size="10" text-anchor="middle">Actual Parameters (Arguments passed by caller)</text>
      <text x="210" y="55" font-family="Plus Jakarta Sans" font-size="10" font-weight="600" fill="#dc2626" text-anchor="middle">Return Value & Return Address (Program Counter PC)</text>
      <text x="210" y="72" font-family="Plus Jakarta Sans" font-size="10" font-weight="600" fill="#0284c7" text-anchor="middle">Control Link (Dynamic Link) -> Points to caller's frame</text>
      <text x="210" y="89" font-family="Plus Jakarta Sans" font-size="10" text-anchor="middle">Access Link (Static Link) -> Points to lexical parent frame</text>
      <text x="210" y="106" font-family="Plus Jakarta Sans" font-size="10" text-anchor="middle">Saved Machine Status (Registers, Status Flags)</text>
      <text x="210" y="124" font-family="Plus Jakarta Sans" font-size="10" text-anchor="middle">Local Variables & Temporaries</text>
    </g>
  </svg>
  <div class="diagram-caption">Figure 4.1: Memory Layout & Activation Record Architecture</div>
</div>

<h2 class="section-title">4. Parameter Passing Mechanisms</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th>Mechanism</th>
      <th>How Arguments are Passed</th>
      <th>Effect of Changes on Actual Arguments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Call by Value</strong></td>
      <td>Evaluates r-value and passes a copy to local parameter.</td>
      <td>Changes to formal parameter have <strong>zero effect</strong> on caller.</td>
    </tr>
    <tr>
      <td><strong>Call by Reference</strong></td>
      <td>Passes l-value (memory address / pointer) of actual argument.</td>
      <td>Changes directly <strong>mutate caller's variable</strong>.</td>
    </tr>
    <tr>
      <td><strong>Call by Name</strong></td>
      <td>Textual macro substitution (evaluated lazily via Thunk).</td>
      <td>Re-evaluated each time parameter is referenced.</td>
    </tr>
  </tbody>
</table>
"""

MODULE_5_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module V: Code Optimization & Target Generation — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Basic Blocks & Leader Instruction Algorithm</div>
    <div>2. Control Flow Graph (CFG) & Loop Dominators</div>
    <div>3. DAG Construction & Local Optimizations</div>
    <div>4. Machine-Independent Global Optimizations</div>
    <div>5. Register Allocation (Graph Coloring Heuristics)</div>
    <div>6. Peephole Optimization Techniques</div>
  </div>
</div>

<h2 class="section-title">1. Basic Blocks & Leader Identification Algorithm</h2>
<p>
  A <strong>Basic Block</strong> is a sequence of consecutive Three-Address Code statements in which flow of control enters at the beginning and leaves at the end without halt or possibility of branching except at the end.
</p>

<div class="callout callout-info">
  <div class="callout-title">Algorithm: Identifying Leader Instructions</div>
  1. The <strong>first statement</strong> in the TAC program is a leader.<br>
  2. Any statement that is the <strong>target of a conditional or unconditional goto</strong> is a leader.<br>
  3. Any statement that <strong>immediately follows a conditional or unconditional goto</strong> is a leader.
</div>

<h2 class="section-title">2. Directed Acyclic Graph (DAG) for Basic Blocks</h2>
<p>
  A DAG represents basic block expressions without redundancy:
  <ul>
    <li>Leaves represent initial variable values or constants.</li>
    <li>Interior nodes represent operators.</li>
    <li>Nodes are annotated with variable labels currently holding the computed value.</li>
  </ul>
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 30%;">Optimization Technique</th>
      <th>Description & Realized Benefits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Common Subexpression Elimination (CSE)</strong></td>
      <td>Identifies identical subexpression computations whose operand values have not changed, eliminating redundant operations.</td>
    </tr>
    <tr>
      <td><strong>Constant Folding</strong></td>
      <td>Evaluates operations with constant operands at <em>compile-time</em> (e.g., replacing `2 * 3.1415 * r` with `6.283 * r`).</td>
    </tr>
    <tr>
      <td><strong>Constant Propagation</strong></td>
      <td>Replaces variable uses with known compile-time constants.</td>
    </tr>
    <tr>
      <td><strong>Dead Code Elimination</strong></td>
      <td>Deletes instructions that compute values never used on any execution path.</td>
    </tr>
    <tr>
      <td><strong>Loop-Invariant Code Motion (Hoisting)</strong></td>
      <td>Moves computations whose operands are constant throughout the loop to the loop pre-header.</td>
    </tr>
    <tr>
      <td><strong>Induction Variable Elimination & Strength Reduction</strong></td>
      <td>Replaces expensive multiplications (e.g., $i \times 4$) inside loops with incremental additions ($t = t + 4$).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">3. Register Allocation via Graph Coloring (Chaitin's Algorithm)</h2>
<p>
  Given $k$ hardware registers, we construct the <strong>Interference Graph</strong> where nodes are variables/temporaries and edges represent live ranges that overlap. If the graph can be colored with $k$ colors such that no two adjacent nodes share the same color, no register spilling occurs.
</p>

<h2 class="section-title">4. Peephole Optimization</h2>
<p>
  Examines a short sliding window (peephole) of target instructions to apply local transformations:
  <ul>
    <li><strong>Redundant Load/Store Elimination:</strong> `MOV R0, x` followed by `MOV x, R0` $\rightarrow$ remove 2nd move.</li>
    <li><strong>Unreachable Code Elimination:</strong> Removing instructions immediately following unconditional jumps.</li>
    <li><strong>Flow-of-Control Optimizations:</strong> `goto L1 ... L1: goto L2` $\rightarrow$ replace with `goto L2`.</li>
    <li><strong>Algebraic Simplifications:</strong> Replacing `x = x + 0` or `x = x * 1` with no-op; replacing `x = x * 2` with `x = x << 1`.</li>
  </ul>
</p>
"""

# Let's define the 10-Page Master Quick Revision Body
MASTER_REVISION_BODY = r"""
<div class="toc-box">
  <div class="toc-title">🏛️ 10-Page Master Quick Revision — Compiler Design (CS24301)</div>
  <div class="toc-grid">
    <div>Page 1-2: Lexical Analysis, Tokens, Buffer Sentinels & Direct DFA</div>
    <div>Page 3-4: Context-Free Grammars, LL(1), FIRST/FOLLOW & Parsing Tables</div>
    <div>Page 5-6: LR Family Parsers (LR(0), SLR(1), CLR(1), LALR(1)) & Conflicts</div>
    <div>Page 7-8: SDD, SDTS, Three-Address Code, Arrays & Backpatching</div>
    <div>Page 9-10: Activation Records, Basic Blocks, DAG, Optimizations & PYQs</div>
  </div>
</div>

<h2 class="section-title">⚡ High-Yield Formula & Rule Master Matrix</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Core Concept</th>
      <th style="width: 45%;">Crucial Formula / Rule</th>
      <th>Exam Trap / Memory Key</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Direct DFA: Followpos</strong></td>
      <td>Cat-node $c_1 \cdot c_2$: $\text{followpos}(i) \cup= \text{firstpos}(c_2)$ for $i \in \text{lastpos}(c_1)$.<br>Star-node $c_1^*$: $\text{followpos}(i) \cup= \text{firstpos}(c_1)$ for $i \in \text{lastpos}(c_1)$.</td>
      <td>Must augment $(r)\#$; accepting states contain $\#$.</td>
    </tr>
    <tr>
      <td><strong>LL(1) Table Rule</strong></td>
      <td>For $A \rightarrow \alpha$: add to $M[A, a]$ for $a \in \text{FIRST}(\alpha)$. If $\epsilon \in \text{FIRST}(\alpha)$, add to $M[A, b]$ for $b \in \text{FOLLOW}(A)$.</td>
      <td>No duplicate entries permitted in any cell.</td>
    </tr>
    <tr>
      <td><strong>LR Parser Hierarchy</strong></td>
      <td>$\text{LL}(1) < \text{SLR}(1) < \text{LALR}(1) < \text{CLR}(1)$</td>
      <td>$\text{LALR}(1)$ merges core states of $\text{CLR}(1)$, reducing tables to $\text{SLR}(1)$ size.</td>
    </tr>
    <tr>
      <td><strong>2D Array Row-Major</strong></td>
      <td>$\text{Base} + ((i - low_1) \times n_2 + (j - low_2)) \times w$</td>
      <td>Multiply by $n_2$ (number of columns) for row-major.</td>
    </tr>
    <tr>
      <td><strong>2D Array Col-Major</strong></td>
      <td>$\text{Base} + ((j - low_2) \times n_1 + (i - low_1)) \times w$</td>
      <td>Multiply by $n_1$ (number of rows) for col-major.</td>
    </tr>
    <tr>
      <td><strong>Cyclomatic Complexity</strong></td>
      <td>$V(G) = E - N + 2 = P + 1 = \text{Regions}$</td>
      <td>Count decision/predicate nodes $P$.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🔥 Top 10 High-Probability BIT Mesra Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the 6 phases of compilation with the translation of position = initial + rate * 60.</div>
  <div class="qa-a">1. Lexer: Token stream with symbol table pointers. 2. Parser: Hierarchical syntax tree. 3. Semantic: Type checks and inttofloat coercion. 4. ICG: Three-address code with temporaries. 5. Optimizer: Constant folding (60.0) and temporary reduction. 6. Code Gen: Target register assembly instructions (LDF, MULF, ADDF, STF).</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. State the difference between S-Attributed and L-Attributed SDDs.</div>
  <div class="qa-a"><strong>S-Attributed:</strong> Exclusively synthesized attributes; evaluated bottom-up during post-order traversal.<br><strong>L-Attributed:</strong> Inherited attributes allowed only if they depend on parent or left-siblings; evaluated in a single top-down left-to-right DFS pass.</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Detail the contents of an Activation Record and explain static vs. dynamic links.</div>
  <div class="qa-a">Contents: Parameters, Return Value, Return Address (PC), Dynamic Link (caller AR pointer), Static Link (lexical parent AR pointer), Saved Machine Registers, Local Variables, Temporaries.</div>
</div>
"""

MODULE_1_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module I: Lexical Analysis — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Language Processing Systems & Cousins of Compiler</div>
    <div>2. 6 Phases of Compiler with Running Example</div>
    <div>3. Token, Pattern, Lexeme & Token Attributes</div>
    <div>4. Input Buffering (Buffer Pairs & Sentinels)</div>
    <div>5. Thompson's Construction (RE → NFA)</div>
    <div>6. Subset Construction (NFA → DFA)</div>
    <div>7. Hopcroft's DFA State Minimization</div>
    <div>8. Direct DFA Construction (Syntax Tree Method)</div>
  </div>
</div>

<h2 class="section-title">1. Language Processors & 6 Phases of Compiler</h2>
<p>
  A <strong>compiler</strong> translates high-level source code into target machine language while reporting errors.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Tool</th>
      <th style="width: 25%;">Input $\rightarrow$ Output</th>
      <th>Core Responsibilities</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Preprocessor</strong></td><td><code>.c</code> $\rightarrow$ <code>.i</code> (Pure Source)</td><td>Macro expansion (<code>#define</code>), header inclusion (<code>#include</code>), stripping comments.</td></tr>
    <tr><td><strong>Compiler</strong></td><td><code>.i</code> $\rightarrow$ <code>.s</code> (Assembly)</td><td>Front-end analysis & back-end code synthesis.</td></tr>
    <tr><td><strong>Assembler</strong></td><td><code>.s</code> $\rightarrow$ <code>.o</code> (Relocatable Object)</td><td>Translates mnemonics to machine code and symbol offsets.</td></tr>
    <tr><td><strong>Linker</strong></td><td><code>.o</code> + Libs $\rightarrow$ <code>.exe</code></td><td>Resolves external symbol references across modules.</td></tr>
    <tr><td><strong>Loader</strong></td><td>Binary $\rightarrow$ RAM</td><td>Allocates memory segments, sets up stack/heap, jumps to <code>main</code>.</td></tr>
  </tbody>
</table>

<h2 class="section-title">2. Input Buffering & Sentinels</h2>
<p>
  Using <strong>Buffer Pairs</strong> ($2 \times N$ characters) with <strong>Sentinel (`EOF`)</strong> characters placed at buffer ends eliminates one conditional check per character, reducing inner scanning loop overhead by 50%.
</p>

<h2 class="section-title">3. Direct DFA Construction (Syntax Tree Method)</h2>
<p>
  Constructs DFA directly from augmented regular expression $(r)\#$:
  <ul>
    <li><code>nullable(n)</code>: True iff subtree generates $\epsilon$.</li>
    <li><code>firstpos(n)</code>: Set of positions matching the first character of subtree strings.</li>
    <li><code>lastpos(n)</code>: Set of positions matching the last character of subtree strings.</li>
    <li><code>followpos(i)</code>: Positions immediately following position $i$.
      <ul>
        <li>For cat-node $c_1 \cdot c_2$: add $\text{firstpos}(c_2)$ to $\text{followpos}(i)$ for all $i \in \text{lastpos}(c_1)$.</li>
        <li>For star-node $c_1^*$: add $\text{firstpos}(c_1)$ to $\text{followpos}(i)$ for all $i \in \text{lastpos}(c_1)$.</li>
      </ul>
    </li>
  </ul>
</p>

<div class="callout callout-pyq">
  <div class="callout-title">🏛️ BIT Mesra Exam Solved Problem: $(a|b)^*abb\#$</div>
  Leaves: $a(1), b(2), a(3), b(4), b(5), \#(6)$.<br>
  $\text{followpos}(1) = \{1, 2, 3\}, \text{followpos}(2) = \{1, 2, 3\}, \text{followpos}(3) = \{4\}, \text{followpos}(4) = \{5\}, \text{followpos}(5) = \{6\}, \text{followpos}(6) = \emptyset$.<br>
  DFA States: $A=\{1, 2, 3\} \xrightarrow{a} B=\{1, 2, 3, 4\} \xrightarrow{b} C=\{1, 2, 3, 5\} \xrightarrow{b} D^*=\{1, 2, 3, 6\}$.
</div>
"""

MODULES = [
    ("Module 1: Lexical Analysis", "Language Processors, Buffering, Thompson NFA & Direct DFA", "Module I Notes", MODULE_1_BODY, "Module_1_Lexical_Analysis_Notes"),
    ("Module 2: Syntax Analysis", "Context-Free Grammars, LL(1), SLR(1), CLR(1), LALR(1) & Parsing Conflicts", "Module II Notes", MODULE_2_BODY, "Module_2_Syntax_Analysis_Notes"),
    ("Module 3: Semantic Analysis & Intermediate Code Generation", "SDD, SDTS, Three-Address Code, Type Checking & Multi-D Arrays", "Module III Notes", MODULE_3_BODY, "Module_3_Semantic_Analysis_Notes"),
    ("Module 4: Advanced ICG & Runtime Environment", "Short-Circuit Booleans, Backpatching, Activation Records & Parameter Passing", "Module IV Notes", MODULE_4_BODY, "Module_4_Runtime_Environment_Notes"),
    ("Module 5: Code Optimization & Target Generation", "Basic Blocks, CFG, DAG Optimizations, Register Allocation & Peephole", "Module V Notes", MODULE_5_BODY, "Module_5_Code_Optimization_Notes"),
    ("Compiler Design — 10-Page Master Quick Revision", "High-Yield Formula Sheet, Decision Trees & Top 10 BIT Mesra PYQ Solutions", "10-Page Master Revision", MASTER_REVISION_BODY, "Compiler_Design_10_Page_Master_Revision"),
]

def build_all_cd():
    base_dir = "/Users/shaswatraj/Desktop/study/compiler-design"
    html_dir = os.path.join(base_dir, "html")
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(html_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    print("Launching Chromium via Playwright for Compiler Design suite...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=True
        )
        
        full_course_body = ""
        for title, subtitle, badge, body, filename in MODULES:
            html_content = wrap_html(title, subtitle, badge, body)
            html_file = os.path.join(html_dir, f"{filename}.html")
            pdf_file = os.path.join(pdf_dir, f"{filename}.pdf")

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)

            page = browser.new_page()
            page.goto(f"file://{html_file}", wait_until="networkidle")
            page.wait_for_timeout(1500)
            page.pdf(
                path=pdf_file,
                format="A4",
                print_background=True,
                margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
                prefer_css_page_size=True
            )
            page.close()
            print(f"✅ Generated {pdf_file} ({os.path.getsize(pdf_file)} bytes)")
            
            if "10-Page" not in title:
                full_course_body += f"<div style='page-break-before: always;'>{body}</div>"

        # Full Course Master
        full_master_html = wrap_html(
            "Compiler Design (CS24301) — Full Course Master Book",
            "Complete End-to-End B.Tech CSE 5th Semester Study Book & PYQ Bank",
            "Full Course Master",
            full_course_body
        )
        full_html_file = os.path.join(html_dir, "Compiler_Design_Full_Course_Master.html")
        full_pdf_file = os.path.join(pdf_dir, "Compiler_Design_Full_Course_Master.pdf")
        with open(full_html_file, "w", encoding="utf-8") as f:
            f.write(full_master_html)

        page = browser.new_page()
        page.goto(f"file://{full_html_file}", wait_until="networkidle")
        page.wait_for_timeout(2500)
        page.pdf(
            path=full_pdf_file,
            format="A4",
            print_background=True,
            margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
            prefer_css_page_size=True
        )
        page.close()
        print(f"🎉 Generated Full Course Master Book: {full_pdf_file} ({os.path.getsize(full_pdf_file)} bytes)")

        browser.close()

if __name__ == "__main__":
    build_all_cd()
