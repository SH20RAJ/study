# Artificial Intelligence Module 1 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

AI_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Introduction to Artificial Intelligence & Intelligent Agents</div>
  <div class="toc-grid">
    <div>1. Foundations & 4 Definitions of AI (Human vs. Rational, Thought vs. Behavior)</div>
    <div>2. The Turing Test, Total Turing Test & Chinese Room Argument</div>
    <div>3. Historical Evolution & Eras of AI (Dartmouth 1956 to Deep Learning)</div>
    <div>4. Concept of Rationality & Mathematical Performance Measures</div>
    <div>5. The PEAS Framework (Performance, Environment, Actuators, Sensors)</div>
    <div>6. Comprehensive PEAS Analysis across 5 Diverse Real-World Domains</div>
    <div>7. Environment Taxonomies (7 Orthogonal Dimensions & Classifications)</div>
    <div>8. Simple Reflex Agents (Condition-Action Rules & Internal Architectures)</div>
    <div>9. Model-Based Reflex Agents (Handling Partial Observability & State Updating)</div>
    <div>10. Goal-Based Agents (Search, Planning & Future State Simulation)</div>
    <div>11. Utility-Based Agents (Trade-Off Optimization & Expected Utility Theory)</div>
    <div>12. Learning Agents (Critic, Learning Element, Performance Element, Generator)</div>
    <div>13. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1: Foundations & The 4 Quadrants of AI Definitions</h2>
<p>
  Artificial Intelligence (AI) is the study and design of intelligent computational entities capable of perceiving their environment, reasoning about state, making optimal decisions, and acting autonomously to maximize success.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Dimension</th>
      <th style="width: 37%;">Human-Centric Approach</th>
      <th>Rationalist (Normative Ideal) Approach</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Thought Processes & Reasoning</strong></td>
      <td>
        <strong>Systems that Think Like Humans:</strong><br>
        • Focuses on Cognitive Science & Cognitive Modeling.<br>
        • Validated by comparing internal neural activation traces and decision response times with human psychological experiments (GPS - General Problem Solver).
      </td>
      <td>
        <strong>Systems that Think Rationally:</strong><br>
        • Focuses on Formal Logic & Laws of Thought.<br>
        • Codifies strict deductive syllogisms (e.g., Aristotle: "Socrates is a man; all men are mortal; therefore Socrates is mortal").
      </td>
    </tr>
    <tr>
      <td><strong>Observable Behavior & Action</strong></td>
      <td>
        <strong>Systems that Act Like Humans:</strong><br>
        • Operationalized by <strong>The Turing Test (1950)</strong>.<br>
        • Requires Natural Language Processing, Knowledge Representation, Automated Reasoning, and Machine Learning.
      </td>
      <td>
        <strong>Systems that Act Rationally (Modern AI Standard):</strong><br>
        • Focuses on <strong>Intelligent Rational Agents</strong>.<br>
        • An agent acts rationally if it selects actions that maximize the expected value of its performance measure, given its perceptual history.
      </td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 2: The Turing Test & The Chinese Room Philosophical Argument</h2>

<h3 class="subsection-title">1. The Standard Turing Test (Alan Turing, 1950):</h3>
<p>
  A human interrogator communicates via text terminal with two hidden entities: another human and a machine. If the interrogator cannot reliably tell which is the machine after 5 minutes of open interrogation, the machine is said to have demonstrated intelligence.
</p>
<ul>
  <li><strong>Total Turing Test:</strong> Augments the text test with video/physical interactions, requiring Computer Vision and Robotics.</li>
</ul>

<h3 class="subsection-title">2. John Searle's Chinese Room Argument (1980):</h3>
<p>
  A human who understands zero Chinese sits inside a sealed room with a rule book (program) that maps incoming Chinese character slips to output slips. To an outside observer, the room answers Chinese queries perfectly.
</p>
<div class="callout callout-info">
  <div class="callout-title">Core Philosophical Takeaway: Syntax vs. Semantics</div>
  Searle proved that <strong>syntactic symbol manipulation</strong> is fundamentally insufficient for <strong>semantic understanding and intentionality</strong> ("Strong AI"). Machines simulate understanding without truly understanding.
</div>

<h2 class="section-title">Topic 4 & 5: Concept of Rationality & The PEAS Framework</h2>

<p>
  A <strong>Rational Agent</strong> is one that does the right thing. Formally, for each possible percept sequence, a rational agent selects an action that is expected to maximize its performance measure, based on the evidence provided by the percept sequence and whatever built-in knowledge the agent has.
</p>

<div class="callout callout-warning">
  <div class="callout-title">Rationality $\neq$ Omniscience</div>
  <ul>
    <li><strong>Omniscience:</strong> An omniscient agent knows the <em>actual</em> outcome of its actions and can act accordingly (impossible in reality due to incomplete information and stochasticity).</li>
    <li><strong>Rationality:</strong> Maximizes <em>expected</em> success based on available percepts and knowledge. Rationality encourages <strong>information gathering and exploration</strong>.</li>
  </ul>
</div>

<h3 class="subsection-title">The PEAS Formulation Matrix across 5 Standard AI Systems:</h3>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Agent Type</th>
      <th style="width: 22%;">Performance Measure ($P$)</th>
      <th style="width: 22%;">Environment ($E$)</th>
      <th style="width: 18%;">Actuators ($A$)</th>
      <th>Sensors ($S$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Autonomous Taxi Driver</strong></td>
      <td>Safe transit, fast route, legal driving, passenger comfort, maximized profits.</td>
      <td>Roads, traffic, pedestrians, weather, traffic lights, police.</td>
      <td>Steering wheel, accelerator, brake, signals, horn, dashboard display.</td>
      <td>LiDAR, RADAR, cameras, sonar, GPS, speedometer, accelerometer, engine sensors.</td>
    </tr>
    <tr>
      <td><strong>2. Medical Diagnostic System</strong></td>
      <td>Healthy patient, minimized healthcare costs, zero false negatives in critical diagnoses.</td>
      <td>Patient, hospital clinical staff, insurance databases.</td>
      <td>Display screen for diagnoses, recommended prescriptions, test orders.</td>
      <td>Keyboard input of symptoms, lab test analyzers, vital sign monitors, patient EHR.</td>
    </tr>
    <tr>
      <td><strong>3. Automated Vacuum Cleaner</strong></td>
      <td>Cleanliness score, minimal battery consumption, minimal operating time, zero damage to furniture.</td>
      <td>Room floors, carpets, furniture, obstacles, pets, stairs.</td>
      <td>Drive wheels, vacuum suction motor, rotating brush, dust ejection valve.</td>
      <td>Bumper contact switches, infrared cliff sensors, optical floor sensor, dust detector.</td>
    </tr>
    <tr>
      <td><strong>4. Part-Picking Industrial Robot</strong></td>
      <td>Percentage of parts correctly sorted into bins, speed (parts per minute), zero damage.</td>
      <td>Conveyor belt, raw parts bins, assembly trays.</td>
      <td>Jointed mechanical robotic arm, pneumatic gripper hand.</td>
      <td>High-resolution RGB-D camera, joint angle encoders, tactile pressure sensors.</td>
    </tr>
    <tr>
      <td><strong>5. High-Frequency Trading Bot</strong></td>
      <td>Maximized portfolio return on investment (ROI), minimized Value-at-Risk (VaR), Sharpe ratio.</td>
      <td>Global financial exchanges (NASDAQ, NYSE, crypto liquidity pools).</td>
      <td>Automated FIX protocol buy/sell order submissions, cancellation packets.</td>
      <td>Real-time tick-by-tick market data feed, financial news APIs, order books.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 7: Environment Taxonomies (7 Orthogonal Dimensions)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 24%;">Environment Property</th>
      <th style="width: 38%;">Description & Characterization</th>
      <th>Representative Domain Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Fully vs. Partially Observable</strong></td>
      <td>Whether the agent's sensors give complete access to the full state of the environment at all times.</td>
      <td>• <em>Fully:</em> Chess, Crossword puzzle.<br>• <em>Partially:</em> Poker (hidden cards), Automated Driving.</td>
    </tr>
    <tr>
      <td><strong>2. Single-Agent vs. Multi-Agent</strong></td>
      <td>Whether other entities in the environment are treated as agents with their own objective functions.</td>
      <td>• <em>Single:</em> Solitaire, Sudoku.<br>• <em>Multi:</em> Chess (Competitive), Traffic (Cooperative).</td>
    </tr>
    <tr>
      <td><strong>3. Deterministic vs. Stochastic</strong></td>
      <td>Whether the next state is completely determined by the current state and the agent's action.</td>
      <td>• <em>Deterministic:</em> Chess.<br>• <em>Stochastic:</em> Backgammon (dice), Weather-dependent systems.</td>
    </tr>
    <tr>
      <td><strong>4. Episodic vs. Sequential</strong></td>
      <td>In episodic environments, current decisions do not affect future episodes (no memory needed).</td>
      <td>• <em>Episodic:</em> Defect classification on conveyor.<br>• <em>Sequential:</em> Chess, Navigation.</td>
    </tr>
    <tr>
      <td><strong>5. Static vs. Dynamic vs. Semidynamic</strong></td>
      <td>Whether the environment changes while the agent is deliberating. Semidynamic: environment stays fixed but score decreases over time.</td>
      <td>• <em>Static:</em> Crossword.<br>• <em>Dynamic:</em> Taxi driving.<br>• <em>Semidynamic:</em> Timed Chess.</td>
    </tr>
    <tr>
      <td><strong>6. Discrete vs. Continuous</strong></td>
      <td>Whether the state space, time, percepts, and actions are finite discrete values or continuous real numbers.</td>
      <td>• <em>Discrete:</em> Chess (64 squares).<br>• <em>Continuous:</em> Self-driving cars (speed, angle).</td>
    </tr>
    <tr>
      <td><strong>7. Known vs. Unknown</strong></td>
      <td>Whether the physics/rules of the environment are fully known to the agent in advance.</td>
      <td>• <em>Known:</em> Solitaire.<br>• <em>Unknown:</em> Exploring a new video game or planet.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topics 8 – 12: The 5 Fundamental Agent Architectures</h2>

<div class="diagram-container">
  <svg width="100%" height="110" viewBox="0 0 740 110" xmlns="http://www.w3.org/2000/svg">
    <rect x="15" y="15" width="125" height="80" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="77" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Simple Reflex</text>
    <text x="77" y="55" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Condition-Action</text>
    <text x="77" y="70" font-family="Plus Jakarta Sans" font-size="8.5" fill="#64748b" text-anchor="middle">No History Memory</text>

    <path d="M 140 55 L 160 55" stroke="#0284c7" stroke-width="2"/>

    <rect x="165" y="15" width="125" height="80" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="227" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Model-Based</text>
    <text x="227" y="55" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Internal State</text>
    <text x="227" y="70" font-family="Plus Jakarta Sans" font-size="8.5" fill="#64748b" text-anchor="middle">How world evolves</text>

    <path d="M 290 55 L 310 55" stroke="#0284c7" stroke-width="2"/>

    <rect x="315" y="15" width="125" height="80" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="377" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">Goal-Based</text>
    <text x="377" y="55" font-family="Plus Jakarta Sans" font-size="9" fill="#b45309" text-anchor="middle">Search & Planning</text>
    <text x="377" y="70" font-family="Plus Jakarta Sans" font-size="8.5" fill="#64748b" text-anchor="middle">Goal achievement</text>

    <path d="M 440 55 L 460 55" stroke="#0284c7" stroke-width="2"/>

    <rect x="465" y="15" width="125" height="80" rx="6" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="527" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#581c87" text-anchor="middle">Utility-Based</text>
    <text x="527" y="55" font-family="Plus Jakarta Sans" font-size="9" fill="#9333ea" text-anchor="middle">Trade-off mapping</text>
    <text x="527" y="70" font-family="Plus Jakarta Sans" font-size="8.5" fill="#64748b" text-anchor="middle">Utility function U(s)</text>

    <path d="M 590 55 L 610 55" stroke="#0284c7" stroke-width="2"/>

    <rect x="615" y="15" width="115" height="80" rx="6" fill="#ccfbf1" stroke="#0f766e" stroke-width="1.5"/>
    <text x="672" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#0f766e" text-anchor="middle">Learning Agent</text>
    <text x="672" y="55" font-family="Plus Jakarta Sans" font-size="9" fill="#14b8a6" text-anchor="middle">Critic & Generator</text>
    <text x="672" y="70" font-family="Plus Jakarta Sans" font-size="8.5" fill="#64748b" text-anchor="middle">Improves over time</text>
  </svg>
  <div class="diagram-caption">Figure 1.1: Progression of Autonomous Agent Architectures from Simple Reflex to Learning Agents</div>
</div>

<h3 class="subsection-title">1. The Learning Agent Sub-Components:</h3>
<ul>
  <li><strong>Critic:</strong> Evaluates the agent's behavior against an external performance standard and provides reward/penalty feedback.</li>
  <li><strong>Learning Element:</strong> Responsible for making improvements based on feedback from the critic.</li>
  <li><strong>Performance Element:</strong> Responsible for selecting external actions (equivalent to the entire non-learning agent).</li>
  <li><strong>Problem Generator:</strong> Suggests novel exploratory actions that lead to new and informative experiences, rather than sticking only to known suboptimal paths.</li>
</ul>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module I)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Define an Intelligent Agent. Differentiate between Omniscience and Rationality with an example. (8 Marks)</div>
  <div class="qa-a">
    An <strong>Intelligent Agent</strong> is anything that perceives its environment through sensors and acts upon that environment through actuators.<br>
    - <strong>Rationality:</strong> Evaluated based on the expected performance given the percept sequence observed so far and built-in knowledge. It represents optimal decision-making under uncertainty.<br>
    - <strong>Omniscience:</strong> An omniscient agent knows the exact actual outcome of its actions and makes zero errors (impossible due to incomplete state visibility and random environmental events).<br>
    <em>Example:</em> A pedestrian crosses the street after carefully looking left and right (Rational). If a meteor strikes them from the sky, the action was still rational despite the tragic outcome, whereas an omniscient agent would have known about the meteor.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Provide a complete PEAS description for an Automated Medical Diagnosis System and analyze its environment across all 7 dimensions. (10 Marks)</div>
  <div class="qa-a">
    <strong>PEAS Description:</strong><br>
    • <strong>P:</strong> Patient health recovery, minimal diagnostic cost, zero misdiagnoses of critical illnesses.<br>
    • <strong>E:</strong> Patient physiology, hospital staff, clinical lab test systems, electronic health records.<br>
    • <strong>A:</strong> Diagnostic reports, prescription medication orders, clinical test recommendations.<br>
    • <strong>S:</strong> Symptom inputs, patient vital sign telemetry, lab test results, imaging scans.<br><br>
    <strong>Environment Classification:</strong><br>
    1. <em>Partially Observable:</em> Internal physiological processes cannot be fully sensed directly.<br>
    2. <em>Multi-Agent:</em> Interacts with human doctors, nurses, and patients.<br>
    3. <em>Stochastic:</em> Patient biological responses to medication vary probabilistically.<br>
    4. <em>Sequential:</em> Previous treatment choices alter patient physiology and future treatment efficacy.<br>
    5. <em>Dynamic:</em> Patient condition can deteriorate while the system deliberates.<br>
    6. <em>Continuous:</em> Vital signs, lab values, and time are continuous variables.<br>
    7. <em>Known:</em> Medical physics and pharmacology rules are largely established.
  </div>
</div>
"""
