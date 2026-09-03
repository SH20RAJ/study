#!/usr/bin/env python3
"""
Precision booster for AI Modules 3, 4, 5 to ensure 10 pages each.
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

sys.path.insert(0, AI_DIR)
from ai_module3_content import AI_M3_EXHAUSTIVE
from ai_module4_content import AI_M4_EXHAUSTIVE
from ai_module5_content import AI_M5_EXHAUSTIVE

M3_BOOST_FINAL = r"""
<h2 class="section-title">Topic 22.10: Master University Exam Proof Bank (Part IV)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Proof: First-Order Unification with Multiple Variable Bindings</div>
  <p>Find the Most General Unifier (MGU) $\theta$ for the following predicate expressions or show why unification fails:</p>
  <ol>
    <li>$P(x, g(x), y)$ and $P(f(z), g(f(z)), h(w)) \implies \mathbf{\theta = \{ x / f(z), y / h(w) \}}$.</li>
    <li>$Q(a, x, f(g(y)))$ and $Q(z, f(z), f(u)) \implies z/a, x/f(a), u/g(y) \implies \mathbf{\theta = \{ z/a, x/f(a), u/g(y) \}}$.</li>
    <li>$R(x, x)$ and $R(y, f(y)) \implies \mathbf{\text{Occur-check failure: } y \text{ cannot unify with } f(y)}$!</li>
  </ol>
</div>

<div class="qa-card">
  <div class="qa-q">Q18. Explain Automated Theorem Proving with Binary Decision Diagrams (BDDs) and Reduced Ordered BDDs (ROBDDs). (8 Marks)</div>
  <div class="qa-a">
    A <strong>Binary Decision Diagram (BDD)</strong> is a rooted, directed acyclic graph representing a Boolean function $f(x_1, \dots, x_n)$ where non-terminal nodes represent variables and outgoing dashed/solid edges represent $0$ and $1$ assignments.<br>
    <strong>ROBDD Canonical Property (Bryant 1986):</strong> For a fixed variable ordering, every Boolean function has a <em>strictly unique, canonical</em> ROBDD representation. Checking whether a formula is a tautology ($f \equiv 1$) or unsatisfiable ($f \equiv 0$) takes $O(1)$ time! Equivalence checking between two logic circuits $f \equiv g$ reduces to graph isomorphism!
  </div>
</div>
"""

M4_BOOST_FINAL = r"""
<h2 class="section-title">Topic 29.10: Master University Exam Problem Bank (Part IV)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 4: Exact Inference by Enumeration in 5-Node Bayesian Network</div>
  <p>Given DAG $A \rightarrow B \rightarrow C$, with conditional probability tables:</p>
  <ul>
    <li>$P(A=t) = 0.3$.</li>
    <li>$P(B=t \mid A=t) = 0.9, \ P(B=t \mid A=f) = 0.1$.</li>
    <li>$P(C=t \mid B=t) = 0.8, \ P(C=t \mid B=f) = 0.2$.</li>
  </ul>
  <p><strong>Query: Compute posterior probability $P(A=t \mid C=t)$:</strong></p>
  $$P(A=t, C=t) = P(A=t) \sum_b P(b \mid A=t) P(C=t \mid b) = 0.3 [ (0.9)(0.8) + (0.1)(0.2) ] = 0.3 [ 0.72 + 0.02 ] = 0.3(0.74) = \mathbf{0.222}$$
  $$P(A=f, C=t) = P(A=f) \sum_b P(b \mid A=f) P(C=t \mid b) = 0.7 [ (0.1)(0.8) + (0.9)(0.2) ] = 0.7 [ 0.08 + 0.18 ] = 0.7(0.26) = \mathbf{0.182}$$
  $$\mathbf{P(A=t \mid C=t) = \frac{0.222}{0.222 + 0.182} = \frac{0.222}{0.404} = \mathbf{0.5495 = \mathbf{54.95\%}}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: STRIPS Tire Changing Domain</div>
  <pre><code>Init(Tire(Flat) ∧ Tire(Spare) ∧ At(Flat, Axle) ∧ At(Spare, Trunk))
Goal(At(Spare, Axle) ∧ At(Flat, Trunk))

Action(Remove(t, loc),
  PRECOND: At(t, loc)
  EFFECT:  ¬At(t, loc) ∧ Holding(t))

Action(PutOn(t, Axle),
  PRECOND: Holding(t) ∧ ¬At(Flat, Axle) ∧ ¬At(Spare, Axle)
  EFFECT:  At(t, Axle) ∧ ¬Holding(t))

Action(PutIn(t, Trunk),
  PRECOND: Holding(t)
  EFFECT:  At(t, Trunk) ∧ ¬Holding(t))</code></pre>
</div>

<div class="qa-card">
  <div class="qa-q">Q14. Explain Real-Time Heuristic Search (RTA* and LRTA*). (8 Marks)</div>
  <div class="qa-a">
    In dynamic physical environments where planning time is strictly bounded, <strong>Learning Real-Time $A^*$ (LRTA*)</strong> executes action moves within fixed time bounds by searching forward only a few steps, evaluating leaf nodes with heuristic $h(n)$, choosing the best immediate action, and updating its heuristic table at the visited state $s$: $\mathbf{h(s) \leftarrow \min_{a} [c(s, a, s') + h(s')]}$. Over repeated trials, LRTA* is guaranteed to converge to the optimal path!
  </div>
</div>
"""

M5_BOOST_FINAL = r"""
<h2 class="section-title">Topic 38.10: Master University Exam Problem Bank (Part IV)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 5: Neural Network Multiclass Cross-Entropy Loss Derivation</div>
  <p>An image classifier outputs raw unnormalized logits for 3 classes: $\mathbf{z} = [2.0, 1.0, 0.1]^T$. True class label is Class 1 ($\mathbf{y} = [1, 0, 0]^T$).</p>
  <p><strong>1. Compute Softmax Probabilities:</strong></p>
  $$\sum e^{z_i} = e^{2.0} + e^{1.0} + e^{0.1} = 7.389 + 2.718 + 1.105 = \mathbf{11.212}$$
  $$p_1 = \frac{7.389}{11.212} = \mathbf{0.6590} \qquad p_2 = \frac{2.718}{11.212} = \mathbf{0.2424} \qquad p_3 = \frac{1.105}{11.212} = \mathbf{0.0986}$$
  <p><strong>2. Compute Categorical Cross-Entropy Loss:</strong></p>
  $$\mathbf{\mathcal{L} = - \sum_{i=1}^3 y_i \ln(p_i) = - 1.0 \ln(0.6590) = - (-0.417) = \mathbf{0.417 \text{ nats}}}$$
</div>

<div class="qa-card">
  <div class="qa-q">Q14. Explain Batch Normalization, Layer Normalization, and Dropout Regularization. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Batch Normalization (Ioffe & Szegedy):</strong> Normalizes neuron activations across mini-batch samples ($\hat{x} = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$, $y = \gamma \hat{x} + \beta$). Accelerates convergence and stabilizes internal covariate shift.<br>
    • <strong>Layer Normalization (Ba, Kiros, Hinton):</strong> Normalizes across all hidden features of a single sample independent of batch size; the universal standard for Transformer attention blocks.<br>
    • <strong>Dropout (Srivastava et al.):</strong> Randomly zeros out hidden neuron activations with probability $p$ during training, preventing complex co-adaptations and acting as an ensemble over $2^N$ sub-networks.
  </div>
</div>
"""

def boost_and_finish():
    m3_final = AI_M3_EXHAUSTIVE + M3_BOOST_FINAL
    m4_final = AI_M4_EXHAUSTIVE + M4_BOOST_FINAL
    m5_final = AI_M5_EXHAUSTIVE + M5_BOOST_FINAL

    with open(os.path.join(AI_DIR, "ai_module3_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M3_EXHAUSTIVE = r"""{m3_final}"""\n')
    with open(os.path.join(AI_DIR, "ai_module4_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M4_EXHAUSTIVE = r"""{m4_final}"""\n')
    with open(os.path.join(AI_DIR, "ai_module5_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M5_EXHAUSTIVE = r"""{m5_final}"""\n')

    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
    from finalize_ai_10_pages_exact import wrap_html, generate_pdf, LAB_GUIDE_INLINE, AI_M1_EXHAUSTIVE, AI_M2_EXHAUSTIVE, AI_REVISION_EXHAUSTIVE

    modules = [
        (1, "Module 1: Intelligent Agents & PEAS Framework", "Topics 1 to 7 • Foundations, Evolution, Rationality & 5 Agent Types", AI_M1_EXHAUSTIVE, "Module_1_Intelligent_Agents_Notes"),
        (2, "Module 2: Search Algorithms & Game Playing", "Topics 8 to 13 • BFS/DFS/IDDFS, A* Admissibility Proofs & Alpha-Beta Pruning", AI_M2_EXHAUSTIVE, "Module_2_Search_Algorithms_Notes"),
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
    boost_and_finish()
