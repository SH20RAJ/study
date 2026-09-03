AI_REVISION_EXHAUSTIVE = r"""
<h2 class="section-title">Page 1: AI Master Mental Model & Environmental Taxonomy</h2>
<div class="callout callout-info"><div class="callout-title">Core Paradigm</div>Rational Agent: Selects action $a \in \mathcal{A}$ maximizing expected performance measure $P$ given historical percept sequence $\mathcal{P}^*$.</div>
<table class="custom-table">
  <thead><tr><th>Environment</th><th>Observability</th><th>Determinism</th><th>Episodic/Seq</th><th>Static/Dyn</th><th>Discrete/Cont</th><th>Agents</th></tr></thead>
  <tbody>
    <tr><td><strong>Chess</strong></td><td>Fully</td><td>Deterministic</td><td>Sequential</td><td>Static</td><td>Discrete</td><td>Multi (Adversarial)</td></tr>
    <tr><td><strong>Poker</strong></td><td>Partially</td><td>Stochastic</td><td>Sequential</td><td>Static</td><td>Discrete</td><td>Multi (Adversarial)</td></tr>
    <tr><td><strong>Self-Driving</strong></td><td>Partially</td><td>Stochastic</td><td>Sequential</td><td>Dynamic</td><td>Continuous</td><td>Multi</td></tr>
    <tr><td><strong>Medical Diagn.</strong></td><td>Partially</td><td>Stochastic</td><td>Sequential</td><td>Dynamic</td><td>Continuous</td><td>Single</td></tr>
  </tbody>
</table>

<div class="page-break"></div>
<h2 class="section-title">Page 2: Uninformed vs. Informed Search Complexity Matrix</h2>
<table class="custom-table">
  <thead><tr><th>Algorithm</th><th>Data Structure</th><th>Time Complexity</th><th>Space Complexity</th><th>Complete?</th><th>Optimal?</th></tr></thead>
  <tbody>
    <tr><td><strong>BFS</strong></td><td>FIFO Queue</td><td>$O(b^d)$</td><td>$O(b^d)$</td><td>Yes</td><td>Yes (uniform costs)</td></tr>
    <tr><td><strong>DFS</strong></td><td>LIFO Stack</td><td>$O(b^m)$</td><td>$O(b \cdot m)$</td><td>No (infinite trees)</td><td>No</td></tr>
    <tr><td><strong>UCS</strong></td><td>Priority Queue</td><td>$O(b^{1 + \lfloor C^*/\epsilon \rfloor})$</td><td>$O(b^{1 + \lfloor C^*/\epsilon \rfloor})$</td><td>Yes</td><td><strong>Yes (Cost optimal)</strong></td></tr>
    <tr><td><strong>IDDFS</strong></td><td>LIFO Stack</td><td>$O(b^d)$</td><td>$\mathbf{O(b \cdot d)}$</td><td>Yes</td><td>Yes (uniform costs)</td></tr>
    <tr><td><strong>$A^*$ Search</strong></td><td>Priority Queue</td><td>$O(b^d)$</td><td>$O(b^d)$</td><td>Yes</td><td><strong>Yes (if $h$ admissible)</strong></td></tr>
  </tbody>
</table>

<div class="page-break"></div>
<h2 class="section-title">Page 3: $A^*$ Search Admissibility & Consistency Theorems</h2>
<div class="formula-card">
  $$\text{Admissibility: } 0 \le h(n) \le h^*(n) \implies A^* \text{ Tree Search is Optimal}$$
  $$\text{Consistency: } h(n) \le c(n, a, n') + h(n') \implies A^* \text{ Graph Search is Optimal (No node re-expansion!)}$$
</div>

<div class="page-break"></div>
<h2 class="section-title">Page 4: Adversarial Minimax & Alpha-Beta Pruning Rules</h2>
<div class="formula-card">
  $$\alpha \leftarrow \max(\alpha, \text{child\_val}) \quad (\text{Initialized to } -\infty)$$
  $$\beta \leftarrow \min(\beta, \text{child\_val}) \quad (\text{Initialized to } +\infty)$$
  $$\mathbf{\text{PRUNE SUBTREE IF } \alpha \ge \beta}$$
</div>

<div class="page-break"></div>
<h2 class="section-title">Page 5: Propositional & First-Order Logic (FOL) Transformation Rules</h2>
<div class="worked-box">
  $$\alpha \rightarrow \beta \equiv \neg \alpha \lor \beta \qquad \alpha \leftrightarrow \beta \equiv (\neg \alpha \lor \beta) \land (\neg \beta \lor \alpha)$$
  $$\neg (\forall x P(x)) \equiv \exists x \neg P(x) \qquad \neg (\exists x P(x)) \equiv \forall x \neg P(x)$$
  $$\text{Resolution: } \frac{A \lor B, \quad \neg B \lor C}{A \lor C}$$
</div>

<div class="page-break"></div>
<h2 class="section-title">Page 6: Classical Planning STRIPS & Graphplan Mutexes</h2>
<div class="callout callout-info"><div class="callout-title">3 Mutex Conditions</div>Inconsistent Effects (Add vs Delete), Interference (Delete vs Precond), Competing Needs (Mutex Preconditions).</div>

<div class="page-break"></div>
<h2 class="section-title">Page 7: Probability, Bayes' Rule & Bayesian Networks</h2>
<div class="formula-card">
  $$P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)} \qquad P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))$$
</div>

<div class="page-break"></div>
<h2 class="section-title">Page 8: Decision Tree Induction (ID3 Entropy & Gain)</h2>
<div class="formula-card">
  $$H(S) = - \sum p_i \log_2(p_i) \qquad \text{Gain}(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$$
</div>

<div class="page-break"></div>
<h2 class="section-title">Page 9: Multi-Layer Perceptrons & Backpropagation Gradient</h2>
<div class="formula-card">
  $$\delta_k = (y_k - \hat{y}_k) \sigma'(z_k) \qquad \delta_j = \sigma'(z_j) \sum_k \delta_k w_{jk} \qquad \Delta w = \eta \delta a_{\text{in}}$$
</div>

<div class="page-break"></div>
<h2 class="section-title">Page 10: AI Final High-Yield Exam Checklist & Formulas</h2>
<div class="worked-box">
  <div class="worked-title">10 Instant Revision Points</div>
  1. $A^*$ with $h=0$ becomes Uniform Cost Search.<br>
  2. $A^*$ with $g=0$ becomes Greedy Best-First Search.<br>
  3. Iterative Deepening DFS uses $O(bd)$ memory and visits nodes at depth $d$ only once.<br>
  4. Alpha-Beta does not affect final minimax value at root.<br>
  5. Skolemization replaces $\exists x$ with constant or Skolem function $f(y_1\dots y_k)$.<br>
  6. Unification requires variables to be standardized apart.<br>
  7. d-separation isolates nodes given evidence variables.<br>
  8. Backpropagation computes exact gradient via dynamic programming chain rule.<br>
  9. ReLU eliminates vanishing gradient for positive activations.<br>
  10. Softmax produces valid categorical probability distribution.
</div>
"""
