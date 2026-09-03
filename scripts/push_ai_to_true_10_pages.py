#!/usr/bin/env python3
"""
True 10-12 Page Master AI Compiler (CS24307).
Embeds 35k-42k characters per module to guarantee 10-12 pages each and 55+ pages for the Master Book.
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

sys.path.insert(0, AI_DIR)
from ai_module1_content import AI_M1_EXHAUSTIVE
from ai_module2_content import AI_M2_EXHAUSTIVE
from ai_module3_content import AI_M3_EXHAUSTIVE
from ai_module4_content import AI_M4_EXHAUSTIVE
from ai_module5_content import AI_M5_EXHAUSTIVE
from ai_revision_content import AI_REVISION_EXHAUSTIVE

# Additional high-density textbook expansions for M1–M5
M1_EXP = r"""
<h2 class="section-title">Topic 7.6: Detailed Mathematical Properties of State Space & Perception</h2>

<div class="formula-card">
  <strong>Formal Agent Perception History & Action Space:</strong>
  $$\mathbf{\mathcal{P} = \{p_1, p_2, \dots, p_k\} \implies \mathcal{P}^* = \bigcup_{t=0}^\infty \mathcal{P}^t}$$
  $$\mathbf{\text{Number of Possible Agent Functions over Horizon } T: \ |\mathcal{A}|^{|\mathcal{P}|^T}}$$
  <em>Combinatorial Significance:</em> For even modest $|\mathcal{P}|=10$ and $|\mathcal{A}|=5$ over $T=10$ steps, there are $5^{10^{10}}$ candidate agent functions! This astronomical search space proves why tabular lookup reflex agents are physically impossible and why compact, generalizing representations (logic, heuristics, neural networks) are mandatory.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Agent Performance Metric Engineering</div>
  <p>An autonomous street cleaning robot is deployed in an urban city center. Compare two proposed performance measures:</p>
  <ul>
    <li><strong>Metric 1:</strong> Amount of dirt collected in the robot's onboard disposal bin over 24 hours.</li>
    <li><strong>Metric 2:</strong> Cleanliness of the entire street network averaged over 24 hours.</li>
  </ul>
  <p><strong>Critical Agent Analysis:</strong></p>
  <ul>
    <li>Under <strong>Metric 1</strong>, a rational agent maximizes dirt in its bin. To maximize this metric, the agent might clean up a pile of dirt, dump it back onto the clean pavement, and sweep it up again repeatedly!</li>
    <li>Under <strong>Metric 2</strong>, the agent is rewarded strictly for the <em>desired state of the external environment</em> (clean streets), preventing perverse reward hacking!</li>
    <li><strong>Core Principle (Russell & Norvig):</strong> Design performance measures according to what you want to achieve in the environment, NOT according to how you think the agent should behave!</li>
  </ul>
</div>

<div class="qa-card">
  <div class="qa-q">Q16. Explain the Concept of Software Agents (Softbots) and Web Crawling Agents. (8 Marks)</div>
  <div class="qa-a">
    A <strong>Softbot</strong> is an intelligent agent whose environment is entirely digital (operating systems, web networks, databases, cloud infrastructure) rather than physical hardware. Example (Search Engine Indexing Spider):<br>
    • <strong>P:</strong> Freshness of search index, crawl coverage, low server load, high page pagerank relevance.<br>
    • <strong>E:</strong> The World Wide Web (HTTP/HTTPS protocols, HTML/DOM trees, sitemaps, robots.txt constraints).<br>
    • <strong>A:</strong> HTTP GET requests, URL extraction, indexing pipeline dispatch, rate-limiting sleep calls.<br>
    • <strong>S:</strong> HTTP status codes, HTML content strings, header response times.
  </div>
</div>
"""

M2_EXP = r"""
<h2 class="section-title">Topic 13.6: Exhaustive Adversarial Game Theory & Alpha-Beta Deep Traces</h2>

<div class="formula-card">
  <strong>Alpha-Beta Pruning Efficiency Theorems:</strong>
  - <strong>Worst-Case Move Ordering (Worst-first):</strong> Alpha-Beta examines every leaf node $\implies O(b^d)$ (No pruning advantage over standard Minimax).
  - <strong>Ideal / Optimal Move Ordering (Best-first):</strong> The effective branching factor is reduced from $b$ to $\sqrt{b}$ $\implies \mathbf{O(b^{d/2})}$.
  - <em>Profound Consequence:</em> With optimal move ordering, an Alpha-Beta search can search <strong>twice as deep</strong> in the same compute time as standard Minimax (e.g., searching 12 plies instead of 6 plies in Chess)!
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Full 3-Ply Alpha-Beta Pruning Tree Trace</div>
  <p>Consider a 3-ply Minimax tree where Root is MAX, Level 1 is MIN ($B, C$), Level 2 is MAX ($D, E, F, G$), and Level 3 has 8 terminal leaves:</p>
  <ul>
    <li>Node $D$ leaves: $[4, 6]$ $\implies \text{Node } D = \max(4, 6) = 6$.</li>
    <li>Node $E$ leaves: $[7, 9]$ $\implies \text{Node } E = \max(7, 9) = 9$.</li>
    <li>Node $B$ ($\text{MIN}$ of $D, E$): $\beta = \min(6, 9) = 6$. Updates Root MAX: $\alpha = 6$.</li>
    <li>Node $F$ left leaf: $1$. Since $\text{Node } F$ is MAX, $F \ge 1$. Node $F$ right leaf: $2 \implies \text{Node } F = 2$.</li>
    <li>Node $C$ ($\text{MIN}$): Updates $\beta = 2$.</li>
    <li>Now at Node $C$, we have $\mathbf{\alpha = 6 \ge \beta = 2} \implies \mathbf{\text{PRUNE NODE } G \text{ AND ALL ITS LEAVES COMPLETELY!}}$</li>
    <li>$\mathbf{\text{Root Optimal Value } = 6 \quad (\text{Optimal Move: } A \rightarrow B)}$.</li>
  </ul>
</div>

<div class="qa-card">
  <div class="qa-q">Q14. Explain Transposition Tables in Game Tree Search. How do Zobrist Hashing keys operate? (8 Marks)</div>
  <div class="qa-a">
    In games like Chess, different move orders can lead to the identical board position (Transposition: $1. e4 \ e5 \ 2. Nf3 \ Nc6$ vs $1. Nf3 \ Nc6 \ 2. e4 \ e5$). A <strong>Transposition Table</strong> is a high-speed hash map caching previously evaluated board states.<br>
    <strong>Zobrist Hashing:</strong> Assigns a random 64-bit integer to each `(piece, square)` tuple. A board position's hash is computed by XORing ($\oplus$) all present piece keys. When a move occurs, updating the hash takes $O(1)$ XOR operations ($\text{Hash}' = \text{Hash} \oplus \text{Key}_{\text{old}} \oplus \text{Key}_{\text{new}}$), enabling millions of board lookups per second!
  </div>
</div>
"""

M3_EXP = r"""
<h2 class="section-title">Topic 22.6: Advanced Resolution Strategies & Knowledge Compilation</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Resolution Strategy</th>
      <th style="width: 40%;">Algorithmic Restriction</th>
      <th>Completeness & Efficiency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Unit Resolution</strong></td>
      <td>At least one of the two parent clauses must be a <em>unit clause</em> (containing exactly one literal).</td>
      <td>Incomplete in general; complete and runs in $O(N)$ time for Horn KBs.</td>
    </tr>
    <tr>
      <td><strong>Input Resolution</strong></td>
      <td>At least one parent clause must come from the original input KB or negated query (never two derived clauses).</td>
      <td>Incomplete in general; equivalent in power to Unit Resolution.</td>
    </tr>
    <tr>
      <td><strong>Linear Resolution</strong></td>
      <td>Each step resolves the most recently derived clause with either an input clause or a previous ancestor clause.</td>
      <td><strong>Refutation Complete</strong>; basis for Prolog's SLD resolution.</td>
    </tr>
    <tr>
      <td><strong>Set of Support (SOS)</strong></td>
      <td>Every resolution step must involve at least one clause derived from the negated query (the set of support).</td>
      <td><strong>Refutation Complete</strong>; prevents wasteful resolution among mutually consistent background KB axioms.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Proof: The "Customs Official" Full Refutation Proof Tree</div>
  <p><strong>Axioms:</strong></p>
  <ol>
    <li>$C_1: \neg \text{Official}(x) \lor \neg \text{Enters}(y) \lor \text{VIP}(y) \lor \text{Searches}(x, y)$</li>
    <li>$C_2: \text{Smuggler}(A)$ (Skolem constant $A$)</li>
    <li>$C_3: \text{Enters}(A)$</li>
    <li>$C_4: \neg \text{Searches}(z, A) \lor \text{Smuggler}(z)$</li>
    <li>$C_5: \neg \text{Smuggler}(x) \lor \neg \text{VIP}(x)$</li>
    <li>$C_6: \text{Official}(B)$ (Official $B$ exists)</li>
  </ol>
  <p><strong>Query:</strong> Prove $\exists w (\text{Official}(w) \land \text{Smuggler}(w))$. Negated Query: $C_7: \neg \text{Official}(w) \lor \neg \text{Smuggler}(w)$.</p>
  <p><strong>Resolution Proof Steps:</strong></p>
  <ol>
    <li>Resolve $C_2$ ($\text{Smuggler}(A)$) with $C_5$ $\{x/A\} \implies \mathbf{C_8: \neg \text{VIP}(A)}$.</li>
    <li>Resolve $C_1$ with $C_3$ $\{y/A\} \implies \mathbf{C_9: \neg \text{Official}(x) \lor \text{VIP}(A) \lor \text{Searches}(x, A)}$.</li>
    <li>Resolve $C_9$ with $C_8 \implies \mathbf{C_{10}: \neg \text{Official}(x) \lor \text{Searches}(x, A)}$.</li>
    <li>Resolve $C_{10}$ with $C_4$ $\{z/x\} \implies \mathbf{C_{11}: \neg \text{Official}(x) \lor \text{Smuggler}(x)}$.</li>
    <li>Resolve $C_{11}$ with $C_6$ $\{x/B\} \implies \mathbf{C_{12}: \text{Smuggler}(B)}$.</li>
    <li>Resolve $C_{12}$ with $C_7$ $\{w/B\} \implies \mathbf{C_{13}: \neg \text{Official}(B)}$.</li>
    <li>Resolve $C_{13}$ with $C_6$ ($\text{Official}(B)$) $\implies \mathbf{\Box \text{ (EMPTY CLAUSE - CONTRADICTION!)}}$.</li>
  </ol>
  $$\mathbf{\text{Q.E.D. Strictly proven that some official must be a smuggler!}}$$
</div>
"""

M4_EXP = r"""
<h2 class="section-title">Topic 29.6: Advanced Decision Networks & Value of Information (VOI)</h2>

<div class="formula-card">
  <strong>Value of Perfect Information (VPI / VOI):</strong>
  The expected value of information regarding an unobserved random variable $E_j$ is the difference between the expected utility with $E_j$ known versus without knowing $E_j$:
  $$\mathbf{\text{VPI}(E_j) = \left( \sum_k P(E_j = e_{jk}) \max_a \mathbb{E}[U(a \mid e_{jk})] \right) - \max_a \mathbb{E}[U(a)]}$$
  <strong>Properties of VPI:</strong>
  1. Non-negative: $\text{VPI}(E_j) \ge 0$ (Information never reduces expected utility).<br>
  2. Non-additive: $\text{VPI}(E_j, E_k) \neq \text{VPI}(E_j) + \text{VPI}(E_k)$.<br>
  3. Order-independent: $\text{VPI}(E_j, E_k) = \text{VPI}(E_j) + \text{VPI}(E_k \mid E_j) = \text{VPI}(E_k) + \text{VPI}(E_j \mid E_k)$.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Value of Information in Oil Drilling</div>
  <p>An oil company is deciding whether to drill an offshore site ($a_1$) or sell the lease for $\$3\text{M}$ ($a_2$). Prior probability of oil is $P(\text{Oil}) = 0.5$. If oil is present, profit is $\$10\text{M}$; if dry, loss is $-\$4\text{M}$.</p>
  <ul>
    <li>Expected utility of drilling ($a_1$): $\mathbb{E}[U(a_1)] = 0.5(10) + 0.5(-4) = 5 - 2 = \mathbf{\$3\text{M}}$.</li>
    <li>Expected utility of selling ($a_2$): $\mathbb{E}[U(a_2)] = \mathbf{\$3\text{M}}$. Base optimal utility = $\$3\text{M}$.</li>
  </ul>
  <p><strong>A seismic survey ($S$) provides perfect information about whether oil is present:</strong></p>
  <ul>
    <li>If seismic says Oil ($P=0.5$): Drill ($a_1$) $\implies \text{Utility} = \$10\text{M}$.</li>
    <li>If seismic says Dry ($P=0.5$): Sell ($a_2$) $\implies \text{Utility} = \$3\text{M}$.</li>
    <li>Expected utility with seismic test: $0.5(10) + 0.5(3) = 5 + 1.5 = \mathbf{\$6.5\text{M}}$.</li>
  </ul>
  $$\mathbf{\text{VPI}(\text{Seismic}) = \$6.5\text{M} - \$3\text{M} = \mathbf{\$3.5\text{M}}}$$
  <p><em>Decision:</em> The company should pay up to <strong>$\$3.5\text{M}$</strong> for the seismic survey test!</p>
</div>
"""

M5_EXP = r"""
<h2 class="section-title">Topic 38.6: Advanced Statistical Learning Theory & Optimization Algorithms</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Optimization Algorithm</th>
      <th style="width: 45%;">Mathematical Update Rule</th>
      <th>Key Advantages in Deep Learning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Stochastic Gradient Descent (SGD)</strong></td>
      <td>$\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}_i(\theta_t)$</td>
      <td>Fast per-iteration computation; noisy gradients escape shallow saddle points.</td>
    </tr>
    <tr>
      <td><strong>Momentum SGD</strong></td>
      <td>$v_{t+1} = \gamma v_t + \eta \nabla_\theta \mathcal{L}(\theta_t), \quad \theta_{t+1} = \theta_t - v_{t+1}$</td>
      <td>Dampens oscillations across high-curvature ravines; accelerates progress along flat valleys.</td>
    </tr>
    <tr>
      <td><strong>Adam (Adaptive Moment Estimation)</strong></td>
      <td>$m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t, \quad v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$<br>$\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \ \hat{v}_t = \frac{v_t}{1-\beta_2^t} \implies \theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$</td>
      <td>Combines momentum with adaptive per-parameter learning rates; the universal standard for Transformers and Deep Neural Networks.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Support Vector Machine Dual Formulation & Support Vector Identification</div>
  <p>Given 3 training data points in 2D space: $\mathbf{x}_1 = (1, 1)^T, y_1 = -1$; $\mathbf{x}_2 = (2, 0)^T, y_2 = -1$; $\mathbf{x}_3 = (2, 3)^T, y_3 = +1$.</p>
  <p><strong>1. SVM Dual Formulation:</strong></p>
  $$\mathbf{\max_\alpha \sum_{i=1}^3 \alpha_i - \frac{1}{2} \sum_{i=1}^3 \sum_{j=1}^3 \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j) \quad \text{subject to } \sum \alpha_i y_i = 0, \ \alpha_i \ge 0}$$
  <p><strong>2. Optimal Solution:</strong> $\alpha_1 = 0, \ \alpha_2 = 0.5, \ \alpha_3 = 0.5$.</p>
  $$\mathbf{\mathbf{w} = \sum_{i=1}^3 \alpha_i y_i \mathbf{x}_i = 0.5(-1)(2, 0)^T + 0.5(+1)(2, 3)^T = (-1, 0)^T + (1, 1.5)^T = \mathbf{(0, 1.5)^T}}$$
  <p><strong>3. Hyperplane Bias $b$:</strong> For support vector $\mathbf{x}_3$: $y_3(\mathbf{w}^T \mathbf{x}_3 + b) = 1 \implies 1(0(2) + 1.5(3) + b) = 1 \implies 4.5 + b = 1 \implies \mathbf{b = -3.5}$.</p>
  $$\mathbf{\text{Optimal Decision Boundary: } 1.5 x_2 - 3.5 = 0 \iff \mathbf{x_2 = 2.333}}$$
</div>
"""

CSS_STYLES = """
@page {
  size: A4 portrait;
  margin: 15mm 12mm 15mm 12mm;
}
*, *::before, *::after { box-sizing: border-box; }
body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 11.8px;
  line-height: 1.60;
  color: #1e293b;
  background: #ffffff;
  margin: 0;
  padding: 0;
}
.cover-container {
  padding: 30px 20px;
  text-align: center;
  border-bottom: 2px solid #3b82f6;
  margin-bottom: 24px;
}
.course-badge {
  display: inline-block;
  background: #eff6ff;
  color: #1d4ed8;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 20px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 12px;
  border: 1px solid #bfdbfe;
}
.book-title {
  font-size: 26px;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 8px 0;
  letter-spacing: -0.5px;
}
.book-subtitle { font-size: 13.5px; color: #475569; margin: 0 0 16px 0; font-weight: 500; }
.toc-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 16px 20px;
  margin: 20px 0 28px 0;
}
.toc-title { font-size: 13.5px; font-weight: 700; color: #1d4ed8; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
.toc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px 16px; font-size: 11px; color: #334155; }
h2.section-title {
  font-size: 15px;
  font-weight: 700;
  color: #1d4ed8;
  border-bottom: 1.5px solid #e2e8f0;
  padding-bottom: 5px;
  margin: 26px 0 14px 0;
  page-break-after: avoid;
}
p { margin: 0 0 10px 0; text-align: justify; }
.callout { border-radius: 6px; padding: 14px 18px; margin: 14px 0; font-size: 11.5px; page-break-inside: avoid; }
.callout-info { background: #eff6ff; border-left: 4px solid #3b82f6; color: #1e3a8a; }
.callout-title { font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 6px; }
.custom-table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 11px; page-break-inside: avoid; }
.custom-table th, .custom-table td { border: 1px solid #cbd5e1; padding: 8px 10px; text-align: left; vertical-align: top; }
.custom-table th { background: #f1f5f9; color: #0f172a; font-weight: 700; }
.custom-table tr:nth-child(even) { background: #f8fafc; }
.formula-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #8b5cf6;
  border-radius: 6px;
  padding: 14px 18px;
  margin: 14px 0;
  page-break-inside: avoid;
  text-align: center;
}
.worked-box {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-left: 4px solid #22c55e;
  border-radius: 6px;
  padding: 14px 18px;
  margin: 16px 0;
  page-break-inside: avoid;
}
.worked-title { font-weight: 700; color: #15803d; font-size: 12px; margin-bottom: 8px; }
.diagram-container { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; margin: 14px 0; text-align: center; page-break-inside: avoid; }
.diagram-caption { font-size: 10.5px; color: #64748b; margin-top: 8px; font-weight: 500; }
.qa-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 16px; margin: 12px 0; page-break-inside: avoid; }
.qa-q { font-weight: 700; color: #0f172a; margin-bottom: 6px; }
.qa-a { color: #334155; line-height: 1.55; }
pre { background: #0f172a; color: #f8fafc; padding: 12px 16px; border-radius: 6px; font-family: 'Fira Code', monospace; font-size: 10.5px; line-height: 1.45; overflow-x: auto; margin: 12px 0; page-break-inside: avoid; }
code { font-family: 'Fira Code', monospace; font-size: 11px; background: #f1f5f9; color: #2563eb; padding: 2px 5px; border-radius: 4px; }
pre code { background: transparent; color: inherit; padding: 0; }
.page-break { page-break-before: always; }
"""

def wrap_html(title, subtitle, body_html, module_num=None):
    badge = f"CS24307 • Module {module_num}" if module_num else "CS24307 • Complete Master Guide"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <style>
    {CSS_STYLES}
  </style>
</head>
<body>
  <div class="cover-container">
    <div class="course-badge">{badge}</div>
    <h1 class="book-title">{title}</h1>
    <div class="book-subtitle">{subtitle}</div>
  </div>
  {body_html}
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      if (window.renderMathInElement) {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ]
        }});
      }}
    }});
  </script>
</body>
</html>"""

def generate_pdf(html_path, pdf_path, title):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath(html_path)}", wait_until="networkidle")
        page.evaluate("""() => {
            if (window.renderMathInElement) {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ]
                });
            }
        }""")
        page.wait_for_timeout(1200)
        
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "12mm", "right": "12mm"},
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=f"""
            <div style="font-size: 8.5pt; font-family: 'Plus Jakarta Sans', sans-serif; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 12mm;">
              <span>{title} • BIT Mesra CSE</span>
              <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
            </div>
            """
        )
        browser.close()
    print(f"✅ Generated {pdf_path} ({os.path.getsize(pdf_path)} bytes)")

def build_ultimate_ai():
    m1_final = AI_M1_EXHAUSTIVE + M1_EXP
    m2_final = AI_M2_EXHAUSTIVE + M2_EXP
    m3_final = AI_M3_EXHAUSTIVE + M3_EXP
    m4_final = AI_M4_EXHAUSTIVE + M4_EXP
    m5_final = AI_M5_EXHAUSTIVE + M5_EXP

    print("M1 final chars:", len(m1_final))
    print("M2 final chars:", len(m2_final))
    print("M3 final chars:", len(m3_final))
    print("M4 final chars:", len(m4_final))
    print("M5 final chars:", len(m5_final))

    with open(os.path.join(AI_DIR, "ai_module1_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M1_EXHAUSTIVE = r"""{m1_final}"""\n')
    with open(os.path.join(AI_DIR, "ai_module2_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M2_EXHAUSTIVE = r"""{m2_final}"""\n')
    with open(os.path.join(AI_DIR, "ai_module3_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M3_EXHAUSTIVE = r"""{m3_final}"""\n')
    with open(os.path.join(AI_DIR, "ai_module4_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M4_EXHAUSTIVE = r"""{m4_final}"""\n')
    with open(os.path.join(AI_DIR, "ai_module5_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M5_EXHAUSTIVE = r"""{m5_final}"""\n')

    modules = [
        (1, "Module 1: Intelligent Agents & PEAS Framework", "Topics 1 to 7 • Foundations, Evolution, Rationality & 5 Agent Types", m1_final, "Module_1_Intelligent_Agents_Notes"),
        (2, "Module 2: Search Algorithms & Game Playing", "Topics 8 to 13 • BFS/DFS/IDDFS, A* Admissibility Proofs & Alpha-Beta Pruning", m2_final, "Module_2_Search_Algorithms_Notes"),
        (3, "Module 3: Knowledge Representation & Logic", "Topics 14 to 22 • Wumpus World, Propositional CNF, First-Order Logic & Resolution", m3_final, "Module_3_Knowledge_Logic_Notes"),
        (4, "Module 4: Classical Planning & Bayesian Networks", "Topics 23 to 29 • STRIPS / PDDL, Graphplan Mutexes, Probability & Bayes Nets", m4_final, "Module_4_Planning_Bayes_Notes"),
        (5, "Module 5: Machine Learning & Neural Networks", "Topics 30 to 38 • Decision Trees ID3, Perceptrons & Backpropagation Math", m5_final, "Module_5_Machine_Learning_Notes"),
    ]

    for num, title, subtitle, content, fname in modules:
        html_content = wrap_html(title, subtitle, content, module_num=num)
        html_file = os.path.join(HTML_DIR, f"{fname}.html")
        pdf_file = os.path.join(PDF_DIR, f"{fname}.pdf")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        generate_pdf(html_file, pdf_file, f"AI Module {num}")

    # Revision
    rev_html = wrap_html(
        "Artificial Intelligence (CS24307) 10-Page Master Revision",
        "High-Yield Formulas, Search Matrices, Logic Rules, Bayes Formulas & Flashcards",
        AI_REVISION_EXHAUSTIVE
    )
    rev_html_file = os.path.join(HTML_DIR, "AI_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "AI_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "AI 10-Page Master Revision")

    # Full Master Book
    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
    from build_complete_ai_master_suite import LAB_GUIDE
    full_body = []
    for num, title, subtitle, content, _ in modules:
        full_body.append(f"""
        <div class="page-break"></div>
        <div class="cover-container" style="margin-top: 40px;">
          <div class="course-badge">Module {num} of 5</div>
          <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">{title}</h2>
          <div style="font-size: 12.5px; color: #64748b;">{subtitle}</div>
        </div>
        {content}
        """)

    full_body.append(LAB_GUIDE)
    full_body.append(f"""
    <div class="page-break"></div>
    <div class="cover-container" style="margin-top: 40px;">
      <div class="course-badge">Comprehensive Revision Appendix</div>
      <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">10-Page Master Quick Revision Guide</h2>
      <div style="font-size: 12.5px; color: #64748b;">Formulas, Algorithm Checklists & Solved Exam Cards</div>
    </div>
    {AI_REVISION_EXHAUSTIVE}
    """)

    full_master_html = wrap_html(
        "Artificial Intelligence (CS24307) Full Course Master",
        "Exhaustive 38-Topic Textbook, Python Lab Guide & Solved University Question Bank",
        "".join(full_body)
    )
    master_html_file = os.path.join(HTML_DIR, "AI_Full_Course_Master.html")
    master_pdf_file = os.path.join(PDF_DIR, "AI_Full_Course_Master.pdf")
    with open(master_html_file, "w", encoding="utf-8") as f:
        f.write(full_master_html)
    generate_pdf(master_html_file, master_pdf_file, "AI Full Course Master")

if __name__ == "__main__":
    build_ultimate_ai()
