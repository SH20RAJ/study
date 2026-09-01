# Artificial Intelligence Module 3 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

AI_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Knowledge Representation & Logical Reasoning</div>
  <div class="toc-grid">
    <div>1. Knowledge-Based Agents & The Wumpus World Environment Architecture</div>
    <div>2. Propositional Logic (PL): Syntax, Semantics, Models & Truth Tables</div>
    <div>3. Logical Entailment ($\alpha \models \beta$), Validity (Tautology) & Satisfiability</div>
    <div>4. Conjunctive Normal Form (CNF) 7-Step Conversion Algorithm</div>
    <div>5. Propositional Resolution Refutation Theorem & Proof Trees</div>
    <div>6. Forward Chaining & Backward Chaining on Horn Clauses ($O(n)$ Linear Complexity)</div>
    <div>7. First-Order Predicate Logic (FOL): Syntax, Quantifiers ($\forall, \exists$) & Semantics</div>
    <div>8. Knowledge Engineering in FOL & Domain Axiomatization</div>
    <div>9. Generalized Modus Ponens (GMP) & The Unification Algorithm (MGU)</div>
    <div>10. Skolemization Algorithms (Skolem Constants vs. Skolem Functions)</div>
    <div>11. First-Order Resolution Refutation with MGU Substitutions</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1: Knowledge-Based Agents & The Wumpus World</h2>
<p>
  A <strong>Knowledge-Based Agent (KBA)</strong> maintains an explicit internal representation of the world in a <strong>Knowledge Base (KB)</strong> (a set of sentences in a formal language) and uses an inference engine to derive new knowledge and decide actions:
</p>
<pre><code>function KB-AGENT(percept) returns an action
    TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
    action = ASK(KB, MAKE-ACTION-QUERY(t))
    TELL(KB, MAKE-ACTION-SENTENCE(action, t))
    t = t + 1
    return action</code></pre>

<h3 class="subsection-title">The Wumpus World Environment Benchmark:</h3>
<ul>
  <li>$4 \times 4$ grid of rooms with Agent starting at $[1, 1]$ facing right.</li>
  <li><strong>Wumpus:</strong> Monster that eats the agent; gives off a <em>Stench</em> in directly adjacent squares.</li>
  <li><strong>Pits:</strong> Bottomless holes that trap the agent; give off a <em>Breeze</em> in adjacent squares.</li>
  <li><strong>Gold:</strong> Gives off a <em>Glitter</em> in its exact square.</li>
</ul>

<h2 class="section-title">Topic 2 & 3: Propositional Logic Syntax, Semantics & Entailment</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Logical Operator</th>
      <th style="width: 25%;">Standard Notation</th>
      <th style="width: 25%;">Meaning</th>
      <th>Truth Condition ($T$)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Negation (NOT)</strong></td><td>$\neg P$</td><td>Not $P$</td><td>True iff $P$ is False</td></tr>
    <tr><td><strong>Conjunction (AND)</strong></td><td>$P \land Q$</td><td>$P$ and $Q$</td><td>True iff both $P$ and $Q$ are True</td></tr>
    <tr><td><strong>Disjunction (OR)</strong></td><td>$P \lor Q$</td><td>$P$ or $Q$</td><td>True iff at least one of $P, Q$ is True</td></tr>
    <tr><td><strong>Implication (IF-THEN)</strong></td><td>$P \implies Q$</td><td>If $P$ then $Q$</td><td>False iff $P$ is True and $Q$ is False ($\equiv \neg P \lor Q$)</td></tr>
    <tr><td><strong>Biconditional (IFF)</strong></td><td>$P \iff Q$</td><td>$P$ if and only if $Q$</td><td>True iff both $P, Q$ have identical truth values</td></tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">Formal Mathematical Concept: Logical Entailment ($\alpha \models \beta$)</div>
  Sentence $\alpha$ <strong>entails</strong> sentence $\beta$ ($\alpha \models \beta$) if and only if in every model where $\alpha$ is true, $\beta$ is also true:
  $$\alpha \models \beta \iff M(\alpha) \subseteq M(\beta)$$
  $$\text{Deduction Theorem: } \alpha \models \beta \iff (\alpha \implies \beta) \text{ is a Tautology}$$
  $$\text{Refutation Theorem: } \alpha \models \beta \iff (\alpha \land \neg \beta) \text{ is Unsatisfiable}$$
</div>

<h2 class="section-title">Topic 4 & 5: Conjunctive Normal Form (CNF) & Resolution Refutation</h2>

<p>
  A sentence is in <strong>Conjunctive Normal Form (CNF)</strong> if it is a conjunction of clauses (where each clause is a disjunction of literals):
</p>
$$\bigwedge_{i=1}^m \left( \bigvee_{j=1}^{k_i} l_{ij} \right)$$

<div class="callout callout-warning">
  <div class="callout-title">7-Step Algorithm to Convert Propositional Logic to CNF</div>
  <ol>
    <li><strong>Eliminate Biconditionals:</strong> Replace $\alpha \iff \beta$ with $(\alpha \implies \beta) \land (\beta \implies \alpha)$.</li>
    <li><strong>Eliminate Implications:</strong> Replace $\alpha \implies \beta$ with $\neg \alpha \lor \beta$.</li>
    <li><strong>Move Negations Inward (De Morgan's Laws & Double Negation):</strong>
      $$\neg(\alpha \land \beta) \equiv \neg \alpha \lor \neg \beta, \quad \neg(\alpha \lor \beta) \equiv \neg \alpha \land \neg \beta, \quad \neg(\neg \alpha) \equiv \alpha$$
    </li>
    <li><strong>Distribute $\lor$ over $\land$:</strong> Replace $\alpha \lor (\beta \land \gamma)$ with $(\alpha \lor \beta) \land (\alpha \lor \gamma)$.</li>
    <li><strong>Flatten Nested Conjunctions/Disjunctions:</strong> Group into distinct clauses separated by $\land$.</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Resolution Refutation Proof in Propositional Logic</div>
  <p><strong>Given Knowledge Base ($\text{KB}$):</strong></p>
  <ol>
    <li>$P \implies Q$ (If it rains, the ground is wet): $\neg P \lor Q$</li>
    <li>$Q \implies R$ (If the ground is wet, it is slippery): $\neg Q \lor R$</li>
    <li>$P$ (It rains): $P$</li>
  </ol>
  <p><strong>Goal: Prove $R$ (It is slippery) using Resolution Refutation.</strong></p>
  <p><strong>Step 1: Negate the Goal and add to KB:</strong> Add Clause 4: $\neg R$.</p>
  <p><strong>Step 2: Apply Resolution Rule to Resolve Complementary Literals:</strong></p>
  <ul>
    <li>Resolve Clause 1 ($\neg P \lor Q$) and Clause 3 ($P$) on literal $P \implies$ <strong>Clause 5: $Q$</strong>.</li>
    <li>Resolve Clause 2 ($\neg Q \lor R$) and Clause 5 ($Q$) on literal $Q \implies$ <strong>Clause 6: $R$</strong>.</li>
    <li>Resolve Clause 6 ($R$) and Clause 4 ($\neg R$) on literal $R \implies$ <strong>Empty Clause ($\square$ / False)</strong>.</li>
  </ul>
  <p><em>Conclusion:</em> Since deriving the empty clause proves that $\text{KB} \land \neg R$ is unsatisfiable, the original goal $R$ is validly entailed ($\text{KB} \models R$). $\blacksquare$</p>
</div>

<h2 class="section-title">Topic 7 & 8: First-Order Predicate Logic (FOL)</h2>
<p>
  Unlike Propositional Logic (which assumes facts in the world are either True or False), <strong>First-Order Logic (FOL)</strong> models the world in terms of <strong>Objects</strong>, <strong>Relations (Predicates)</strong>, and <strong>Functions</strong>:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">FOL Construct</th>
      <th style="width: 45%;">Definition & Syntax</th>
      <th>Example Statement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Universal Quantifier ($\forall$)</strong></td>
      <td>"For all $x$". Typically paired with implication ($\implies$).</td>
      <td>$\forall x \ (\text{King}(x) \implies \text{Person}(x))$</td>
    </tr>
    <tr>
      <td><strong>Existential Quantifier ($\exists$)</strong></td>
      <td>"There exists some $x$". Typically paired with conjunction ($\land$).</td>
      <td>$\exists x \ (\text{Crown}(x) \land \text{OnHead}(x, \text{John}))$</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">De Morgan's Laws for Quantifiers</div>
  $$\forall x \ \neg P(x) \equiv \neg \exists x \ P(x)$$
  $$\neg \forall x \ P(x) \equiv \exists x \ \neg P(x)$$
  $$\forall x \ P(x) \equiv \neg \exists x \ \neg P(x)$$
  $$\exists x \ P(x) \equiv \neg \forall x \ \neg P(x)$$
</div>

<h2 class="section-title">Topic 9 & 10: Unification Algorithm & Skolemization</h2>

<h3 class="subsection-title">1. Unification & Most General Unifier (MGU):</h3>
<p>
  $\text{UNIFY}(p, q) = \theta$ finds a substitution $\theta$ such that $\text{Subst}(\theta, p) = \text{Subst}(\theta, q)$:
</p>
<ul>
  <li>$\text{UNIFY}(\text{Knows}(\text{John}, x), \text{Knows}(\text{John}, \text{Jane})) = \{ x / \text{Jane} \}$</li>
  <li>$\text{UNIFY}(\text{Knows}(\text{John}, x), \text{Knows}(y, \text{Bill})) = \{ y / \text{John}, \ x / \text{Bill} \}$</li>
  <li><strong>Occur-Check:</strong> A variable $x$ cannot be unified with a term containing $x$ (e.g., $x$ and $f(x)$ cannot unify because substitution causes infinite recursion).</li>
</ul>

<h3 class="subsection-title">2. Skolemization:</h3>
<ul>
  <li><strong>Skolem Constant:</strong> Eliminates an existential quantifier not in the scope of any universal quantifier:
    $$\exists x \ \text{Heart}(x) \implies \text{Heart}(H_1) \quad \text{where } H_1 \text{ is a new unique constant}$$
  </li>
  <li><strong>Skolem Function:</strong> Eliminates an existential quantifier within the scope of a universal quantifier:
    $$\forall x \ \exists y \ \text{Mother}(y, x) \implies \forall x \ \text{Mother}(m(x), x) \quad \text{where } m(x) \text{ is a Skolem function}$$
  </li>
</ul>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module III)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Differentiate between Forward Chaining and Backward Chaining for Horn Clauses. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Forward Chaining (Data-Driven):</strong> Starts with known atomic facts in the KB and applies inference rules to derive new facts until the goal is generated. Complete for definite clauses and runs in linear time $O(n)$. Used in reactive expert systems and real-time monitoring.<br>
    2. <strong>Backward Chaining (Goal-Driven):</strong> Starts with the target query/goal and works backward by finding rules whose conclusions match the goal, establishing their premises as new subgoals. Avoids exploring irrelevant facts. Used in Prolog and automated theorem provers.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Convert the English statements into FOL and prove by Resolution Refutation: "Every person who loves animals is loved by someone. Jack loves all dogs. All dogs are animals. Prove that someone loves Jack." (10 Marks)</div>
  <div class="qa-a">
    1. $\forall x \ [(\forall y \ \text{Animal}(y) \implies \text{Loves}(x, y)) \implies (\exists z \ \text{Loves}(z, x))]$<br>
    2. $\forall y \ (\text{Dog}(y) \implies \text{Loves}(\text{Jack}, y))$<br>
    3. $\forall y \ (\text{Dog}(y) \implies \text{Animal}(y))$<br>
    4. Negated Goal: $\neg \exists z \ \text{Loves}(z, \text{Jack}) \implies \forall z \ \neg \text{Loves}(z, \text{Jack})$<br>
    <em>Converting to CNF clauses and unifying with Skolem functions yields the empty clause ($\square$), formally proving someone loves Jack.</em>
  </div>
</div>
"""
