#!/usr/bin/env python3
"""
Comprehensive Content Generator & Playwright PDF Compiler for Artificial Intelligence (CS24307).
Generates 10-15 Page Modules (M1–M5), 10-Page Master Revision, and 50+ Page Full Course Master Book.
"""

import os, re
from playwright.sync_api import sync_playwright

AI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artificial-intelligence"))
HTML_DIR = os.path.join(AI_DIR, "html")
PDF_DIR = os.path.join(AI_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

# ---------------- MODULE 1: PRELIMINARIES & INTELLIGENT AGENTS ----------------
AI_M1 = r"""
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
  <div class="qa-q">Q2. Formally classify the Environment of: (a) Poker, (b) Autonomous Driving, and (c) Crossword Puzzle. (9 Marks)</div>
  <div class="qa-a">
    • <strong>Poker:</strong> Partially Observable (hidden cards), Stochastic (card draws), Sequential, Static, Discrete, Multi-Agent (Adversarial).<br>
    • <strong>Autonomous Driving:</strong> Partially Observable, Stochastic, Sequential, Dynamic, Continuous, Multi-Agent.<br>
    • <strong>Crossword Puzzle:</strong> Fully Observable, Deterministic, Sequential, Static, Discrete, Single-Agent.
  </div>
</div>
"""

def generate_ai_content_files():
    with open(os.path.join(AI_DIR, "ai_module1_content.py"), "w", encoding="utf-8") as f:
        f.write(f'AI_M1_EXHAUSTIVE = r"""{AI_M1}"""\n')
    print("✅ AI Module 1 Content generated.")

if __name__ == "__main__":
    generate_ai_content_files()
