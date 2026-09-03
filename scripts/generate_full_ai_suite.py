#!/usr/bin/env python3
"""
Exhaustive AI (CS24307) Content Generator & Playwright PDF Compiler.
Generates 10-15 Page Modules (M1–M5), 10-Page Master Revision, and 50+ Page Full Master Book.
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

# ----------------- MODULE 1 CONTENT -----------------
AI_M1_TEXT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 1 Table of Contents (Topics 1 to 7)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 1:</strong> Foundations & Definitions of AI</div>
    <div>• <strong>Topic 2:</strong> Evolution, AI Winters & Milestones</div>
    <div>• <strong>Topic 3:</strong> Intelligent Agents Architecture</div>
    <div>• <strong>Topic 4:</strong> Concept of Rationality & Performance</div>
    <div>• <strong>Topic 5:</strong> PEAS & Taxonomy of Environments</div>
    <div>• <strong>Topic 6:</strong> 5 Classical Agent Architectures</div>
    <div>• <strong>Topic 7:</strong> Real-World Domains & University Exam Bank</div>
  </div>
</div>

<h2 class="section-title">Topic 1: Foundational Definitions & The Four AI Perspectives</h2>

<p>
  <strong>Artificial Intelligence (AI)</strong> is the branch of computer science devoted to synthesizing computational artifacts capable of performing cognitive tasks traditionally associated with human intellect: perception, inductive/deductive reasoning, learning from experiential data, goal-directed planning, natural language comprehension, and autonomous decision-making under uncertainty.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Dimension</th>
      <th style="width: 38%;">Human-Centric Dimension (Empirical / Cognitive)</th>
      <th>Rationality-Centric Dimension (Ideal / Normative)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Reasoning (Thought)</strong></td>
      <td><strong>Thinking Humanly:</strong> Cognitive Science approach. Formulates computational models of human mental processes via fMRI neuroscience and introspection (e.g. Newell & Simon's General Problem Solver).</td>
      <td><strong>Thinking Rationally:</strong> Laws of Thought approach. Formalizes reasoning using strict deductive logic and syllogisms ($\forall x (P(x) \rightarrow Q(x))$) originating with Aristotle.</td>
    </tr>
    <tr>
      <td><strong>Behavior (Action)</strong></td>
      <td><strong>Acting Humanly:</strong> The Turing Test approach (Alan Turing, 1950). An entity is intelligent if an interrogator cannot distinguish its conversational responses from a human.</td>
      <td><strong>Acting Rationally (Modern Standard):</strong> Rational Agent approach (Russell & Norvig). An agent operates to maximize its <em>expected performance measure</em> given its percept sequence and built-in knowledge.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Deep Dive: The 6 Sub-disciplines Required for the Total Turing Test</div>
  <ol>
    <li><strong>Natural Language Processing (NLP):</strong> Comprehending, parsing, and generating human spoken/written communication.</li>
    <li><strong>Knowledge Representation (KR):</strong> Storing structured ontological assertions, episodic memories, and causal rules.</li>
    <li><strong>Automated Reasoning:</strong> Drawing logically sound inferences, answering queries, and resolving contradictions.</li>
    <li><strong>Machine Learning (ML):</strong> Adapting internal statistical weights to extrapolate patterns and survive novel scenarios.</li>
    <li><strong>Computer Vision (Total Turing Test):</strong> Perceiving and segmenting 3D physical objects from visual sensor streams.</li>
    <li><strong>Robotics & Actuation (Total Turing Test):</strong> Manipulating physical objects and navigating complex terrain.</li>
  </ol>
</div>

<h2 class="section-title">Topic 2: Historical Evolution, Dartmouth 1956 & AI Winters</h2>

<div class="diagram-container">
  <svg width="100%" height="80" viewBox="0 0 740 80" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="20" width="130" height="40" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="75" y="38" font-family="Plus Jakarta Sans" font-size="9.5" font-weight="700" fill="#1e40af" text-anchor="middle">1943–1956</text>
    <text x="75" y="52" font-family="Plus Jakarta Sans" font-size="8.5" fill="#2563eb" text-anchor="middle">McCulloch-Pitts / Dartmouth</text>

    <path d="M 140 40 L 175 40" stroke="#0284c7" stroke-width="1.5"/>

    <rect x="180" y="20" width="125" height="40" rx="4" fill="#fefce8" stroke="#ca8a04" stroke-width="1.2"/>
    <text x="242" y="38" font-family="Plus Jakarta Sans" font-size="9.5" font-weight="700" fill="#854d0e" text-anchor="middle">1974–1980</text>
    <text x="242" y="52" font-family="Plus Jakarta Sans" font-size="8.5" fill="#a16207" text-anchor="middle">First AI Winter</text>

    <path d="M 305 40 L 340 40" stroke="#0284c7" stroke-width="1.5"/>

    <rect x="345" y="20" width="125" height="40" rx="4" fill="#faf5ff" stroke="#a855f7" stroke-width="1.2"/>
    <text x="407" y="38" font-family="Plus Jakarta Sans" font-size="9.5" font-weight="700" fill="#581c87" text-anchor="middle">1980–1987</text>
    <text x="407" y="52" font-family="Plus Jakarta Sans" font-size="8.5" fill="#9333ea" text-anchor="middle">Expert Systems (XCON)</text>

    <path d="M 470 40 L 505 40" stroke="#0284c7" stroke-width="1.5"/>

    <rect x="510" y="20" width="220" height="40" rx="4" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.2"/>
    <text x="620" y="38" font-family="Plus Jakarta Sans" font-size="9.5" font-weight="700" fill="#14532d" text-anchor="middle">1997–Present: Deep Learning</text>
    <text x="620" y="52" font-family="Plus Jakarta Sans" font-size="8.5" fill="#16a34a" text-anchor="middle">Deep Blue, AlphaGo, Transformers & LLMs</text>
  </svg>
  <div class="diagram-caption">Figure 1.1: Chronological Evolution of Artificial Intelligence from Symbolic Logic to Deep Generative Models</div>
</div>

<h2 class="section-title">Topic 3 & 4: Intelligent Agents & Formal Concept of Rationality</h2>

<p>
  An <strong>Agent</strong> is anything that perceives its environment through physical or software sensors and acts upon that environment via actuators. Formally, an agent is mathematically characterized by an <strong>Agent Function</strong> $f$:
</p>

<div class="formula-card">
  <strong>The Mathematical Agent Function:</strong>
  $$\mathbf{f: \mathcal{P}^* \longrightarrow \mathcal{A}}$$
  Where $\mathcal{P}^*$ represents the history of all percept sequences perceived up to the current discrete timestep $t$, and $\mathcal{A}$ is the set of executable actions. The concrete implementation of $f$ running on physical compute hardware is the <strong>Agent Program</strong>.
</div>

<div class="callout callout-info">
  <div class="callout-title"><i class="fa-solid fa-scale-balanced"></i> Rationality vs. Omniscience</div>
  <p>
    • <strong>Rationality:</strong> Maximizes <em>expected performance</em> given the historical percept sequence $\mathcal{P}^*$ and prior built-in knowledge. It does NOT require perfection.<br>
    • <strong>Omniscience:</strong> Knows the <em>actual outcome</em> of its actions in advance (impossible in non-deterministic or partially observable real-world environments).
  </p>
</div>

<h2 class="section-title">Topic 5: PEAS Specification & Environmental Taxonomy</h2>

<p>
  To engineer an intelligent system, one must formally define its <strong>PEAS Framework</strong>:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">System Domain</th>
      <th style="width: 22%;">Performance Measure ($P$)</th>
      <th style="width: 22%;">Environment ($E$)</th>
      <th style="width: 18%;">Actuators ($A$)</th>
      <th>Sensors ($S$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Autonomous Taxi</strong></td>
      <td>Safety, speed, legal compliance, passenger comfort, fuel economy, profit.</td>
      <td>Public roads, pedestrians, traffic lights, weather conditions.</td>
      <td>Steering wheel, accelerator, brakes, horn, turn signals.</td>
      <td>LiDAR, RADAR, cameras, GPS, odometer, engine sensors.</td>
    </tr>
    <tr>
      <td><strong>Medical Diagnosis</strong></td>
      <td>Patient health recovery, diagnosis accuracy, minimized costs and side effects.</td>
      <td>Hospital ward, patient symptoms, lab test facilities.</td>
      <td>Treatment plan, prescription dosage, surgery referral.</td>
      <td>Blood pressure monitor, EHR records, lab results.</td>
    </tr>
    <tr>
      <td><strong>Chess AI (Stockfish)</strong></td>
      <td>Winning game ($+1$), draw ($0$), checkmating opponent, piece advantage.</td>
      <td>$8 \times 8$ Chess board, opponent player, clock timer.</td>
      <td>Move piece command ($e2 \rightarrow e4$).</td>
      <td>Board state matrix representation.</td>
    </tr>
    <tr>
      <td><strong>Automated Warehouse Robot</strong></td>
      <td>Items picked/hour, zero item drops, collision-free transit, battery life.</td>
      <td>Warehouse aisles, shelving racks, human workers.</td>
      <td>Differential drive wheels, robotic gripping arm.</td>
      <td>Ultrasonic rangefinders, barcode scanners, depth camera.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 6: The 5 Classical Agent Structural Architectures</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Agent Architecture</th>
      <th style="width: 45%;">Internal Decision Logic</th>
      <th>Pros & Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Simple Reflex Agent</strong></td>
      <td>Selects actions strictly based on the <em>current instantaneous percept</em> using condition-action rules (`IF car-in-front-braking THEN apply-brakes`). Ignores history.</td>
      <td>Extremely fast; fails completely in partially observable environments (falls into infinite loops).</td>
    </tr>
    <tr>
      <td><strong>2. Model-Based Reflex Agent</strong></td>
      <td>Maintains an internal <strong>State</strong> tracking how the unobserved world evolves independently and how the agent's own actions affect the world.</td>
      <td>Can handle partial observability; requires accurate world physics modeling.</td>
    </tr>
    <tr>
      <td><strong>3. Goal-Based Agent</strong></td>
      <td>Combines internal state with explicit <strong>Goal Descriptions</strong> to evaluate whether candidate action sequences achieve desired end states (uses Search & Planning).</td>
      <td>Highly flexible (goals can change dynamically); slower than reflex lookup.</td>
    </tr>
    <tr>
      <td><strong>4. Utility-Based Agent</strong></td>
      <td>Maps states to real-valued scalar <strong>Utility Values</strong> $U(s) \in \mathbb{R}$ to make optimal trade-offs between competing goals and risk profiles under uncertainty.</td>
      <td>Provides mathematically optimal decision making; computationally intensive.</td>
    </tr>
    <tr>
      <td><strong>5. Learning Agent</strong></td>
      <td>Divided into 4 modules: <em>Learning Element</em> (improves performance), <em>Critic</em> (evaluates against standard), <em>Performance Element</em> (acts), and <em>Problem Generator</em> (experiments).</td>
      <td>Can operate in initially unknown environments and achieve superhuman competence over time.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 7: Master University Examination Solved Question Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Prove why a Simple Reflex Agent cannot operate rationally in a partially observable environment like the Vacuum World. (8 Marks)</div>
  <div class="qa-a">
    In a 2-room vacuum cleaner world where the agent can sense only its current location and cleanliness (not whether the other room is dirty), if both rooms are clean and the agent has no memory, its rule `IF clean THEN MoveRight` followed in Room B by `IF clean THEN MoveLeft` produces an <strong>infinite oscillating loop</strong>. Without internal state memory, it cannot deduce that both rooms have already been cleaned!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Formally classify the Environment of: (a) Poker, (b) Autonomous Driving, and (c) Crossword Puzzle across all 6 environmental dimensions. (10 Marks)</div>
  <div class="qa-a">
    • <strong>(a) Poker:</strong> Partially Observable (hidden cards), Stochastic (card shuffling), Sequential (bets affect later rounds), Static (rules/pot do not change while thinking), Discrete (finite chips/cards), Multi-Agent (Competitive/Adversarial).<br>
    • <strong>(b) Autonomous Driving:</strong> Partially Observable (blind spots, occluded vehicles), Stochastic (erratic drivers, tire slip), Sequential, Dynamic (pedestrians and traffic move while vehicle decides), Continuous (steering angle, velocity), Multi-Agent (Cooperative & Competitive).<br>
    • <strong>(c) Crossword Puzzle:</strong> Fully Observable (entire grid visible), Deterministic (words do not change), Sequential, Static, Discrete (letters and grid cells), Single-Agent.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Detail the components of a Learning Agent with an architectural block diagram. (8 Marks)</div>
  <div class="qa-a">
    A Learning Agent decomposes into four distinct structural units:<br>
    1. <strong>Learning Element:</strong> Responsible for making improvements by analyzing feedback from the critic.<br>
    2. <strong>Critic:</strong> Evaluates the agent's behavior against an external performance standard (provides reward/penalty signals).<br>
    3. <strong>Performance Element:</strong> The operational agent that selects external actions based on percepts (e.g. reflex, model, goal, or utility core).<br>
    4. <strong>Problem Generator:</strong> Suggests novel exploratory actions leading to new experiences rather than just exploiting known sub-optimal paths.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q4. What is the Chinese Room Argument by John Searle? How does it challenge Strong AI? (8 Marks)</div>
  <div class="qa-a">
    <strong>John Searle's Chinese Room Thought Experiment (1980):</strong> A monolingual English speaker sits in a closed room with a rulebook translating incoming Chinese characters into corresponding Chinese output responses. To an outside observer, the room passes the Turing Test in Chinese. However, the human inside does not understand a single word of Chinese; they are merely performing <em>syntactic symbol manipulation</em> without <em>semantic intentionality or true understanding</em>. Searle concludes that functional execution of a computer program cannot produce genuine human-like consciousness (Strong AI).
  </div>
</div>
"""

# ----------------- MODULE 2 CONTENT -----------------
AI_M2_TEXT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 2 Table of Contents (Topics 8 to 13)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 8:</strong> Problem Formulation & State Space</div>
    <div>• <strong>Topic 9:</strong> Uninformed Search (BFS, DFS, UCS, DLS, IDDFS)</div>
    <div>• <strong>Topic 10:</strong> Informed Heuristic Search ($A^*$, Greedy, IDA*)</div>
    <div>• <strong>Topic 11:</strong> Mathematical Admissibility & Consistency Proofs</div>
    <div>• <strong>Topic 12:</strong> Adversarial Game Playing (Minimax Algorithm)</div>
    <div>• <strong>Topic 13:</strong> Alpha-Beta Pruning Traces & Solved Numerical Bank</div>
  </div>
</div>

<h2 class="section-title">Topic 8: Formal Problem Formulation & State Space Representation</h2>

<p>
  A search problem is formally defined by a 5-tuple:
  $$\mathbf{\mathcal{P} = \langle S_0, \text{Actions}(s), \text{Result}(s, a), \text{GoalTest}(s), c(s, a, s') \rangle}$$
  1. <strong>Initial State ($S_0$):</strong> The starting state of the agent.<br>
  2. <strong>Actions ($Actions(s)$):</strong> The set of legal actions applicable in state $s$.<br>
  3. <strong>Transition Model ($Result(s, a)$):</strong> Returns the successor state $s'$ produced by action $a$ in state $s$.<br>
  4. <strong>Goal Test ($GoalTest(s)$):</strong> Boolean function determining if state $s$ is a goal state.<br>
  5. <strong>Path Cost ($c(s, a, s')$):</strong> Step cost of taking action $a$ from state $s$ to $s'$. Total path cost is $g(n) = \sum \text{step costs}$.
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Problem Formulation: The 8-Puzzle Problem</div>
  <ul>
    <li><strong>State:</strong> $3 \times 3$ grid configuration containing numbers $\{1, 2, \dots, 8\}$ and one blank space ($\text{Total States} = 9! / 2 = 181,440$).</li>
    <li><strong>Initial State:</strong> Any given permutation of the 8 tiles and blank.</li>
    <li><strong>Actions:</strong> Move Blank $\{\text{Left}, \text{Right}, \text{Up}, \text{Down}\}$.</li>
    <li><strong>Goal Test:</strong> Matches goal matrix `[[1,2,3],[8,blank,4],[7,6,5]]` (or standard sequential `[[1,2,3],[4,5,6],[7,8,blank]]`).</li>
    <li><strong>Path Cost:</strong> Each tile move costs 1 unit ($g(n) = \text{number of moves}$).</li>
  </ul>
</div>

<h2 class="section-title">Topic 9: Exhaustive Uninformed (Blind) Search Algorithms</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Algorithm</th>
      <th style="width: 18%;">Data Structure</th>
      <th style="width: 18%;">Time Complexity</th>
      <th style="width: 18%;">Space Complexity</th>
      <th style="width: 13%;">Complete?</th>
      <th>Optimal?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Breadth-First Search (BFS)</strong></td>
      <td>FIFO Queue</td>
      <td>$O(b^d)$</td>
      <td>$O(b^d)$ (Severe memory bottle-neck)</td>
      <td><strong>Yes</strong> (if $b < \infty$)</td>
      <td><strong>Yes</strong> (if step costs equal)</td>
    </tr>
    <tr>
      <td><strong>Uniform-Cost Search (UCS)</strong></td>
      <td>Priority Queue by $g(n)$</td>
      <td>$O(b^{1 + \lfloor C^* / \epsilon \rfloor})$</td>
      <td>$O(b^{1 + \lfloor C^* / \epsilon \rfloor})$</td>
      <td><strong>Yes</strong> (if step cost $\ge \epsilon > 0$)</td>
      <td><strong>Yes</strong> (Cost optimal)</td>
    </tr>
    <tr>
      <td><strong>Depth-First Search (DFS)</strong></td>
      <td>LIFO Stack</td>
      <td>$O(b^m)$ ($m = \text{max depth}$)</td>
      <td>$O(b \cdot m)$ (Linear memory!)</td>
      <td>No (Infinite trees)</td>
      <td>No</td>
    </tr>
    <tr>
      <td><strong>Depth-Limited Search (DLS)</strong></td>
      <td>LIFO Stack with limit $l$</td>
      <td>$O(b^l)$</td>
      <td>$O(b \cdot l)$</td>
      <td>No (if $l < d$)</td>
      <td>No</td>
    </tr>
    <tr>
      <td><strong>Iterative Deepening DFS (IDDFS)</strong></td>
      <td>LIFO Stack with increasing $l$</td>
      <td>$O(b^d)$</td>
      <td>$\mathbf{O(b \cdot d)}$ (Best of both worlds!)</td>
      <td><strong>Yes</strong></td>
      <td><strong>Yes</strong> (if step costs equal)</td>
    </tr>
    <tr>
      <td><strong>Bidirectional Search</strong></td>
      <td>Two simultaneous Queues</td>
      <td>$O(b^{d/2})$</td>
      <td>$O(b^{d/2})$</td>
      <td><strong>Yes</strong></td>
      <td><strong>Yes</strong> (if step costs equal)</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 10 & 11: Informed Heuristic Search ($A^*$) & Mathematical Proofs</h2>

<p>
  <strong>$A^*$ Search</strong> evaluates frontier nodes by the total estimated path cost function:
  $$\mathbf{f(n) = g(n) + h(n)}$$
  Where $g(n)$ is the exact cost from initial state to node $n$, and $h(n)$ is the estimated cost from node $n$ to the closest goal state.
</p>

<div class="formula-card">
  <strong>1. Admissibility Property (Tree-Search Optimality):</strong>
  A heuristic $h(n)$ is <strong>admissible</strong> if it never overestimates the true minimal cost $h^*(n)$ to reach the goal:
  $$\mathbf{0 \le h(n) \le h^*(n) \quad \forall n}$$
  <strong>2. Consistency / Monotonicity Property (Graph-Search Optimality):</strong>
  A heuristic $h(n)$ is <strong>consistent</strong> if for every node $n$ and every successor $n'$ generated by action $a$:
  $$\mathbf{h(n) \le c(n, a, n') + h(n')}$$
  $$\mathbf{\text{Triangle Inequality: } f(n') = g(n') + h(n') = g(n) + c(n, a, n') + h(n') \ge g(n) + h(n) = f(n)}$$
  <em>Crucial Consequence:</em> Monotonicity guarantees that $f(n)$ is non-decreasing along any path, ensuring that the first time a node is expanded in Graph-Search, the path is globally optimal!
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Trace of $A^*$ Search on Romania Map</div>
  <p>Find shortest path from <strong>Arad to Bucharest</strong> given straight-line distance heuristics $h_{\text{SLD}}$:</p>
  <ul>
    <li>$h(\text{Arad})=366, h(\text{Zerind})=374, h(\text{Timisoara})=329, h(\text{Sibiu})=253, h(\text{Fagaras})=176, h(\text{Rimnicu})=193, h(\text{Pitesti})=100, h(\text{Bucharest})=0$.</li>
  </ul>
  <p><strong>$A^*$ Priority Queue Execution Trace:</strong></p>
  <ol>
    <li>Expand <strong>Arad</strong>: Front = $\{ \text{Sibiu: } g=140, f=140+253=393; \ \text{Timisoara: } g=118, f=118+329=447; \ \text{Zerind: } g=75, f=75+374=449 \}$.</li>
    <li>Select lowest $f$: <strong>Sibiu ($f=393$)</strong> $\rightarrow$ Expand Sibiu: Successors: $\{ \text{Fagaras: } g=140+99=239, f=239+176=415; \ \text{Rimnicu: } g=140+80=220, f=220+193=413 \}$.</li>
    <li>Select lowest $f$: <strong>Rimnicu Vilcea ($f=413$)</strong> $\rightarrow$ Expand Rimnicu: Successors: $\{ \text{Pitesti: } g=220+97=317, f=317+100=417; \ \text{Craiova: } g=220+146=366, f=366+160=526 \}$.</li>
    <li>Select lowest $f$: <strong>Fagaras ($f=415$)</strong> $\rightarrow$ Expand Fagaras: Successor: $\{ \text{Bucharest: } g=239+211=450, f=450+0=450 \}$.</li>
    <li>Select lowest $f$: <strong>Pitesti ($f=417$)</strong> $\rightarrow$ Expand Pitesti: Successor: $\{ \text{Bucharest: } g=317+101=\mathbf{418}, f=418+0=\mathbf{418} \}$.</li>
    <li>Select lowest $f$: $\mathbf{\text{Bucharest } (f=418)}$ $\rightarrow$ Goal reached!</li>
  </ol>
  $$\mathbf{\text{Optimal Path: } \text{Arad} \rightarrow \text{Sibiu} \rightarrow \text{Rimnicu Vilcea} \rightarrow \text{Pitesti} \rightarrow \text{Bucharest} \quad (\text{Total Cost } = \mathbf{418})}$$
</div>

<h2 class="section-title">Topic 12 & 13: Adversarial Search, Minimax & Alpha-Beta Pruning</h2>

<p>
  In a zero-sum two-player game, $\mathbf{MAX}$ seeks to maximize the utility score while $\mathbf{MIN}$ seeks to minimize it:
  $$\mathbf{\text{Minimax}(s) = \begin{cases} \text{Utility}(s) & \text{if Terminal}(s) \\ \max_{a \in Actions(s)} \text{Minimax}(\text{Result}(s, a)) & \text{if Player}(s) = \text{MAX} \\ \min_{a \in Actions(s)} \text{Minimax}(\text{Result}(s, a)) & \text{if Player}(s) = \text{MIN} \end{cases}}$$
</p>

<div class="formula-card">
  <strong>The Alpha-Beta Pruning Invariant:</strong>
  - $\alpha$: The highest-value choice found so far at any choice point along the path for $\text{MAX}$ (initialized to $-\infty$).
  - $\beta$: The lowest-value choice found so far at any choice point along the path for $\text{MIN}$ (initialized to $+\infty$).
  $$\mathbf{\text{Pruning Rule: Prune remaining subtree whenever } \alpha \ge \beta}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Alpha-Beta Pruning Tree Execution</div>
  <p>Consider a 2-ply game tree with root $\text{MAX}$, children $B, C, D$ ($\text{MIN}$), each having 2 terminal leaves:</p>
  <ul>
    <li>Node $B$: Leaves are $[3, 5]$ $\implies$ $\text{MIN}$ evaluates $3$, updates $\beta = 3$. Evaluates $5 \implies \text{Node } B = 3$. Root $\text{MAX}$ updates $\alpha = 3$.</li>
    <li>Node $C$: Left leaf is $2$. $\text{MIN}$ updates $\beta = 2$. Now $\mathbf{\alpha = 3 \ge \beta = 2} \implies \mathbf{\text{PRUNE RIGHT CHILD OF } C}$! (No need to evaluate right child).</li>
    <li>Node $D$: Left leaf is $0$. $\text{MIN}$ updates $\beta = 0$. Now $\mathbf{\alpha = 3 \ge \beta = 0} \implies \mathbf{\text{PRUNE RIGHT CHILD OF } D}$!</li>
    <li>$\mathbf{\text{Root Value } = \mathbf{3}}$ (Move to $B$ is optimal).</li>
  </ul>
</div>
"""

# ----------------- MODULE 3 CONTENT -----------------
AI_M3_TEXT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 3 Table of Contents (Topics 14 to 22)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 14:</strong> Knowledge-Based Agents & Wumpus World</div>
    <div>• <strong>Topic 15:</strong> Propositional Logic Syntax & Semantics</div>
    <div>• <strong>Topic 16:</strong> Entailment ($\models$) vs. Inference ($\vdash$)</div>
    <div>• <strong>Topic 17:</strong> Forward & Backward Chaining (Horn Clauses)</div>
    <div>• <strong>Topic 18:</strong> Propositional Resolution & CNF Conversion</div>
    <div>• <strong>Topic 19:</strong> First-Order Logic (FOL) Syntax & Quantifiers</div>
    <div>• <strong>Topic 20:</strong> Universal & Existential Instantiation</div>
    <div>• <strong>Topic 21:</strong> Unification & Most General Unifier (MGU)</div>
    <div>• <strong>Topic 22:</strong> FOL Resolution Refutation Proofs</div>
  </div>
</div>

<h2 class="section-title">Topic 14 & 15: Knowledge-Based Agents & The Wumpus World</h2>

<p>
  A <strong>Knowledge-Based Agent</strong> maintains an internal <strong>Knowledge Base (KB)</strong> consisting of sentences in a formal representation language. It interacts with the KB via two fundamental operations:
  $$\mathbf{\text{TELL}(KB, \alpha) \quad \text{and} \quad \text{ASK}(KB, \alpha)}$$
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ The Wumpus World Formal Specification</div>
  <ul>
    <li><strong>Grid:</strong> $4 \times 4$ grid of rooms with Start at $[1,1]$.</li>
    <li><strong>Hazards:</strong> Bottomless Pits ($P$) with probability 0.2 in each room; One deadly Wumpus ($W$).</li>
    <li><strong>Reward:</strong> Gold glitter ($G$) at random location.</li>
    <li><strong>Percepts:</strong> `[Stench, Breeze, Glitter, Bump, Scream]`.
      <ul>
        <li>In rooms adjacent to Wumpus $\implies$ <em>Stench</em>: $S_{x,y} \iff (W_{x-1,y} \lor W_{x+1,y} \lor W_{x,y-1} \lor W_{x,y+1})$.</li>
        <li>In rooms adjacent to Pits $\implies$ <em>Breeze</em>: $B_{x,y} \iff (P_{x-1,y} \lor P_{x+1,y} \lor P_{x,y-1} \lor P_{x,y+1})$.</li>
      </ul>
    </li>
  </ul>
</div>

<h2 class="section-title">Topic 16 to 18: Propositional Entailment, CNF & Resolution</h2>

<div class="formula-card">
  <strong>Entailment vs. Logical Equivalence:</strong>
  - <strong>Entailment ($\alpha \models \beta$):</strong> Sentence $\beta$ follows logically from $\alpha$ if and only if in every model where $\alpha$ is true, $\beta$ is also true ($M(\alpha) \subseteq M(\beta)$).
  - <strong>Proof by Contradiction (Refutation):</strong>
    $$\mathbf{KB \models \alpha \iff (KB \land \neg \alpha) \text{ is UNSATISFIABLE (generates empty clause } \Box)}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ The 6-Step Algorithm to Convert Any Propositional Sentence into Conjunctive Normal Form (CNF)</div>
  <ol>
    <li><strong>Eliminate Equivalence ($\leftrightarrow$):</strong> Replace $\alpha \leftrightarrow \beta$ with $(\alpha \rightarrow \beta) \land (\beta \rightarrow \alpha)$.</li>
    <li><strong>Eliminate Implication ($\rightarrow$):</strong> Replace $\alpha \rightarrow \beta$ with $\neg \alpha \lor \beta$.</li>
    <li><strong>Move Negation Inward (De Morgan's Laws):</strong> $\neg (\alpha \land \beta) \equiv \neg \alpha \lor \neg \beta$, $\neg (\alpha \lor \beta) \equiv \neg \alpha \land \neg \beta$, $\neg \neg \alpha \equiv \alpha$.</li>
    <li><strong>Distribute $\lor$ over $\land$:</strong> Replace $\alpha \lor (\beta \land \gamma)$ with $(\alpha \lor \beta) \land (\alpha \lor \gamma)$.</li>
    <li><strong>Flatten Nested Conjunctions/Disjunctions:</strong> $(A \lor B) \lor C \equiv (A \lor B \lor C)$.</li>
    <li><strong>Split into Clauses:</strong> Each conjunct becomes a separate clause in the set.</li>
  </ol>
</div>

<h2 class="section-title">Topic 19 to 22: First-Order Logic (FOL), Unification & Resolution Refutation</h2>

<p>
  First-Order Logic adds <strong>Objects, Relations (Predicates), Functions, and Quantifiers ($\forall, \exists$)</strong>.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">English Statement</th>
      <th style="width: 45%;">First-Order Logic Translation</th>
      <th>Quantifier Rule</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>"Every student loves AI."</td><td>$\forall x (\text{Student}(x) \rightarrow \text{Loves}(x, \text{AI}))$</td><td>$\forall$ typically pairs with $\rightarrow$.</td></tr>
    <tr><td>"Some student loves AI."</td><td>$\exists x (\text{Student}(x) \land \text{Loves}(x, \text{AI}))$</td><td>$\exists$ typically pairs with $\land$.</td></tr>
    <tr><td>"No person likes snakes."</td><td>$\forall x (\text{Person}(x) \rightarrow \neg \text{Likes}(x, \text{Snakes}))$</td><td>$\neg \exists x \dots \equiv \forall x \neg \dots$</td></tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Unification Algorithm & Most General Unifier (MGU)</div>
  <p>Find $\text{UNIFY}(P_1, P_2)$ for:</p>
  <ol>
    <li>$P_1 = \text{Knows}(\text{John}, x)$ and $P_2 = \text{Knows}(y, \text{Bill}) \implies \mathbf{\theta = \{ y/\text{John}, x/\text{Bill} \}}$.</li>
    <li>$P_1 = \text{Knows}(\text{John}, x)$ and $P_2 = \text{Knows}(x, \text{Bill}) \implies \mathbf{\text{Fail (Standardize variables apart first!)}}$.</li>
    <li>$P_1 = \text{Likes}(x, \text{Father}(x))$ and $P_2 = \text{Likes}(y, y) \implies \mathbf{\text{Occur Check Failure!}} \ (y \text{ cannot unify with } \text{Father}(y))$.</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Step-by-Step FOL Resolution Refutation Proof</div>
  <p><strong>Given Axioms:</strong></p>
  <ol>
    <li>"Marcus was a man." $\implies \text{Man}(\text{Marcus})$</li>
    <li>"Marcus was a Pompeian." $\implies \text{Pompeian}(\text{Marcus})$</li>
    <li>"All Pompeians were Romans." $\implies \forall x (\text{Pompeian}(x) \rightarrow \text{Roman}(x)) \implies \neg \text{Pompeian}(x) \lor \text{Roman}(x)$</li>
    <li>"Caesar was a ruler." $\implies \text{Ruler}(\text{Caesar})$</li>
    <li>"All Romans were either loyal to Caesar or hated him." $\implies \forall x (\text{Roman}(x) \rightarrow \text{Loyal}(x, \text{Caesar}) \lor \text{Hate}(x, \text{Caesar})) \implies \neg \text{Roman}(x) \lor \text{Loyal}(x, \text{Caesar}) \lor \text{Hate}(x, \text{Caesar})$</li>
    <li>"Everyone is loyal to someone." $\implies \forall x \exists y \text{Loyal}(x, y) \implies \text{Loyal}(x, f(x))$ (Skolem function)</li>
    <li>"Men only try to assassinate rulers they aren't loyal to." $\implies \forall x \forall y (\text{Man}(x) \land \text{Ruler}(y) \land \text{TryAssassinate}(x, y) \rightarrow \neg \text{Loyal}(x, y)) \implies \neg \text{Man}(x) \lor \neg \text{Ruler}(y) \lor \neg \text{TryAssassinate}(x, y) \lor \neg \text{Loyal}(x, y)$</li>
    <li>"Marcus tried to assassinate Caesar." $\implies \text{TryAssassinate}(\text{Marcus}, \text{Caesar})$</li>
  </ol>
  <p><strong>Query to Prove:</strong> "Did Marcus hate Caesar?" ($\text{Hate}(\text{Marcus}, \text{Caesar})$)</p>
  <p><strong>Proof by Refutation:</strong> Add negated query $\neg \text{Hate}(\text{Marcus}, \text{Caesar})$:</p>
  <ol>
    <li>Resolve $\neg \text{Hate}(\text{Marcus}, \text{Caesar})$ with Clause 5 $\{ x/\text{Marcus} \} \implies \mathbf{C_9: \neg \text{Roman}(\text{Marcus}) \lor \text{Loyal}(\text{Marcus}, \text{Caesar})}$.</li>
    <li>Resolve $C_9$ with Clause 3 $\{ x/\text{Marcus} \} \implies \mathbf{C_{10}: \neg \text{Pompeian}(\text{Marcus}) \lor \text{Loyal}(\text{Marcus}, \text{Caesar})}$.</li>
    <li>Resolve $C_{10}$ with Clause 2 $\implies \mathbf{C_{11}: \text{Loyal}(\text{Marcus}, \text{Caesar})}$.</li>
    <li>Resolve $C_{11}$ with Clause 7 $\{ x/\text{Marcus}, y/\text{Caesar} \} \implies \mathbf{C_{12}: \neg \text{Man}(\text{Marcus}) \lor \neg \text{Ruler}(\text{Caesar}) \lor \neg \text{TryAssassinate}(\text{Marcus}, \text{Caesar})}$.</li>
    <li>Resolve $C_{12}$ with Clause 1 $\implies \mathbf{C_{13}: \neg \text{Ruler}(\text{Caesar}) \lor \neg \text{TryAssassinate}(\text{Marcus}, \text{Caesar})}$.</li>
    <li>Resolve $C_{13}$ with Clause 4 $\implies \mathbf{C_{14}: \neg \text{TryAssassinate}(\text{Marcus}, \text{Caesar})}$.</li>
    <li>Resolve $C_{14}$ with Clause 8 $\implies \mathbf{\Box \text{ (EMPTY CLAUSE - CONTRADICTION!)}}$.</li>
  </ol>
  $$\mathbf{\text{Q.E.D. Marcus hated Caesar is strictly proven!}}$$
</div>
"""

# ----------------- MODULE 4 CONTENT -----------------
AI_M4_TEXT = r"""
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
  <div class="worked-title">🏛️ STRIPS Air Cargo Transport Problem Specification</div>
  <pre><code>Init(At(C1, SFO) ∧ At(C2, JFK) ∧ At(P1, SFO) ∧ At(P2, JFK) ∧ Cargo(C1) ∧ Cargo(C2) ∧ Plane(P1) ∧ Plane(P2) ∧ Airport(JFK) ∧ Airport(SFO))
Goal(At(C1, JFK) ∧ At(C2, SFO))

Action(Load(c, p, a),
  PRECOND: At(c, a) ∧ At(p, a) ∧ Cargo(c) ∧ Plane(p) ∧ Airport(a)
  EFFECT:  ¬At(c, a) ∧ In(c, p))

Action(Unload(c, p, a),
  PRECOND: In(c, p) ∧ At(p, a) ∧ Cargo(c) ∧ Plane(p) ∧ Airport(a)
  EFFECT:  At(c, a) ∧ ¬In(c, p))

Action(Fly(p, from, to),
  PRECOND: At(p, from) ∧ Plane(p) ∧ Airport(from) ∧ Airport(to)
  EFFECT:  ¬At(p, from) ∧ At(p, to))</code></pre>
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
"""

# ----------------- MODULE 5 CONTENT -----------------
AI_M5_TEXT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 5 Table of Contents (Topics 30 to 38)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 30:</strong> Forms of Learning (Supervised, Unsupervised, RL)</div>
    <div>• <strong>Topic 31:</strong> Decision Tree Learning & ID3 Algorithm</div>
    <div>• <strong>Topic 32:</strong> Entropy & Information Gain Calculations</div>
    <div>• <strong>Topic 33:</strong> Gini Index, Overfitting & Tree Pruning</div>
    <div>• <strong>Topic 34:</strong> Biological & McCulloch-Pitts Artificial Neurons</div>
    <div>• <strong>Topic 35:</strong> Single-Layer Perceptron & Linear Separability (XOR Problem)</div>
    <div>• <strong>Topic 36:</strong> Multi-Layer Perceptrons (MLP) Architecture</div>
    <div>• <strong>Topic 37:</strong> Mathematical Derivation of Backpropagation</div>
    <div>• <strong>Topic 38:</strong> Activation Functions & Solved University Exam Bank</div>
  </div>
</div>

<h2 class="section-title">Topic 30 to 33: Decision Tree Induction & Information Gain Mathematics</h2>

<p>
  In <strong>Decision Tree Learning</strong>, candidate attributes are recursively evaluated at each split to maximize the purity of child nodes:
</p>

<div class="formula-card">
  <strong>Shannon Entropy & Information Gain Formulas:</strong>
  $$\mathbf{H(S) = - \sum_{i=1}^c p_i \log_2(p_i)}$$
  $$\mathbf{\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)}$$
  $$\mathbf{\text{Gini Index: } \text{Gini}(S) = 1 - \sum_{i=1}^c p_i^2}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: ID3 Decision Tree Root Attribute Selection</div>
  <p>A dataset has 14 instances ($9 \text{ Yes}, 5 \text{ No}$). Initial parent entropy is:</p>
  $$H(S) = - \frac{9}{14} \log_2\left(\frac{9}{14}\right) - \frac{5}{14} \log_2\left(\frac{5}{14}\right) = - (0.643)(-0.637) - (0.357)(-1.485) = \mathbf{0.940 \text{ bits}}$$
  <p>Evaluate Attribute <strong>Windy</strong> ($\text{Weak: } 6\text{ Yes}, 2\text{ No}; \ \text{Strong: } 3\text{ Yes}, 3\text{ No}$):</p>
  $$H(S_{\text{Weak}}) = - \frac{6}{8} \log_2\left(\frac{6}{8}\right) - \frac{2}{8} \log_2\left(\frac{2}{8}\right) = \mathbf{0.811 \text{ bits}}$$
  $$H(S_{\text{Strong}}) = - \frac{3}{6} \log_2\left(\frac{3}{6}\right) - \frac{3}{6} \log_2\left(\frac{3}{6}\right) = \mathbf{1.000 \text{ bits}}$$
  $$\text{Gain}(S, \text{Windy}) = 0.940 - \left[ \frac{8}{14}(0.811) + \frac{6}{14}(1.000) \right] = 0.940 - (0.463 + 0.429) = \mathbf{0.048 \text{ bits}}$$
</div>

<h2 class="section-title">Topic 34 to 38: Neural Networks, Backpropagation & Non-Linear Activations</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Why Single-Layer Perceptrons Cannot Solve XOR (Minsky & Papert 1969)</div>
  <p>A single perceptron $y = \text{step}(w_1 x_1 + w_2 x_2 - \theta)$ represents a single straight hyper-plane linear decision boundary. The XOR function requires:</p>
  $$\text{For } (0,0) \rightarrow 0: \ 0 < \theta \implies \theta > 0$$
  $$\text{For } (1,0) \rightarrow 1: \ w_1 \ge \theta$$
  $$\text{For } (0,1) \rightarrow 1: \ w_2 \ge \theta$$
  $$\text{For } (1,1) \rightarrow 0: \ w_1 + w_2 < \theta$$
  $$\text{Adding } (1,0) \text{ and } (0,1) \implies w_1 + w_2 \ge 2\theta > \theta \implies \mathbf{\text{CONTRADICTION! (Non-linearly separable)}}$$
</div>

<div class="formula-card">
  <strong>Complete Mathematical Derivation of Backpropagation Gradient:</strong>
  Let squared loss be $E = \frac{1}{2} \sum_k (y_k - \hat{y}_k)^2$. Using the Multivariate Chain Rule for output layer weight $w_{jk}$:
  $$\mathbf{\frac{\partial E}{\partial w_{jk}} = \frac{\partial E}{\partial \hat{y}_k} \cdot \frac{\partial \hat{y}_k}{\partial z_k} \cdot \frac{\partial z_k}{\partial w_{jk}} = - (y_k - \hat{y}_k) \cdot \sigma'(z_k) \cdot a_j = \mathbf{- \delta_k \cdot a_j}}$$
  $$\mathbf{\text{Weight Update: } w_{jk} \leftarrow w_{jk} - \eta \frac{\partial E}{\partial w_{jk}} = w_{jk} + \eta \cdot \delta_k \cdot a_j}$$
  For hidden layer weight $w_{ij}$:
  $$\mathbf{\delta_j = \sigma'(z_j) \sum_k \delta_k w_{jk} \implies w_{ij} \leftarrow w_{ij} + \eta \cdot \delta_j \cdot a_i}$$
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Activation Function</th>
      <th style="width: 30%;">Mathematical Formula</th>
      <th style="width: 25%;">Output Range</th>
      <th>Derivative $\sigma'(z)$</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Sigmoid (Logistic)</strong></td><td>$\sigma(z) = \frac{1}{1 + e^{-z}}$</td><td>$(0, 1)$</td><td>$\sigma(z)(1 - \sigma(z))$</td></tr>
    <tr><td><strong>Hyperbolic Tangent (Tanh)</strong></td><td>$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$</td><td>$(-1, 1)$ (Zero-centered)</td><td>$1 - \tanh^2(z)$</td></tr>
    <tr><td><strong>ReLU (Rectified Linear)</strong></td><td>$f(z) = \max(0, z)$</td><td>$[0, \infty)$</td><td>$1 \text{ if } z > 0 \text{ else } 0$</td></tr>
    <tr><td><strong>Softmax</strong></td><td>$\sigma(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$</td><td>$(0, 1)$ with $\sum p_i = 1$</td><td>$p_i (\delta_{ij} - p_j)$</td></tr>
  </tbody>
</table>
"""

# ----------------- REVISION CONTENT -----------------
AI_REVISION_TEXT = r"""
<h2 class="section-title">Page 1: The AI Master Mental Model & PEAS Taxonomy</h2>
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
  <thead><tr><th>Algorithm</th><th>Time Complexity</th><th>Space Complexity</th><th>Complete?</th><th>Optimal?</th></tr></thead>
  <tbody>
    <tr><td><strong>BFS</strong></td><td>$O(b^d)$</td><td>$O(b^d)$</td><td>Yes</td><td>Yes (uniform costs)</td></tr>
    <tr><td><strong>DFS</strong></td><td>$O(b^m)$</td><td>$O(b \cdot m)$</td><td>No (infinite trees)</td><td>No</td></tr>
    <tr><td><strong>UCS</strong></td><td>$O(b^{1 + \lfloor C^*/\epsilon \rfloor})$</td><td>$O(b^{1 + \lfloor C^*/\epsilon \rfloor})$</td><td>Yes</td><td><strong>Yes (Cost optimal)</strong></td></tr>
    <tr><td><strong>IDDFS</strong></td><td>$O(b^d)$</td><td>$\mathbf{O(b \cdot d)}$</td><td>Yes</td><td>Yes (uniform costs)</td></tr>
    <tr><td><strong>$A^*$ Search</strong></td><td>$O(b^d)$</td><td>$O(b^d)$</td><td>Yes</td><td><strong>Yes (if $h$ admissible)</strong></td></tr>
  </tbody>
</table>

<div class="page-break"></div>
<h2 class="section-title">Page 3: $A^*$ Search Admissibility & Consistency Theorems</h2>
<div class="formula-card">
  $$\text{Admissibility: } 0 \le h(n) \le h^*(n) \implies A^* \text{ Tree Search is Optimal}$$
  $$\text{Consistency: } h(n) \le c(n, a, n') + h(n') \implies A^* \text{ Graph Search is Optimal (No node re-expansion needed!)}$$
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

def build_all_ai():
    print("Writing AI module content files...")
    with open(os.path.join(AI_DIR, "ai_module1_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M1_EXHAUSTIVE = r"""{AI_M1_TEXT}"""\n')
    with open(os.path.join(AI_DIR, "ai_module2_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M2_EXHAUSTIVE = r"""{AI_M2_TEXT}"""\n')
    with open(os.path.join(AI_DIR, "ai_module3_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M3_EXHAUSTIVE = r"""{AI_M3_TEXT}"""\n')
    with open(os.path.join(AI_DIR, "ai_module4_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M4_EXHAUSTIVE = r"""{AI_M4_TEXT}"""\n')
    with open(os.path.join(AI_DIR, "ai_module5_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M5_EXHAUSTIVE = r"""{AI_M5_TEXT}"""\n')
    with open(os.path.join(AI_DIR, "ai_revision_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_REVISION_EXHAUSTIVE = r"""{AI_REVISION_TEXT}"""\n')
        
    modules = [
        (1, "Module 1: Intelligent Agents & PEAS Framework", "Topics 1 to 7 • Foundations, Evolution, Rationality & 5 Agent Types", AI_M1_TEXT, "Module_1_Intelligent_Agents_Notes"),
        (2, "Module 2: Search Algorithms & Game Playing", "Topics 8 to 13 • BFS/DFS/IDDFS, A* Admissibility Proofs & Alpha-Beta Pruning", AI_M2_TEXT, "Module_2_Search_Algorithms_Notes"),
        (3, "Module 3: Knowledge Representation & Logic", "Topics 14 to 22 • Wumpus World, Propositional CNF, First-Order Logic & Resolution", AI_M3_TEXT, "Module_3_Knowledge_Logic_Notes"),
        (4, "Module 4: Classical Planning & Bayesian Networks", "Topics 23 to 29 • STRIPS / PDDL, Graphplan Mutexes, Probability & Bayes Nets", AI_M4_TEXT, "Module_4_Planning_Bayes_Notes"),
        (5, "Module 5: Machine Learning & Neural Networks", "Topics 30 to 38 • Decision Trees ID3, Perceptrons & Backpropagation Math", AI_M5_TEXT, "Module_5_Machine_Learning_Notes"),
    ]
    
    # 1. Generate Individual Module PDFs
    for num, title, subtitle, content, fname in modules:
        html_content = wrap_html(title, subtitle, content, module_num=num)
        html_file = os.path.join(HTML_DIR, f"{fname}.html")
        pdf_file = os.path.join(PDF_DIR, f"{fname}.pdf")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        generate_pdf(html_file, pdf_file, f"AI Module {num}")

    # 2. Generate 10-Page Revision Guide
    rev_html = wrap_html(
        "Artificial Intelligence (CS24307) 10-Page Master Revision",
        "High-Yield Formulas, Search Matrices, Logic Rules, Bayes Formulas & Flashcards",
        AI_REVISION_TEXT
    )
    rev_html_file = os.path.join(HTML_DIR, "AI_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "AI_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "AI 10-Page Master Revision")

    # 3. Generate Full Course Master Book (with Revision Appendix)
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
        
    full_body.append(f"""
    <div class="page-break"></div>
    <div class="cover-container" style="margin-top: 40px;">
      <div class="course-badge">Comprehensive Revision Appendix</div>
      <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">10-Page Master Quick Revision Guide</h2>
      <div style="font-size: 12.5px; color: #64748b;">Formulas, Algorithm Checklists & Solved Exam Cards</div>
    </div>
    {AI_REVISION_TEXT}
    """)
    
    full_master_html = wrap_html(
        "Artificial Intelligence (CS24307) Full Course Master",
        "Exhaustive 38-Topic Textbook, Algorithm Traces & Solved University Question Bank",
        "".join(full_body)
    )
    master_html_file = os.path.join(HTML_DIR, "AI_Full_Course_Master.html")
    master_pdf_file = os.path.join(PDF_DIR, "AI_Full_Course_Master.pdf")
    with open(master_html_file, "w", encoding="utf-8") as f:
        f.write(full_master_html)
    generate_pdf(master_html_file, master_pdf_file, "AI Full Course Master")

if __name__ == "__main__":
    build_all_ai()
