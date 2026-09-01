# Artificial Intelligence 10-Page Master Revision Exhaustive Content (CS24307)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

AI_REVISION_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title">⚡ 10-Page Master Quick Revision — Artificial Intelligence (CS24307)</div>
  <div class="toc-grid">
    <div>Page 1: 4 Definitions of AI, Turing Test & PEAS Framework Formulations</div>
    <div>Page 2: 7 Environment Taxonomies & 5 Intelligent Agent Architectures</div>
    <div>Page 3: Uninformed Search (BFS, DFS, UCS, IDS) Complexity Comparison Matrix</div>
    <div>Page 4: Informed $A^*$ Search: Admissibility & Consistency Proofs & Trace</div>
    <div>Page 5: Adversarial Game Playing: Minimax & Alpha-Beta Pruning Rules</div>
    <div>Page 6: Propositional Logic: Entailment, CNF Conversion & Resolution Refutation</div>
    <div>Page 7: First-Order Logic: Unification (MGU) & Skolemization Mechanics</div>
    <div>Page 8: Classical Planning: STRIPS, PDDL & Graphplan Mutex Relations</div>
    <div>Page 9: Probabilistic Reasoning: Bayes' Rule, BBN Factorization & d-separation</div>
    <div>Page 10: Machine Learning: ID3 Entropy Math, Perceptron Rule & Backprop Equations</div>
  </div>
</div>

<h2 class="section-title">⚡ Master Formula, Algorithm & Search Complexity Cheat Sheet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Algorithm / Concept</th>
      <th style="width: 45%;">Core Mathematical Formulation / Rule</th>
      <th>Key Exam Takeaway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Iterative Deepening Search (IDS)</strong></td>
      <td>Time: $O(b^d)$, Space: $O(bd)$</td>
      <td>Linear space of DFS + Complete & Optimal like BFS.</td>
    </tr>
    <tr>
      <td><strong>$A^*$ Evaluation Function</strong></td>
      <td>$$f(n) = g(n) + h(n), \quad 0 \le h(n) \le h^*(n)$$</td>
      <td>Admissible $\implies$ Optimal Tree Search; Consistent $\implies$ Optimal Graph Search.</td>
    </tr>
    <tr>
      <td><strong>Alpha-Beta Pruning Rule</strong></td>
      <td>$$\text{Prune if } \alpha \ge \beta$$</td>
      <td>Reduces search time from $O(b^m)$ to $O(b^{m/2})$ with perfect move ordering.</td>
    </tr>
    <tr>
      <td><strong>Bayesian Network Joint Formula</strong></td>
      <td>$$P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))$$</td>
      <td>Drastically reduces probability parameters from $O(2^n)$ to $O(n \cdot 2^k)$.</td>
    </tr>
    <tr>
      <td><strong>Shannon Entropy</strong></td>
      <td>$$H(S) = - \sum_{i=1}^c p_i \log_2(p_i)$$</td>
      <td>Measures data impurity; maximized at uniform probability distributions.</td>
    </tr>
    <tr>
      <td><strong>Information Gain</strong></td>
      <td>$$\text{Gain}(S, A) = H(S) - \sum_{v} \frac{|S_v|}{|S|} H(S_v)$$</td>
      <td>Splitting criterion used in ID3 Decision Tree algorithm.</td>
    </tr>
    <tr>
      <td><strong>Perceptron Weight Update</strong></td>
      <td>$$\mathbf{w} \leftarrow \mathbf{w} + \eta (y_{\text{true}} - y_{\text{pred}}) \mathbf{x}$$</td>
      <td>Guaranteed to converge in finite steps for linearly separable datasets.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🔥 Top 10 High-Yield BIT Mesra Exam Questions & Solutions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. State the 4 components of PEAS for an Automated Taxi Driver. (6 Marks)</div>
  <div class="qa-a">
    - <strong>P (Performance):</strong> Safety, speed, legal adherence, passenger comfort, profits.<br>
    - <strong>E (Environment):</strong> Roads, traffic, pedestrians, weather, signals.<br>
    - <strong>A (Actuators):</strong> Steering wheel, accelerator, brake, signal indicators, horn.<br>
    - <strong>S (Sensors):</strong> Cameras, LiDAR, RADAR, GPS, speedometer, odometer, sonar.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Prove that if $h(n)$ is consistent, $A^*$ using graph search never re-opens any node. (8 Marks)</div>
  <div class="qa-a">
    By consistency, $h(n) \le c(n, a, n') + h(n') \implies g(n) + h(n) \le g(n) + c(n, a, n') + h(n') = g(n') + h(n') \implies f(n) \le f(n')$.<br>
    Thus, $f(n)$ values along any path are monotonically non-decreasing. When $A^*$ selects node $n$ from the frontier for expansion, the optimal path cost to $n$ has already been found. Hence, no shorter path to $n$ can be discovered later, making re-opening closed nodes unnecessary. $\blacksquare$
  </div>
</div>
"""
