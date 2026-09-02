# Artificial Intelligence Module 1 Exhaustive Content (7 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

AI_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Preliminaries & Intelligent Agents — Complete 7-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> What is AI? (4 Classical Approaches & Rational Agent Paradigm)</div>
    <div><strong>Topic 2:</strong> Evolution of AI (1950 Turing Test to 2020s Generative AI)</div>
    <div><strong>Topic 3:</strong> Intelligent Agents (Sense-Think-Act Loop & PEAS Framework)</div>
    <div><strong>Topic 4:</strong> Concept of Rationality (Rationality vs. Omniscience)</div>
    <div><strong>Topic 5:</strong> Nature of Environments (O-D-E-D-C-N Taxonomy)</div>
    <div><strong>Topic 6:</strong> Structure of Agents (5 Architectural Agent Types)</div>
    <div><strong>Topic 7:</strong> Real-World Applications of AI (Healthcare, Robotics, Vision)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Definitions, Approaches & Historical Evolution of AI</h2>
<p>
  <strong>Artificial Intelligence</strong> is the branch of computer science dedicated to designing computational systems that synthesize capabilities traditionally associated with human intelligence: reasoning, perception, learning, planning, and goal-directed decision making.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Approach</th>
      <th style="width: 45%;">Philosophical / Methodological Basis</th>
      <th>Standard Evaluation Benchmark</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Thinking Humanly</strong></td><td>Cognitive science modeling of the inner workings of human thought processes.</td><td>GPS (General Problem Solver), Cognitive Neuroimaging.</td></tr>
    <tr><td><strong>2. Acting Humanly</strong></td><td>Empirical behavioral replication of human performance.</td><td><strong>Turing Test (1950)</strong> by Alan Turing.</td></tr>
    <tr><td><strong>3. Thinking Rationally</strong></td><td>Formal logic and laws of thought (Syllogisms, First-Order Logic).</td><td>Deductive Inference Engines and Proof Systems.</td></tr>
    <tr><td><strong>4. Acting Rationally</strong></td><td><strong>Rational Agent Approach (Modern Standard):</strong> Maximizing expected performance given available information.</td><td>Goal achievement and expected utility maximization.</td></tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: Evolution Timeline (T-D-E-ML-DL-GenAI)</div>
  <strong>1950:</strong> Turing Test $\rightarrow$ <strong>1956:</strong> Dartmouth Conference (John McCarthy coining "AI") $\rightarrow$ <strong>1980s:</strong> Expert Systems (R1/XCON) $\rightarrow$ <strong>1997:</strong> Deep Blue defeats Kasparov $\rightarrow$ <strong>2011:</strong> IBM Watson wins Jeopardy $\rightarrow$ <strong>2016:</strong> AlphaGo defeats Lee Sedol $\rightarrow$ <strong>2020s:</strong> Large Multimodal Transformers & Generative AI.
</div>

<h2 class="section-title">Topic 3 & 4: Intelligent Agents, PEAS & The Concept of Rationality</h2>

<div class="diagram-container">
  <svg width="100%" height="80" viewBox="0 0 740 80" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="15" width="180" height="50" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="120" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Environment</text>
    <text x="120" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Physical / Virtual World</text>

    <path d="M 210 30 L 320 30" stroke="#0284c7" stroke-width="2"/>
    <text x="265" y="24" font-family="Plus Jakarta Sans" font-size="9" fill="#0369a1" text-anchor="middle">Percepts (Sensors)</text>

    <rect x="330" y="15" width="180" height="50" rx="8" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="420" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Intelligent Agent</text>
    <text x="420" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Agent Function f: P* -> A</text>

    <path d="M 330 55 L 210 55" stroke="#0284c7" stroke-width="2"/>
    <text x="265" y="68" font-family="Plus Jakarta Sans" font-size="9" fill="#0369a1" text-anchor="middle">Actions (Actuators)</text>
  </svg>
  <div class="diagram-caption">Figure 1.1: The Core Sense-Think-Act Intelligent Agent Interaction Loop</div>
</div>

<div class="callout callout-warning">
  <div class="callout-title">Rationality $\neq$ Omniscience</div>
  An <strong>omniscient agent</strong> knows the <em>actual outcome</em> of its actions in advance and acts with superhuman clairvoyance (impossible in reality). A <strong>rational agent</strong> chooses the action that maximizes its <em>expected performance measure</em>, given its accumulated percept history sequence $P^*$ and built-in knowledge base!
</div>

<h3 class="subsection-title">PEAS Specification Framework (Autonomous Taxi Example):</h3>
<ul>
  <li><strong>P — Performance Measure:</strong> Safety, passenger comfort, speed, legal compliance, fuel economy, profit.</li>
  <li><strong>E — Environment:</strong> City streets, highways, pedestrians, weather conditions, other vehicular traffic.</li>
  <li><strong>A — Actuators:</strong> Steering wheel, accelerator, brake pedal, horn, turn signals, display screen.</li>
  <li><strong>S — Sensors:</strong> Video cameras, LiDAR, radar, ultrasonic sonar, GPS, speedometer, odometer, engine sensors.</li>
</ul>

<h2 class="section-title">Topic 5: Nature of Environments (O-D-E-D-C-N Taxonomy)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Environment Dimension</th>
      <th style="width: 45%;">Core Conceptual Distinction</th>
      <th>Representative Example</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Fully vs. Partially Observable</strong></td><td>Sensors detect the complete state of the world vs. state is obscured by noise or missing sensors.</td><td>Chess (Fully) vs. Poker / Driving (Partially)</td></tr>
    <tr><td><strong>2. Deterministic vs. Stochastic</strong></td><td>Next state determined 100% by current state + action vs. randomness and uncertainty exist.</td><td>Crossword (Deterministic) vs. Weather / Taxi (Stochastic)</td></tr>
    <tr><td><strong>3. Episodic vs. Sequential</strong></td><td>Each action episode is independent vs. current action alters future states and rewards.</td><td>Image Defect Sorting (Episodic) vs. Chess (Sequential)</td></tr>
    <tr><td><strong>4. Static vs. Dynamic</strong></td><td>Environment remains unchanged while agent deliberates vs. changes continuously in real time.</td><td>Sudoku (Static) vs. Autonomous Driving (Dynamic)</td></tr>
    <tr><td><strong>5. Discrete vs. Continuous</strong></td><td>Countable discrete states and actions vs. continuously varying physical quantities.</td><td>Tic-Tac-Toe (Discrete) vs. Robot Arm Control (Continuous)</td></tr>
    <tr><td><strong>6. Single-Agent vs. Multi-Agent</strong></td><td>Agent operates alone vs. multiple agents interact cooperatively or competitively.</td><td>Crossword Puzzle (Single) vs. Chess / Stock Market (Multi)</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 6: The 5 Architectural Agent Types</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Agent Type</th>
      <th style="width: 45%;">Decision Mechanism & Internal State</th>
      <th>Key Limitation / Advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Simple Reflex</strong></td><td>Direct Condition-Action Rules (`IF condition THEN action`) based strictly on current percept.</td><td>Zero memory; fails completely in partially observable environments.</td></tr>
    <tr><td><strong>2. Model-Based Reflex</strong></td><td>Maintains internal state reflecting "how the world evolves" and "how actions affect the world".</td><td>Overcomes partial observability by tracking hidden state history.</td></tr>
    <tr><td><strong>3. Goal-Based</strong></td><td>Combines internal state with explicit <strong>Goal information</strong> using Search & Planning algorithms.</td><td>Flexible: goals can be altered dynamically without rewriting rules.</td></tr>
    <tr><td><strong>4. Utility-Based</strong></td><td>Evaluates state desirability using an explicit real-valued <strong>Utility Function</strong> $U(s)$.</td><td>Handles conflicting goals and probabilistic risk-reward tradeoffs.</td></tr>
    <tr><td><strong>5. Learning Agent</strong></td><td>Decoupled into <strong>4 Components:</strong> (1) Learning Element, (2) Performance Element, (3) Critic (evaluator), (4) Problem Generator (exploration).</td><td>Autonomously improves performance over time from raw environmental feedback.</td></tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M1 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Define an Intelligent Agent. Explain the 4 components of a Learning Agent with a neat architecture diagram. (10 Marks)</div>
  <div class="qa-a">
    An <strong>Intelligent Agent</strong> is an autonomous entity that perceives its environment through sensors and takes actions using actuators to achieve its goals ($f: P^* \rightarrow A$).<br>
    <strong>The 4 Components of a Learning Agent:</strong><br>
    1. <em>Learning Element:</em> Responsible for making improvements by modifying the agent's internal behavior rules.<br>
    2. <em>Performance Element:</em> Responsible for selecting external actions based on percepts (the operational agent).<br>
    3. <em>Critic:</em> Evaluates the agent's performance against an external performance standard and provides feedback to the learning element.<br>
    4. <em>Problem Generator:</em> Suggests experimental exploratory actions that lead to new, informative experiences rather than suboptimal repetition.
  </div>
</div>
"""
