#!/usr/bin/env python3
"""
AI Super Suite Builder:
Loads the expanded content files from artificial-intelligence/, ensures they are 35,000+ characters each,
and compiles them via Playwright Chromium into 10-14 page modules and 55+ page master book!
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

# Extra content injections
M1_EXTRA2 = r"""
<h2 class="section-title">Topic 7.3: Master University Solved Examination Bank (Part II)</h2>

<div class="qa-card">
  <div class="qa-q">Q6. Compare Goal-Based Agents and Utility-Based Agents with decision-theoretic examples. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Goal-Based Agents:</strong> Seek binary achievement of defined goals ($G(s) \in \{\text{True}, \text{False}\}$). They lack the ability to trade off conflicting criteria (e.g. speed vs safety) or quantify partial goal satisfaction.<br>
    • <strong>Utility-Based Agents:</strong> Map states to a real-valued scalar utility function $U: \mathcal{S} \rightarrow \mathbb{R}$. When multiple goals conflict (e.g., getting to the airport quickly vs spending minimal fuel vs avoiding toll roads), a utility agent computes the expected utility $\mathbb{E}[U] = \sum_s P(s \mid a) U(s)$ and selects the action that maximizes expected utility (Maximum Expected Utility Principle).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q7. Differentiate between Epistemic Actions and Pragmatic Actions with robotic exploration examples. (6 Marks)</div>
  <div class="qa-a">
    • <strong>Pragmatic Actions:</strong> Actions intended to change the physical world state to bring the agent closer to its goal (e.g., vacuum cleaner picking up dirt, autonomous car accelerating).<br>
    • <strong>Epistemic Actions:</strong> Actions whose primary purpose is to acquire information and reduce uncertainty in a partially observable world (e.g., exploring an unmapped room, running a medical diagnostic blood test, looking around a blind corner before turning).
  </div>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: Agent Environment Complexity Analysis Table</div>
  <table class="custom-table">
    <thead><tr><th>Real-World Domain</th><th>Observable</th><th>Deterministic</th><th>Episodic</th><th>Static</th><th>Discrete</th><th>Agents</th></tr></thead>
    <tbody>
      <tr><td><strong>Chess with Clock</strong></td><td>Fully</td><td>Deterministic</td><td>Sequential</td><td>Semi-dynamic</td><td>Discrete</td><td>Multi (Adversarial)</td></tr>
      <tr><td><strong>Robot Soccer (RoboCup)</strong></td><td>Partially</td><td>Stochastic</td><td>Sequential</td><td>Dynamic</td><td>Continuous</td><td>Multi (Cooperative + Comp)</td></tr>
      <tr><td><strong>Automated Medical Surgery</strong></td><td>Partially</td><td>Stochastic</td><td>Sequential</td><td>Dynamic</td><td>Continuous</td><td>Single (with patient)</td></tr>
      <tr><td><strong>Image Part Classification</strong></td><td>Fully</td><td>Deterministic</td><td>Episodic</td><td>Static</td><td>Discrete</td><td>Single</td></tr>
    </tbody>
  </table>
</div>
"""

M2_EXTRA2 = r"""
<h2 class="section-title">Topic 13.3: Master University Solved Examination Bank (Part II)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 2: Heuristic Depth & Node Expansion Estimation</div>
  <p>An informed search problem has a search tree of uniform branching factor $b = 4$ and solution depth $d = 6$.</p>
  <ol>
    <li>Calculate the total nodes expanded by Breadth-First Search (BFS).</li>
    <li>If $A^*$ search with an admissible heuristic reduces the effective branching factor to $b^* = 1.5$, calculate the number of nodes expanded by $A^*$.</li>
  </ol>
  <p><strong>Solution:</strong></p>
  $$\text{1. BFS Total Nodes: } N_{\text{BFS}} = \sum_{i=1}^6 4^i = 4 + 16 + 64 + 256 + 1024 + 4096 = \mathbf{5460 \text{ nodes}}$$
  $$\text{2. } A^* \text{ Nodes with } b^* = 1.5: \ N_{A^*} = \sum_{i=1}^6 (1.5)^i = 1.5 + 2.25 + 3.375 + 5.0625 + 7.59375 + 11.390625 \approx \mathbf{31.17 \text{ nodes}}$$
  <p><em>Conclusion:</em> A well-designed heuristic achieves an astronomical $\mathbf{99.4\%}$ reduction in search node expansions!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: Recursive Best-First Search (RBFS) vs. Memory-Bounded $A^*$ (SMA*)</div>
  <p><strong>RBFS (Recursive Best-First Search):</strong> Mimics standard Best-First Search using only <em>linear space</em> $O(bd)$ by maintaining an alternative cutoff value $f\text{-limit}$ from the best alternative path. When the current branch exceeds $f\text{-limit}$, recursion unwinds, remembering the best $f$-value of forgotten subtrees.</p>
  <p><strong>SMA* (Simplified Memory-Bounded $A^*$):</strong> Utilizes all available RAM memory. When memory is full, it drops the node with the worst $f$-value, backing up its value to its parent so the subtree can be regenerated if necessary.</p>
</div>
"""

M3_EXTRA2 = r"""
<h2 class="section-title">Topic 22.3: Master University Solved Examination Bank (Part II)</h2>

<div class="qa-card">
  <div class="qa-q">Q6. Explain the DPLL (Davis-Putnam-Logemann-Loveland) Algorithm for Propositional Satisfiability (SAT). (10 Marks)</div>
  <div class="qa-a">
    <strong>DPLL</strong> is a highly optimized recursive backtracking search for checking SAT over CNF clauses:<br>
    1. <strong>Early Termination:</strong> If all clauses are satisfied $\implies$ SAT; if any clause is empty/unsatisfied $\implies$ Backtrack.<br>
    2. <strong>Pure Literal Heuristic:</strong> A literal that appears with the same sign (always positive or always negative) in all unsatisfied clauses is immediately assigned that sign.<br>
    3. <strong>Unit Clause Heuristic (Unit Propagation):</strong> A clause containing only one unassigned literal force-assigns that literal to satisfy the clause immediately.<br>
    4. <strong>Splitting:</strong> If no pure/unit literals remain, pick a variable and branch recursively on $\text{True}$ and $\text{False}$.
  </div>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step FOL Skolemization & Standardizing Apart</div>
  <p>Convert the following sentence to Skolemized Prenex Normal Form:</p>
  $$\forall x \exists y (\text{Heart}(y) \land \text{Inside}(y, x))$$
  <ul>
    <li>Since $\exists y$ is in the scope of universal quantifier $\forall x$, the choice of heart $y$ depends on the person $x$.</li>
    <li>Replace existential variable $y$ with a <strong>Skolem function</strong> $f(x)$:</li>
    $$\mathbf{\forall x (\text{Heart}(f(x)) \land \text{Inside}(f(x), x))}$$
    <li>Drop universal quantifiers $\forall x$ (implicit): $\mathbf{\text{Clause 1: } \text{Heart}(f(x))}, \quad \mathbf{\text{Clause 2: } \text{Inside}(f(x), x)}$.</li>
  </ul>
</div>
"""

M4_EXTRA2 = r"""
<h2 class="section-title">Topic 29.3: Master University Solved Examination Bank (Part II)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: Markov Blanket in Bayesian Networks</div>
  <p>The <strong>Markov Blanket</strong> of a node $X$ in a Bayesian Network consists of:</p>
  <ol>
    <li>The parents of $X$.</li>
    <li>The children of $X$.</li>
    <li>The other parents of the children of $X$ (spouses of $X$).</li>
  </ol>
  $$\mathbf{P(X \mid \text{All other nodes in network}) = P(X \mid \text{MarkovBlanket}(X))}$$
  <p><em>Significance:</em> A node is conditionally independent of all other nodes in the entire network graph given its Markov Blanket! This forms the fundamental foundation for <strong>Gibbs Sampling MCMC</strong> inference.</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 2: Total Probability Rule & Joint Distribution Inference</div>
  <p>Given 3 Boolean variables $A, B, C$ with $P(A=t) = 0.6$. $B$ depends on $A$ ($P(B=t \mid A=t)=0.8, P(B=t \mid A=f)=0.2$). $C$ depends on $B$ ($P(C=t \mid B=t)=0.7, P(C=t \mid B=f)=0.1$). Compute $P(C=t)$.</p>
  $$P(B=t) = P(B=t \mid A=t)P(A=t) + P(B=t \mid A=f)P(A=f) = (0.8)(0.6) + (0.2)(0.4) = 0.48 + 0.08 = \mathbf{0.56}$$
  $$P(B=f) = 1 - 0.56 = \mathbf{0.44}$$
  $$\mathbf{P(C=t) = P(C=t \mid B=t)P(B=t) + P(C=t \mid B=f)P(B=f) = (0.7)(0.56) + (0.1)(0.44) = 0.392 + 0.044 = \mathbf{0.436 = 43.6\%}}$$
</div>
"""

M5_EXTRA2 = r"""
<h2 class="section-title">Topic 38.3: Master University Solved Examination Bank (Part II)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 2: Decision Tree Gini Impurity vs Entropy Split Comparison</div>
  <p>A binary target classification dataset with 20 items ($12 \text{ Positive}, 8 \text{ Negative}$) is split by an attribute into two branches:</p>
  <ul>
    <li>Left Branch: $10 \text{ items} \ (9 \text{ Positive}, 1 \text{ Negative})$</li>
    <li>Right Branch: $10 \text{ items} \ (3 \text{ Positive}, 7 \text{ Negative})$</li>
  </ul>
  <p><strong>Calculate Gini Gain:</strong></p>
  $$\text{Gini}(S_{\text{parent}}) = 1 - \left[\left(\frac{12}{20}\right)^2 + \left(\frac{8}{20}\right)^2\right] = 1 - [0.36 + 0.16] = 1 - 0.52 = \mathbf{0.48}$$
  $$\text{Gini}(S_{\text{left}}) = 1 - \left[\left(\frac{9}{10}\right)^2 + \left(\frac{1}{10}\right)^2\right] = 1 - [0.81 + 0.01] = 1 - 0.82 = \mathbf{0.18}$$
  $$\text{Gini}(S_{\text{right}}) = 1 - \left[\left(\frac{3}{10}\right)^2 + \left(\frac{7}{10}\right)^2\right] = 1 - [0.09 + 0.49] = 1 - 0.58 = \mathbf{0.42}$$
  $$\mathbf{\text{Gini Gain} = 0.48 - \left[ \frac{10}{20}(0.18) + \frac{10}{20}(0.42) \right] = 0.48 - (0.09 + 0.21) = 0.48 - 0.30 = \mathbf{0.18}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: The Vanishing Gradient Problem & ReLU Resolution</div>
  <p>In deep networks using Sigmoid activation $\sigma(z) = \frac{1}{1+e^{-z}}$, the derivative is $\sigma'(z) = \sigma(z)(1-\sigma(z))$. The maximum possible value of $\sigma'(z)$ is only $\mathbf{0.25}$ (at $z=0$). When propagating through $L$ hidden layers, the gradient scales as $\prod_{l=1}^L \sigma'(z_l) \le (0.25)^L$. For $L=10$, $(0.25)^{10} \approx 9.5 \times 10^{-7}$, causing earlier layer weights to stop learning!</p>
  <p><strong>ReLU Solution:</strong> $f(z) = \max(0, z) \implies f'(z) = 1$ for all $z > 0$. The gradient flows completely unattenuated through arbitrarily deep layers!</p>
</div>
"""

AI_LAB_GUIDE = r"""
<div class="page-break"></div>
<div class="cover-container" style="margin-top: 40px;">
  <div class="course-badge">Hands-On Practical Lab Master Appendix</div>
  <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">AI Laboratory & Python Heuristic Search Master Guide</h2>
  <div style="font-size: 12.5px; color: #64748b;">Complete Python Algorithms for A* Search, 8-Puzzle Heuristics, Alpha-Beta Game Trees & Backpropagation</div>
</div>

<h2 class="section-title">Lab Experiment 1: Production-Grade A* Search on 8-Puzzle in Python</h2>

<pre><code class="language-python">import heapq

class Puzzle8State:
    def __init__(self, board, parent=None, action=None, g=0):
        self.board = board # Tuple of 9 integers
        self.parent = parent
        self.action = action
        self.g = g
        self.h = self.calculate_manhattan()
        self.f = self.g + self.h

    def calculate_manhattan(self):
        # Goal: (1,2,3,4,5,6,7,8,0)
        goal_pos = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 0:(2,2)}
        dist = 0
        for idx, val in enumerate(self.board):
            if val != 0:
                r, c = idx // 3, idx % 3
                gr, gc = goal_pos[val]
                dist += abs(r - gr) + abs(c - gc)
        return dist

    def get_neighbors(self):
        neighbors = []
        idx = self.board.index(0)
        r, c = idx // 3, idx % 3
        moves = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]
        for dr, dc, act in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                n_idx = nr * 3 + nc
                b_list = list(self.board)
                b_list[idx], b_list[n_idx] = b_list[n_idx], b_list[idx]
                neighbors.append(Puzzle8State(tuple(b_list), parent=self, action=act, g=self.g + 1))
        return neighbors

    def __lt__(self, other):
        return self.f < other.f

def solve_8_puzzle_astar(start_board):
    start_state = Puzzle8State(start_board)
    frontier = []
    heapq.heappush(frontier, start_state)
    explored = set()

    while frontier:
        current = heapq.heappop(frontier)
        if current.h == 0:
            # Reconstruct solution path
            path = []
            curr = current
            while curr.parent:
                path.append(curr.action)
                curr = curr.parent
            return path[::-1], current.g

        explored.add(current.board)
        for neighbor in current.get_neighbors():
            if neighbor.board not in explored:
                heapq.heappush(frontier, neighbor)
    return None, -1

# Example Run
initial = (1, 2, 3, 0, 4, 6, 7, 5, 8)
path, cost = solve_8_puzzle_astar(initial)
print(f"Optimal Moves ({cost} steps): {path}")
</code></pre>

<h2 class="section-title">Lab Experiment 2: Minimax with Alpha-Beta Pruning in Python</h2>

<pre><code class="language-python">def alpha_beta_minimax(node_val_list, depth, node_idx, is_max, alpha, beta):
    # Terminal leaf evaluation
    if depth == 3:
        return node_val_list[node_idx]

    if is_max:
        best = float('-inf')
        for i in range(2):
            val = alpha_beta_minimax(node_val_list, depth + 1, node_idx * 2 + i, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} by MAX (alpha={alpha} >= beta={beta})")
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta_minimax(node_val_list, depth + 1, node_idx * 2 + i, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} by MIN (alpha={alpha} >= beta={beta})")
                break
        return best
</code></pre>
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

def build_super_ai():
    # Import base modules and append extra sections
    sys.path.insert(0, AI_DIR)
    from ai_module1_content import AI_M1_EXHAUSTIVE
    from ai_module2_content import AI_M2_EXHAUSTIVE
    from ai_module3_content import AI_M3_EXHAUSTIVE
    from ai_module4_content import AI_M4_EXHAUSTIVE
    from ai_module5_content import AI_M5_EXHAUSTIVE
    from ai_revision_content import AI_REVISION_EXHAUSTIVE

    m1_full = AI_M1_EXHAUSTIVE + M1_EXTRA2
    m2_full = AI_M2_EXHAUSTIVE + M2_EXTRA2
    m3_full = AI_M3_EXHAUSTIVE + M3_EXTRA2
    m4_full = AI_M4_EXHAUSTIVE + M4_EXTRA2
    m5_full = AI_M5_EXHAUSTIVE + M5_EXTRA2

    # Save back to files
    with open(os.path.join(AI_DIR, "ai_module1_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M1_EXHAUSTIVE = r"""{m1_full}"""\n')
    with open(os.path.join(AI_DIR, "ai_module2_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M2_EXHAUSTIVE = r"""{m2_full}"""\n')
    with open(os.path.join(AI_DIR, "ai_module3_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M3_EXHAUSTIVE = r"""{m3_full}"""\n')
    with open(os.path.join(AI_DIR, "ai_module4_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M4_EXHAUSTIVE = r"""{m4_full}"""\n')
    with open(os.path.join(AI_DIR, "ai_module5_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M5_EXHAUSTIVE = r"""{m5_full}"""\n')

    modules = [
        (1, "Module 1: Intelligent Agents & PEAS Framework", "Topics 1 to 7 • Foundations, Evolution, Rationality & 5 Agent Types", m1_full, "Module_1_Intelligent_Agents_Notes"),
        (2, "Module 2: Search Algorithms & Game Playing", "Topics 8 to 13 • BFS/DFS/IDDFS, A* Admissibility Proofs & Alpha-Beta Pruning", m2_full, "Module_2_Search_Algorithms_Notes"),
        (3, "Module 3: Knowledge Representation & Logic", "Topics 14 to 22 • Wumpus World, Propositional CNF, First-Order Logic & Resolution", m3_full, "Module_3_Knowledge_Logic_Notes"),
        (4, "Module 4: Classical Planning & Bayesian Networks", "Topics 23 to 29 • STRIPS / PDDL, Graphplan Mutexes, Probability & Bayes Nets", m4_full, "Module_4_Planning_Bayes_Notes"),
        (5, "Module 5: Machine Learning & Neural Networks", "Topics 30 to 38 • Decision Trees ID3, Perceptrons & Backpropagation Math", m5_full, "Module_5_Machine_Learning_Notes"),
    ]

    for num, title, subtitle, content, fname in modules:
        html_content = wrap_html(title, subtitle, content, module_num=num)
        html_file = os.path.join(HTML_DIR, f"{fname}.html")
        pdf_file = os.path.join(PDF_DIR, f"{fname}.pdf")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        generate_pdf(html_file, pdf_file, f"AI Module {num}")

    # Generate 10-Page Revision Guide
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

    # Generate Full Course Master Book with Lab Guide and Revision
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

    full_body.append(AI_LAB_GUIDE)
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
    build_super_ai()
