#!/usr/bin/env python3
"""
Final Boost for AI Modules 3, 4, 5 to make EVERY module 10-12 pages,
and AI_Full_Course_Master.pdf 55+ pages!
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

sys.path.insert(0, AI_DIR)
from ai_module1_content import AI_M1_EXHAUSTIVE
from ai_module2_content import AI_M2_EXHAUSTIVE
from ai_module3_content import AI_M3_EXHAUSTIVE
from ai_module4_content import AI_M4_EXHAUSTIVE
from ai_module5_content import AI_M5_EXHAUSTIVE
from ai_revision_content import AI_REVISION_EXHAUSTIVE

M3_EXTRA_PAGES = r"""
<h2 class="section-title">Topic 22.9: Modal Logic, Epistemic Reasoning & Dempster-Shafer Theory</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Formal Logic System</th>
      <th style="width: 35%;">Modal Operators & Axioms</th>
      <th>AI Multi-Agent Application</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Epistemic Logic ($S5$)</strong></td>
      <td>Knowledge operator $K_i \phi$ ("Agent $i$ knows $\phi$"). Axioms: $K_i \phi \rightarrow \phi$ (Truth), $K_i \phi \rightarrow K_i K_i \phi$ (Positive Introspection), $\neg K_i \phi \rightarrow K_i \neg K_i \phi$ (Negative Introspection).</td>
      <td>Distributed systems consensus, multi-agent common knowledge ($C \phi$), Muddy Children puzzle.</td>
    </tr>
    <tr>
      <td><strong>Temporal Logic (LTL / CTL)</strong></td>
      <td>LTL operators: $\mathbf{G}\phi$ (Always), $\mathbf{F}\phi$ (Eventually), $\mathbf{X}\phi$ (Next), $\phi \mathbf{U} \psi$ (Until). CTL adds path quantifiers $\mathbf{A}$ (All paths), $\mathbf{E}$ (Exists path).</td>
      <td>Model checking automated safety verification of autonomous flight control and medical robotics software.</td>
    </tr>
    <tr>
      <td><strong>Dempster-Shafer Theory of Evidence</strong></td>
      <td>Mass function $m(A) \in [0, 1]$ over power set $2^\Theta$. Belief function $\text{Bel}(A) = \sum_{B \subseteq A} m(B)$, Plausibility $\text{Pl}(A) = 1 - \text{Bel}(\neg A)$. Dempster's Rule of Combination: $m_1 \oplus m_2(A) = \frac{\sum_{B \cap C = A} m_1(B) m_2(C)}{1 - K}$.</td>
      <td>Sensor fusion with epistemic ignorance (distinguishes total ignorance from equal probability!).</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Dempster's Rule of Combination in Sensor Fusion</div>
  <p>Two medical sensors diagnose a patient for three mutually exclusive conditions $\Theta = \{\text{Flu } (F), \text{Cold } (C), \text{Pneumonia } (P)\}$:</p>
  <ul>
    <li>Sensor 1: $m_1(\{F\}) = 0.6, \ m_1(\Theta) = 0.4$.</li>
    <li>Sensor 2: $m_2(\{F, C\}) = 0.7, \ m_2(\Theta) = 0.3$.</li>
  </ul>
  <p><strong>Dempster Combination Matrix:</strong></p>
  <table class="custom-table">
    <thead><tr><th>$m_1 \backslash m_2$</th><th>$m_2(\{F, C\}) = 0.7$</th><th>$m_2(\Theta) = 0.3$</th></tr></thead>
    <tbody>
      <tr><td><strong>$m_1(\{F\}) = 0.6$</strong></td><td>$\{F\} \cap \{F, C\} = \{F\} \implies 0.42$</td><td>$\{F\} \cap \Theta = \{F\} \implies 0.18$</td></tr>
      <tr><td><strong>$m_1(\Theta) = 0.4$</strong></td><td>$\Theta \cap \{F, C\} = \{F, C\} \implies 0.28$</td><td>$\Theta \cap \Theta = \Theta \implies 0.12$</td></tr>
    </tbody>
  </table>
  <p>No empty set intersections ($K = 0$). Combined masses:</p>
  $$\mathbf{m_{1,2}(\{F\}) = 0.42 + 0.18 = \mathbf{0.60} \qquad m_{1,2}(\{F, C\}) = \mathbf{0.28} \qquad m_{1,2}(\Theta) = \mathbf{0.12}}$$
  $$\mathbf{\text{Belief in Flu: } \text{Bel}(\{F\}) = m_{1,2}(\{F\}) = \mathbf{0.60} \qquad \text{Plausibility of Flu: } \text{Pl}(\{F\}) = 0.60 + 0.28 + 0.12 = \mathbf{1.00}}}$$
</div>

<div class="qa-card">
  <div class="qa-q">Q17. Explain the Resolution Refutation Proof with Equality (Paramodulation and Demodulation). (8 Marks)</div>
  <div class="qa-a">
    Standard resolution handles predicate symbols but cannot natively reason about equality axioms ($x = x, x = y \rightarrow y = x, x = y \land y = z \rightarrow x = z$).<br>
    • <strong>Paramodulation:</strong> A specialized inference rule that incorporates equality: From clause $(l = r \lor C)$ and clause $(P(t) \lor D)$, where a subterm of $t$ unifies with $l$ under $\theta = \text{UNIFY}(t|_p, l)$, infer $(P(t[r\theta]_p) \lor C\theta \lor D\theta)$.<br>
    • <strong>Demodulation:</strong> A deterministic rewriting rule that uses unit equality clauses $l = r$ to simplify terms in other clauses to a canonical normal form, preventing exponential branching in equational theorem provers like Otter and Vampire!
  </div>
</div>
"""

M4_EXTRA_PAGES = r"""
<h2 class="section-title">Topic 29.9: Complete Partial-Order Planning (POP) Algorithm & Flaw Repair</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Partial-Order Planning (POP) Algorithm Walkthrough</div>
  <p>Consider the classic <strong>"Put on Shoes and Socks"</strong> planning domain:</p>
  <ul>
    <li>Actions: $\text{RightSock}, \text{RightShoe}, \text{LeftSock}, \text{LeftShoe}$.</li>
    <li>Preconditions & Effects:
      <ul>
        <li>$\text{RightShoe}$: Precondition $\text{RightSockOn}$; Effect $\text{RightShoeOn}$.</li>
        <li>$\text{LeftShoe}$: Precondition $\text{LeftSockOn}$; Effect $\text{LeftShoeOn}$.</li>
      </ul>
    </li>
    <li>Goal: $\text{RightShoeOn} \land \text{LeftShoeOn}$.</li>
  </ul>
  <p><strong>POP Execution Steps:</strong></p>
  <ol>
    <li>Start with initial dummy plan: $\text{Start} \prec \text{Finish}$. Open preconditions: $\text{RightShoeOn}, \text{LeftShoeOn}$.</li>
    <li>Achieve $\text{RightShoeOn}$ by adding step $\text{RightShoe}$ with causal link $\text{RightShoe} \xrightarrow{\text{RightShoeOn}} \text{Finish}$.</li>
    <li>Achieve $\text{LeftShoeOn}$ by adding step $\text{LeftShoe}$ with causal link $\text{LeftShoe} \xrightarrow{\text{LeftShoeOn}} \text{Finish}$.</li>
    <li>Resolve open precondition $\text{RightSockOn}$ of $\text{RightShoe}$ by adding $\text{RightSock}$ with causal link $\text{RightSock} \xrightarrow{\text{RightSockOn}} \text{RightShoe}$.</li>
    <li>Resolve open precondition $\text{LeftSockOn}$ of $\text{LeftShoe}$ by adding $\text{LeftSock}$ with causal link $\text{LeftSock} \xrightarrow{\text{LeftSockOn}} \text{LeftShoe}$.</li>
    <li><strong>Threat Checking:</strong> No action deletes any established causal link ($\text{Threats} = \emptyset$).</li>
  </ol>
  $$\mathbf{\text{Final Partial Order Plan: } (\text{RightSock} \prec \text{RightShoe}) \land (\text{LeftSock} \prec \text{LeftShoe})}$$
  <p><em>Power of POP:</em> The left-foot and right-foot operations remain completely unordered with respect to each other, allowing parallel execution on a dual-arm robot!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Step-by-Step MCMC Gibbs Sampling Trace on Bayesian Networks</div>
  <p>Given 3 variables $C$ (Cloudy), $R$ (Rain), $W$ (WetGrass) with query $P(C \mid W=\text{true})$:</p>
  <ul>
    <li>Evidence: $W = \text{true}$. Hidden non-evidence variables: $C, R$.</li>
    <li><strong>Step 0:</strong> Randomly initialize hidden variables: $C_0 = \text{true}, \ R_0 = \text{false}$. State = $(\text{true}, \text{false}, \text{true})$.</li>
    <li><strong>Iteration 1 (Sample $C$):</strong> Compute $P(C \mid R=\text{false}, W=\text{true}) = \alpha P(C) P(R=\text{false} \mid C) P(W=\text{true} \mid C, R=\text{false})$. Suppose distribution evaluates to $[0.35, 0.65]$. Sample random $u = 0.42 > 0.35 \implies C_1 = \mathbf{\text{false}}$.</li>
    <li><strong>Iteration 2 (Sample $R$):</strong> Compute $P(R \mid C=\text{false}, W=\text{true})$. Suppose evaluates to $[0.82, 0.18]$. Sample random $u = 0.10 < 0.82 \implies R_1 = \mathbf{\text{true}}$.</li>
    <li><strong>Iteration 3 to $N$:</strong> Repeat sampling. Tally the number of iterations where $C = \text{true}$ versus $C = \text{false}$ to compute the empirical posterior probability!</li>
  </ul>
</div>
"""

M5_EXTRA_PAGES = r"""
<h2 class="section-title">Topic 38.9: Advanced Statistical Machine Learning & KKT Support Vector Bounds</h2>

<div class="formula-card">
  <strong>The Karush-Kuhn-Tucker (KKT) Optimality Conditions for Soft-Margin SVM:</strong>
  For primal objective $\min_{\mathbf{w}, b, \mathbf{\xi}} \frac{1}{2}\|\mathbf{w}\|^2 + C \sum_{i=1}^N \xi_i$ with constraints $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \ \xi_i \ge 0$:
  1. <strong>Stationarity:</strong> $\mathbf{w} = \sum_{i=1}^N \alpha_i y_i \mathbf{x}_i, \quad \sum_{i=1}^N \alpha_i y_i = 0, \quad C - \alpha_i - \mu_i = 0$.<br>
  2. <strong>Primal Feasibility:</strong> $y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1 + \xi_i \ge 0, \quad \xi_i \ge 0$.<br>
  3. <strong>Dual Feasibility:</strong> $0 \le \alpha_i \le C, \quad \mu_i \ge 0$.<br>
  4. <strong>Complementary Slackness:</strong> $\alpha_i [y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1 + \xi_i] = 0 \quad \text{and} \quad \mu_i \xi_i = (C - \alpha_i)\xi_i = 0$.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Support Vector Classification Case Analysis</div>
  <p>From KKT Complementary Slackness, data points fall into three mathematically distinct regimes based on $\alpha_i$:</p>
  <ul>
    <li><strong>Case 1 ($\alpha_i = 0$):</strong> Point is strictly on the correct side of the margin ($y_i(\mathbf{w}^T \mathbf{x}_i + b) > 1, \xi_i = 0$). It has zero influence on the decision boundary!</li>
    <li><strong>Case 2 ($0 < \alpha_i < C$):</strong> Point is a <strong>Free Support Vector</strong> lying exactly on the margin ($y_i(\mathbf{w}^T \mathbf{x}_i + b) = 1, \xi_i = 0$). These points determine the exact location of the hyperplane bias $b$!</li>
    <li><strong>Case 3 ($\alpha_i = C$):</strong> Point is a <strong>Bounded Support Vector</strong> violating the margin ($\xi_i > 0$). It lies inside the margin band or is misclassified.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Deep Multilayer Perceptron Matrix Form</div>
  <p>Consider a 3-layer neural network with layer dimensions $d_0 \rightarrow d_1 \rightarrow d_2 \rightarrow d_3$:</p>
  $$\mathbf{a^{(0)} = \mathbf{x} \in \mathbb{R}^{d_0}}$$
  $$\mathbf{z^{(1)} = \mathbf{W}^{(1)} \mathbf{a}^{(0)} + \mathbf{b}^{(1)} \in \mathbb{R}^{d_1}, \quad \mathbf{a}^{(1)} = \sigma(\mathbf{z}^{(1)})}$$
  $$\mathbf{z^{(2)} = \mathbf{W}^{(2)} \mathbf{a}^{(1)} + \mathbf{b}^{(2)} \in \mathbb{R}^{d_2}, \quad \mathbf{a}^{(2)} = \sigma(\mathbf{z}^{(2)})}$$
  $$\mathbf{z^{(3)} = \mathbf{W}^{(3)} \mathbf{a}^{(2)} + \mathbf{b}^{(3)} \in \mathbb{R}^{d_3}, \quad \hat{\mathbf{y}} = \text{softmax}(\mathbf{z}^{(3)})}$$
  <p>Cross-Entropy Loss with Softmax Output has the remarkably clean gradient:</p>
  $$\mathbf{\delta^{(3)} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(3)}} = \hat{\mathbf{y}} - \mathbf{y}}$$
  $$\mathbf{\delta^{(2)} = (\mathbf{W}^{(3)})^T \delta^{(3)} \odot \sigma'(\mathbf{z}^{(2)}) \qquad \frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(2)}} = \delta^{(2)} (\mathbf{a}^{(1)})^T}$$
</div>
"""

def boost_and_build():
    m1_final = AI_M1_EXHAUSTIVE
    m2_final = AI_M2_EXHAUSTIVE
    m3_final = AI_M3_EXHAUSTIVE + M3_EXTRA_PAGES
    m4_final = AI_M4_EXHAUSTIVE + M4_EXTRA_PAGES
    m5_final = AI_M5_EXHAUSTIVE + M5_EXTRA_PAGES

    # Save to files
    with open(os.path.join(AI_DIR, "ai_module3_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M3_EXHAUSTIVE = r"""{m3_final}"""\n')
    with open(os.path.join(AI_DIR, "ai_module4_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M4_EXHAUSTIVE = r"""{m4_final}"""\n')
    with open(os.path.join(AI_DIR, "ai_module5_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M5_EXHAUSTIVE = r"""{m5_final}"""\n')

    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
    from finalize_ai_10_pages_exact import wrap_html, generate_pdf, LAB_GUIDE_INLINE

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
    boost_and_build()
