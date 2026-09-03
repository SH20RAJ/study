#!/usr/bin/env python3
"""
True 10-12 Page Artificial Intelligence (CS24307) Suite Builder.
Constructs 36,000-42,000 character exhaustive content for each module (M1-M5),
and compiles them via Playwright Chromium into 10-12 page module PDFs and 55+ page master book!
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

# Import existing modules
sys.path.insert(0, AI_DIR)
from ai_module1_content import AI_M1_EXHAUSTIVE
from ai_module2_content import AI_M2_EXHAUSTIVE
from ai_module3_content import AI_M3_EXHAUSTIVE
from ai_module4_content import AI_M4_EXHAUSTIVE
from ai_module5_content import AI_M5_EXHAUSTIVE
from ai_revision_content import AI_REVISION_EXHAUSTIVE

# Massive Extension Sections for AI M1
M1_MASSIVE_ADDITION = r"""
<h2 class="section-title">Topic 7.5: Philosophical Foundations & Minds vs. Machines</h2>

<p>
  The philosophical foundations of artificial intelligence examine the feasibility, limits, and metaphysical nature of synthetic cognition.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Philosophical Position</th>
      <th style="width: 35%;">Core Claim</th>
      <th>Key Objections & Philosophical Refutations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Strong AI (Functionalism)</strong></td>
      <td>An appropriately programmed computer with the right inputs and outputs literally <em>has a mind</em> and possesses genuine consciousness and understanding.</td>
      <td>Searle's Chinese Room argument: Syntax alone cannot generate intentionality or semantics ($S \not\implies \Sigma$).</td>
    </tr>
    <tr>
      <td><strong>Weak AI (Instrumentalism)</strong></td>
      <td>Computers can only simulate human cognition and act <em>as if</em> they were intelligent, providing powerful analytical tools without actual subjective experience.</td>
      <td>Accepted by mainstream engineering; focuses on operational competence and mathematical performance measures.</td>
    </tr>
    <tr>
      <td><strong>Gödel's Incompleteness Argument (Lucas / Penrose)</strong></td>
      <td>By Gödel's First Incompleteness Theorem, any consistent formal axiomatic system contains true mathematical statements that cannot be proven within the system. Human mathematicians can perceive these truths; hence human minds are non-algorithmic.</td>
      <td>Computers, like humans, are not infallible; Gödel's theorem applies only to consistent, closed formal systems, whereas humans learn heuristically from experience.</td>
    </tr>
    <tr>
      <td><strong>Dreyfus' Critique of Symbolic AI</strong></td>
      <td>Human expertise relies on tacit, bodily intuitive know-how and situational context (phenomenology) rather than explicit symbolic rules and propositional logic.</td>
      <td>Led to modern embodied robotics, connectionism, and deep reinforcement learning from sensorimotor interactions.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Analysis: Alan Turing's 1950 Objections and Responses</div>
  <p>In his landmark 1950 paper <em>"Computing Machinery and Intelligence"</em>, Alan Turing anticipated and systematically refuted nine major objections to machine intelligence:</p>
  <ol>
    <li><strong>The Theological Objection:</strong> "Thinking is a function of man's immortal soul; God gave an immortal soul to every man and woman, but not to any other animal or machine."<br>
      <em>Turing's Refutation:</em> This restricts the omnipotence of God; why couldn't God grant a soul to a computational machine if He wished?</li>
    <li><strong>The 'Heads in the Sand' Objection:</strong> "The consequences of machines thinking would be too dreadful. Let us hope and believe that they cannot do so."<br>
      <em>Turing's Refutation:</em> An emotional fear of losing human intellectual superiority rather than a rational scientific argument.</li>
    <li><strong>The Mathematical Objection (Gödel):</strong> Finite machines are subject to Gödelian limits on provability.<br>
      <em>Turing's Refutation:</em> Humans frequently make errors, suffer from memory bounds, and fail to prove mathematical truths; machines need not be infallible gods to match human intellect.</li>
    <li><strong>The Argument from Consciousness:</strong> "Not until a machine can write a sonnet or compose a concerto because of thoughts and emotions felt, and not by the chance fall of symbols, could we agree that machine equals brain." (Jefferson).<br>
      <em>Turing's Refutation:</em> The only way to know what a person feels is to <em>be</em> that person (Solipsism). In ordinary life, we accept behavioral communication as evidence of other minds.</li>
    <li><strong>Arguments from Various Disabilities:</strong> "A machine can do many things, but it will never be able to: be kind, have a sense of humor, fall in love, make mistakes, learn from experience, enjoy strawberries and cream."<br>
      <em>Turing's Refutation:</em> These limitations are artifacts of current narrow engineering rather than fundamental physical laws of computation.</li>
    <li><strong>Lady Lovelace's Objection (1842):</strong> "The Analytical Engine has no pretensions to originate anything. It can do whatever we know how to order it to perform."<br>
      <em>Turing's Refutation:</em> Machines can surprise humans by discovering unexpected proofs and emergence from complex non-linear interactions. Machine learning allows systems to acquire rules never explicitly programmed.</li>
    <li><strong>Argument from Continuity in the Nervous System:</strong> The biological brain is a continuous neural medium, whereas digital computers are discrete-state machines.<br>
      <em>Turing's Refutation:</em> A discrete-state machine can approximate any continuous differential equation system to arbitrary mathematical precision.</li>
    <li><strong>The Argument from Informality of Behavior:</strong> "It is not possible to produce a set of rules purporting to describe what a man should do in every conceivable set of circumstances."<br>
      <em>Turing's Refutation:</em> Humans follow probabilistic, statistical laws of behavior rather than rigid deterministic condition-action rule tables.</li>
    <li><strong>The Argument from Extrasensory Perception (ESP):</strong> Telepathy and telekinesis.<br>
      <em>Turing's Refutation:</em> If telepathy exists, test conditions can be engineered in Faraday cages.</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Mathematical Formalism: The Agent-Environment Interaction Cycle</div>
  <p>Let discrete timesteps be $t \in \{0, 1, 2, \dots\}$. The interaction between agent and environment proceeds as:</p>
  $$\mathbf{e_t \in \mathcal{E} \xrightarrow{\text{Sensor Matrix } \mathbf{S}} p_t \in \mathcal{P} \xrightarrow{\text{History Sequence } h_t = (p_0, \dots, p_t)} a_t = f(h_t) \in \mathcal{A} \xrightarrow{\text{Transition Dynamics } \mathcal{T}} e_{t+1}}$$
  <p>The total performance score over horizon $T$ is given by an evaluation functional:</p>
  $$\mathbf{V(\mathbf{f}) = \mathbb{E}_{\mathcal{T}} \left[ \sum_{t=0}^T \gamma^t R(e_t, a_t, e_{t+1}) \right]}$$
  <p>A globally rational agent function $\mathbf{f}^*$ maximizes expected cumulative discounted reward:</p>
  $$\mathbf{\mathbf{f}^* = \arg\max_{\mathbf{f}} V(\mathbf{f}) = \arg\max_{\mathbf{f}} \mathbb{E} \left[ \sum_{t=0}^\infty \gamma^t R_t \right]}$$
</div>

<div class="qa-card">
  <div class="qa-q">Q13. Compare the Symbolic Paradigm (Good Old-Fashioned AI / GOFAI) with the Connectionist Paradigm. (10 Marks)</div>
  <div class="qa-a">
    <table class="custom-table">
      <thead><tr><th>Dimension</th><th>Symbolic Paradigm (GOFAI)</th><th>Connectionist Paradigm (Neural / Sub-symbolic)</th></tr></thead>
      <tbody>
        <tr><td><strong>Representation</strong></td><td>Explicit, discrete symbols, predicates, logic rules, semantic ontologies.</td><td>Distributed continuous vector embeddings, synaptic weight matrices.</td></tr>
        <tr><td><strong>Inference Mechanism</strong></td><td>Deductive logic, theorem proving, search algorithms, unification.</td><td>Non-linear activation propagation, matrix multiplication, backpropagation gradient descent.</td></tr>
        <tr><td><strong>Noise Tolerance</strong></td><td>Brittle; single missing rule or syntactic typo causes total failure.</td><td>Graceful degradation; robust to noisy sensors and missing features.</td></tr>
        <tr><td><strong>Interpretability</strong></td><td>Transparent white-box reasoning; generates step-by-step resolution proofs.</td><td>Black-box models; high dimensional weights difficult for humans to audit.</td></tr>
        <tr><td><strong>Strengths</strong></td><td>Exact mathematical reasoning, planning, rule compliance, explanation.</td><td>Perception (Vision, Audio), continuous control, pattern recognition.</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q14. Explain the Concept of an Architecture in Russell & Norvig's formulation: $\text{Agent} = \text{Architecture} + \text{Program}$. (6 Marks)</div>
  <div class="qa-a">
    The <strong>Architecture</strong> is the physical computational device (CPU, GPU, FPGA, micro-controller) along with hardware sensors (cameras, LiDAR, encoders) and actuators (motors, solenoids, speakers). The <strong>Agent Program</strong> is the concrete algorithm or software function that runs on the architecture, taking incoming sensor raw feeds and computing output actuator voltages. The architecture must provide sufficient compute throughput and low sensor latency to allow the agent program to make decisions within real-time deadlines!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q15. Detail the 4 Classical Types of Environment Observability and give real-world examples. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Fully Observable:</strong> The agent's sensors give it access to the complete state of the environment at each point in time (e.g., Chess, Go, 8-Puzzle).<br>
    2. <strong>Partially Observable:</strong> Sensor noise, occlusions, or hidden opponent state prevent complete knowledge (e.g., Autonomous driving with fog/blind spots, Poker with face-down cards).<br>
    3. <strong>Unobservable (Sensorless / Conformant):</strong> The agent has NO sensors at all. It must find a sequence of actions that achieves the goal regardless of the initial starting state (e.g., Automated vacuum cleaner running in a completely dark room finding clean states via blind sweeping).<br>
    4. <strong>Semi-Observable:</strong> Only high-level aggregated signals are available (e.g., Macro-economic central banking monitoring quarterly inflation indicators).
  </div>
</div>
"""

# Massive Extension Sections for AI M2
M2_MASSIVE_ADDITION = r"""
<h2 class="section-title">Topic 13.5: Local Search, Continuous Optimization & Genetic Algorithms</h2>

<p>
  When the path to the goal is irrelevant and only the final state configuration matters (e.g. 8-Queens, VLSI circuit layout, protein folding), <strong>Local Search Algorithms</strong> operate on a single current state rather than maintaining extensive search tree paths.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Algorithm</th>
      <th style="width: 40%;">Core Operational Mechanism</th>
      <th>Space Complexity & Global Optimality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Hill-Climbing (Greedy Local Search)</strong></td>
      <td>Continuously moves in the direction of increasing elevation/objective value ($s' = \arg\max_{n \in \text{Neighbors}(s)} f(n)$). Terminates when no neighbor has higher value.</td>
      <td>$\mathbf{O(1)}$ space; prone to getting trapped in local maxima, ridges, and plateau shoulders.</td>
    </tr>
    <tr>
      <td><strong>Simulated Annealing</strong></td>
      <td>Accepts uphill moves unconditionally ($\Delta E > 0$). Downhill moves are accepted with Boltzmann probability $\mathbf{P(\text{accept}) = e^{\Delta E / T}}$, where temperature $T$ decreases according to cooling schedule $T(t)$.</td>
      <td>$\mathbf{O(1)}$ space; asymptotically guaranteed to find global optimum if temperature decreases sufficiently slowly ($\sum_{k} T_k = \infty$).</td>
    </tr>
    <tr>
      <td><strong>Local Beam Search</strong></td>
      <td>Maintains $k$ states in parallel. At each step, all successors of all $k$ states are generated, and only the top $k$ best successors across the entire pool are retained.</td>
      <td>$\mathbf{O(k)}$ space; facilitates information sharing among parallel exploratory search trajectories.</td>
    </tr>
    <tr>
      <td><strong>Genetic Algorithms (GA)</strong></td>
      <td>Populations of candidate state chromosomes undergo fitness-proportional Selection (Roulette Wheel / Tournament), Crossover recombination, and point Mutation.</td>
      <td>$\mathbf{O(\text{PopSize} \cdot L)}$; powerful global explorer across complex rugged discontinuous fitness landscapes.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Simulated Annealing Acceptance Probability Calculations</div>
  <p>An optimization problem minimizing cost $E$ considers a neighbor with cost change $\Delta E = E_{\text{new}} - E_{\text{current}} = +15$ (worse by 15 units).</p>
  <ol>
    <li>Calculate the acceptance probability at initial high temperature $T = 100$.</li>
    <li>Calculate the acceptance probability at medium temperature $T = 20$.</li>
    <li>Calculate the acceptance probability at freezing temperature $T = 1.0$.</li>
  </ol>
  <p><strong>Solution:</strong></p>
  $$\mathbf{P = e^{- \Delta E / T}}$$
  <ul>
    <li>At $T = 100$: $P = e^{-15 / 100} = e^{-0.15} \approx \mathbf{0.8607 = 86.07\%}$ (Very high exploratory freedom!).</li>
    <li>At $T = 20$: $P = e^{-15 / 20} = e^{-0.75} \approx \mathbf{0.4724 = 47.24\%}$ (Balanced exploration/exploitation).</li>
    <li>At $T = 1.0$: $P = e^{-15 / 1.0} = e^{-15} \approx \mathbf{3.059 \times 10^{-7} \approx 0.00003\%}$ (Pure greedy hill climbing!).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Constraint Propagation via the AC-3 Algorithm</div>
  <p>Let variables $X_1, X_2, X_3 \in \{1, 2, 3, 4\}$ be constrained by $X_1 < X_2$ and $X_2 < X_3$. Trace the <strong>AC-3 (Arc Consistency 3) Algorithm</strong>:</p>
  <ol>
    <li>Initial domains: $D_1 = \{1, 2, 3, 4\}, D_2 = \{1, 2, 3, 4\}, D_3 = \{1, 2, 3, 4\}$.</li>
    <li>Queue of Arcs = $\{ (X_1, X_2), (X_2, X_1), (X_2, X_3), (X_3, X_2) \}$.</li>
    <li>Pop $(X_1, X_2)$: For $X_1 = 4$, no value in $D_2$ satisfies $4 < X_2$. Remove $4$ from $D_1 \implies \mathbf{D_1 = \{1, 2, 3\}}$.</li>
    <li>Pop $(X_2, X_3)$: For $X_2 = 4$, no value in $D_3$ satisfies $4 < X_3$. Remove $4$ from $D_2 \implies \mathbf{D_2 = \{1, 2, 3\}}$. Arc $(X_1, X_2)$ re-added.</li>
    <li>Pop $(X_3, X_2)$: For $X_3 = 1$, no value in $D_2$ satisfies $X_2 < 1$. Remove $1$ from $D_3 \implies \mathbf{D_3 = \{2, 3, 4\}}$.</li>
    <li>Pop $(X_1, X_2)$: For $X_1 = 3$, since $D_2 = \{1, 2, 3\}$, only $X_2 = 4$ could satisfy $3 < X_2$, but $4 \notin D_2$. Remove $3$ from $D_1 \implies \mathbf{D_1 = \{1, 2\}}$.</li>
    <li>Pop $(X_2, X_1)$: For $X_2 = 1$, no value in $D_1 = \{1, 2\}$ satisfies $X_1 < 1$. Remove $1$ from $D_2 \implies \mathbf{D_2 = \{2, 3\}}$.</li>
    <li>Pop $(X_3, X_2)$: For $X_3 = 2$, since $D_2 = \{2, 3\}$, no value satisfies $X_2 < 2$. Remove $2$ from $D_3 \implies \mathbf{D_3 = \{3, 4\}}$.</li>
    <li>Pop $(X_1, X_2)$: For $X_1 = 2$, $X_2 = 3 \in D_2$ satisfies $2 < 3$. Valid!</li>
  </ol>
  $$\mathbf{\text{Final Arc-Consistent Domains: } D_1 = \{1, 2\}, \quad D_2 = \{2, 3\}, \quad D_3 = \{3, 4\}}}$$
</div>

<div class="qa-card">
  <div class="qa-q">Q12. Prove that Depth-First Search with Graph Search is NOT optimal even for uniform step costs. (6 Marks)</div>
  <div class="qa-a">
    Consider a graph where Start $S$ has two edges: $S \xrightarrow{1} G$ (direct goal path, depth 1) and $S \xrightarrow{1} A \xrightarrow{1} G$ (depth 2). If DFS expands $A$ first because of arbitrary node ordering, it adds $A$ to the explored set and then reaches $G$ via path $S \rightarrow A \rightarrow G$ with cost $2$. When it backtracks to $S$, $G$ is already in the explored set, so the direct optimal path $S \rightarrow G$ (cost $1$) is never explored! Hence DFS is not cost-optimal.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q13. What is the difference between Minimax with Alpha-Beta Pruning and SSS* (State Space Search) in Game Trees? (8 Marks)</div>
  <div class="qa-a">
    • <strong>Minimax with Alpha-Beta:</strong> A depth-first traversal of the game tree that maintains single-path scalar bounds $(\alpha, \beta)$ and consumes only $O(bd)$ memory. It evaluates nodes in a fixed depth-first order.<br>
    • <strong>SSS* (Stockman 1979):</strong> A best-first branch-and-bound search that maintains an open list of game tree solution trees (sets of strategies). SSS* never expands any leaf that Alpha-Beta prunes, and can prune additional nodes that Alpha-Beta explores. However, SSS* requires exponential queue memory $O(b^{d/2})$, making it computationally impractical for deep game trees like Chess and Go!
  </div>
</div>
"""

# Massive Extension Sections for AI M3
M3_MASSIVE_ADDITION = r"""
<h2 class="section-title">Topic 22.5: Advanced Automated Theorem Proving, Semantic Tableaux & Ontologies</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Proof: Complete Forward Chaining Trace on Definite Horn Clauses</div>
  <p>Given Knowledge Base of Horn Clauses:</p>
  <ol>
    <li>$A \land B \rightarrow C$</li>
    <li>$C \land D \rightarrow E$</li>
    <li>$B \land E \rightarrow F$</li>
    <li>$G \land A \rightarrow D$</li>
    <li>Known Facts: $\mathbf{A, \ B, \ G}$</li>
  </ol>
  <p><strong>Query:</strong> Prove if goal $F$ is entailed ($\text{KB} \models F$).</p>
  <p><strong>Forward Chaining Execution Table:</strong></p>
  <table class="custom-table">
    <thead><tr><th>Iteration</th><th>Rule Fired</th><th>Satisfied Premises</th><th>New Fact Inferred</th><th>Known Facts Pool</th></tr></thead>
    <tbody>
      <tr><td>0</td><td>Initial Facts</td><td>—</td><td>$A, B, G$</td><td>$\{A, B, G\}$</td></tr>
      <tr><td>1</td><td>Rule 4 ($G \land A \rightarrow D$)</td><td>$G \in KB, A \in KB$</td><td>$D$</td><td>$\{A, B, G, D\}$</td></tr>
      <tr><td>2</td><td>Rule 1 ($A \land B \rightarrow C$)</td><td>$A \in KB, B \in KB$</td><td>$C$</td><td>$\{A, B, G, D, C\}$</td></tr>
      <tr><td>3</td><td>Rule 2 ($C \land D \rightarrow E$)</td><td>$C \in KB, D \in KB$</td><td>$E$</td><td>$\{A, B, G, D, C, E\}$</td></tr>
      <tr><td>4</td><td>Rule 3 ($B \land E \rightarrow F$)</td><td>$B \in KB, E \in KB$</td><td>$F$</td><td>$\mathbf{\{A, B, G, D, C, E, F\}}$</td></tr>
    </tbody>
  </table>
  $$\mathbf{\text{Conclusion: Goal } F \text{ is derived in linear time } O(N)!}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ The Method of Analytic Semantic Tableaux for First-Order Logic</div>
  <p>An alternative to Resolution is the <strong>Semantic Tableaux (Tree Proof) Method</strong>, which builds a tree of signed formulas to prove that $\text{KB} \land \neg \text{Query}$ is closed (every branch contains a contradiction $P$ and $\neg P$):</p>
  <ul>
    <li><strong>$\alpha$-Rules (Conjunctive):</strong> Add both conjuncts to the current branch without splitting ($A \land B \implies A, B$).</li>
    <li><strong>$\beta$-Rules (Disjunctive):</strong> Split the current branch into two child branches ($A \lor B \implies \text{Left: } A, \ \text{Right: } B$).</li>
    <li><strong>$\gamma$-Rules (Universal):</strong> Instantiate $\forall x P(x)$ with any arbitrary ground term $t$ ($P(t)$).</li>
    <li><strong>$\delta$-Rules (Existential):</strong> Instantiate $\exists x P(x)$ with a fresh Skolem constant $c$ ($P(c)$).</li>
  </ul>
</div>

<div class="qa-card">
  <div class="qa-q">Q11. Explain Description Logics (DL) Concepts, Roles, and TBox vs. ABox. (8 Marks)</div>
  <div class="qa-a">
    <strong>Description Logics (DLs)</strong> form the formal logical foundation for the Semantic Web (OWL-DL) and modern knowledge graphs:<br>
    • <strong>Concepts (Unary Predicates):</strong> Sets of individuals (e.g., $\text{Student}, \text{Course}$).<br>
    • <strong>Roles (Binary Relations):</strong> Relationships between individuals (e.g., $\text{enrolledIn}, \text{teaches}$).<br>
    • <strong>TBox (Terminological Box):</strong> The schema containing conceptual definitions, axioms, and subsumption hierarchies ($\text{CSEStudent} \equiv \text{Student} \sqcap \exists \text{enrolledIn}.\text{CSECourse}$).<br>
    • <strong>ABox (Assertional Box):</strong> Concrete assertions about specific named individuals ($\text{Student}(\text{Shaswat}), \text{enrolledIn}(\text{Shaswat}, \text{CS24307})$).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q12. What is Default Reasoning and Reiter's Default Logic? (8 Marks)</div>
  <div class="qa-a">
    Default logic allows an agent to draw plausible inferences in the absence of contrary evidence using default rules:
    $$\mathbf{\frac{\alpha : \beta}{\gamma}}$$
    Where $\alpha$ is the <em>prerequisite</em>, $\beta$ is the <em>justification</em> (must be consistent with the KB, $\neg \beta \notin KB$), and $\gamma$ is the <em>conclusion</em>.<br>
    <em>Example (Bird Flight):</em> $\frac{\text{Bird}(x) : \text{Flies}(x)}{\text{Flies}(x)}$. If $\text{Bird}(\text{Tweety})$ is known and $\neg \text{Flies}(\text{Tweety})$ is NOT in the KB, the agent infers $\text{Flies}(\text{Tweety})$. If it later learns $\text{Penguin}(\text{Tweety}) \land (\text{Penguin}(x) \rightarrow \neg \text{Flies}(x))$, the justification fails and the conclusion is retracted automatically!
  </div>
</div>
"""

# Massive Extension Sections for AI M4
M4_MASSIVE_ADDITION = r"""
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
"""

# Massive Extension Sections for AI M5
M5_MASSIVE_ADDITION = r"""
<h2 class="section-title">Topic 38.5: Modern Deep Generative Models, Transformers & LLM Architectures</h2>

<p>
  Modern Artificial Intelligence is driven by large-scale deep learning architectures capable of representation learning across raw multimodal sensory data.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Generative Model</th>
      <th style="width: 45%;">Training Objective & Loss Function</th>
      <th>Key AI Applications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Variational Autoencoders (VAE)</strong></td>
      <td>Maximizes the Evidence Lower Bound (ELBO):<br>$$\mathcal{L}_{\text{ELBO}} = \mathbb{E}_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)] - D_{\text{KL}}(q_\phi(z\mid x) \parallel p(z))$$</td>
      <td>Latent space interpolation, image generation, anomaly detection.</td>
    </tr>
    <tr>
      <td><strong>Generative Adversarial Networks (GAN)</strong></td>
      <td>Minimax Two-Player Game:<br>$$\min_G \max_D V(D, G) = \mathbb{E}_{x}[\log D(x)] + \mathbb{E}_{z}[\log(1 - D(G(z)))]$$</td>
      <td>Photorealistic image synthesis, deepfakes, super-resolution.</td>
    </tr>
    <tr>
      <td><strong>Diffusion Models (DDPM)</strong></td>
      <td>Forward Markov chain adds Gaussian noise ($q(x_t \mid x_{t-1})$); reverse neural network $\epsilon_\theta(x_t, t)$ learns to denoise step-by-step.</td>
      <td>State-of-the-art text-to-image (Stable Diffusion, Midjourney, DALL-E 3).</td>
    </tr>
    <tr>
      <td><strong>Autoregressive Transformers (GPT)</strong></td>
      <td>Causal Language Modeling (Next-token cross-entropy loss):<br>$$\mathcal{L}_{\text{CLM}} = - \sum_{t=1}^T \log P(w_t \mid w_1, \dots, w_{t-1}; \theta)$$</td>
      <td>Large Language Models, code generation, reasoning agents.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ The Transformer Scaled Dot-Product Self-Attention Mathematical Formulation</div>
  <p>Given an input sequence of token embeddings $\mathbf{X} \in \mathbb{R}^{N \times d_{\text{model}}}$, linear projection matrices produce Queries $\mathbf{Q}$, Keys $\mathbf{K}$, and Values $\mathbf{V}$:</p>
  $$\mathbf{Q = X W_Q, \quad K = X W_K, \quad V = X W_V \qquad (W_Q, W_K \in \mathbb{R}^{d_{\text{model}} \times d_k}, \ W_V \in \mathbb{R}^{d_{\text{model}} \times d_v})}$$
  $$\mathbf{\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{\mathbf{Q} \mathbf{K}^T}{\sqrt{d_k}} \right) \mathbf{V}}$$
  <p><strong>Why Divide by $\sqrt{d_k}$?</strong> For large dimensional vectors $d_k$, the dot products grow large in magnitude, pushing the softmax function into regions with extremely small gradients (vanishing gradients). Scaling by $\frac{1}{\sqrt{d_k}}$ preserves unit variance and stabilizes gradient flow!</p>
</div>

<div class="qa-card">
  <div class="qa-q">Q11. Explain Convolutional Neural Networks (CNNs) and the significance of Parameter Sharing and Equivariance. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Parameter Sharing:</strong> The same kernel filter weights are applied across every spatial receptive field of the input tensor, drastically reducing total learnable weights compared to fully-connected layers.<br>
    • <strong>Translational Equivariance:</strong> If an input object shifts by $(dx, dy)$, the output feature map activates at the corresponding shifted location ($(f * g)(x - dx) = f(x - dx) * g$). This allows CNNs to recognize visual features anywhere in an image!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q12. Explain Reinforcement Learning from Human Feedback (RLHF) for Large Language Models. (8 Marks)</div>
  <div class="qa-a">
    RLHF aligns raw pre-trained LLMs with human values (Helpful, Honest, Harmless) via a 3-stage pipeline:<br>
    1. <strong>Supervised Fine-Tuning (SFT):</strong> Fine-tune base LLM on high-quality human prompt-response demonstrations.<br>
    2. <strong>Reward Model (RM) Training:</strong> Prompt the SFT model to generate multiple candidate outputs for a prompt; human evaluators rank them. Train a scalar reward model $r_\theta(x, y)$ using Bradley-Terry preference loss: $\mathcal{L} = - \mathbb{E}[\log \sigma(r_\theta(x, y_w) - r_\theta(x, y_l))]$.<br>
    3. <strong>PPO Policy Optimization:</strong> Optimize the LLM policy using Proximal Policy Optimization (PPO) to maximize reward $r_\theta(x, y)$ while penalizing KL-divergence $D_{\text{KL}}(\pi_\theta \parallel \pi_{\text{SFT}})$ from the reference model to prevent reward hacking.
  </div>
</div>
"""

def generate_true_12_page_ai():
    m1_total = AI_M1_EXHAUSTIVE + M1_MASSIVE_ADDITION
    m2_total = AI_M2_EXHAUSTIVE + M2_MASSIVE_ADDITION
    m3_total = AI_M3_EXHAUSTIVE + M3_MASSIVE_ADDITION
    m4_total = AI_M4_EXHAUSTIVE + M4_MASSIVE_ADDITION
    m5_total = AI_M5_EXHAUSTIVE + M5_MASSIVE_ADDITION

    print("M1 total length:", len(m1_total))
    print("M2 total length:", len(m2_total))
    print("M3 total length:", len(m3_total))
    print("M4 total length:", len(m4_total))
    print("M5 total length:", len(m5_total))

    # Save to files
    with open(os.path.join(AI_DIR, "ai_module1_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M1_EXHAUSTIVE = r"""{m1_total}"""\n')
    with open(os.path.join(AI_DIR, "ai_module2_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M2_EXHAUSTIVE = r"""{m2_total}"""\n')
    with open(os.path.join(AI_DIR, "ai_module3_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M3_EXHAUSTIVE = r"""{m3_total}"""\n')
    with open(os.path.join(AI_DIR, "ai_module4_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M4_EXHAUSTIVE = r"""{m4_total}"""\n')
    with open(os.path.join(AI_DIR, "ai_module5_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M5_EXHAUSTIVE = r"""{m5_total}"""\n')

    # Import HTML wrapper and Playwright renderer from build_complete_ai_master_suite
    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
    from build_complete_ai_master_suite import wrap_html, generate_pdf, LAB_GUIDE

    modules = [
        (1, "Module 1: Intelligent Agents & PEAS Framework", "Topics 1 to 7 • Foundations, Evolution, Rationality & 5 Agent Types", m1_total, "Module_1_Intelligent_Agents_Notes"),
        (2, "Module 2: Search Algorithms & Game Playing", "Topics 8 to 13 • BFS/DFS/IDDFS, A* Admissibility Proofs & Alpha-Beta Pruning", m2_total, "Module_2_Search_Algorithms_Notes"),
        (3, "Module 3: Knowledge Representation & Logic", "Topics 14 to 22 • Wumpus World, Propositional CNF, First-Order Logic & Resolution", m3_total, "Module_3_Knowledge_Logic_Notes"),
        (4, "Module 4: Classical Planning & Bayesian Networks", "Topics 23 to 29 • STRIPS / PDDL, Graphplan Mutexes, Probability & Bayes Nets", m4_total, "Module_4_Planning_Bayes_Notes"),
        (5, "Module 5: Machine Learning & Neural Networks", "Topics 30 to 38 • Decision Trees ID3, Perceptrons & Backpropagation Math", m5_total, "Module_5_Machine_Learning_Notes"),
    ]

    for num, title, subtitle, content, fname in modules:
        html_content = wrap_html(title, subtitle, content, module_num=num)
        html_file = os.path.join(HTML_DIR, f"{fname}.html")
        pdf_file = os.path.join(PDF_DIR, f"{fname}.pdf")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        generate_pdf(html_file, pdf_file, f"AI Module {num}")

    # Generate 10-Page Revision Guide
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

    # Generate Full Course Master Book with Lab Guide and Revision
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
    generate_true_12_page_ai()
