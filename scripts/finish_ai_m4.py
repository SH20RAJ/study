#!/usr/bin/env python3
"""
Final push for AI Module 4 to make it 10 pages and make the Master Book 55 pages!
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

sys.path.insert(0, AI_DIR)
from ai_module4_content import AI_M4_EXHAUSTIVE

M4_FINAL_TOUCH = r"""
<h2 class="section-title">Topic 29.11: Formal Decision Theory, Axioms of Utility & Influence Diagrams</h2>

<p>
  <strong>Decision Theory</strong> unifies probability theory with utility theory: $\text{Decision Theory} = \text{Probability Theory} + \text{Utility Theory}$. An agent represents preferences between lotteries using scalar utility functions.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Axiom of Rationality (Von Neumann-Morgenstern)</th>
      <th style="width: 45%;">Mathematical Formulation</th>
      <th>Implication for Rational Agents</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Orderability (Completeness)</strong></td>
      <td>$(A \succ B) \lor (B \succ A) \lor (A \sim B)$</td>
      <td>An agent cannot avoid making a choice between any two states or lotteries.</td>
    </tr>
    <tr>
      <td><strong>Transitivity</strong></td>
      <td>$(A \succ B) \land (B \succ C) \implies (A \succ C)$</td>
      <td>Prevents cyclical preferences (intransitive agents become "money pumps" exploited by opponents).</td>
    </tr>
    <tr>
      <td><strong>Continuity</strong></td>
      <td>$A \succ B \succ C \implies \exists p \in [0, 1] \text{ s.t. } [p, A; (1-p), C] \sim B$</td>
      <td>There is always a lottery between best and worst outcomes equivalent to an intermediate outcome.</td>
    </tr>
    <tr>
      <td><strong>Substitutability (Independence)</strong></td>
      <td>$A \sim B \implies [p, A; (1-p), C] \sim [p, B; (1-p), C]$</td>
      <td>Indifference between two outcomes is preserved when embedded in larger compound lotteries.</td>
    </tr>
    <tr>
      <td><strong>Monotonicity</strong></td>
      <td>$A \succ B \land (p > q) \implies [p, A; (1-p), B] \succ [q, A; (1-q), B]$</td>
      <td>Agents strictly prefer lotteries with higher probabilities of receiving the more desirable prize.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Influence Diagram Evaluation Algorithm</div>
  <p>An <strong>Influence Diagram (Decision Network)</strong> augments Bayesian Networks with <em>Decision Nodes</em> (rectangles) and <em>Utility Nodes</em> (diamonds):</p>
  <ol>
    <li><strong>Evaluation Algorithm:</strong>
      <ul>
        <li>For each possible assignment to the decision node $D = d_i$:</li>
        <li>Set evidence $D = d_i$ in the network.</li>
        <li>Calculate posterior probabilities $P(X \mid d_i)$ for parents $X$ of the utility node $U$ using Variable Elimination.</li>
        <li>Compute expected utility: $\mathbb{E}[U \mid d_i] = \sum_x P(X=x \mid d_i) U(x, d_i)$.</li>
      </ul>
    </li>
    <li><strong>Optimal Policy:</strong> Choose action $d^* = \arg\max_{d_i} \mathbb{E}[U \mid d_i]$!</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ The St. Petersburg Paradox & Risk Neutrality vs. Risk Aversion</div>
  <p>A fair coin is tossed until heads appears on flip $n$. The player receives prize $\$2^n$. What is the fair price to play?</p>
  <ul>
    <li><strong>Expected Monetary Value (EMV):</strong> $\mathbb{E}[\text{Money}] = \sum_{n=1}^\infty \left(\frac{1}{2}\right)^n (2^n) = \sum_{n=1}^\infty 1 = \mathbf{1 + 1 + 1 + \dots = \infty}$.</li>
    <li>Yet real humans will only pay $\sim \$10$ to $\$25$ to play this game!</li>
    <li><strong>Bernoulli's Resolution (1738):</strong> Humans maximize <em>Expected Utility</em> $U(w) = \ln(w)$ (concave logarithmic utility function), NOT raw monetary payout!</li>
    $$\mathbb{E}[U] = \sum_{n=1}^\infty \left(\frac{1}{2}\right)^n \ln(2^n) = \ln(2) \sum_{n=1}^\infty \frac{n}{2^n} = \ln(2) \times 2 = \mathbf{2 \ln(2) \approx 1.386 \text{ utils}}$$
    $$U^{-1}(1.386) = e^{1.386} = \mathbf{\$4.00 \text{ (Certainty Equivalent)}}$$
  </ul>
</div>
"""

def finish_m4():
    m4_final = AI_M4_EXHAUSTIVE + M4_FINAL_TOUCH
    with open(os.path.join(AI_DIR, "ai_module4_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M4_EXHAUSTIVE = r"""{m4_final}"""\n')

    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
    from finalize_ai_10_pages_exact import wrap_html, generate_pdf, LAB_GUIDE_INLINE, AI_M1_EXHAUSTIVE, AI_M2_EXHAUSTIVE, AI_M3_EXHAUSTIVE, AI_M5_EXHAUSTIVE, AI_REVISION_EXHAUSTIVE

    modules = [
        (1, "Module 1: Intelligent Agents & PEAS Framework", "Topics 1 to 7 • Foundations, Evolution, Rationality & 5 Agent Types", AI_M1_EXHAUSTIVE, "Module_1_Intelligent_Agents_Notes"),
        (2, "Module 2: Search Algorithms & Game Playing", "Topics 8 to 13 • BFS/DFS/IDDFS, A* Admissibility Proofs & Alpha-Beta Pruning", AI_M2_EXHAUSTIVE, "Module_2_Search_Algorithms_Notes"),
        (3, "Module 3: Knowledge Representation & Logic", "Topics 14 to 22 • Wumpus World, Propositional CNF, First-Order Logic & Resolution", AI_M3_EXHAUSTIVE, "Module_3_Knowledge_Logic_Notes"),
        (4, "Module 4: Classical Planning & Bayesian Networks", "Topics 23 to 29 • STRIPS / PDDL, Graphplan Mutexes, Probability & Bayes Nets", m4_final, "Module_4_Planning_Bayes_Notes"),
        (5, "Module 5: Machine Learning & Neural Networks", "Topics 30 to 38 • Decision Trees ID3, Perceptrons & Backpropagation Math", AI_M5_EXHAUSTIVE, "Module_5_Machine_Learning_Notes"),
    ]

    html_content = wrap_html("Module 4: Classical Planning & Bayesian Networks", "Topics 23 to 29 • STRIPS / PDDL, Graphplan Mutexes, Probability & Bayes Nets", m4_final, module_num=4)
    html_file = os.path.join(HTML_DIR, "Module_4_Planning_Bayes_Notes.html")
    pdf_file = os.path.join(PDF_DIR, "Module_4_Planning_Bayes_Notes.pdf")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    generate_pdf(html_file, pdf_file, "AI Module 4")

    # Full Master Book
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

    full_body.append(LAB_GUIDE_INLINE)
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
    finish_m4()
