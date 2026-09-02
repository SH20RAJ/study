# Artificial Intelligence Module 4 Exhaustive Content (7 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

AI_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Planning & Probabilistic Reasoning — Complete 7-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 24:</strong> Planning in AI (Goal-Directed Action Sequences)</div>
    <div><strong>Topic 25:</strong> Components of Planning Problems (STRIPS Operators: PRE, ADD, DEL)</div>
    <div><strong>Topic 26:</strong> Types of Planning (State-Space, Partial-Order & Hierarchical HTN)</div>
    <div><strong>Topic 27:</strong> Goal Stack Planning (Subgoal Interactions & Sussman Anomaly)</div>
    <div><strong>Topic 28:</strong> Reasoning Under Uncertainty (Axioms of Probability)</div>
    <div><strong>Topic 29:</strong> Bayesian Inference (Prior, Likelihood, Posterior & Evidence)</div>
    <div><strong>Topic 30:</strong> Probabilistic Reasoning & Bayesian Belief Networks (DAGs)</div>
  </div>
</div>

<h2 class="section-title">Topic 24 & 25: Planning Foundations & STRIPS Representation</h2>

<div class="callout callout-info">
  <div class="callout-title">STRIPS Action Operator Representation (Fikes & Nilsson, 1971)</div>
  An action $A$ is represented as a triple:
  <ul>
    <li><strong>Action Name:</strong> e.g., $\text{Move}(b, x, y)$ (Move block $b$ from surface $x$ to surface $y$).</li>
    <li><strong>Preconditions (PRE):</strong> Set of positive logical literals that must be true for action to execute ($\text{On}(b, x) \wedge \text{Clear}(b) \wedge \text{Clear}(y)$).</li>
    <li><strong>Add-List (ADD):</strong> Set of literals made true by executing the action ($\text{On}(b, y) \wedge \text{Clear}(x)$).</li>
    <li><strong>Delete-List (DEL):</strong> Set of literals made false by executing the action ($\text{On}(b, x) \wedge \text{Clear}(y)$).</li>
  </ul>
</div>

<h2 class="section-title">Topic 26 & 27: Goal Stack Planning & Types of Planning</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Planning Paradigm</th>
      <th style="width: 45%;">Operating Mechanism</th>
      <th>Key Limitation / Advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Goal Stack Planning</strong></td>
      <td>Maintains a LIFO stack of subgoals and STRIPS operators. Solves subgoals sequentially one by one.</td>
      <td>Vulnerable to <strong>Subgoal Interleaving (Sussman Anomaly)</strong>: achieving one subgoal may inadvertently undo a previously satisfied subgoal.</td>
    </tr>
    <tr>
      <td><strong>2. Partial-Order Planning (POP)</strong></td>
      <td>Works in plan space; adds actions and orders them only when strictly necessary (Least-Commitment principle).</td>
      <td>Eliminates unnecessary search commitments; handles interleaved subgoals gracefully.</td>
    </tr>
    <tr>
      <td><strong>3. Hierarchical Task Network (HTN)</strong></td>
      <td>Recursively decomposes high-level abstract tasks into executable primitive action sequences.</td>
      <td>Scales to industrial-scale engineering and manufacturing planning problems.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 28 & 29: Reasoning Under Uncertainty & Bayesian Inference</h2>

<div class="formula-card">
  <strong>1. Fundamental Axioms of Probability:</strong>
  - Range: $0 \le P(A) \le 1, \quad P(\text{True}) = 1, \quad P(\text{False}) = 0$
  - Disjunction: $P(A \vee B) = P(A) + P(B) - P(A \wedge B)$
  - Conditional Probability: $P(A \mid B) = \frac{P(A \wedge B)}{P(B)} \implies P(A \wedge B) = P(A \mid B) P(B)$
</div>

<div class="formula-card">
  <strong>2. Bayes' Rule Formulation (Bayes, 1763):</strong>
  $$P(\text{Hypothesis} \mid \text{Evidence}) = \frac{P(\text{Evidence} \mid \text{Hypothesis}) \cdot P(\text{Hypothesis})}{P(\text{Evidence})}$$
  $$\mathbf{\text{Posterior}} = \frac{\mathbf{\text{Likelihood}} \times \mathbf{\text{Prior}}}{\mathbf{\text{Evidence}}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Bayesian Medical Diagnosis Problem</div>
  <p>A disease affects $1\%$ of the population ($P(D) = 0.01$). A test has $95\%$ true positive rate ($P(T \mid D) = 0.95$) and $5\%$ false positive rate ($P(T \mid \neg D) = 0.05$). Find the probability a patient who tests positive actually has the disease $P(D \mid T)$.</p>
  <ol>
    <li>Total Evidence $P(T) = P(T \mid D)P(D) + P(T \mid \neg D)P(\neg D) = (0.95)(0.01) + (0.05)(0.99) = 0.0095 + 0.0495 = \mathbf{0.0590}$.</li>
    <li>$P(D \mid T) = \frac{P(T \mid D)P(D)}{P(T)} = \frac{0.0095}{0.0590} \approx \mathbf{0.161} \ (\mathbf{16.1\%})$.</li>
  </ol>
</div>

<h2 class="section-title">Topic 30: Probabilistic Reasoning & Bayesian Belief Networks</h2>

<div class="formula-card">
  <strong>Full Joint Distribution Chain Rule for Bayesian Networks:</strong>
  A <strong>Bayesian Network</strong> is a Directed Acyclic Graph (DAG) where nodes represent random variables and directed edges represent direct conditional dependencies:
  $$P(X_1, X_2, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))$$
  Reduces storage from $O(2^n)$ in full joint table to $O(n \cdot 2^k)$ where $k$ is maximum parent in-degree!
</div>

<h2 class="section-title">🧠 M4 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Define STRIPS. Explain the components of a planning action with a clear example. (8 Marks)</div>
  <div class="qa-a">
    <strong>STRIPS (Stanford Research Institute Problem Solver)</strong> is a formal action representation language where world states are conjunctions of function-free positive literals.<br>
    An action is defined by: (1) <em>Name/Parameters</em>, (2) <em>Preconditions</em> (what must hold before execution), (3) <em>Add-List</em> (positive effects added to state), and (4) <em>Delete-List</em> (literals removed from state).<br>
    <em>Example:</em> $\text{Stack}(A, B)$<br>
    • $\text{PRE: } \text{Clear}(A), \text{Clear}(B), \text{On}(A, \text{Table})$<br>
    • $\text{ADD: } \text{On}(A, B)$<br>
    • $\text{DEL: } \text{Clear}(B), \text{On}(A, \text{Table})$
  </div>
</div>
"""
