#!/usr/bin/env python3
"""
Pushes Artificial Intelligence Modules (M1–M5) to 10–12 Pages each,
and AI_Full_Course_Master.pdf to 55+ Pages!
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

# Load existing base contents
sys.path.insert(0, AI_DIR)
from ai_module1_content import AI_M1_EXHAUSTIVE
from ai_module2_content import AI_M2_EXHAUSTIVE
from ai_module3_content import AI_M3_EXHAUSTIVE
from ai_module4_content import AI_M4_EXHAUSTIVE
from ai_module5_content import AI_M5_EXHAUSTIVE
from ai_revision_content import AI_REVISION_EXHAUSTIVE

# In-depth expansion for Module 1
M1_BOOST = r"""
<h2 class="section-title">Topic 7.4: Advanced Agent Design Patterns & Multi-Agent Game Theory</h2>

<p>
  When scaling from single rational agents to <strong>Multi-Agent Systems (MAS)</strong>, agents must reason about the strategic intentions and utility profiles of other autonomous entities.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Multi-Agent Paradigm</th>
      <th style="width: 35%;">Theoretical Mechanism</th>
      <th>Industrial Application</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Cooperative Agents</strong></td>
      <td>Shared global utility function $U_{\text{team}} = \sum U_i$. Agents communicate via Contract Net Protocol or blackboard architectures to divide tasks without conflict.</td>
      <td>Fleet of search-and-rescue UAVs, warehouse logistics robots (Kiva/Amazon).</td>
    </tr>
    <tr>
      <td><strong>Competitive / Adversarial</strong></td>
      <td>Zero-sum or non-zero-sum game theory. Agents calculate Nash Equilibria ($\forall i, U_i(s_i^*, s_{-i}^*) \ge U_i(s_i, s_{-i}^*)$) to prevent exploitation.</td>
      <td>Automated financial market trading, adversarial cybersecurity defence.</td>
    </tr>
    <tr>
      <td><strong>Social Conventions & Norms</strong></td>
      <td>Pre-established behavioral constraints (e.g. drive on right side of road) that resolve collisions without communication overhead.</td>
      <td>Urban autonomous traffic coordination, airspace management.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Formal Agent Architecture Selection & State Modeling</div>
  <p>An engineer is designing an <strong>Automated Air Traffic Collision Avoidance System (TCAS-AI)</strong>. Formally specify:</p>
  <ol>
    <li>The most appropriate Agent Architecture (Simple Reflex, Model-Based, Goal-Based, Utility-Based, or Learning).</li>
    <li>The exact PEAS specification.</li>
    <li>State-Space representation and transition safety invariants.</li>
  </ol>
  <p><strong>Comprehensive Design Solution:</strong></p>
  <ul>
    <li><strong>1. Optimal Architecture:</strong> <em>Utility-Based Agent</em>. Why? Collision avoidance requires balancing multiple conflicting factors under severe sensor noise: maintaining safe 3D separation ($>1000\text{ ft}$ vertical, $>3\text{ miles}$ lateral), passenger comfort (avoiding excessive g-forces), fuel consumption, and air traffic corridor adherence. Binary goal satisfaction is inadequate; continuous utility optimization $\mathbb{E}[U]$ under probabilistic trajectory extrapolation is mandatory!</li>
    <li><strong>2. PEAS Specification:</strong>
      <ul>
        <li><strong>P (Performance):</strong> Zero mid-air collisions ($-\infty$ penalty), minimal deviation from flight plan, smooth acceleration ($< 0.5\text{g}$).</li>
        <li><strong>E (Environment):</strong> 3D Airspace, other aircraft (transponders), wind shear, turbulence, cloud banks.</li>
        <li><strong>A (Actuators):</strong> Flight Management Computer auto-pilot commands (Climb, Descend, Turn Left/Right, Adjust Thrust).</li>
        <li><strong>S (Sensors):</strong> Mode-S Transponder telemetry (altitude, heading, airspeed), Secondary Surveillance Radar (SSR), GPS/ADS-B broadcast receivers, pitot-static airspeed sensors.</li>
      </ul>
    </li>
    <li><strong>3. Mathematical Transition Invariant:</strong>
      $$\forall t, \quad \min_{j \neq i} \|\mathbf{p}_i(t) - \mathbf{p}_j(t)\| \ge D_{\text{safety}} \quad \text{with confidence } P \ge 1 - 10^{-9}$$
    </li>
  </ul>
</div>

<div class="qa-card">
  <div class="qa-q">Q11. Explain the Concept of Teleo-Reactive Agents (Nilsson). How do they differ from finite state machines? (8 Marks)</div>
  <div class="qa-a">
    <strong>Teleo-Reactive (T-R) Agents</strong> execute goal-directed action sequences while remaining continuously sensitive to environmental changes. A T-R program consists of an ordered sequence of production rules: $K_1 \rightarrow A_1, K_2 \rightarrow A_2, \dots, K_m \rightarrow A_m$ where $K_i$ are conditions and $A_i$ are continuous actions. The agent continuously evaluates all conditions and executes the action corresponding to the <em>highest-ranking condition that is currently true</em>. If an unexpected external event undoes progress, the agent automatically drops back to an earlier action without complex exception handling!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q12. What is the Frame Axiom in Agent Knowledge Representation? Detail the Successor-State Axiom. (8 Marks)</div>
  <div class="qa-a">
    In classical situation calculus, <strong>Frame Axioms</strong> specify what properties do NOT change when an action occurs ($P(s') \iff P(s)$). Writing frame axioms for every fluent-action pair requires $O(|F| \cdot |A|)$ rules, creating computational explosion.<br>
    <strong>Successor-State Axioms (Reiter):</strong> Provide an elegant solution by writing one axiom per <em>fluent</em> rather than per action:<br>
    $$\mathbf{F(t+1) \iff [\text{Action causes } F \text{ to become True}] \lor [F(t) \land \neg(\text{Action causes } F \text{ to become False})]}$$
    This completely eliminates the Frame Problem in deterministic environments!
  </div>
</div>
"""

# In-depth expansion for Module 2
M2_BOOST = r"""
<h2 class="section-title">Topic 13.4: Advanced Heuristic Topologies & Bidirectional Search Mathematics</h2>

<div class="formula-card">
  <strong>Bidirectional $A^*$ Termination & Bounded Heuristic Error:</strong>
  In Bidirectional $A^*$ search (searching forward from $S_0$ and backward from $Goal$), let $f_F(n) = g_F(n) + h_F(n)$ and $f_B(n) = g_B(n) + h_B(n)$. The search terminates with guaranteed global optimality when:
  $$\mathbf{\max(\min_{u \in \text{Frontier}_F} f_F(u), \min_{v \in \text{Frontier}_B} f_B(v)) \ge C^* \quad (\text{or } f_F(u) + f_B(v) \ge \mu)}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Non-Trivial 15-Puzzle Pattern Database Heuristics</div>
  <p>Explain how <strong>Disjoint Pattern Databases</strong> are constructed for the 15-Puzzle and prove why they are strictly admissible.</p>
  <ol>
    <li><strong>Concept:</strong> Partition the 15 tiles into disjoint subsets (e.g. 7-8 partition: Tiles $\{1,2,3,4,5,6,7\}$ in Pattern DB 1; Tiles $\{8,9,10,11,12,13,14,15\}$ in Pattern DB 2).</li>
    <li><strong>Precomputation:</strong> Run backward Breadth-First Search from the goal state, abstracting all other tiles into blanks. Record the exact minimal number of moves required to solve the pattern tiles into a lookup table.</li>
    <li><strong>Disjoint Additivity:</strong> Since moving a tile in Group 1 does not count as a move for Group 2, and the pattern groups are strictly disjoint, the sum of heuristics is:
      $$\mathbf{h_{\text{combined}}(n) = h_{\text{DB1}}(n) + h_{\text{DB2}}(n) \le h^*(n)}$$
    </li>
    <li><strong>Performance:</strong> Reduces node expansions by over $\mathbf{10^6}$ compared to Manhattan distance alone!</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Numerical: $A^*$ Search with Inconsistent Heuristic Trace</div>
  <p>Consider graph: $S \xrightarrow{1} A \xrightarrow{1} B \xrightarrow{1} G$, with direct edge $S \xrightarrow{2.5} B$.</p>
  <ul>
    <li>Heuristics: $h(S) = 2, \ h(A) = 3 \ (\text{Inconsistent! } h(S) \not\le c(S,A) + h(A) = 1 + 3), \ h(B) = 1, \ h(G) = 0$.</li>
  </ul>
  <p><strong>Graph Search Trace:</strong></p>
  <ol>
    <li>Start at $S$: Front = $\{ (A: g=1, f=1+3=4), \ (B: g=2.5, f=2.5+1=3.5) \}$.</li>
    <li>Expand $B$ ($f=3.5$): Generates $G$ ($g=2.5+1=3.5, f=3.5$). Closed = $\{S, B\}$.</li>
    <li>Expand $G$ ($f=3.5$): Returns path $S \rightarrow B \rightarrow G$ with cost $3.5$.</li>
    <li><em>Notice:</em> The true optimal path is $S \rightarrow A \rightarrow B \rightarrow G$ (cost $3.0$)! Because $h(A)$ was inconsistent, $A^*$ closed $B$ with a sub-optimal cost!</li>
    <li><strong>Lesson:</strong> Graph Search $A^*$ without node re-opening <em>requires consistency (monotonicity)</em> for guaranteed optimality!</li>
  </ol>
</div>

<div class="qa-card">
  <div class="qa-q">Q11. Explain Beam Search and Stochastic Beam Search. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Beam Search:</strong> A heuristic search optimization that retains only the $k$ best nodes (beam width $k$) at each level of the search tree, discarding all other generated nodes. It drastically limits memory to $O(kB)$ and time to $O(kBd)$, but sacrifices completeness and optimality.<br>
    • <strong>Stochastic Beam Search:</strong> Instead of deterministically choosing the top $k$ successors, it selects $k$ successors probabilistically proportional to their heuristic fitness: $P(n_i) = \frac{e^{f(n_i)/T}}{\sum_j e^{f(n_j)/T}}$, preventing premature convergence to local clusters of similar states.
  </div>
</div>
"""

# In-depth expansion for Module 3
M3_BOOST = r"""
<h2 class="section-title">Topic 22.4: Advanced First-Order Theorem Proving & Clause Normalization</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ The 9-Step Complete First-Order Logic to CNF Conversion Pipeline</div>
  <ol>
    <li><strong>Eliminate Implications:</strong> Replace $\alpha \rightarrow \beta$ with $\neg \alpha \lor \beta$, and $\alpha \leftrightarrow \beta$ with $(\neg \alpha \lor \beta) \land (\neg \beta \lor \alpha)$.</li>
    <li><strong>Move Negations Inward:</strong> Apply De Morgan's Laws and Quantifier Negation Rules ($\neg \forall x P(x) \equiv \exists x \neg P(x)$; $\neg \exists x P(x) \equiv \forall x \neg P(x)$).</li>
    <li><strong>Standardize Variables Apart:</strong> Ensure each quantifier binds a unique variable name (e.g. $(\forall x P(x)) \lor (\forall x Q(x)) \implies (\forall x P(x)) \lor (\forall y Q(y))$).</li>
    <li><strong>Skolemization (Eliminate Existential Quantifiers):</strong> Replace $\exists y$ inside the scope of universal quantifiers $\forall x_1 \dots \forall x_k$ with Skolem function $f(x_1, \dots, x_k)$. If outside any universal quantifier, replace with Skolem constant $A$.</li>
    <li><strong>Drop Universal Quantifiers:</strong> Move all universal quantifiers to front (Prenex Normal Form) and drop prefix ($\forall x$).</li>
    <li><strong>Distribute $\lor$ over $\land$:</strong> Convert matrix to conjunction of disjunctions ($A \lor (B \land C) \equiv (A \lor B) \land (A \lor C)$).</li>
    <li><strong>Flatten Clauses:</strong> Split into individual disjunctive clauses.</li>
    <li><strong>Standardize Variables per Clause:</strong> Ensure no variable name is shared across different clauses.</li>
    <li><strong>Eliminate Tautologies & Subsumption:</strong> Remove clauses containing $P \lor \neg P$ and discard redundant subsumed clauses.</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Proof: The "Col. West is a Criminal" FOL Resolution Proof</div>
  <p><strong>Axioms:</strong></p>
  <ol>
    <li>"It is a crime for an American to sell weapons to hostile nations."<br>
      $\forall x \forall y \forall z (\text{American}(x) \land \text{Weapon}(y) \land \text{Sells}(x, y, z) \land \text{Hostile}(z) \rightarrow \text{Criminal}(x))$<br>
      $\implies \neg \text{American}(x) \lor \neg \text{Weapon}(y) \lor \neg \text{Sells}(x, y, z) \lor \neg \text{Hostile}(z) \lor \text{Criminal}(x)$</li>
    <li>"Nono has some missiles." $\implies \exists x (\text{Missile}(x) \land \text{Owns}(\text{Nono}, x)) \implies \mathbf{\text{Missile}(M_1)}, \ \mathbf{\text{Owns}(\text{Nono}, M_1)}$</li>
    <li>"All of its missiles were sold to it by Col. West." $\implies \forall x (\text{Missile}(x) \land \text{Owns}(\text{Nono}, x) \rightarrow \text{Sells}(\text{West}, x, \text{Nono})) \implies \neg \text{Missile}(x) \lor \neg \text{Owns}(\text{Nono}, x) \lor \text{Sells}(\text{West}, x, \text{Nono})$</li>
    <li>"Missiles are weapons." $\implies \forall x (\text{Missile}(x) \rightarrow \text{Weapon}(x)) \implies \neg \text{Missile}(x) \lor \text{Weapon}(x)$</li>
    <li>"An enemy of America is hostile." $\implies \forall x (\text{Enemy}(x, \text{America}) \rightarrow \text{Hostile}(x)) \implies \neg \text{Enemy}(x, \text{America}) \lor \text{Hostile}(x)$</li>
    <li>"West is an American." $\implies \mathbf{\text{American}(\text{West})}$</li>
    <li>"Nono is an enemy of America." $\implies \mathbf{\text{Enemy}(\text{Nono}, \text{America})}$</li>
  </ol>
  <p><strong>Refutation:</strong> Negated Query: $\mathbf{\neg \text{Criminal}(\text{West})}$.</p>
  <p><strong>Proof Steps:</strong></p>
  <ol>
    <li>Resolve Negated Query with Clause 1 $\{x/\text{West}\} \implies \neg \text{American}(\text{West}) \lor \neg \text{Weapon}(y) \lor \neg \text{Sells}(\text{West}, y, z) \lor \neg \text{Hostile}(z)$.</li>
    <li>Resolve with Clause 6 ($\text{American}(\text{West})) \implies \neg \text{Weapon}(y) \lor \neg \text{Sells}(\text{West}, y, z) \lor \neg \text{Hostile}(z)$.</li>
    <li>Resolve with Clause 4 $\{y/x\} \implies \neg \text{Missile}(y) \lor \neg \text{Sells}(\text{West}, y, z) \lor \neg \text{Hostile}(z)$.</li>
    <li>Resolve with Clause 2 ($\text{Missile}(M_1)) \{y/M_1\} \implies \neg \text{Sells}(\text{West}, M_1, z) \lor \neg \text{Hostile}(z)$.</li>
    <li>Resolve with Clause 3 $\{x/M_1\} \implies \neg \text{Missile}(M_1) \lor \neg \text{Owns}(\text{Nono}, M_1) \lor \neg \text{Hostile}(\text{Nono})$.</li>
    <li>Resolve with Clause 2 ($\text{Missile}(M_1)$ and $\text{Owns}(\text{Nono}, M_1)) \implies \neg \text{Hostile}(\text{Nono})$.</li>
    <li>Resolve with Clause 5 $\implies \neg \text{Enemy}(\text{Nono}, \text{America})$.</li>
    <li>Resolve with Clause 7 ($\text{Enemy}(\text{Nono}, \text{America})) \implies \mathbf{\Box \text{ (EMPTY CLAUSE)}}$.</li>
  </ol>
  $$\mathbf{\text{Q.E.D. Proven that Col. West is a criminal!}}$$
</div>
"""

# In-depth expansion for Module 4
M4_BOOST = r"""
<h2 class="section-title">Topic 29.4: Markov Decision Processes (MDPs) & Value Iteration</h2>

<p>
  When an agent acts in a fully observable, stochastic environment with sequential rewards, the problem is formulated as a <strong>Markov Decision Process (MDP)</strong>:
</p>

<div class="formula-card">
  <strong>The 5-Tuple MDP Definition:</strong>
  $$\mathbf{\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, \mathcal{P}(s' \mid s, a), \mathcal{R}(s, a, s'), \gamma \rangle}$$
  Where $\gamma \in [0, 1)$ is the discount factor. The goal is to discover the <strong>Optimal Policy $\pi^*(s)$</strong> maximizing infinite-horizon expected discounted return:
  $$\mathbf{U^\pi(s) = \mathbb{E}\left[ \sum_{t=0}^\infty \gamma^t R(s_t, a_t, s_{t+1}) \ \middle|\  s_0 = s, \pi \right]}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ The Value Iteration Algorithm (Dynamic Programming)</div>
  <p>Value iteration iteratively updates state utilities using the <strong>Bellman Update Equation</strong> until convergence ($\|U_{k+1} - U_k\| < \frac{\epsilon(1-\gamma)}{\gamma}$):</p>
  $$\mathbf{U_{k+1}(s) \leftarrow \max_{a \in \mathcal{A}} \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma U_k(s') \right]}$$
  <p>Once utilities converge, the optimal policy is extracted greedily:</p>
  $$\mathbf{\pi^*(s) = \arg\max_{a \in \mathcal{A}} \sum_{s'} P(s' \mid s, a) \left[ R(s, a, s') + \gamma U^*(s') \right]}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Value Iteration on Gridworld</div>
  <p>Consider a 2-state MDP with states $\{S_1, S_2\}$, actions $\{a_1, a_2\}$, discount factor $\gamma = 0.9$:</p>
  <ul>
    <li>In $S_1$, action $a_1$ stays in $S_1$ with prob 0.8 ($R=+2$) and transitions to $S_2$ with prob 0.2 ($R=0$).</li>
    <li>In $S_1$, action $a_2$ moves to $S_2$ deterministically ($R=+5$).</li>
    <li>$S_2$ is an absorbing terminal state ($U(S_2) = 0$).</li>
  </ul>
  <p><strong>Iteration 1 ($U_0(S_1) = 0, U_0(S_2) = 0$):</strong></p>
  $$Q_1(S_1, a_1) = 0.8[2 + 0.9(0)] + 0.2[0 + 0.9(0)] = 1.6$$
  $$Q_1(S_1, a_2) = 1.0[5 + 0.9(0)] = 5.0 \implies \mathbf{U_1(S_1) = \max(1.6, 5.0) = \mathbf{5.0}}$$
  <p><strong>Iteration 2:</strong></p>
  $$Q_2(S_1, a_1) = 0.8[2 + 0.9(5.0)] + 0.2[0 + 0.9(0)] = 0.8[2 + 4.5] = 0.8(6.5) = 5.2$$
  $$Q_2(S_1, a_2) = 1.0[5 + 0.9(0)] = 5.0 \implies \mathbf{U_2(S_1) = \max(5.2, 5.0) = \mathbf{5.2}}$$
  <p><em>Optimal Policy:</em> Initially choose $a_2$, but once future value is accounted for, $a_1$ is preferred ($\pi^*(S_1) = a_1$)!</p>
</div>
"""

# In-depth expansion for Module 5
M5_BOOST = r"""
<h2 class="section-title">Topic 38.4: Advanced Deep Learning & Convolutional / Recurrent Architectures</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Architecture</th>
      <th style="width: 40%;">Core Mathematical Formulation</th>
      <th>Key Strengths & AI Domains</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Convolutional Neural Network (CNN)</strong></td>
      <td>Convolution: $(I * K)(i, j) = \sum_m \sum_n I(i-m, j-n) K(m, n)$. Feature maps with parameter sharing and translational equivariance. Max Pooling.</td>
      <td>Computer Vision, medical image radiology, visual object detection.</td>
    </tr>
    <tr>
      <td><strong>Recurrent Neural Network (LSTM)</strong></td>
      <td>Forget Gate: $f_t = \sigma(W_f x_t + U_f h_{t-1} + b_f)$, Cell State: $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$, Output: $h_t = o_t \odot \tanh(C_t)$.</td>
      <td>Sequential data, time series forecasting, speech signal processing.</td>
    </tr>
    <tr>
      <td><strong>Transformer (Self-Attention)</strong></td>
      <td>$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$. Multi-Head Attention. Fully parallelizable matrix multiplication.</td>
      <td>Large Language Models (GPT-4, Gemini, Claude), multimodal reasoning.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Numerical: Convolutional Layer Output Dimensions</div>
  <p>An input image of dimension $W \times H = 224 \times 224$ with $C = 3$ channels passes through a convolutional layer with $K = 64$ filters of size $F \times F = 7 \times 7$, stride $S = 2$, and padding $P = 3$.</p>
  <p><strong>1. Output Spatial Dimensions:</strong></p>
  $$\mathbf{W_{\text{out}} = \left\lfloor \frac{W - F + 2P}{S} \right\rfloor + 1 = \left\lfloor \frac{224 - 7 + 2(3)}{2} \right\rfloor + 1 = \left\lfloor \frac{223}{2} \right\rfloor + 1 = 111 + 1 = \mathbf{112}}$$
  $$\mathbf{\text{Output Feature Map Volume: } 112 \times 112 \times 64}$$
  <p><strong>2. Total Learnable Parameters:</strong></p>
  $$\mathbf{\text{Weights: } (F \times F \times C) \times K = (7 \times 7 \times 3) \times 64 = 147 \times 64 = 9408}$$
  $$\mathbf{\text{Biases: } 64 \implies \text{Total Parameters} = 9408 + 64 = \mathbf{9472}}$$
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

def push_ai_all():
    m1_final = AI_M1_EXHAUSTIVE + M1_BOOST
    m2_final = AI_M2_EXHAUSTIVE + M2_BOOST
    m3_final = AI_M3_EXHAUSTIVE + M3_BOOST
    m4_final = AI_M4_EXHAUSTIVE + M4_BOOST
    m5_final = AI_M5_EXHAUSTIVE + M5_BOOST

    # Save to files
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
    push_ai_all()
