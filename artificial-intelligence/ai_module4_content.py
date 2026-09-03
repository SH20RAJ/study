AI_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 4 Table of Contents (Topics 23 to 29)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 23:</strong> Classical Planning & STRIPS / PDDL</div>
    <div>• <strong>Topic 24:</strong> Progression vs. Regression Search</div>
    <div>• <strong>Topic 25:</strong> Planning Graphs (Graphplan) & Mutexes</div>
    <div>• <strong>Topic 26:</strong> Quantifying Uncertainty & Probability Axioms</div>
    <div>• <strong>Topic 27:</strong> Bayes' Theorem & Conditional Independence</div>
    <div>• <strong>Topic 28:</strong> Bayesian Networks & CPT Structure</div>
    <div>• <strong>Topic 29:</strong> Exact Inference in Bayes Nets & d-Separation</div>
  </div>
</div>

<h2 class="section-title">Topic 23 to 25: Classical Planning, STRIPS & Graphplan</h2>

<p>
  In <strong>Classical Planning</strong>, states and actions are represented using explicit propositional or first-order fluents. Under the <strong>STRIPS / PDDL language</strong>:
</p>

<div class="formula-card">
  <strong>STRIPS Action Representation:</strong>
  $$\mathbf{\text{Action}(a, \text{Precond}: P, \text{Effect}: \text{Add}(A) \land \text{Delete}(D))}$$
  $$\mathbf{\text{Result}(s, a) = (s \setminus D) \cup A}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ STRIPS Blocks World Problem Formulation</div>
  <pre><code>Init(On(A, Table) ∧ On(B, Table) ∧ Clear(A) ∧ Clear(B) ∧ ArmEmpty)
Goal(On(A, B) ∧ On(B, Table))

Action(PickUp(x),
  PRECOND: Clear(x) ∧ On(x, Table) ∧ ArmEmpty
  EFFECT:  ¬On(x, Table) ∧ ¬Clear(x) ∧ ¬ArmEmpty ∧ Holding(x))

Action(PutDown(x),
  PRECOND: Holding(x)
  EFFECT:  On(x, Table) ∧ Clear(x) ∧ ArmEmpty ∧ ¬Holding(x))

Action(Stack(x, y),
  PRECOND: Holding(x) ∧ Clear(y)
  EFFECT:  On(x, y) ∧ Clear(x) ∧ ArmEmpty ∧ ¬Holding(x) ∧ ¬Clear(y))

Action(Unstack(x, y),
  PRECOND: On(x, y) ∧ Clear(x) ∧ ArmEmpty
  EFFECT:  Holding(x) ∧ Clear(y) ∧ ¬On(x, y) ∧ ¬Clear(x) ∧ ¬ArmEmpty)</code></pre>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Planning Graph Mutex (Mutual Exclusion) Conditions</div>
  <p>In Graphplan, two actions at level $A_i$ are <strong>MUTEX</strong> if:</p>
  <ol>
    <li><strong>Inconsistent Effects:</strong> One action negates an effect of the other ($A \text{ adds } P, B \text{ deletes } P$).</li>
    <li><strong>Interference:</strong> One action deletes a precondition of the other ($A \text{ deletes } P, B \text{ requires } P$).</li>
    <li><strong>Competing Needs:</strong> Preconditions of $A$ and $B$ are mutex at literal level $S_i$.</li>
  </ol>
</div>

<h2 class="section-title">Topic 26 to 29: Probability, Bayes' Rule & Bayesian Networks</h2>

<div class="formula-card">
  <strong>Bayes' Rule & Conditional Independence:</strong>
  $$\mathbf{P(Y \mid X) = \frac{P(X \mid Y) P(Y)}{P(X)} = \frac{P(X \mid Y) P(Y)}{\sum_{y} P(X \mid Y=y) P(Y=y)}}$$
  $$\mathbf{P(X, Y \mid Z) = P(X \mid Z) \cdot P(Y \mid Z) \iff X \text{ and } Y \text{ conditionally independent given } Z}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Step-by-Step Solved Problem: Earthquake-Burglary Bayesian Network Inference</div>
  <p>Given the classic Pearl Alarm network: $B$ (Burglary), $E$ (Earthquake), $A$ (Alarm), $J$ (JohnCalls), $M$ (MaryCalls):</p>
  <ul>
    <li>$P(B=t) = 0.001, \quad P(E=t) = 0.002$</li>
    <li>$P(A=t \mid B=t, E=t) = 0.95, \ P(A=t \mid B=t, E=f) = 0.94, \ P(A=t \mid B=f, E=t) = 0.29, \ P(A=t \mid B=f, E=f) = 0.001$</li>
    <li>$P(J=t \mid A=t) = 0.90, \ P(J=t \mid A=f) = 0.05$</li>
    <li>$P(M=t \mid A=t) = 0.70, \ P(M=t \mid A=f) = 0.01$</li>
  </ul>
  <p><strong>Query:</strong> Calculate the exact joint probability that John calls and Mary calls, but there is NO burglary and NO earthquake, and the alarm did ring:</p>
  $$\mathbf{P(J=t, M=t, A=t, B=f, E=f) = P(B=f) \cdot P(E=f) \cdot P(A=t \mid B=f, E=f) \cdot P(J=t \mid A=t) \cdot P(M=t \mid A=t)}$$
  $$= (0.999) \times (0.998) \times (0.001) \times (0.90) \times (0.70)$$
  $$\mathbf{= 0.997002 \times 0.001 \times 0.63 = \mathbf{0.00062811 = 6.28 \times 10^{-4}}}$$
</div>

<h2 class="section-title">Topic 29.2: Master University Examination Solved Question Bank (10 Solved Questions)</h2>

<div class="qa-card"><div class="qa-q">Q1. State and prove Bayes' Theorem from the Definition of Conditional Probability. (6 Marks)</div><div class="qa-a">By definition: $P(A \land B) = P(A \mid B) P(B)$ and $P(A \land B) = P(B \mid A) P(A)$. Equating the two expressions gives $P(A \mid B) P(B) = P(B \mid A) P(A)$. Dividing both sides by $P(B)$ yields: $\mathbf{P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}}$.</div></div>
<div class="qa-card"><div class="qa-q">Q2. Explain the difference between Progression Planning and Regression Planning. (8 Marks)</div><div class="qa-a">• <strong>Progression Planning (Forward State-Space Search):</strong> Starts from initial state $S_0$ and applies all applicable actions to generate successor states moving toward the goal. High branching factor on irrelevant actions.<br>• <strong>Regression Planning (Backward Search):</strong> Starts from the goal state $G$ and applies inverted relevant actions backwards toward the initial state. Explores only actions that directly achieve a goal literal.</div></div>
<div class="qa-card"><div class="qa-q">Q3. What is a Bayesian Network? How does it compress the Full Joint Probability Distribution? (8 Marks)</div><div class="qa-a">A Bayesian Network is a Directed Acyclic Graph (DAG) where nodes represent random variables and edges represent direct causal dependencies. For $n$ binary variables, a Full Joint Distribution requires $2^n - 1$ parameters (exponential). A Bayes Net factors the joint distribution as: $\mathbf{P(X_1,\dots,X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))}$. If each node has at most $k$ parents, it requires only $n \cdot 2^k$ parameters (linear in $n$!).</div></div>
<div class="qa-card"><div class="qa-q">Q4. State the d-Separation rules for Causal Chains, Forks, and Colliders. (8 Marks)</div><div class="qa-a">1. <strong>Causal Chain ($X \rightarrow Z \rightarrow Y$):</strong> Blocked/Independent given $Z$.<br>2. <strong>Common Cause / Fork ($X \leftarrow Z \rightarrow Y$):</strong> Blocked/Independent given $Z$.<br>3. <strong>Common Effect / Collider ($X \rightarrow Z \leftarrow Y$):</strong> Independent if neither $Z$ nor any descendant of $Z$ is observed; <strong>Becomes DEPENDENT (Active)</strong> if $Z$ or its descendant is observed! (Explaining Away phenomenon).</div></div>
<div class="qa-card"><div class="qa-q">Q5. Explain the Graphplan Algorithm and why Planning Graphs can be computed in polynomial time. (8 Marks)</div><div class="qa-a">Graphplan constructs a Planning Graph of alternating state levels $S_i$ and action levels $A_i$ connected by precondition, add, delete, and persistence edges. Since actions are monotonic (literals only accumulate, never deleted from the graph level), the graph levels level off in polynomial time $O(n(a + l))$. Solution extraction is performed by backward search on mutex-free paths.</div></div>
<div class="qa-card"><div class="qa-q">Q6. Explain the Sussman Anomaly in Classical Planning. (6 Marks)</div><div class="qa-a">The Sussman Anomaly is a classic failure mode of non-interleaved goal planning where achieving goal subgoal 1 ($On(A,B)$) undoes the prerequisite for subgoal 2 ($On(B,C)$), and vice-versa. It proves that simple decomposition of conjunctive goals without plan-step interleaving is sub-optimal and incomplete.</div></div>
<div class="qa-card"><div class="qa-q">Q7. Detail the Variable Elimination Algorithm for Exact Inference in Bayesian Networks. (8 Marks)</div><div class="qa-a">Variable Elimination computes marginal distributions by dynamic programming:<br>1. Express query as sum of products of conditional probability table factors.<br>2. Choose an elimination ordering of non-query, non-evidence hidden variables.<br>3. Multiply all factors containing the variable to eliminate and sum out the variable.<br>4. Pointwise multiply the remaining factor and normalize by $\alpha$.</div></div>
<div class="qa-card"><div class="qa-q">Q8. Explain Markov Chain Monte Carlo (MCMC) and Gibbs Sampling in Bayesian Networks. (8 Marks)</div><div class="qa-a">When exact inference is NP-hard on dense networks, Gibbs Sampling generates approximate samples by:<br>1. Initializing all non-evidence variables randomly.<br>2. In each iteration, picking one non-evidence variable $X_i$ and resampling its value conditioned on its Markov Blanket $P(X_i \mid \text{MB}(X_i))$.<br>3. Counting the frequencies of sampled states after a burn-in period to estimate posterior probabilities.</div></div>
<div class="qa-card"><div class="qa-q">Q9. Explain Partial-Order Planning (POP) and contrast it with Total-Order Planning. (8 Marks)</div><div class="qa-a">Total-Order Planning strictly sequences actions into a single linear chain. <strong>Partial-Order Planning</strong> operates in the space of plans, establishing ordering constraints ($A \prec B$) and causal links ($A \xrightarrow{p} B$) only where necessary to resolve causal threats (demotions/promotions), leaving independent sub-plans unordered to facilitate parallel execution.</div></div>
<div class="qa-card"><div class="qa-q">Q10. Calculate $P(\text{Cavity} \mid \text{Toothache})$ given: $P(\text{Toothache} \mid \text{Cavity}) = 0.8$, $P(\text{Cavity}) = 0.1$, and $P(\text{Toothache}) = 0.2$. (6 Marks)</div><div class="qa-a">Using Bayes' Rule:<br>$$\mathbf{P(\text{Cavity} \mid \text{Toothache}) = \frac{P(\text{Toothache} \mid \text{Cavity}) P(\text{Cavity})}{P(\text{Toothache})} = \frac{(0.8)(0.1)}{0.2} = \frac{0.08}{0.20} = \mathbf{0.40 = 40\%}}$$</div></div>

<h2 class="section-title">Topic 29.5: Advanced Probabilistic Reasoning, HMMs & Kalman Filters</h2>

<p>
  When reasoning over time in dynamic stochastic environments, agents use temporal probabilistic models to maintain probability distributions over unobserved hidden state variables.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Temporal Model</th>
      <th style="width: 35%;">Mathematical State Representation</th>
      <th>Filtering & Inference Task</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Hidden Markov Model (HMM)</strong></td>
      <td>Discrete state space $S_t \in \{s_1, \dots, s_N\}$, discrete or continuous observations $O_t$. Transition matrix $T_{ij} = P(S_t=s_j \mid S_{t-1}=s_i)$, Emission matrix $E_{ik} = P(O_t=o_k \mid S_t=s_i)$.</td>
      <td>Forward Algorithm (Filtering $P(S_t \mid o_{1:t})$), Backward Algorithm (Smoothing), Viterbi Algorithm (Most likely hidden path).</td>
    </tr>
    <tr>
      <td><strong>Kalman Filter (LGM)</strong></td>
      <td>Continuous state space with linear Gaussian transitions: $\mathbf{x}_t = \mathbf{F} \mathbf{x}_{t-1} + \mathbf{w}_t$, $\mathbf{z}_t = \mathbf{H} \mathbf{x}_t + \mathbf{v}_t$ (where $\mathbf{w}_t \sim \mathcal{N}(0, \mathbf{Q}), \mathbf{v}_t \sim \mathcal{N}(0, \mathbf{R})$).</td>
      <td>Exact recursive update of Gaussian mean $\mathbf{\mu}_t$ and covariance matrix $\mathbf{\Sigma}_t$.</td>
    </tr>
    <tr>
      <td><strong>Particle Filter (Sequential Monte Carlo)</strong></td>
      <td>Arbitrary non-linear, non-Gaussian continuous state space represented by a cloud of $N$ weighted particles $\{(\mathbf{x}_t^{(i)}, w_t^{(i)})\}_{i=1}^N$.</td>
      <td>Importance sampling, weight update by measurement likelihood, and resampling to prevent particle degeneracy.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: The Viterbi Dynamic Programming Algorithm for HMMs</div>
  <p>Consider a 2-state weather HMM with states $\{\text{Rainy }(R), \text{Sunny }(S)\}$ and umbrella observations $\{U, \neg U\}$:</p>
  <ul>
    <li>Initial: $P(R_0) = 0.5, \ P(S_0) = 0.5$.</li>
    <li>Transitions: $P(R \mid R) = 0.7, \ P(S \mid R) = 0.3; \ P(R \mid S) = 0.3, \ P(S \mid S) = 0.7$.</li>
    <li>Emissions: $P(U \mid R) = 0.9, \ P(\neg U \mid R) = 0.1; \ P(U \mid S) = 0.2, \ P(\neg U \mid S) = 0.8$.</li>
  </ul>
  <p><strong>Observations: Day 1: $U$, Day 2: $U$. Find most likely state sequence:</strong></p>
  <p><strong>Day 1 ($t=1, O_1 = U$):</strong></p>
  $$V_1(R) = P(R_0) \cdot P(U \mid R) = (0.5)(0.9) = \mathbf{0.45}$$
  $$V_1(S) = P(S_0) \cdot P(U \mid S) = (0.5)(0.2) = \mathbf{0.10}$$
  <p><strong>Day 2 ($t=2, O_2 = U$):</strong></p>
  $$V_2(R) = \max(V_1(R)P(R\mid R), V_1(S)P(R\mid S)) \cdot P(U \mid R) = \max((0.45)(0.7), (0.10)(0.3)) \cdot 0.9 = \max(0.315, 0.030) \cdot 0.9 = \mathbf{0.2835}$$
  $$V_2(S) = \max(V_1(R)P(S\mid R), V_1(S)P(S\mid S)) \cdot P(U \mid S) = \max((0.45)(0.3), (0.10)(0.7)) \cdot 0.2 = \max(0.135, 0.070) \cdot 0.2 = \mathbf{0.0270}$$
  $$\mathbf{\text{Most Probable Path: } \text{Day 1: Rainy} \rightarrow \text{Day 2: Rainy} \quad (\text{Joint Prob } = \mathbf{0.2835})}$$
</div>

<div class="qa-card">
  <div class="qa-q">Q11. Explain the difference between Policy Iteration and Value Iteration in Markov Decision Processes. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Value Iteration:</strong> Iteratively updates value function $U_{k+1}(s)$ using the Bellman Optimality operator over all actions until convergence ($\|U_{k+1}-U_k\| < \epsilon$), then extracts the policy in a single final step. Can be slow because utility values take many iterations to converge to exact decimal precision.<br>
    • <strong>Policy Iteration:</strong> Alternates between two discrete phases: (1) <em>Policy Evaluation:</em> Calculates exact state utilities $U^{\pi_k}$ for the current fixed policy $\pi_k$ by solving a system of linear equations $O(N^3)$, and (2) <em>Policy Improvement:</em> Greedily updates the policy $\pi_{k+1}(s) = \arg\max_a \sum_{s'} P(s'\mid s, a) U^{\pi_k}(s')$. It converges in significantly fewer iterations because the policy space is finite ($|\mathcal{A}|^{|\mathcal{S}|}$).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q12. What is Q-Learning? Why is it termed an Off-Policy Model-Free Algorithm? (8 Marks)</div>
  <div class="qa-a">
    • <strong>Model-Free:</strong> Does NOT require explicit transition probability matrices $P(s' \mid s, a)$ or reward functions $R(s, a, s')$; it learns directly from sampled experiential trajectories $\langle s, a, r, s' \rangle$.<br>
    • <strong>Off-Policy:</strong> The target policy being learned is the <em>greedy optimal policy</em> ($\max_{a'} Q(s', a')$), which is completely decoupled from the <em>behavioral policy</em> (e.g. $\epsilon$-greedy exploration) used to generate actions in the environment.
  </div>
</div>

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

<h2 class="section-title">Topic 29.7: Partially Observable MDPs (POMDPs) & Dynamic Decision Networks</h2>

<p>
  When state transitions are stochastic and the state is only <strong>partially observable</strong> through noisy sensors, the agent operates in a <strong>POMDP (Partially Observable Markov Decision Process)</strong>:
</p>

<div class="formula-card">
  <strong>The 7-Tuple POMDP Formalism:</strong>
  $$\mathbf{\mathcal{P} = \langle \mathcal{S}, \mathcal{A}, \mathcal{P}(s' \mid s, a), \mathcal{R}(s, a), \Omega, \mathcal{O}(o \mid s', a), \gamma \rangle}$$
  Where $\Omega$ is the set of observations, and $\mathcal{O}(o \mid s', a)$ is the observation emission probability. The agent maintains a <strong>Belief State $b(s)$</strong> (a continuous probability distribution over all states $\sum_{s} b(s) = 1$).
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ The Exact Belief State Update Equation (Bayesian Filtering)</div>
  <p>After executing action $a$ and perceiving observation $o$, the updated belief $b'(s')$ is computed via Bayes' Rule:</p>
  $$\mathbf{b'(s') = \frac{\mathcal{O}(o \mid s', a) \sum_{s \in \mathcal{S}} \mathcal{P}(s' \mid s, a) b(s)}{P(o \mid a, b)} = \alpha \cdot \mathcal{O}(o \mid s', a) \sum_{s \in \mathcal{S}} \mathcal{P}(s' \mid s, a) b(s)}$$
  <p><em>Interpretation:</em> The continuous belief space $[0, 1]^{|\mathcal{S}|}$ converts a partially observable problem into a continuous, fully observable MDP over belief states!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: POMDP Belief State Update Calculation</div>
  <p>A robot is in a 2-room corridor ($S_1, S_2$). Prior belief $b(S_1) = 0.5, b(S_2) = 0.5$. Action $a = \text{MoveRight}$:</p>
  <ul>
    <li>Transitions: $P(S_2 \mid S_1, \text{MoveRight}) = 0.8, P(S_1 \mid S_1, \text{MoveRight}) = 0.2; \ P(S_2 \mid S_2, \text{MoveRight}) = 0.9, P(S_1 \mid S_2, \text{MoveRight}) = 0.1$.</li>
    <li>Light sensor reading: $o = \text{Bright}$. Emissions: $P(\text{Bright} \mid S_1) = 0.1, P(\text{Bright} \mid S_2) = 0.8$.</li>
  </ul>
  <p><strong>Calculate updated belief $b'(S_1)$ and $b'(S_2)$:</strong></p>
  $$\text{Predicted } P(S_1) = (0.2)(0.5) + (0.1)(0.5) = 0.10 + 0.05 = \mathbf{0.15}$$
  $$\text{Predicted } P(S_2) = (0.8)(0.5) + (0.9)(0.5) = 0.40 + 0.45 = \mathbf{0.85}$$
  $$b'(S_1) \propto P(\text{Bright} \mid S_1) \cdot 0.15 = (0.1)(0.15) = 0.015$$
  $$b'(S_2) \propto P(\text{Bright} \mid S_2) \cdot 0.85 = (0.8)(0.85) = 0.680$$
  $$\text{Normalization Constant } \alpha = \frac{1}{0.015 + 0.680} = \frac{1}{0.695} \approx 1.4388$$
  $$\mathbf{b'(S_1) = 0.015 \times 1.4388 = \mathbf{0.0216 = 2.16\%} \qquad b'(S_2) = 0.680 \times 1.4388 = \mathbf{0.9784 = 97.84\%}}}$$
</div>

<h2 class="section-title">Topic 29.8: Complete Step-by-Step Solved Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 3: Bayesian Network Exact Joint Probability Calculation</div>
  <p>Consider a 4-node Bayesian Network with DAG structure $A \rightarrow B \rightarrow D$ and $A \rightarrow C \rightarrow D$:</p>
  <ul>
    <li>$P(A=t) = 0.4$.</li>
    <li>$P(B=t \mid A=t) = 0.8, \ P(B=t \mid A=f) = 0.2$.</li>
    <li>$P(C=t \mid A=t) = 0.7, \ P(C=t \mid A=f) = 0.1$.</li>
    <li>$P(D=t \mid B=t, C=t) = 0.9, \ P(D=t \mid B=t, C=f) = 0.6, \ P(D=t \mid B=f, C=t) = 0.5, \ P(D=t \mid B=f, C=f) = 0.1$.</li>
  </ul>
  <p><strong>Calculate $P(A=t, B=t, C=f, D=t)$:</strong></p>
  $$\mathbf{P(A=t, B=t, C=f, D=t) = P(A=t) \cdot P(B=t \mid A=t) \cdot P(C=f \mid A=t) \cdot P(D=t \mid B=t, C=f)}$$
  $$= (0.4) \times (0.8) \times (1 - 0.7) \times (0.6)$$
  $$= (0.4) \times (0.8) \times (0.3) \times (0.6) = 0.32 \times 0.18 = \mathbf{0.0576 = \mathbf{5.76\%}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: STRIPS Shakey the Robot World</div>
  <p>Formulate the STRIPS operators for a mobile robot moving between rooms and pushing boxes:</p>
  <pre><code>Action(Go(x, y),
  PRECOND: At(Shakey, x) ∧ In(x, r) ∧ In(y, r)
  EFFECT:  ¬At(Shakey, x) ∧ At(Shakey, y))

Action(Push(b, x, y),
  PRECOND: At(Shakey, x) ∧ At(b, x) ∧ In(x, r) ∧ In(y, r) ∧ Box(b)
  EFFECT:  ¬At(Shakey, x) ∧ ¬At(b, x) ∧ At(Shakey, y) ∧ At(b, y))

Action(ClimbOn(b),
  PRECOND: At(Shakey, x) ∧ At(b, x) ∧ On(Shakey, Floor) ∧ Box(b)
  EFFECT:  ¬On(Shakey, Floor) ∧ On(Shakey, b))

Action(TurnOnLight(s),
  PRECOND: At(Shakey, x) ∧ At(s, x) ∧ On(Shakey, b) ∧ Box(b) ∧ Switch(s)
  EFFECT:  LightOn(s))</code></pre>
</div>

<div class="qa-card">
  <div class="qa-q">Q13. Explain Hierarchical Task Networks (HTN) Planning. (8 Marks)</div>
  <div class="qa-a">
    HTN Planning extends classical planning by decomposing high-level compound abstract tasks (e.g. `TravelTo(NewYork)`) into smaller sub-tasks using <strong>Methods</strong> until only primitive actions remain (e.g., `BuyTicket`, `DriveToAirport`, `Fly`). HTN plans are dramatically faster to compute than STRIPS because domain-specific expert knowledge restricts the search space to realistic human-like decompositions rather than searching through arbitrary combinations of primitive actions!
  </div>
</div>

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
