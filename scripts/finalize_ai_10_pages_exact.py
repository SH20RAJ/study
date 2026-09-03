#!/usr/bin/env python3
"""
Finalizes Artificial Intelligence (CS24307) Suite to 100% PASS:
- Every Module (M1 to M5) is exactly 10-12 pages.
- 10-Page Master Revision is 10-13 pages.
- Full Course Master Book is 55+ pages.
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

# Targeted expansions
M1_EXTRA_BOOST = r"""
<h2 class="section-title">Topic 7.7: Ethical Foundations, Safety & Fairness in Autonomous Systems</h2>

<p>
  As autonomous agents transition from laboratory benchmarks to real-world deployment, ethical constraints and safety bounds must be formalized as mathematical invariants within utility functions.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Ethical Dimension</th>
      <th style="width: 35%;">Theoretical Formalization</th>
      <th>Industrial Deployment Standard</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Value Alignment (Nick Bostrom)</strong></td>
      <td>Ensuring an agent's objective utility function $\mathcal{U}$ strictly aligns with true human intent rather than literal narrow specifications (preventing the Paperclip Maximizer catastrophe).</td>
      <td>Inverse Reinforcement Learning (IRL), Cooperative Inverse Reinforcement Learning (CIRL).</td>
    </tr>
    <tr>
      <td><strong>Algorithmic Fairness</strong></td>
      <td><strong>Demographic Parity:</strong> $P(\hat{Y}=1 \mid A=0) = P(\hat{Y}=1 \mid A=1)$; <strong>Equalized Odds:</strong> True positive and false positive rates are equal across protected demographic attributes $A$.</td>
      <td>AI-driven hiring tools, automated credit risk scoring, judicial recidivism prediction.</td>
    </tr>
    <tr>
      <td><strong>Explainability & Interpretability (XAI)</strong></td>
      <td>Generating post-hoc explanations for black-box neural decisions via Local Interpretable Model-agnostic Explanations (LIME) and SHAP (Shapley Additive exPlanations).</td>
      <td>EU AI Act high-risk compliance, FDA medical device diagnostic validation.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Formal Mathematical Fair Decision Metric</div>
  <p>A credit underwriting agent evaluates loan applications from two demographic groups ($A=0, A=1$):</p>
  <ul>
    <li>Group $A=0$: 1000 applicants, 200 approved ($\hat{Y}=1$), 150 repaid ($Y=1$).</li>
    <li>Group $A=1$: 2000 applicants, 600 approved ($\hat{Y}=1$), 450 repaid ($Y=1$).</li>
  </ul>
  <p><strong>1. Demographic Parity Check:</strong></p>
  $$P(\hat{Y}=1 \mid A=0) = \frac{200}{1000} = 0.20 \qquad P(\hat{Y}=1 \mid A=1) = \frac{600}{2000} = 0.30$$
  $$\mathbf{\text{Disparate Impact Ratio: } \frac{0.20}{0.30} = 0.667 < 0.80 \implies \text{Violates 80\% EEOC Rule!}}$$
  <p><strong>2. True Positive Rate (Equality of Opportunity):</strong></p>
  $$\text{TPR}_{A=0} = \frac{\text{True Positives}}{\text{Actual Positives}} = \frac{150}{200} = 0.75 \qquad \text{TPR}_{A=1} = \frac{450}{600} = 0.75$$
  $$\mathbf{\text{Equality of Opportunity is SATISFIED} \ (\text{TPR}_0 = \text{TPR}_1 = 0.75)!}$$
</div>
"""

M2_EXTRA_BOOST = r"""
<h2 class="section-title">Topic 13.7: Advanced Adversarial Search & Monte Carlo Tree Search (MCTS)</h2>

<p>
  In ultra-large state space games where evaluation functions cannot be hand-crafted (e.g. Go, Chess variants), <strong>Monte Carlo Tree Search (MCTS)</strong> uses stochastic rollouts to evaluate positions.
</p>

<div class="diagram-container">
  <svg width="100%" height="70" viewBox="0 0 740 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="15" width="160" height="40" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="90" y="32" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#1e40af" text-anchor="middle">1. SELECTION</text>
    <text x="90" y="45" font-family="Plus Jakarta Sans" font-size="8" fill="#2563eb" text-anchor="middle">Traverse via UCT Formula</text>

    <path d="M 170 35 L 200 35" stroke="#0284c7" stroke-width="1.5"/>

    <rect x="205" y="15" width="160" height="40" rx="4" fill="#fefce8" stroke="#ca8a04" stroke-width="1.2"/>
    <text x="285" y="32" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#854d0e" text-anchor="middle">2. EXPANSION</text>
    <text x="285" y="45" font-family="Plus Jakarta Sans" font-size="8" fill="#a16207" text-anchor="middle">Add New Child Node</text>

    <path d="M 365 35 L 395 35" stroke="#0284c7" stroke-width="1.5"/>

    <rect x="400" y="15" width="160" height="40" rx="4" fill="#faf5ff" stroke="#a855f7" stroke-width="1.2"/>
    <text x="480" y="32" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#581c87" text-anchor="middle">3. SIMULATION</text>
    <text x="480" y="45" font-family="Plus Jakarta Sans" font-size="8" fill="#9333ea" text-anchor="middle">Random Rollout to Terminal</text>

    <path d="M 560 35 L 590 35" stroke="#0284c7" stroke-width="1.5"/>

    <rect x="595" y="15" width="135" height="40" rx="4" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.2"/>
    <text x="662" y="32" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#14532d" text-anchor="middle">4. BACKPROPAGATION</text>
    <text x="662" y="45" font-family="Plus Jakarta Sans" font-size="8" fill="#16a34a" text-anchor="middle">Update Visit Counts & $Q$</text>
  </svg>
  <div class="diagram-caption">Figure 2.1: The Four Discrete Phases of Monte Carlo Tree Search (MCTS / AlphaGo)</div>
</div>

<div class="formula-card">
  <strong>The Upper Confidence Bound for Trees (UCT) Formula:</strong>
  $$\mathbf{\text{UCT}(v_i, v) = \frac{Q(v_i)}{N(v_i)} + c \sqrt{\frac{\ln N(v)}{N(v_i)}} = \text{Exploitation Term} + \text{Exploration Term}}$$
  Where $Q(v_i)$ is total simulation reward, $N(v_i)$ is child visit count, $N(v)$ is parent visit count, and $c = \sqrt{2}$ is the exploration parameter balancing exploitation of winning moves with exploration of rarely visited branches.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: MCTS UCT Calculation</div>
  <p>A parent node $v$ has been visited $N(v) = 100$ times. It has two children $A$ and $B$:</p>
  <ul>
    <li>Child $A$: Visited $N(A) = 60$ times with total wins $Q(A) = 45$.</li>
    <li>Child $B$: Visited $N(B) = 40$ times with total wins $Q(B) = 28$.</li>
  </ul>
  $$\text{UCT}(A) = \frac{45}{60} + \sqrt{2} \sqrt{\frac{\ln 100}{60}} = 0.75 + 1.414 \sqrt{\frac{4.605}{60}} = 0.75 + 1.414(0.277) = 0.75 + 0.392 = \mathbf{1.142}$$
  $$\text{UCT}(B) = \frac{28}{40} + \sqrt{2} \sqrt{\frac{\ln 100}{40}} = 0.70 + 1.414 \sqrt{\frac{4.605}{40}} = 0.70 + 1.414(0.339) = 0.70 + 0.479 = \mathbf{1.179}$$
  $$\mathbf{\text{Selection Decision: Choose Child } B \text{ because its exploration potential (1.179) outweighs Child } A \text{ (1.142)!}}$$
</div>
"""

M3_EXTRA_BOOST = r"""
<h2 class="section-title">Topic 22.7: Advanced Knowledge Graphs & Description Logic Semantics</h2>

<div class="formula-card">
  <strong>Description Logic ($\mathcal{ALC}$) Syntax & Semantics:</strong>
  - Top (Universal Concept): $\top \implies \Delta^\mathcal{I}$ (All domain elements)
  - Bottom (Empty Concept): $\bot \implies \emptyset$
  - Conjunction: $(C \sqcap D)^\mathcal{I} = C^\mathcal{I} \cap D^\mathcal{I}$
  - Disjunction: $(C \sqcup D)^\mathcal{I} = C^\mathcal{I} \cup D^\mathcal{I}$
  - Negation: $(\neg C)^\mathcal{I} = \Delta^\mathcal{I} \setminus C^\mathcal{I}$
  - Universal Role Restriction: $(\forall R.C)^\mathcal{I} = \{ x \in \Delta^\mathcal{I} \mid \forall y ((x, y) \in R^\mathcal{I} \rightarrow y \in C^\mathcal{I}) \}$
  - Existential Role Restriction: $(\exists R.C)^\mathcal{I} = \{ x \in \Delta^\mathcal{I} \mid \exists y ((x, y) \in R^\mathcal{I} \land y \in C^\mathcal{I}) \}$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Description Logic Subsumption Proof</div>
  <p>Prove that $\text{Mother} \sqsubseteq \text{Parent}$ given the TBox axioms:</p>
  <ol>
    <li>$\text{Parent} \equiv \text{Human} \sqcap \exists \text{hasChild}.\text{Human}$</li>
    <li>$\text{Mother} \equiv \text{Woman} \sqcap \exists \text{hasChild}.\text{Human}$</li>
    <li>$\text{Woman} \sqsubseteq \text{Human}$</li>
  </ol>
  <p><strong>Proof Trace:</strong></p>
  <ul>
    <li>Let $x \in \text{Mother}^\mathcal{I} \implies x \in \text{Woman}^\mathcal{I} \land x \in (\exists \text{hasChild}.\text{Human})^\mathcal{I}$.</li>
    <li>Since $\text{Woman}^\mathcal{I} \subseteq \text{Human}^\mathcal{I}$ (Axiom 3), we have $x \in \text{Human}^\mathcal{I}$.</li>
    <li>Therefore, $x \in \text{Human}^\mathcal{I} \land x \in (\exists \text{hasChild}.\text{Human})^\mathcal{I} \implies x \in \text{Parent}^\mathcal{I}$.</li>
    <li>$\mathbf{\text{Q.E.D. Subsumption } \text{Mother} \sqsubseteq \text{Parent} \text{ holds in all models!}}$</li>
  </ul>
</div>
"""

M4_EXTRA_BOOST = r"""
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
"""

M5_EXTRA_BOOST = r"""
<h2 class="section-title">Topic 38.7: Advanced Deep Reinforcement Learning (DQN & Policy Gradients)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Deep RL Algorithm</th>
      <th style="width: 40%;">Core Loss Function & Update Mechanism</th>
      <th>Key Innovations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Deep Q-Networks (DQN)</strong></td>
      <td>$$\mathcal{L}(\theta) = \mathbb{E}\left[ \left( r + \gamma \max_{a'} Q(s', a'; \theta^-) - Q(s, a; \theta) \right)^2 \right]$$</td>
      <td>Experience Replay Buffer (breaks temporal correlation), Target Network $\theta^-$ (stabilizes targets).</td>
    </tr>
    <tr>
      <td><strong>REINFORCE (Policy Gradient)</strong></td>
      <td>$$\nabla_\theta J(\theta) = \mathbb{E}\left[ \sum_{t=0}^T \nabla_\theta \ln \pi_\theta(a_t \mid s_t) G_t \right]$$</td>
      <td>Direct optimization of parameterized policy $\pi_\theta(a\mid s)$ without action-value discretization.</td>
    </tr>
    <tr>
      <td><strong>Actor-Critic (A2C / PPO)</strong></td>
      <td>Actor updates $\pi_\theta(a\mid s)$ using Advantage $A(s,a) = Q(s,a) - V(s)$; Critic updates value function $V_\phi(s)$ via MSE loss.</td>
      <td>Significantly reduces gradient variance while retaining high sample efficiency.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Policy Gradient (REINFORCE) Parameter Update Calculation</div>
  <p>A policy network outputs action probabilities $\pi_\theta(a_1 \mid s) = 0.70, \pi_\theta(a_2 \mid s) = 0.30$ using Softmax over linear logits $z_1 = \theta_1 x, z_2 = \theta_2 x$ with $x = 1.0$. The agent executes action $a_1$ and receives return $G_t = +5.0$. Learning rate $\eta = 0.1$.</p>
  <p><strong>1. Log-Likelihood Gradient for Softmax:</strong></p>
  $$\nabla_{\theta_1} \ln \pi_\theta(a_1 \mid s) = x(1 - \pi_\theta(a_1 \mid s)) = 1.0(1 - 0.70) = \mathbf{+0.30}$$
  $$\nabla_{\theta_2} \ln \pi_\theta(a_1 \mid s) = - x \cdot \pi_\theta(a_2 \mid s) = - 1.0(0.30) = \mathbf{-0.30}$$
  <p><strong>2. Policy Parameter Updates:</strong></p>
  $$\Delta \theta_1 = \eta \cdot \nabla_{\theta_1} \ln \pi(a_1 \mid s) \cdot G_t = 0.1 \times 0.30 \times 5.0 = \mathbf{+0.15}$$
  $$\Delta \theta_2 = \eta \cdot \nabla_{\theta_2} \ln \pi(a_1 \mid s) \cdot G_t = 0.1 \times (-0.30) \times 5.0 = \mathbf{-0.15}$$
  <p><em>Result:</em> $\theta_1$ is boosted by $+0.15$, increasing the probability of choosing successful action $a_1$ in state $s$ on future episodes!</p>
</div>
"""

LAB_GUIDE_INLINE = r"""
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
        self.board = board
        self.parent = parent
        self.action = action
        self.g = g
        self.h = self.calculate_manhattan()
        self.f = self.g + self.h

    def calculate_manhattan(self):
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

def finalize_all_ai():
    m1_final = AI_M1_EXHAUSTIVE + M1_EXTRA_BOOST
    m2_final = AI_M2_EXHAUSTIVE + M2_EXTRA_BOOST
    m3_final = AI_M3_EXHAUSTIVE + M3_EXTRA_BOOST
    m4_final = AI_M4_EXHAUSTIVE + M4_EXTRA_BOOST
    m5_final = AI_M5_EXHAUSTIVE + M5_EXTRA_BOOST

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
    finalize_all_ai()
