# Artificial Intelligence Module 3 Exhaustive Content (9 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

AI_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Knowledge Representation & Logical Reasoning — Complete 9-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 15:</strong> Knowledge-Based Agents (KB, Inference Engine & TELL/ASK)</div>
    <div><strong>Topic 16:</strong> Propositional Logic (Syntax, Semantics, Truth Tables & Equivalences)</div>
    <div><strong>Topic 17:</strong> Propositional to Predicate Logic Transition</div>
    <div><strong>Topic 18:</strong> Propositional Logic-Based Agents (Wumpus World)</div>
    <div><strong>Topic 19:</strong> First-Order Predicate Logic (Constants, Predicates & Quantifiers)</div>
    <div><strong>Topic 20:</strong> Knowledge Representation in FOL (English to Logic Translation)</div>
    <div><strong>Topic 21:</strong> Forward Chaining (Data-Driven Deductive Reasoning)</div>
    <div><strong>Topic 22:</strong> Backward Chaining (Goal-Driven Hypothesis Verification)</div>
    <div><strong>Topic 23:</strong> The Resolution Inference Rule (Refutation Proofs & CNF)</div>
  </div>
</div>

<h2 class="section-title">Topic 15: Knowledge-Based Agents (KB Architecture)</h2>
<p>
  A <strong>Knowledge-Based Agent (KBA)</strong> uses a formal, explicit internal representation of knowledge (the Knowledge Base $KB$) and an Inference Engine to deduce new facts and make decisions:
</p>
<pre><code>TELL(KB, sentence)   <-- Adds new percept facts/rules to KB
ASK(KB, query)       <-- Deduces whether KB |= query (Entailment)</code></pre>

<h2 class="section-title">Topic 16 & 17: Propositional Logic vs. First-Order Logic (FOL)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Formal Logic System</th>
      <th style="width: 35%;">Ontological Commitment</th>
      <th>Epistemological Commitment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Propositional Logic</strong></td>
      <td>Facts that are either <strong>True or False</strong> (Boolean propositions $P, Q$). Treats atomic sentences as indivisible black boxes.</td>
      <td>Belief states: $\{\text{True}, \text{False}, \text{Unknown}\}$.</td>
    </tr>
    <tr>
      <td><strong>First-Order Logic (FOL)</strong></td>
      <td><strong>Objects</strong> (Constants), <strong>Relations</strong> (Predicates), <strong>Functions</strong>, and <strong>Quantifiers</strong> ($\forall, \exists$).</td>
      <td>Belief states: $\{\text{True}, \text{False}, \text{Unknown}\}$. Expressive power to model complex domains.</td>
    </tr>
  </tbody>
</table>

<div class="formula-card">
  <strong>Key Propositional Equivalence Laws:</strong>
  - Implication Elimination: $P \implies Q \equiv \neg P \vee Q$
  - Biconditional Elimination: $P \iff Q \equiv (P \implies Q) \wedge (Q \implies P)$
  - De Morgan's Laws: $\neg (P \wedge Q) \equiv \neg P \vee \neg Q, \quad \neg (P \vee Q) \equiv \neg P \wedge \neg Q$
</div>

<h2 class="section-title">Topic 19 & 20: Knowledge Representation in First-Order Logic (FOL)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Classic English $\rightarrow$ First-Order Logic Translation Suite</div>
  <table class="custom-table">
    <thead><tr><th>Natural English Statement</th><th>First-Order Predicate Logic Formulation</th></tr></thead>
    <tbody>
      <tr><td>"Every student is intelligent."</td><td>$\forall x \ (\text{Student}(x) \implies \text{Intelligent}(x))$</td></tr>
      <tr><td>"Some students like AI."</td><td>$\exists x \ (\text{Student}(x) \wedge \text{Likes}(x, \text{AI}))$</td></tr>
      <tr><td>"No person can live on the sun."</td><td>$\neg \exists x \ (\text{Person}(x) \wedge \text{LivesOn}(x, \text{Sun})) \equiv \forall x \ (\text{Person}(x) \implies \neg \text{LivesOn}(x, \text{Sun}))$</td></tr>
      <tr><td>"Everyone has a mother."</td><td>$\forall x \ \exists y \ \text{MotherOf}(y, x)$</td></tr>
    </tbody>
  </table>
</div>

<h2 class="section-title">Topic 21 & 22: Forward Chaining vs. Backward Chaining</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Parameter</th>
      <th style="width: 37%;">Forward Chaining (Data-Driven)</th>
      <th>Backward Chaining (Goal-Driven)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Starting Point</strong></td><td>Starts from known initial <strong>atomic facts</strong> in the KB.</td><td>Starts from the <strong>Goal query hypothesis</strong> $Q$.</td></tr>
    <tr><td><strong>Execution Direction</strong></td><td>Applies Modus Ponens forward: $P, P \implies Q \implies \text{infer } Q$. Adds new facts until goal is reached.</td><td>Works backward: finds rules that have $Q$ in the conclusion, and recursively proves their premises.</td></tr>
    <tr><td><strong>Suitability</strong></td><td>Ideal for monitoring, diagnosis, and reactive synthesis systems.</td><td>Ideal for targeted automated theorem proving, diagnosis, and query answering (Prolog).</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 23: The Resolution Refutation Algorithm</h2>

<div class="formula-card">
  <strong>The Resolution Inference Rule:</strong>
  $$\frac{\ell_1 \vee \dots \vee \ell_i \vee \dots \vee \ell_k, \quad m_1 \vee \dots \vee \neg \ell_i \vee \dots \vee m_n}{\ell_1 \vee \dots \vee \ell_{i-1} \vee \ell_{i+1} \vee \dots \vee \ell_k \vee m_1 \vee \dots \vee m_{j-1} \vee m_{j+1} \vee \dots \vee m_n}$$
</div>

<div class="callout callout-warning">
  <div class="callout-title">Algorithm: Proof by Resolution Refutation ($KB \models \alpha$)</div>
  <ol>
    <li>Convert all sentences in $KB$ into <strong>Conjunctive Normal Form (CNF)</strong> (Eliminate $\implies$, push $\neg$ inward, standardize variables, Skolemize $\exists$, drop $\forall$, distribute $\vee$ over $\wedge$).</li>
    <li><strong>Negate the Query:</strong> Add $\neg \alpha$ to the CNF knowledge base.</li>
    <li>Repeatedly apply the Resolution Rule to pairs of complementary literals ($\ell$ and $\neg \ell$) to generate new resolvents.</li>
    <li>If resolution derives the <strong>Empty Clause ($\Box$)</strong>, a formal logical contradiction is achieved $\implies$ Original query $\alpha$ is mathematically proven!</li>
  </ol>
</div>

<h2 class="section-title">🧠 M3 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Given $KB = \{ P \implies Q, \ Q \implies R, \ P \}$, prove $R$ using Resolution Refutation. (8 Marks)</div>
  <div class="qa-a">
    <strong>Step 1: Convert $KB$ to CNF Clauses:</strong><br>
    (1) $P \implies Q \equiv \neg P \vee Q$<br>
    (2) $Q \implies R \equiv \neg Q \vee R$<br>
    (3) $P$<br>
    <strong>Step 2: Add Negation of Goal $R$:</strong><br>
    (4) $\neg R$<br>
    <strong>Step 3: Resolution Steps:</strong><br>
    (5) Resolve (1) and (3) on literal $P \implies Q$<br>
    (6) Resolve (2) and (5) on literal $Q \implies R$<br>
    (7) Resolve (4) and (6) on literal $R \implies \Box$ (Empty Clause / Contradiction).<br>
    $\therefore R$ is proven true by refutation!
  </div>
</div>
"""
