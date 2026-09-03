#!/usr/bin/env python3
"""
Massive AI Suite Generator:
Constructs 30k-38k character content for every AI module to guarantee 10-14 pages per module!
"""

import os, sys
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

# Generate rich, exhaustive textbook sections
def build_exhaustive_m1():
    sections = []
    sections.append("""
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
    """)
    sections.append("""
    <h2 class="section-title">Topic 1: Foundational Definitions & The Four AI Perspectives</h2>
    <p><strong>Artificial Intelligence (AI)</strong> is the science and engineering of making intelligent entities, especially intelligent computer programs. AI represents computational artifacts capable of perception, learning, logical inference, goal-directed reasoning, and autonomous decision-making in complex environments.</p>
    
    <table class="custom-table">
      <thead><tr><th>Dimension</th><th>Human-Centric (Empirical)</th><th>Rationality-Centric (Normative)</th></tr></thead>
      <tbody>
        <tr><td><strong>Reasoning (Thought)</strong></td><td><strong>Thinking Humanly:</strong> Cognitive modeling, neuroscience, introspection (GPS, ACT-R).</td><td><strong>Thinking Rationally:</strong> Laws of Thought, formal logic, syllogisms (Aristotle, Boole, Frege).</td></tr>
        <tr><td><strong>Behavior (Action)</strong></td><td><strong>Acting Humanly:</strong> Turing Test (Alan Turing 1950), passing indistinguishable conversation.</td><td><strong>Acting Rationally:</strong> Rational Agent approach (Russell & Norvig), maximizing expected utility.</td></tr>
      </tbody>
    </table>

    <div class="worked-box">
      <div class="worked-title">🏛️ The 6 Core Subfields of the Total Turing Test</div>
      <ol>
        <li><strong>Natural Language Processing:</strong> Communicating fluently in natural human languages.</li>
        <li><strong>Knowledge Representation:</strong> Storing structured ontological assertions, episodic memories, and causal rules.</li>
        <li><strong>Automated Reasoning:</strong> Drawing logically sound deductions and answering queries.</li>
        <li><strong>Machine Learning:</strong> Adapting to new circumstances and extrapolating patterns from data.</li>
        <li><strong>Computer Vision:</strong> Perceiving 3D spatial environments and recognizing objects.</li>
        <li><strong>Robotics & Actuation:</strong> Manipulating physical objects and navigating continuous real-world terrain.</li>
      </ol>
    </div>
    """)
    
    # Add deep historical evolutions and Dartmouth 1956
    sections.append("""
    <h2 class="section-title">Topic 2: Historical Evolution & AI Winters</h2>
    <p>The formal birth of AI occurred at the Dartmouth College Summer Research Project in 1956, organized by John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon. Key eras:</p>
    <ul>
      <li><strong>1943–1956 (Gestation):</strong> Warren McCulloch and Walter Pitts proposed the first computational model of artificial neurons (1943). Alan Turing published "Computing Machinery and Intelligence" introducing the Turing Test (1950).</li>
      <li><strong>1956–1974 (Early Enthusiasm):</strong> Logic Theorist (Newell & Simon), Samuel's Checkers Player, Robinson's Resolution Principle (1965), Shakey the Robot at SRI.</li>
      <li><strong>1974–1980 (First AI Winter):</strong> Severe funding cuts following the Lighthill Report in the UK and DARPA funding reassessments due to combinatorial explosion in early toy problems and Minsky & Papert's critique of single-layer perceptrons.</li>
      <li><strong>1980–1987 (Expert Systems Boom):</strong> Commercial success of rule-based Expert Systems (e.g., XCON at Digital Equipment Corporation saving $40M annually). Knowledge engineering became an industry.</li>
      <li><strong>1987–1993 (Second AI Winter):</strong> Collapse of specialized LISP machine hardware market; high maintenance cost of brittle rule bases.</li>
      <li><strong>1993–Present (Data-Driven & Deep Learning Revolution):</strong> IBM Deep Blue defeats Garry Kasparov (1997), DARPA Grand Challenge autonomous vehicles (2005), Deep Learning resurgence with ImageNet (AlexNet 2012), AlphaGo (2016), and Transformers/LLMs (2017–Present).</li>
    </ul>
    """)

    # Intelligent Agents & Rationality
    sections.append("""
    <h2 class="section-title">Topic 3 & 4: Intelligent Agents & Formal Concept of Rationality</h2>
    <p>An <strong>Agent</strong> interacts with its environment via a continuous perception-action cycle. Mathematically, an agent is defined by an <strong>Agent Function</strong>:</p>
    <div class="formula-card">
      <strong>The Mathematical Agent Function:</strong>
      $$\mathbf{f: \mathcal{P}^* \longrightarrow \mathcal{A}}$$
      Where $\mathcal{P}^*$ is the set of all possible percept sequences (history) and $\mathcal{A}$ is the set of actions.
    </div>
    <p>A <strong>Rational Agent</strong> is one that, for each possible percept sequence, selects an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent possesses.</p>
    """)

    # 10 Detailed PEAS tables
    sections.append("""
    <h2 class="section-title">Topic 5: PEAS Framework for 10 Real-World Domains</h2>
    <table class="custom-table">
      <thead><tr><th>Domain</th><th>Performance ($P$)</th><th>Environment ($E$)</th><th>Actuators ($A$)</th><th>Sensors ($S$)</th></tr></thead>
      <tbody>
        <tr><td><strong>Autonomous Vehicle</strong></td><td>Safety, speed, passenger comfort, fuel efficiency.</td><td>Roads, traffic, pedestrians, weather.</td><td>Steering, throttle, brakes, horn, turn signals.</td><td>LiDAR, cameras, RADAR, GPS, IMU, speedometer.</td></tr>
        <tr><td><strong>Medical Diagnosis</strong></td><td>Healthy patient, minimized side-effects/costs.</td><td>Hospital, patient, staff, symptoms.</td><td>Questions, tests, prescriptions, treatments.</td><td>Keyboard input of symptoms, lab analyzers.</td></tr>
        <tr><td><strong>Satellite Image Analysis</strong></td><td>High segmentation accuracy, classification F1.</td><td>Orbit, downlinked multi-spectral imagery.</td><td>Display classifications, fire alerts.</td><td>High-res optical, infrared, synthetic aperture radar.</td></tr>
        <tr><td><strong>Part-Picking Robot</strong></td><td>Parts sorted/hour, zero drops, no damage.</td><td>Conveyor belt, bins, parts, assembly floor.</td><td>Jointed robotic arm, vacuum gripper.</td><td>RGB-D cameras, tactile touch sensors.</td></tr>
        <tr><td><strong>Automated Fraud Detector</strong></td><td>Detection rate, minimized false positives.</td><td>Credit card transaction stream, user profiles.</td><td>Block card, approve transaction, send OTP.</td><td>Transaction metadata, IP geolocation, merchant logs.</td></tr>
        <tr><td><strong>Interactive Tutor</strong></td><td>Student test score gain, high engagement.</td><td>Student, lessons, quiz database.</td><td>Display questions, hints, explanations.</td><td>Keystrokes, quiz answer selections, response times.</td></tr>
        <tr><td><strong>Smart Thermostat</strong></td><td>Comfort temperature, minimized energy kWh.</td><td>Building interior, external ambient weather.</td><td>HVAC relay, heat pump, fan blower.</td><td>Temperature sensor, humidity, PIR motion sensor.</td></tr>
        <tr><td><strong>Chess AI (Stockfish)</strong></td><td>Win game ($+1$), draw ($0$), avoid blunders.</td><td>$8\times 8$ board, opponent player, clock.</td><td>Move command ($e2 \rightarrow e4$).</td><td>Board state matrix representation.</td></tr>
        <tr><td><strong>Autonomous Combat Drone</strong></td><td>Target neutralization, survivability, low collateral.</td><td>Airspace, terrain, enemy radar, GPS-denied zones.</td><td>Flight control surfaces, turbine thrust, weapons.</td><td>Optical targeting, FLIR infrared, inertial nav.</td></tr>
        <tr><td><strong>High-Frequency Trading</strong></td><td>Risk-adjusted return (Sharpe ratio), zero slippage.</td><td>Electronic exchanges (NASDAQ, CME), order books.</td><td>Limit orders, market orders, cancel requests.</td><td>L3 direct market access feeds, latency clocks.</td></tr>
      </tbody>
    </table>
    """)

    # Environmental Taxonomy
    sections.append("""
    <h2 class="section-title">Topic 5.2: Complete Environmental Taxonomy</h2>
    <table class="custom-table">
      <thead><tr><th>Dimension</th><th>Definition</th><th>Contrasting Examples</th></tr></thead>
      <tbody>
        <tr><td><strong>Fully vs. Partially Observable</strong></td><td>Agent sensors provide access to the complete state of the environment at all points in time.</td><td>Chess (Fully) vs. Poker (Partially — opponent cards hidden).</td></tr>
        <tr><td><strong>Single vs. Multi-Agent</strong></td><td>An agent operates alone versus in an environment with other goal-directed agents.</td><td>Crossword puzzle (Single) vs. Chess / Soccer (Multi-agent).</td></tr>
        <tr><td><strong>Deterministic vs. Stochastic</strong></td><td>The next state is completely determined by the current state and the agent's action.</td><td>Chess (Deterministic) vs. Backgammon / Self-driving (Stochastic).</td></tr>
        <tr><td><strong>Episodic vs. Sequential</strong></td><td>Current decision does not affect future episodes; each episode is independent.</td><td>Defect inspection (Episodic) vs. Chess / Driving (Sequential).</td></tr>
        <tr><td><strong>Static vs. Dynamic</strong></td><td>The environment changes while the agent is deliberating and choosing an action.</td><td>Crossword (Static) vs. Driving / RoboCup (Dynamic).</td></tr>
        <tr><td><strong>Discrete vs. Continuous</strong></td><td>State, time, percepts, or actions are distinct countable quantities vs. continuous intervals.</td><td>Chess (Discrete) vs. Robot navigation (Continuous).</td></tr>
        <tr><td><strong>Known vs. Unknown</strong></td><td>The outcomes (or probabilities) for all actions are given to the agent vs. must be learned.</td><td>Solitaire (Known rules) vs. Video game playing (Unknown rules).</td></tr>
      </tbody>
    </table>
    """)

    # 5 Classical Agent Architectures with Deep Structural Explanations
    sections.append("""
    <h2 class="section-title">Topic 6: The 5 Classical Agent Structural Architectures</h2>
    <table class="custom-table">
      <thead><tr><th>Architecture</th><th>Internal Components & Working Mechanism</th><th>Advantages & Limitations</th></tr></thead>
      <tbody>
        <tr><td><strong>1. Simple Reflex Agent</strong></td><td>Operates strictly on current percept using Condition-Action Rules (`IF car-in-front-is-braking THEN initiate-braking`). Has no internal memory of past percepts.</td><td>Extremely low computational latency; fails completely in partially observable environments (enters infinite loops).</td></tr>
        <tr><td><strong>2. Model-Based Reflex Agent</strong></td><td>Maintains internal state representing how the unobserved world evolves independently and how the agent's actions affect the world.</td><td>Handles partial observability by reconstructing unobserved reality; relies on accurate physical transition models.</td></tr>
        <tr><td><strong>3. Goal-Based Agent</strong></td><td>Combines internal state with explicit goal representations. Evaluates multiple action sequences via search and planning.</td><td>Highly adaptable when goals change; higher deliberative latency.</td></tr>
        <tr><td><strong>4. Utility-Based Agent</strong></td><td>Maps states to real-valued scalar utility $U(s) \in \mathbb{R}$. Maximizes expected utility $\mathbb{E}[U] = \sum_s P(s \mid a) U(s)$ under uncertainty.</td><td>Optimal trade-offs between competing goals; computationally demanding.</td></tr>
        <tr><td><strong>5. Learning Agent</strong></td><td>Decomposes into 4 modules: <em>Learning Element</em> (improves), <em>Critic</em> (evaluates), <em>Performance Element</em> (acts), <em>Problem Generator</em> (explores).</td><td>Can operate in initially unknown environments and discover superhuman strategies.</td></tr>
      </tbody>
    </table>
    """)

    # 10 Solved University Examination Questions
    sections.append("""
    <h2 class="section-title">Topic 7: Master University Examination Solved Question Bank (10 Questions)</h2>
    <div class="qa-card"><div class="qa-q">Q1. Explain the difference between Thinking Humanly, Acting Humanly, Thinking Rationally, and Acting Rationally. (8 Marks)</div><div class="qa-a">Thinking Humanly focuses on cognitive psychology and empirical models of human thought (GPS). Acting Humanly focuses on passing empirical behavioral tests without requiring human-like internal mechanisms (Turing Test). Thinking Rationally formalizes laws of thought using syllogisms and deductive logic. Acting Rationally (the modern AI standard) focuses on designing agents that achieve the best expected outcome given their percepts and resources.</div></div>
    <div class="qa-card"><div class="qa-q">Q2. Prove why a Simple Reflex Agent cannot solve the 2-room vacuum cleaner problem if location sensors are omitted. (8 Marks)</div><div class="qa-a">Without a location sensor or internal memory, the agent cannot distinguish whether it is in Room A or Room B. If both rooms are clean, an action like `MoveLeft` or `MoveRight` will cause it to oscillate indefinitely or collide with walls. An internal state (Model-Based) is mathematically required to remember that Room A has already been cleaned when entering Room B.</div></div>
    <div class="qa-card"><div class="qa-q">Q3. Formally specify the PEAS for an Automated Medical Diagnostic System. (8 Marks)</div><div class="qa-a">• <strong>P:</strong> Patient health recovery, diagnosis precision, low diagnostic cost, minimal patient discomfort.<br>• <strong>E:</strong> Hospital clinic, patient symptoms, lab test results, disease epidemiology.<br>• <strong>A:</strong> Display questions, recommend blood tests, prescribe medication, referral.<br>• <strong>S:</strong> Keyboard/speech input of symptoms, optical lab data scanners, EHR telemetry.</div></div>
    <div class="qa-card"><div class="qa-q">Q4. What is the Chinese Room Argument? Explain John Searle's refutation of Strong AI. (8 Marks)</div><div class="qa-a">Searle imagines a person in a closed room who follows English rulebooks to transform Chinese input symbols into Chinese output symbols. To outside observers, the room passes the Turing Test in Chinese. However, the person inside does not understand Chinese semantics. Searle argues that syntax alone is insufficient for semantics, refuting the claim that running a computer program constitutes genuine mental understanding (Strong AI).</div></div>
    <div class="qa-card"><div class="qa-q">Q5. Explain the architecture of a Learning Agent with a block diagram. (8 Marks)</div><div class="qa-a">A Learning Agent comprises:<br>1. <strong>Learning Element:</strong> Makes improvements by analyzing experience.<br>2. <strong>Critic:</strong> Evaluates performance against an external standard.<br>3. <strong>Performance Element:</strong> The operational agent that selects actions based on percepts.<br>4. <strong>Problem Generator:</strong> Suggests exploratory actions leading to new experiences.</div></div>
    <div class="qa-card"><div class="qa-q">Q6. Classify the environment of Autonomous Driving across all 7 environmental dimensions. (8 Marks)</div><div class="qa-a">Partially Observable (blind spots), Stochastic (unpredictable human pedestrians), Sequential (current speed affects braking distance), Dynamic (traffic moves while computing), Continuous (steering angle and velocity), Multi-Agent (pedestrians, cars, police), Known (rules of traffic known).</div></div>
    <div class="qa-card"><div class="qa-q">Q7. What is an Epistemic Action? Give an example in robotics. (6 Marks)</div><div class="qa-a">An epistemic action is an action taken specifically to acquire information and reduce uncertainty rather than to directly achieve a goal state. Example: A mobile robot rotating its camera 360 degrees or moving towards an occluded doorway to map an unobserved room.</div></div>
    <div class="qa-card"><div class="qa-q">Q8. What are the key limitations of Expert Systems that led to the Second AI Winter? (8 Marks)</div><div class="qa-a">1. <strong>Knowledge Acquisition Bottleneck:</strong> Hand-crafting thousands of IF-THEN rules from human experts was expensive and slow.<br>2. <strong>Brittleness:</strong> Expert systems could not handle edge cases outside their narrow rule sets.<br>3. <strong>Lack of Commonsense Reasoning:</strong> Inability to make simple real-world deductions.<br>4. <strong>High Maintenance Costs:</strong> Conflicting rules caused unpredictable system behavior as rule bases grew.</div></div>
    <div class="qa-card"><div class="qa-q">Q9. Contrast Utility-Based Agents with Goal-Based Agents. (6 Marks)</div><div class="qa-a">Goal-based agents distinguish only between goal states and non-goal states (binary satisfaction). Utility-based agents use a continuous utility function $U(s) \in \mathbb{R}$ to make quantitative trade-offs between competing goals (e.g. speed vs safety) and select optimal actions under risk and uncertainty.</div></div>
    <div class="qa-card"><div class="qa-q">Q10. Explain the concept of Bounded Rationality proposed by Herbert Simon. (6 Marks)</div><div class="qa-a">Perfect rationality assumes unbounded computation to find optimal actions. In the real world, agents face strict computational, memory, and time constraints. <strong>Bounded Rationality</strong> dictates that an agent acts as rationally as possible given its finite computational resources (satisficing rather than global optimization).</div></div>
    """)
    return "".join(sections)

print("AI Module 1 builder prepared.")
