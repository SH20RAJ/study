# Artificial Intelligence Module 2 Exhaustive Content (6 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

AI_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Problem Solving by Search Agents — Complete 6-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 8:</strong> Search-Based Problem Solving (5-Tuple Formal Problem Formulation)</div>
    <div><strong>Topic 9 & 10:</strong> State-Space Search (BFS, DFS, UCS, DLS, IDDFS & Graph Search)</div>
    <div><strong>Topic 11:</strong> Heuristic Search (Greedy Best-First, A* Search & Admissibility)</div>
    <div><strong>Topic 12:</strong> Local Search (Hill Climbing, Simulated Annealing & Genetic Algo)</div>
    <div><strong>Topic 13:</strong> Search in Complex Environments (Belief States & Contingencies)</div>
    <div><strong>Topic 14:</strong> Adversarial Game-Tree Search (Minimax Algorithm & Alpha-Beta Pruning)</div>
  </div>
</div>

<h2 class="section-title">Topic 8: Search Problem Formulation (The 5-Tuple)</h2>

<div class="callout callout-info">
  <div class="callout-title">Formal Problem Formulation 5-Tuple: $\langle S_0, A(s), \text{Result}(s, a), \text{GoalTest}(s), c(s, a, s') \rangle$</div>
  <ol>
    <li><strong>Initial State ($S_0$):</strong> The starting state the agent begins in (e.g., $\text{In}(\text{Arad})$).</li>
    <li><strong>Actions ($A(s)$):</strong> Set of legal executable actions available in state $s$.</li>
    <li><strong>Transition Model ($\text{Result}(s, a)$):</strong> Returns the successor state after taking action $a$ in state $s$.</li>
    <li><strong>Goal Test ($\text{GoalTest}(s)$):</strong> Boolean function determining if state $s$ is a target goal.</li>
    <li><strong>Path Cost Function ($c(s, a, s')$):</strong> Step cost $g(n)$ of taking action $a$ to reach $s'$. Total path cost $= \sum c$.</li>
  </ol>
</div>

<h2 class="section-title">Topic 9 & 10: Uninformed (Blind) Search Strategies</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Algorithm</th>
      <th style="width: 18%;">Frontier Data Structure</th>
      <th style="width: 18%;">Time Complexity</th>
      <th style="width: 18%;">Space Complexity</th>
      <th style="width: 14%;">Complete?</th>
      <th>Optimal?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. BFS</strong></td><td>FIFO Queue</td><td>$O(b^{d+1})$</td><td>$O(b^{d+1})$ (High)</td><td>Yes</td><td>Yes (if equal step costs)</td></tr>
    <tr><td><strong>2. DFS</strong></td><td>LIFO Stack / Recursion</td><td>$O(b^m)$</td><td>$O(b \cdot m)$ (Low)</td><td>No (in infinite trees)</td><td>No</td></tr>
    <tr><td><strong>3. UCS</strong></td><td>Priority Queue by $g(n)$</td><td>$O(b^{1 + \lfloor C^* / \epsilon \rfloor})$</td><td>$O(b^{1 + \lfloor C^* / \epsilon \rfloor})$</td><td>Yes</td><td>Yes (for step costs $\ge \epsilon > 0$)</td></tr>
    <tr><td><strong>4. IDDFS</strong></td><td>Iterative LIFO Stack</td><td>$O(b^d)$</td><td>$O(b \cdot d)$ (Low)</td><td>Yes</td><td>Yes (if equal step costs)</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 11: Informed Heuristic Search & The A* Algorithm</h2>

<div class="formula-card">
  <strong>1. Evaluation Functions:</strong>
  - <strong>Greedy Best-First Search:</strong> $f(n) = h(n)$ (Fast, but non-optimal; can get trapped in loops).
  - <strong>A* Search:</strong> $f(n) = g(n) + h(n)$ where $g(n)$ is the exact cost from start to $n$, and $h(n)$ is estimated cost to goal.
</div>

<div class="formula-card">
  <strong>2. Admissibility and Consistency Conditions for A* Optimality:</strong>
  - <strong>Admissible Heuristic:</strong> $h(n) \le h^*(n)$ for all $n$ (never overestimates the true remaining cost). Guarantees A* is optimal in Tree Search!
  - <strong>Consistent (Monotonic) Heuristic:</strong> $h(n) \le c(n, a, n') + h(n')$ (satisfies the triangle inequality). Guarantees A* is optimal in Graph Search with zero node re-expansions!
</div>

<h2 class="section-title">Topic 12: Local Search & Optimization Algorithms</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Local Search Algorithm</th>
      <th style="width: 45%;">Operating Strategy & State Space Navigation</th>
      <th>Key Pitfall & Solution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Hill Climbing</strong></td>
      <td>Greedy local search that continuously moves in the direction of increasing elevation (value).</td>
      <td>Gets trapped on <strong>Local Maxima, Plateaus, and Ridges</strong>. Solution: Random-restart hill climbing.</td>
    </tr>
    <tr>
      <td><strong>2. Simulated Annealing</strong></td>
      <td>Escapes local maxima by allowing downhill moves with probability $P = e^{\frac{\Delta E}{T}}$. Temperature $T$ decreases according to a cooling schedule.</td>
      <td>Guaranteed asymptotic convergence to global optimum as $T \rightarrow 0$ if cooled sufficiently slowly.</td>
    </tr>
    <tr>
      <td><strong>3. Genetic Algorithms</strong></td>
      <td>Population-based search simulating natural selection: <strong>Selection</strong> (fitness proportionate) $\rightarrow$ <strong>Crossover</strong> $\rightarrow$ <strong>Mutation</strong>.</td>
      <td>Excellent for massive, complex, multi-modal search landscapes (e.g., TSP, circuit design).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 14: Adversarial Game-Tree Search (Minimax & Alpha-Beta Pruning)</h2>

<div class="formula-card">
  <strong>1. Minimax Value Recursive Definition:</strong>
  $$\text{Minimax}(s) = \begin{cases} \text{Utility}(s) & \text{if } \text{Terminal}(s) \\ \max_{a \in A(s)} \text{Minimax}(\text{Result}(s, a)) & \text{if } \text{Player}(s) = \text{MAX} \\ \min_{a \in A(s)} \text{Minimax}(\text{Result}(s, a)) & \text{if } \text{Player}(s) = \text{MIN} \end{cases}$$
</div>

<div class="callout callout-warning">
  <div class="callout-title">Alpha-Beta ($\alpha$-$\beta$) Pruning Invariant Rule</div>
  Maintain two bounds during recursive DFS traversal:
  <ul>
    <li>$\alpha = $ the highest value choice found so far along the path for $\text{MAX}$ (initialized to $-\infty$).</li>
    <li>$\beta = $ the lowest value choice found so far along the path for $\text{MIN}$ (initialized to $+\infty$).</li>
  </ul>
  <strong>Pruning Condition:</strong> Whenever $\mathbf{\alpha \ge \beta}$, prune the remaining subtree below the current node immediately! (Reduces effective branching factor from $b$ to $\sqrt{b}$, doubling search depth!).
</div>

<h2 class="section-title">🧠 M2 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Prove that A* Search is optimal when using an Admissible Heuristic in Tree Search. (8 Marks)</div>
  <div class="qa-a">
    Let $G_2$ be a suboptimal goal with cost $g(G_2) > C^*$, and $G$ be an optimal goal with $g(G) = C^*$.<br>
    Suppose $G_2$ is in the frontier and is about to be selected. For any unexpanded node $n$ on the optimal path to $G$:<br>
    1. Since $h$ is admissible: $f(n) = g(n) + h(n) \le C^*$.<br>
    2. For the suboptimal goal: $f(G_2) = g(G_2) + h(G_2) = g(G_2) > C^*$.<br>
    3. Therefore, $f(n) \le C^* < f(G_2) \implies f(n) < f(G_2)$.<br>
    Hence, A* will always expand node $n$ on the optimal path before ever selecting $G_2$, guaranteeing that $G_2$ can never be chosen before an optimal path is found!
  </div>
</div>
"""
