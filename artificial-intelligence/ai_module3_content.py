AI_M3_EXHAUSTIVE = r"""
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

<h2 class="section-title">Topic 22.2: Master University Examination Solved Question Bank (10 Solved Questions)</h2>

<div class="qa-card"><div class="qa-q">Q1. Prove that Modus Ponens is sound. (6 Marks)</div><div class="qa-a">Modus Ponens states: From $\alpha$ and $\alpha \rightarrow \beta$, infer $\beta$. In truth table semantics: Whenever $\alpha$ is True and $\alpha \rightarrow \beta$ is True, $\beta$ must be True (since if $\beta$ were False, $\alpha \rightarrow \beta$ would be False, contradicting the premise). Thus, Modus Ponens preserves truth in all possible models.</div></div>
<div class="qa-card"><div class="qa-q">Q2. Convert the sentence $\neg \forall x (\text{Dog}(x) \rightarrow \exists y (\text{Cat}(y) \land \text{Chases}(x, y)))$ into Skolemized CNF. (10 Marks)</div><div class="qa-a">1. Move negation inward: $\exists x \neg (\neg \text{Dog}(x) \lor \exists y (\text{Cat}(y) \land \text{Chases}(x, y))) \implies \exists x (\text{Dog}(x) \land \forall y (\neg \text{Cat}(y) \lor \neg \text{Chases}(x, y)))$.<br>2. Skolemize existential variable $x$ with Skolem constant $D$: $\mathbf{\text{Clause 1: } \text{Dog}(D)}$, $\mathbf{\text{Clause 2: } \neg \text{Cat}(y) \lor \neg \text{Chases}(D, y)}$.</div></div>
<div class="qa-card"><div class="qa-q">Q3. Explain Forward Chaining and Backward Chaining for Horn Clauses. Compare their computational efficiencies. (8 Marks)</div><div class="qa-a">• <strong>Forward Chaining (Data-Driven):</strong> Starts from known facts in the KB and iteratively fires rules whose premises are satisfied, adding new conclusions until the query is reached. Complete and runs in $O(\text{size of KB})$ time for definite clauses.<br>• <strong>Backward Chaining (Goal-Driven):</strong> Starts from the goal query and recursively searches backwards for rules whose conclusions match the goal, resolving sub-goals against facts. Avoids generating facts irrelevant to the goal.</div></div>
<div class="qa-card"><div class="qa-q">Q4. What is the Occur Check in the Unification Algorithm? Why is it crucial? (8 Marks)</div><div class="qa-a">The Occur Check verifies whether a variable $v$ appears inside the term $t$ before binding $v/t$. Example: Unifying $x$ with $f(x)$. If permitted, it produces an infinite recursive term $x = f(f(f(\dots)))$, which leads to non-terminating loops and logical unsoundness in automated theorem provers! (Standard Prolog omits occur-check for speed, leading to occasional unsound derivations).</div></div>
<div class="qa-card"><div class="qa-q">Q5. Explain the Frame Problem, Qualification Problem, and Ramification Problem in Knowledge Representation. (8 Marks)</div><div class="qa-a">1. <strong>Frame Problem:</strong> Representing what remains <em>unchanged</em> in the world when an action is executed without explicitly listing millions of non-effects.<br>2. <strong>Qualification Problem:</strong> The impossibility of listing all infinite preconditions required for an action to succeed (e.g. car starting requires battery, gas, no potato in tailpipe, no asteroid strike).<br>3. <strong>Ramification Problem:</strong> Handling implicit side-effects (indirect consequences) of actions without writing separate explicit rules for each.</div></div>
<div class="qa-card"><div class="qa-q">Q6. Convert the proposition $(A \land B) \rightarrow (C \lor D)$ into Conjunctive Normal Form (CNF). (6 Marks)</div><div class="qa-a">1. Eliminate implication: $\neg (A \land B) \lor (C \lor D)$.<br>2. De Morgan's: $(\neg A \lor \neg B) \lor (C \lor D)$.<br>3. Flatten disjunction: $\mathbf{(\neg A \lor \neg B \lor C \lor D)}$ (Single valid CNF clause!).</div></div>
<div class="qa-card"><div class="qa-q">Q7. Explain Semantic Networks and Frames as Knowledge Representation schemes. (8 Marks)</div><div class="qa-a">• <strong>Semantic Networks:</strong> Represent knowledge as directed graphs where nodes represent concepts/objects and edges represent binary relations (e.g., `is-a`, `has-a`, `part-of`). Enables taxonomic property inheritance.<br>• <strong>Frames (Minsky):</strong> Structured data structures containing named <em>slots</em> and associated <em>fillers</em> (values, default values, or procedural attachment methods/demons).</div></div>
<div class="qa-card"><div class="qa-q">Q8. What is Non-Monotonic Logic? Explain Default Reasoning and Circumscription. (8 Marks)</div><div class="qa-a">In classical monotonic logic, adding new axioms can never invalidate previously derived theorems. In <strong>Non-Monotonic Logic</strong>, conclusions can be retracted when new evidence arrives (e.g. "Tweety is a bird $\implies$ Tweety flies"; Learning "Tweety is a penguin" retracts "Tweety flies"). <strong>Default Logic</strong> introduces default inference rules $\frac{\alpha : \beta}{\gamma}$. <strong>Circumscription</strong> formalizes the assumption that things are normal unless explicitly stated otherwise.</div></div>
<div class="qa-card"><div class="qa-q">Q9. Explain the DPLL (Davis-Putnam-Logemann-Loveland) Satisfiability Algorithm. (8 Marks)</div><div class="qa-a">DPLL is a recursive backtracking search for checking SAT over CNF clauses:<br>1. Early Termination (SAT if all clauses true; Backtrack if any clause empty).<br>2. Pure Literal Rule: Literals appearing with only one polarity across all clauses are assigned that polarity immediately.<br>3. Unit Propagation: Unit clauses force immediate deterministic variable assignments.<br>4. Splitting: Branch recursively on $X=\text{True}$ and $X=\text{False}$.</div></div>
<div class="qa-card"><div class="qa-q">Q10. Explain Ontology Engineering and the Role of Description Logics (OWL). (8 Marks)</div><div class="qa-a">An <strong>Ontology</strong> formally defines the concepts, entities, categories, and relationships within a domain. <strong>Description Logics (DLs)</strong> (like $\mathcal{SHIQ}, \mathcal{SROIQ}$) are decidable fragments of First-Order Logic providing the theoretical foundation for Semantic Web standards (OWL / RDF). DL systems provide automated subsumption checking ($C \sqsubseteq D$) and consistency checking.</div></div>

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

<h2 class="section-title">Topic 22.6: Advanced Resolution Strategies & Knowledge Compilation</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Resolution Strategy</th>
      <th style="width: 40%;">Algorithmic Restriction</th>
      <th>Completeness & Efficiency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Unit Resolution</strong></td>
      <td>At least one of the two parent clauses must be a <em>unit clause</em> (containing exactly one literal).</td>
      <td>Incomplete in general; complete and runs in $O(N)$ time for Horn KBs.</td>
    </tr>
    <tr>
      <td><strong>Input Resolution</strong></td>
      <td>At least one parent clause must come from the original input KB or negated query (never two derived clauses).</td>
      <td>Incomplete in general; equivalent in power to Unit Resolution.</td>
    </tr>
    <tr>
      <td><strong>Linear Resolution</strong></td>
      <td>Each step resolves the most recently derived clause with either an input clause or a previous ancestor clause.</td>
      <td><strong>Refutation Complete</strong>; basis for Prolog's SLD resolution.</td>
    </tr>
    <tr>
      <td><strong>Set of Support (SOS)</strong></td>
      <td>Every resolution step must involve at least one clause derived from the negated query (the set of support).</td>
      <td><strong>Refutation Complete</strong>; prevents wasteful resolution among mutually consistent background KB axioms.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Proof: The "Customs Official" Full Refutation Proof Tree</div>
  <p><strong>Axioms:</strong></p>
  <ol>
    <li>$C_1: \neg \text{Official}(x) \lor \neg \text{Enters}(y) \lor \text{VIP}(y) \lor \text{Searches}(x, y)$</li>
    <li>$C_2: \text{Smuggler}(A)$ (Skolem constant $A$)</li>
    <li>$C_3: \text{Enters}(A)$</li>
    <li>$C_4: \neg \text{Searches}(z, A) \lor \text{Smuggler}(z)$</li>
    <li>$C_5: \neg \text{Smuggler}(x) \lor \neg \text{VIP}(x)$</li>
    <li>$C_6: \text{Official}(B)$ (Official $B$ exists)</li>
  </ol>
  <p><strong>Query:</strong> Prove $\exists w (\text{Official}(w) \land \text{Smuggler}(w))$. Negated Query: $C_7: \neg \text{Official}(w) \lor \neg \text{Smuggler}(w)$.</p>
  <p><strong>Resolution Proof Steps:</strong></p>
  <ol>
    <li>Resolve $C_2$ ($\text{Smuggler}(A)$) with $C_5$ $\{x/A\} \implies \mathbf{C_8: \neg \text{VIP}(A)}$.</li>
    <li>Resolve $C_1$ with $C_3$ $\{y/A\} \implies \mathbf{C_9: \neg \text{Official}(x) \lor \text{VIP}(A) \lor \text{Searches}(x, A)}$.</li>
    <li>Resolve $C_9$ with $C_8 \implies \mathbf{C_{10}: \neg \text{Official}(x) \lor \text{Searches}(x, A)}$.</li>
    <li>Resolve $C_{10}$ with $C_4$ $\{z/x\} \implies \mathbf{C_{11}: \neg \text{Official}(x) \lor \text{Smuggler}(x)}$.</li>
    <li>Resolve $C_{11}$ with $C_6$ $\{x/B\} \implies \mathbf{C_{12}: \text{Smuggler}(B)}$.</li>
    <li>Resolve $C_{12}$ with $C_7$ $\{w/B\} \implies \mathbf{C_{13}: \neg \text{Official}(B)}$.</li>
    <li>Resolve $C_{13}$ with $C_6$ ($\text{Official}(B)$) $\implies \mathbf{\Box \text{ (EMPTY CLAUSE - CONTRADICTION!)}}$.</li>
  </ol>
  $$\mathbf{\text{Q.E.D. Strictly proven that some official must be a smuggler!}}$$
</div>

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

<h2 class="section-title">Topic 22.8: Complete Step-by-Step Solved Proof Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Proof: The "Customs and Smuggler" Full Resolution Refutation Tree</div>
  <p><strong>Axioms:</strong></p>
  <ol>
    <li>$\neg \text{Official}(x) \lor \neg \text{Enters}(y) \lor \text{VIP}(y) \lor \text{Searches}(x, y)$</li>
    <li>$\text{Smuggler}(A) \land \text{Enters}(A) \land (\neg \text{Searches}(z, A) \lor \text{Smuggler}(z))$ (Skolem constant $A$)</li>
    <li>$\neg \text{Smuggler}(x) \lor \neg \text{VIP}(x)$</li>
    <li>$\text{Official}(O_1)$</li>
  </ol>
  <p><strong>Refutation Steps:</strong></p>
  <ol>
    <li>Resolve $\text{Smuggler}(A)$ with Clause 3 $\{x/A\} \implies \mathbf{\neg \text{VIP}(A)}$.</li>
    <li>Resolve Clause 1 with $\text{Enters}(A)$ $\{y/A\} \implies \neg \text{Official}(x) \lor \text{VIP}(A) \lor \text{Searches}(x, A)$.</li>
    <li>Resolve with $\neg \text{VIP}(A) \implies \neg \text{Official}(x) \lor \text{Searches}(x, A)$.</li>
    <li>Resolve with Clause 2 ($\neg \text{Searches}(z, A) \lor \text{Smuggler}(z)$) $\{z/x\} \implies \mathbf{\neg \text{Official}(x) \lor \text{Smuggler}(x)}$.</li>
    <li>Resolve with $\text{Official}(O_1) \implies \mathbf{\text{Smuggler}(O_1)}$.</li>
    <li>Resolve with Negated Query clause $(\neg \text{Official}(O_1) \lor \neg \text{Smuggler}(O_1)) \implies \mathbf{\Box \text{ (EMPTY CLAUSE)}}$.</li>
  </ol>
  $$\mathbf{\text{Q.E.D. Proof complete!}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Situation Calculus Axiomatization</div>
  <p>In Situation Calculus, actions take an agent from situation $s$ to situation $do(a, s)$:</p>
  <ul>
    <li><strong>Possibility Axiom (Preconditions for Pickup):</strong>
      $$\mathbf{\text{Poss}(\text{PickUp}(x), s) \iff \text{Clear}(x, s) \land \text{At}(\text{Robot}, x, s) \land \text{ArmEmpty}(s)}$$
    </li>
    <li><strong>Successor-State Axiom (Effect on Holding):</strong>
      $$\mathbf{\text{Holding}(x, do(a, s)) \iff (a = \text{PickUp}(x)) \lor (\text{Holding}(x, s) \land a \neq \text{Release}(x))}$$
    </li>
  </ul>
</div>

<div class="qa-card">
  <div class="qa-q">Q16. Explain Knowledge Base Consistency and Model Checking using Truth Tables. (8 Marks)</div>
  <div class="qa-a">
    A Knowledge Base $KB$ is <strong>consistent (satisfiable)</strong> if there exists at least one truth assignment (model) under which all sentences in $KB$ evaluate to True. <strong>Model Checking</strong> enumerates all $2^n$ interpretations of the $n$ proposition symbols in a truth table. For each row where $KB = \text{True}$, it verifies if the query sentence $\alpha = \text{True}$. If $\alpha$ is True in every model where $KB$ is True, then $KB \models \alpha$ (sound and complete, but exponential time $O(2^n)$).
  </div>
</div>

<h2 class="section-title">Topic 22.9: Modal Logic, Epistemic Reasoning & Dempster-Shafer Theory</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Formal Logic System</th>
      <th style="width: 35%;">Modal Operators & Axioms</th>
      <th>AI Multi-Agent Application</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Epistemic Logic ($S5$)</strong></td>
      <td>Knowledge operator $K_i \phi$ ("Agent $i$ knows $\phi$"). Axioms: $K_i \phi \rightarrow \phi$ (Truth), $K_i \phi \rightarrow K_i K_i \phi$ (Positive Introspection), $\neg K_i \phi \rightarrow K_i \neg K_i \phi$ (Negative Introspection).</td>
      <td>Distributed systems consensus, multi-agent common knowledge ($C \phi$), Muddy Children puzzle.</td>
    </tr>
    <tr>
      <td><strong>Temporal Logic (LTL / CTL)</strong></td>
      <td>LTL operators: $\mathbf{G}\phi$ (Always), $\mathbf{F}\phi$ (Eventually), $\mathbf{X}\phi$ (Next), $\phi \mathbf{U} \psi$ (Until). CTL adds path quantifiers $\mathbf{A}$ (All paths), $\mathbf{E}$ (Exists path).</td>
      <td>Model checking automated safety verification of autonomous flight control and medical robotics software.</td>
    </tr>
    <tr>
      <td><strong>Dempster-Shafer Theory of Evidence</strong></td>
      <td>Mass function $m(A) \in [0, 1]$ over power set $2^\Theta$. Belief function $\text{Bel}(A) = \sum_{B \subseteq A} m(B)$, Plausibility $\text{Pl}(A) = 1 - \text{Bel}(\neg A)$. Dempster's Rule of Combination: $m_1 \oplus m_2(A) = \frac{\sum_{B \cap C = A} m_1(B) m_2(C)}{1 - K}$.</td>
      <td>Sensor fusion with epistemic ignorance (distinguishes total ignorance from equal probability!).</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Dempster's Rule of Combination in Sensor Fusion</div>
  <p>Two medical sensors diagnose a patient for three mutually exclusive conditions $\Theta = \{\text{Flu } (F), \text{Cold } (C), \text{Pneumonia } (P)\}$:</p>
  <ul>
    <li>Sensor 1: $m_1(\{F\}) = 0.6, \ m_1(\Theta) = 0.4$.</li>
    <li>Sensor 2: $m_2(\{F, C\}) = 0.7, \ m_2(\Theta) = 0.3$.</li>
  </ul>
  <p><strong>Dempster Combination Matrix:</strong></p>
  <table class="custom-table">
    <thead><tr><th>$m_1 \backslash m_2$</th><th>$m_2(\{F, C\}) = 0.7$</th><th>$m_2(\Theta) = 0.3$</th></tr></thead>
    <tbody>
      <tr><td><strong>$m_1(\{F\}) = 0.6$</strong></td><td>$\{F\} \cap \{F, C\} = \{F\} \implies 0.42$</td><td>$\{F\} \cap \Theta = \{F\} \implies 0.18$</td></tr>
      <tr><td><strong>$m_1(\Theta) = 0.4$</strong></td><td>$\Theta \cap \{F, C\} = \{F, C\} \implies 0.28$</td><td>$\Theta \cap \Theta = \Theta \implies 0.12$</td></tr>
    </tbody>
  </table>
  <p>No empty set intersections ($K = 0$). Combined masses:</p>
  $$\mathbf{m_{1,2}(\{F\}) = 0.42 + 0.18 = \mathbf{0.60} \qquad m_{1,2}(\{F, C\}) = \mathbf{0.28} \qquad m_{1,2}(\Theta) = \mathbf{0.12}}$$
  $$\mathbf{\text{Belief in Flu: } \text{Bel}(\{F\}) = m_{1,2}(\{F\}) = \mathbf{0.60} \qquad \text{Plausibility of Flu: } \text{Pl}(\{F\}) = 0.60 + 0.28 + 0.12 = \mathbf{1.00}}}$$
</div>

<div class="qa-card">
  <div class="qa-q">Q17. Explain the Resolution Refutation Proof with Equality (Paramodulation and Demodulation). (8 Marks)</div>
  <div class="qa-a">
    Standard resolution handles predicate symbols but cannot natively reason about equality axioms ($x = x, x = y \rightarrow y = x, x = y \land y = z \rightarrow x = z$).<br>
    • <strong>Paramodulation:</strong> A specialized inference rule that incorporates equality: From clause $(l = r \lor C)$ and clause $(P(t) \lor D)$, where a subterm of $t$ unifies with $l$ under $\theta = \text{UNIFY}(t|_p, l)$, infer $(P(t[r\theta]_p) \lor C\theta \lor D\theta)$.<br>
    • <strong>Demodulation:</strong> A deterministic rewriting rule that uses unit equality clauses $l = r$ to simplify terms in other clauses to a canonical normal form, preventing exponential branching in equational theorem provers like Otter and Vampire!
  </div>
</div>

<h2 class="section-title">Topic 22.10: Master University Exam Proof Bank (Part IV)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Proof: First-Order Unification with Multiple Variable Bindings</div>
  <p>Find the Most General Unifier (MGU) $\theta$ for the following predicate expressions or show why unification fails:</p>
  <ol>
    <li>$P(x, g(x), y)$ and $P(f(z), g(f(z)), h(w)) \implies \mathbf{\theta = \{ x / f(z), y / h(w) \}}$.</li>
    <li>$Q(a, x, f(g(y)))$ and $Q(z, f(z), f(u)) \implies z/a, x/f(a), u/g(y) \implies \mathbf{\theta = \{ z/a, x/f(a), u/g(y) \}}$.</li>
    <li>$R(x, x)$ and $R(y, f(y)) \implies \mathbf{\text{Occur-check failure: } y \text{ cannot unify with } f(y)}$!</li>
  </ol>
</div>

<div class="qa-card">
  <div class="qa-q">Q18. Explain Automated Theorem Proving with Binary Decision Diagrams (BDDs) and Reduced Ordered BDDs (ROBDDs). (8 Marks)</div>
  <div class="qa-a">
    A <strong>Binary Decision Diagram (BDD)</strong> is a rooted, directed acyclic graph representing a Boolean function $f(x_1, \dots, x_n)$ where non-terminal nodes represent variables and outgoing dashed/solid edges represent $0$ and $1$ assignments.<br>
    <strong>ROBDD Canonical Property (Bryant 1986):</strong> For a fixed variable ordering, every Boolean function has a <em>strictly unique, canonical</em> ROBDD representation. Checking whether a formula is a tautology ($f \equiv 1$) or unsatisfiable ($f \equiv 0$) takes $O(1)$ time! Equivalence checking between two logic circuits $f \equiv g$ reduces to graph isomorphism!
  </div>
</div>
"""
