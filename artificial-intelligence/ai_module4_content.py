# Artificial Intelligence Module 4 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

AI_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Planning & Probabilistic Reasoning in AI</div>
  <div class="toc-grid">
    <div>1. Classical Planning Formalisms (State, Goal & Action Representations)</div>
    <div>2. The STRIPS Language: Preconditions, Add Lists & Delete Lists</div>
    <div>3. Planning Domain Definition Language (PDDL) Action Schemas</div>
    <div>4. Progression (Forward State Search) vs. Regression (Backward Relevant Search)</div>
    <div>5. Goal Stack Planning & The Sussman Anomaly in Blocks World</div>
    <div>6. Planning Graphs (Graphplan) & 3 Classes of Mutual Exclusion (Mutex) Relations</div>
    <div>7. Reasoning Under Uncertainty: Probability Axioms & Conditional Independence</div>
    <div>8. Bayes' Rule & Full Joint Probability Distribution Formulations</div>
    <div>9. Bayesian Belief Networks (BBN): Directed Acyclic Graphs & CPT Matrices</div>
    <div>10. Direction-Dependent Separation (d-separation): Serial, Diverging & Collider Links</div>
    <div>11. Exact Inference (Variable Elimination) vs. Approximate Monte Carlo Sampling</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Classical Planning & The STRIPS Representation</h2>
<p>
  <strong>Planning</strong> is the process of generating a sequence of actions that transforms an initial state $S_0$ into a desired goal state $G$.
</p>

<div class="callout callout-info">
  <div class="callout-title">The STRIPS (Stanford Research Institute Problem Solver) Language</div>
  <ul>
    <li><strong>State:</strong> A conjunction of positive ground function-free literals (e.g., $\text{On}(A, B) \land \text{OnTable}(B) \land \text{Clear}(A) \land \text{HandEmpty}$). Closed-world assumption applies.</li>
    <li><strong>Goal:</strong> A conjunction of positive literals that must hold true in the final state.</li>
    <li><strong>Action Schema $\text{Action}(a)$:</strong> Formally specified by 3 components:
      <ol>
        <li><strong>$\text{Preconditions}(a)$:</strong> Literals that must be satisfied before action $a$ can be legally executed.</li>
        <li><strong>$\text{Add-List}(a)$:</strong> Literals that become True after executing action $a$.</li>
        <li><strong>$\text{Delete-List}(a)$:</strong> Literals that become False and are removed after executing action $a$.</li>
      </ol>
    </li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ STRIPS Operator Schema: Stacking Block $A$ onto Block $B$</div>
  <pre><code>Action: Stack(x, y)
Preconditions: Clear(y) ^ Holding(x)
Delete-List:   Clear(y), Holding(x)
Add-List:      On(x, y), Clear(x), HandEmpty</code></pre>
</div>

<h2 class="section-title">Topic 5: Goal Stack Planning & The Sussman Anomaly</h2>
<p>
  <strong>Goal Stack Planning</strong> uses a Last-In First-Out (LIFO) stack to hold goals and subgoals. It handles multiple goals sequentially by planning for one subgoal, which may inadvertently undo previously achieved subgoals:
</p>

<div class="callout callout-warning">
  <div class="callout-title">The Sussman Anomaly (Interleaved Non-Linear Goals)</div>
  <p>In the Blocks World, given Initial State: $\text{On}(C, A) \land \text{OnTable}(A) \land \text{OnTable}(B)$ and Goal State: $\text{On}(A, B) \land \text{On}(B, C)$.</p>
  <ul>
    <li>If the planner achieves $\text{On}(A, B)$ first, it puts $A$ on $B$. But to put $B$ on $C$, it must unstack $A$, undoing its first goal!</li>
    <li>If it achieves $\text{On}(B, C)$ first, $C$ has $A$ on top, requiring unstacking.</li>
    <li><em>Resolution:</em> Requires <strong>Partial-Order / Non-Linear Planning</strong> that interleaves sub-plans rather than assuming linear independence of subgoals.</li>
  </ul>
</div>

<h2 class="section-title">Topic 6: Planning Graphs & Mutual Exclusion (Mutex) Relations</h2>
<p>
  A <strong>Planning Graph</strong> is a directed leveled graph consisting of alternating proposition levels ($P_0, P_1, \dots$) and action levels ($A_0, A_1, \dots$). Mutex links between actions indicate that two actions cannot occur simultaneously:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Mutex Class</th>
      <th style="width: 45%;">Condition & Geometric Cause</th>
      <th>Example in Blocks World</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Inconsistent Effects</strong></td>
      <td>One action negates an effect added by the other action.</td>
      <td>`Stack(A, B)` adds `On(A, B)` while `Unstack(A, B)` deletes `On(A, B)`.</td>
    </tr>
    <tr>
      <td><strong>2. Interference</strong></td>
      <td>An effect of one action is the negation of a precondition of the other.</td>
      <td>`Stack(A, B)` deletes `Clear(B)`, which is a precondition of `Stack(C, B)`.</td>
    </tr>
    <tr>
      <td><strong>3. Competing Needs</strong></td>
      <td>A precondition of one action is mutually exclusive with a precondition of the other.</td>
      <td>`Pickup(A)` requires `HandEmpty`, while `Stack(B, C)` requires `Holding(B)`.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 7 & 8: Probabilistic Reasoning & Bayes' Rule</h2>

<div class="formula-card">
  <strong>1. Conditional Probability & Product Rule:</strong>
  $$P(A \mid B) = \frac{P(A \land B)}{P(B)} \implies P(A \land B) = P(A \mid B) P(B) = P(B \mid A) P(A)$$
</div>

<div class="formula-card">
  <strong>2. Bayes' Rule Formula:</strong>
  $$P(Y \mid X) = \frac{P(X \mid Y) P(Y)}{P(X)} = \frac{P(X \mid Y) P(Y)}{\sum_{y} P(X \mid y) P(y)}$$
  Where $P(Y)$ is the <em>Prior Probability</em>, $P(X \mid Y)$ is the <em>Likelihood</em>, and $P(Y \mid X)$ is the <em>Posterior Probability</em>.
</div>

<h2 class="section-title">Topic 9 & 10: Bayesian Belief Networks (BBN) & d-separation</h2>

<p>
  A <strong>Bayesian Network</strong> is a Directed Acyclic Graph (DAG) where nodes represent random variables and directed edges represent direct causal/probabilistic dependencies, annotated with Conditional Probability Tables (CPTs).
</p>

<div class="callout callout-info">
  <div class="callout-title">Full Joint Distribution Factorization Formula</div>
  $$P(X_1, X_2, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))$$
  Reduces the number of parameters needed to represent an $n$-variable boolean domain from $2^n - 1$ to $O(n \cdot 2^k)$, where $k$ is the maximum number of parents per node!
</div>

<h3 class="subsection-title">The 3 Structural Connections of d-separation (Direction-Dependent Separation):</h3>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Connection Topology</th>
      <th style="width: 45%;">Graph Structure & Dependency Status</th>
      <th>Blocking Condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Serial / Causal Chain</strong></td>
      <td>$X \rightarrow Z \rightarrow Y$</td>
      <td>$X$ and $Y$ are conditionally independent given $Z$ ($Z$ is observed / instantiated).</td>
    </tr>
    <tr>
      <td><strong>2. Diverging / Common Cause (Fork)</strong></td>
      <td>$X \leftarrow Z \rightarrow Y$</td>
      <td>$X$ and $Y$ are conditionally independent given $Z$ ($Z$ is observed).</td>
    </tr>
    <tr>
      <td><strong>3. Converging / Collider (V-Structure)</strong></td>
      <td>$X \rightarrow Z \leftarrow Y$</td>
      <td>$X$ and $Y$ are independent when $Z$ is <strong>unobserved</strong>. If $Z$ or any of its descendants is observed, $X$ and $Y$ become <strong>dependent</strong> (Explaining Away effect).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module IV)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Given the classic Burglar Alarm Bayesian Network (Burglary, Earthquake, Alarm, JohnCalls, MaryCalls), compute the joint probability $P(B \land \neg E \land A \land J \land \neg M)$. (8 Marks)</div>
  <div class="qa-a">
    Applying the Bayesian Network factorization chain rule:<br>
    $$P(B \land \neg E \land A \land J \land \neg M) = P(B) \cdot P(\neg E) \cdot P(A \mid B, \neg E) \cdot P(J \mid A) \cdot P(\neg M \mid A)$$
    Substituting standard CPT values ($P(B)=0.001, P(\neg E)=0.998, P(A \mid B, \neg E)=0.94, P(J \mid A)=0.90, P(\neg M \mid A)=0.30$):<br>
    $$= 0.001 \times 0.998 \times 0.94 \times 0.90 \times 0.30 = 0.000253 \ (\approx 0.0253\%)$$
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain the 3 mutex conditions in Graphplan with diagrams. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Inconsistent Effects:</strong> Action 1 adds proposition $p$ while Action 2 deletes $p$. They cannot occur concurrently without contradictory states.<br>
    2. <strong>Interference:</strong> Action 1 deletes proposition $p$ which is required as a precondition by Action 2.<br>
    3. <strong>Competing Needs:</strong> A precondition of Action 1 and a precondition of Action 2 are mutually exclusive at the preceding proposition level.
  </div>
</div>
"""
