#!/usr/bin/env python3
"""
Pushes AI Module 4 to 10 pages.
"""
import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

sys.path.insert(0, AI_DIR)
from ai_module4_content import AI_M4_EXHAUSTIVE

EXTRA = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Policy Iteration Dynamic Programming Trace on 3-State Chain</div>
  <p>Consider a 3-state chain MDP with states $\{S_1, S_2, S_3\}$, actions $\{\text{Left}, \text{Right}\}$, discount $\gamma = 0.8$, and terminal absorbing state $S_3$ with reward $R(S_3) = +10$. Other step rewards are $0$.</p>
  <p><strong>1. Initial Policy $\pi_0$:</strong> Always choose $\text{Right}$ ($\pi_0(S_1) = \text{Right}, \pi_0(S_2) = \text{Right}$).</p>
  <p><strong>2. Policy Evaluation:</strong> Solve linear system $U^{\pi_0}(s) = R(s) + \gamma \sum_{s'} P(s' \mid s, \pi_0(s)) U^{\pi_0}(s')$:</p>
  $$U(S_2) = 0 + 0.8 U(S_3) = 0.8(10) = \mathbf{8.0}$$
  $$U(S_1) = 0 + 0.8 U(S_2) = 0.8(8.0) = \mathbf{6.4}$$
  <p><strong>3. Policy Improvement:</strong> Calculate $Q(s, a)$ for alternative action $\text{Left}$:</p>
  $$Q(S_1, \text{Left}) = 0 + 0.8 U(S_1) = 0.8(6.4) = 5.12 < 6.4 \implies \text{Keep Right}$$
  $$Q(S_2, \text{Left}) = 0 + 0.8 U(S_1) = 0.8(6.4) = 5.12 < 8.0 \implies \text{Keep Right}$$
  $$\mathbf{\text{Policy Converged: } \pi^*(S_1) = \text{Right}, \ \pi^*(S_2) = \text{Right} \quad (\text{Optimal Policy Identified in 1 Iteration!})}$$
</div>
"""

m4_total = AI_M4_EXHAUSTIVE + EXTRA
with open(os.path.join(AI_DIR, "ai_module4_content.py"), "w", encoding="utf-8") as f:
    f.write(f'AI_M4_EXHAUSTIVE = r"""{m4_total}"""\n')

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from finalize_ai_10_pages_exact import wrap_html, generate_pdf, LAB_GUIDE_INLINE, AI_M1_EXHAUSTIVE, AI_M2_EXHAUSTIVE, AI_M3_EXHAUSTIVE, AI_M5_EXHAUSTIVE, AI_REVISION_EXHAUSTIVE

html_content = wrap_html("Module 4: Classical Planning & Bayesian Networks", "Topics 23 to 29 • STRIPS / PDDL, Graphplan Mutexes, Probability & Bayes Nets", m4_total, module_num=4)
html_file = os.path.join(HTML_DIR, "Module_4_Planning_Bayes_Notes.html")
pdf_file = os.path.join(PDF_DIR, "Module_4_Planning_Bayes_Notes.pdf")
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)
generate_pdf(html_file, pdf_file, "AI Module 4")

# Re-render Full Master Book
modules = [
    (1, "Module 1: Intelligent Agents & PEAS Framework", "Topics 1 to 7 • Foundations, Evolution, Rationality & 5 Agent Types", AI_M1_EXHAUSTIVE, "Module_1_Intelligent_Agents_Notes"),
    (2, "Module 2: Search Algorithms & Game Playing", "Topics 8 to 13 • BFS/DFS/IDDFS, A* Admissibility Proofs & Alpha-Beta Pruning", AI_M2_EXHAUSTIVE, "Module_2_Search_Algorithms_Notes"),
    (3, "Module 3: Knowledge Representation & Logic", "Topics 14 to 22 • Wumpus World, Propositional CNF, First-Order Logic & Resolution", AI_M3_EXHAUSTIVE, "Module_3_Knowledge_Logic_Notes"),
    (4, "Module 4: Classical Planning & Bayesian Networks", "Topics 23 to 29 • STRIPS / PDDL, Graphplan Mutexes, Probability & Bayes Nets", m4_total, "Module_4_Planning_Bayes_Notes"),
    (5, "Module 5: Machine Learning & Neural Networks", "Topics 30 to 38 • Decision Trees ID3, Perceptrons & Backpropagation Math", AI_M5_EXHAUSTIVE, "Module_5_Machine_Learning_Notes"),
]

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
