AI_M1_EXHAUSTIVE = r"""
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
  <strong>Artificial Intelligence (AI)</strong> is the science and engineering of synthesizing computational artifacts capable of performing cognitive tasks traditionally associated with human intellect: perception, inductive/deductive reasoning, learning from experiential data, goal-directed planning, natural language comprehension, and autonomous decision-making under uncertainty.
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

<h2 class="section-title">Topic 7: Master University Examination Solved Question Bank (10 Solved Questions)</h2>

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

<div class="qa-card">
  <div class="qa-q">Q5. Explain the Subsumption Architecture proposed by Rodney Brooks. How does it contrast with Classical Symbolic AI? (8 Marks)</div>
  <div class="qa-a">
    • <strong>Classical Symbolic AI:</strong> Relies on a centralized "Sense-Plan-Act" pipeline with explicit symbolic internal world models.<br>
    • <strong>Subsumption Architecture (Behavior-Based AI):</strong> Eliminates central representations ("The world is its own best model"). The system is built from parallel, asynchronous, reactive behavioral layers (e.g. Layer 0: Avoid Obstacles; Layer 1: Wander; Layer 2: Explore). Higher layers can <em>suppress</em> inputs or <em>subsume</em> outputs of lower layers, achieving robust physical reactivity in dynamic environments without computationally prohibitive planning bottlenecks!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q6. Compare Goal-Based Agents and Utility-Based Agents with decision-theoretic examples. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Goal-Based Agents:</strong> Seek binary achievement of defined goals ($G(s) \in \{\text{True}, \text{False}\}$). They lack the ability to trade off conflicting criteria (e.g. speed vs safety) or quantify partial goal satisfaction.<br>
    • <strong>Utility-Based Agents:</strong> Map states to a real-valued scalar utility function $U: \mathcal{S} \rightarrow \mathbb{R}$. When multiple goals conflict (e.g., getting to the airport quickly vs spending minimal fuel vs avoiding toll roads), a utility agent computes the expected utility $\mathbb{E}[U] = \sum_s P(s \mid a) U(s)$ and selects the action that maximizes expected utility (Maximum Expected Utility Principle).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q7. Differentiate between Epistemic Actions and Pragmatic Actions with robotic exploration examples. (6 Marks)</div>
  <div class="qa-a">
    • <strong>Pragmatic Actions:</strong> Actions intended to change the physical world state to bring the agent closer to its goal (e.g., vacuum cleaner picking up dirt, autonomous car accelerating).<br>
    • <strong>Epistemic Actions:</strong> Actions whose primary purpose is to acquire information and reduce uncertainty in a partially observable world (e.g., exploring an unmapped room, running a medical diagnostic blood test, looking around a blind corner before turning).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q8. What are the key limitations of Expert Systems that led to the Second AI Winter? (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Knowledge Acquisition Bottleneck:</strong> Hand-crafting thousands of IF-THEN rules from human experts was expensive and slow.<br>
    2. <strong>Brittleness:</strong> Expert systems could not handle edge cases outside their narrow rule sets.<br>
    3. <strong>Lack of Commonsense Reasoning:</strong> Inability to make simple real-world deductions.<br>
    4. <strong>High Maintenance Costs:</strong> Conflicting rules caused unpredictable system behavior as rule bases grew.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q9. Explain the concept of Bounded Rationality proposed by Herbert Simon. (6 Marks)</div>
  <div class="qa-a">
    Perfect rationality assumes unbounded computation to find optimal actions. In the real world, agents face strict computational, memory, and time constraints. <strong>Bounded Rationality</strong> dictates that an agent acts as rationally as possible given its finite computational resources (satisficing rather than global optimization).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q10. Formulate the State-Space representation of the Water Jug Problem (4-Gallon and 3-Gallon Jugs to measure 2 Gallons). (8 Marks)</div>
  <div class="qa-a">
    • <strong>State Space:</strong> Ordered pair $(x, y)$ where $x \in \{0, 1, 2, 3, 4\}$ (water in 4-gal jug) and $y \in \{0, 1, 2, 3\}$ (water in 3-gal jug).<br>
    • <strong>Initial State:</strong> $(0, 0)$.<br>
    • <strong>Goal State:</strong> $(2, y)$ for any $y$.<br>
    • <strong>Production Rules / Operators:</strong><br>
      1. Fill 4-gal jug: $(x, y) \rightarrow (4, y)$ if $x < 4$.<br>
      2. Fill 3-gal jug: $(x, y) \rightarrow (x, 3)$ if $y < 3$.<br>
      3. Empty 4-gal jug: $(x, y) \rightarrow (0, y)$ if $x > 0$.<br>
      4. Empty 3-gal jug: $(x, y) \rightarrow (x, 0)$ if $y > 0$.<br>
      5. Pour from 3 to 4: $(x, y) \rightarrow (\min(4, x+y), y - (\min(4, x+y) - x))$.<br>
      6. Pour from 4 to 3: $(x, y) \rightarrow (x - (\min(3, x+y) - y), \min(3, x+y))$.<br>
    • <strong>Solution Trace:</strong> $(0,0) \rightarrow (0,3) \rightarrow (3,0) \rightarrow (3,3) \rightarrow (4,2) \rightarrow (0,2) \rightarrow (2,0)$ (Goal reached!).
  </div>
</div>

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

<h2 class="section-title">Topic 7.6: Detailed Mathematical Properties of State Space & Perception</h2>

<div class="formula-card">
  <strong>Formal Agent Perception History & Action Space:</strong>
  $$\mathbf{\mathcal{P} = \{p_1, p_2, \dots, p_k\} \implies \mathcal{P}^* = \bigcup_{t=0}^\infty \mathcal{P}^t}$$
  $$\mathbf{\text{Number of Possible Agent Functions over Horizon } T: \ |\mathcal{A}|^{|\mathcal{P}|^T}}$$
  <em>Combinatorial Significance:</em> For even modest $|\mathcal{P}|=10$ and $|\mathcal{A}|=5$ over $T=10$ steps, there are $5^{10^{10}}$ candidate agent functions! This astronomical search space proves why tabular lookup reflex agents are physically impossible and why compact, generalizing representations (logic, heuristics, neural networks) are mandatory.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Agent Performance Metric Engineering</div>
  <p>An autonomous street cleaning robot is deployed in an urban city center. Compare two proposed performance measures:</p>
  <ul>
    <li><strong>Metric 1:</strong> Amount of dirt collected in the robot's onboard disposal bin over 24 hours.</li>
    <li><strong>Metric 2:</strong> Cleanliness of the entire street network averaged over 24 hours.</li>
  </ul>
  <p><strong>Critical Agent Analysis:</strong></p>
  <ul>
    <li>Under <strong>Metric 1</strong>, a rational agent maximizes dirt in its bin. To maximize this metric, the agent might clean up a pile of dirt, dump it back onto the clean pavement, and sweep it up again repeatedly!</li>
    <li>Under <strong>Metric 2</strong>, the agent is rewarded strictly for the <em>desired state of the external environment</em> (clean streets), preventing perverse reward hacking!</li>
    <li><strong>Core Principle (Russell & Norvig):</strong> Design performance measures according to what you want to achieve in the environment, NOT according to how you think the agent should behave!</li>
  </ul>
</div>

<div class="qa-card">
  <div class="qa-q">Q16. Explain the Concept of Software Agents (Softbots) and Web Crawling Agents. (8 Marks)</div>
  <div class="qa-a">
    A <strong>Softbot</strong> is an intelligent agent whose environment is entirely digital (operating systems, web networks, databases, cloud infrastructure) rather than physical hardware. Example (Search Engine Indexing Spider):<br>
    • <strong>P:</strong> Freshness of search index, crawl coverage, low server load, high page pagerank relevance.<br>
    • <strong>E:</strong> The World Wide Web (HTTP/HTTPS protocols, HTML/DOM trees, sitemaps, robots.txt constraints).<br>
    • <strong>A:</strong> HTTP GET requests, URL extraction, indexing pipeline dispatch, rate-limiting sleep calls.<br>
    • <strong>S:</strong> HTTP status codes, HTML content strings, header response times.
  </div>
</div>

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
