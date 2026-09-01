# Artificial Intelligence Module 2 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

AI_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Problem Solving by Search Agents & Game Playing</div>
  <div class="toc-grid">
    <div>1. Problem Formulation 5-Tuple (Initial State, Actions, Result, Goal, Cost)</div>
    <div>2. State Space Graphs vs. Search Trees (Frontier & Explored Sets)</div>
    <div>3. Uninformed Search Strategies (BFS, DFS, Uniform-Cost Search)</div>
    <div>4. Depth-Limited Search (DLS) & Iterative Deepening Search (IDS) Proofs</div>
    <div>5. Heuristic Search: Greedy Best-First Search & $A^*$ Search Algorithm</div>
    <div>6. Admissibility & Consistency (Monotonicity) Formal Mathematical Proofs</div>
    <div>7. Heuristic Dominance, Effective Branching Factor & IDA* / SMA*</div>
    <div>8. Local Search: Hill Climbing, Plateau Escapes & Simulated Annealing ($e^{\Delta E / T}$)</div>
    <div>9. Genetic Algorithms (Selection, Crossover, Mutation Operators)</div>
    <div>10. Adversarial Search & Game Playing: Minimax Algorithm & Ply Traversal</div>
    <div>11. Alpha-Beta Pruning Formulation & Step-by-Step Tree Tracing</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Formulating State Space Search Problems</h2>
<p>
  A search problem is formally specified as a <strong>5-tuple</strong> $\langle S_0, \text{Actions}(s), \text{Result}(s, a), \text{GoalTest}(s), c(s, a, s') \rangle$:
</p>
<ol>
  <li><strong>Initial State ($S_0$):</strong> The world state in which the agent starts (e.g., $\text{In}(\text{Arad})$).</li>
  <li><strong>Actions Set ($\text{Actions}(s)$):</strong> The legal moves executable from state $s$.</li>
  <li><strong>Transition Model ($\text{Result}(s, a)$):</strong> Specifies the successor state $s'$ reached by executing action $a$ in state $s$.</li>
  <li><strong>Goal Test ($\text{GoalTest}(s)$):</strong> A boolean predicate that determines whether state $s$ is a goal state (e.g., $s = \text{In}(\text{Bucharest})$).</li>
  <li><strong>Path Cost Function ($c(s, a, s')$):</strong> Step cost of taking action $a$ from $s$ to reach $s'$. The path cost $g(n)$ is the sum of step costs from $S_0$ to node $n$.</li>
</ol>

<h2 class="section-title">Topic 3 & 4: Uninformed (Blind) Search Algorithms</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Algorithm</th>
      <th style="width: 20%;">Frontier Data Structure</th>
      <th style="width: 15%;">Time Complexity</th>
      <th style="width: 15%;">Space Complexity</th>
      <th style="width: 14%;">Complete?</th>
      <th>Optimal?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Breadth-First (BFS)</strong></td>
      <td>FIFO Queue</td>
      <td>$O(b^d)$</td>
      <td>$O(b^d)$</td>
      <td>Yes (if $b < \infty$)</td>
      <td>Yes (if step costs are equal)</td>
    </tr>
    <tr>
      <td><strong>2. Uniform-Cost (UCS)</strong></td>
      <td>Priority Queue by $g(n)$</td>
      <td>$O(b^{1 + \lfloor C^* / \epsilon \rfloor})$</td>
      <td>$O(b^{1 + \lfloor C^* / \epsilon \rfloor})$</td>
      <td>Yes (if step cost $\ge \epsilon > 0$)</td>
      <td>Yes (for general positive costs)</td>
    </tr>
    <tr>
      <td><strong>3. Depth-First (DFS)</strong></td>
      <td>LIFO Stack</td>
      <td>$O(b^m)$</td>
      <td>$O(b \cdot m)$</td>
      <td>No (fails in infinite paths)</td>
      <td>No</td>
    </tr>
    <tr>
      <td><strong>4. Depth-Limited (DLS)</strong></td>
      <td>LIFO Stack with limit $l$</td>
      <td>$O(b^l)$</td>
      <td>$O(b \cdot l)$</td>
      <td>No (if $l < d$)</td>
      <td>No</td>
    </tr>
    <tr>
      <td><strong>5. Iterative Deepening (IDS)</strong></td>
      <td>Iterative DLS ($l=0, 1, 2, \dots$)</td>
      <td>$O(b^d)$</td>
      <td>$O(b \cdot d)$</td>
      <td>Yes (if $b < \infty$)</td>
      <td>Yes (if unit step costs)</td>
    </tr>
  </tbody>
</table>
<p><em>Where $b$ = branching factor, $d$ = depth of shallowest goal, $m$ = maximum depth of search tree, $C^*$ = cost of optimal solution, $\epsilon$ = minimum positive step cost.</em></p>

<div class="callout callout-info">
  <div class="callout-title">Why Iterative Deepening Search (IDS) is the Preferred Uninformed Search</div>
  IDS combines the <strong>minimal linear memory requirement of DFS ($O(bd)$)</strong> with the <strong>completeness and optimality of BFS</strong>. Although nodes at depth $k$ are re-generated multiple times, the bottom level dominates the sum:
  $$N(\text{IDS}) = (d)b + (d-1)b^2 + \dots + (1)b^d = O(b^d)$$
  For $b=10$ and $d=5$, BFS generates 111,111 nodes while IDS generates 123,456 nodes — an overhead of only $11\%$ for massive memory savings!
</div>

<h2 class="section-title">Topic 5 & 6: Informed Heuristic Search & The $A^*$ Algorithm</h2>

<p>
  $A^*$ search guides exploration using an evaluation function $f(n)$ that estimates the total cost of the cheapest path through node $n$ to the goal:
</p>
$$f(n) = g(n) + h(n)$$
<ul>
  <li>$g(n)$: Exact path cost from initial state $S_0$ to node $n$.</li>
  <li>$h(n)$: Estimated cost of the cheapest path from node $n$ to a goal state (Heuristic).</li>
</ul>

<div class="callout callout-warning">
  <div class="callout-title">Mathematical Conditions for $A^*$ Optimality</div>
  <ol>
    <li>
      <strong>Admissibility (Required for Tree Search):</strong>
      <p>A heuristic $h(n)$ is <strong>admissible</strong> if it never overestimates the true cost to reach the goal:
      $$\forall n, \quad 0 \le h(n) \le h^*(n)$$
      Where $h^*(n)$ is the true optimal cost from $n$ to goal.</p>
    </li>
    <li>
      <strong>Consistency / Monotonicity (Required for Graph Search):</strong>
      <p>A heuristic $h(n)$ is <strong>consistent</strong> if for every node $n$ and every successor $n'$ generated by action $a$:
      $$h(n) \le c(n, a, n') + h(n')$$
      <em>Triangle Inequality Property.</em> Every consistent heuristic is strictly admissible ($Consistency \implies Admissibility$).</p>
    </li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Mathematical Proof: $A^*$ is Optimal with an Admissible Heuristic (Tree Search)</div>
  <p><strong>Theorem:</strong> $A^*$ tree search returns an optimal solution if $h(n)$ is admissible.</p>
  <p><strong>Proof by Contradiction:</strong></p>
  <ol>
    <li>Let $G_2$ be a suboptimal goal state on the frontier, with $g(G_2) > C^*$, where $C^*$ is the cost of optimal goal $G_1$.</li>
    <li>Since $G_2$ is a goal state, $h(G_2) = 0$, so $f(G_2) = g(G_2) + 0 > C^*$.</li>
    <li>Let $n$ be an unexpanded node on the optimal path to $G_1$. Since $h(n)$ is admissible:
      $$f(n) = g(n) + h(n) \le g(n) + h^*(n) = C^*$$
    </li>
    <li>Combining equations:
      $$f(n) \le C^* < f(G_2)$$
    </li>
    <li>Since $A^*$ always selects the frontier node with minimum $f$-value, node $n$ will always be selected before $G_2$. Thus, no suboptimal goal $G_2$ can ever be expanded before an optimal solution is found. $\blacksquare$</li>
  </ol>
</div>

<h2 class="section-title">Topic 8: Local Search & Optimization (Simulated Annealing)</h2>

<p>
  <strong>Simulated Annealing</strong> escapes local optima by combining hill climbing with stochastic exploration inspired by the metallurgical cooling of metals:
</p>
<ul>
  <li>If a neighboring state $s'$ improves the objective ($\Delta E = E(s') - E(s) > 0$), the move is always accepted.</li>
  <li>If $\Delta E \le 0$ (worse move), the move is accepted with Boltzmann probability:
    $$P(\text{Accept}) = e^{\frac{\Delta E}{T}}$$
  </li>
  <li>Where $T$ is the temperature parameter dictated by an annealing schedule $T = \text{Schedule}(t)$. At high $T$, the agent acts like a random walk; as $T \rightarrow 0$, it behaves purely as greedy hill climbing.</li>
</ul>

<h2 class="section-title">Topic 10 & 11: Adversarial Search (Minimax & Alpha-Beta Pruning)</h2>

<div class="formula-card">
  <strong>Minimax Value Formulation:</strong>
  $$\text{Minimax}(s) = \begin{cases} 
    \text{Utility}(s) & \text{if } \text{TerminalTest}(s) \\
    \max_{a \in \text{Actions}(s)} \text{Minimax}(\text{Result}(s, a)) & \text{if } \text{Player}(s) = \text{MAX} \\
    \min_{a \in \text{Actions}(s)} \text{Minimax}(\text{Result}(s, a)) & \text{if } \text{Player}(s) = \text{MIN}
  \end{cases}$$
</div>

<div class="callout callout-info">
  <div class="callout-title">Alpha-Beta ($\alpha$-$\beta$) Pruning Rules</div>
  <ul>
    <li><strong>$\alpha$ (Alpha):</strong> The best value (highest utility) found so far along the path to the current node for <strong>MAX</strong> (initially $-\infty$).</li>
    <li><strong>$\beta$ (Beta):</strong> The best value (lowest utility) found so far along the path to the current node for <strong>MIN</strong> (initially $+\infty$).</li>
    <li><strong>Pruning Condition:</strong> Prune the remaining children of the current node whenever:
      $$\alpha \ge \beta$$
    </li>
    <li><strong>Time Complexity with Perfect Move Ordering:</strong> Reduces search complexity from $O(b^m)$ to $O(b^{m/2})$, effectively doubling the solvable search depth!</li>
  </ul>
</div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module II)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. State the 8-Puzzle problem formulation and compare the Manhattan Distance heuristic $h_1$ with the Misplaced Tiles heuristic $h_2$. (8 Marks)</div>
  <div class="qa-a">
    - <strong>State:</strong> $3 \times 3$ grid containing tiles 1 through 8 and one blank space.<br>
    - <strong>Initial State:</strong> Any arbitrary permutation of the 9 positions.<br>
    - <strong>Actions:</strong> Move blank space Left, Right, Up, Down.<br>
    - <strong>Goal Test:</strong> Tiles arranged in ascending numerical order.<br>
    - <strong>Path Cost:</strong> Each move costs 1 unit ($g(n) = \text{depth}$).<br><br>
    <strong>Comparison of Heuristics:</strong><br>
    1. <em>Misplaced Tiles ($h_1$):</em> Counts number of tiles not in their goal position.<br>
    2. <em>Manhattan Distance ($h_2$):</em> Sum of vertical and horizontal grid distances of each tile from its goal position:
       $$h_2 = \sum_{i=1}^8 (|x_i - x_i^*| + |y_i - y_i^*|)$$
    3. <strong>Dominance:</strong> $\forall n, \ h_2(n) \ge h_1(n)$. Both are admissible, but $h_2$ strictly <strong>dominates</strong> $h_1$, expanding fewer search nodes while guaranteeing optimal solutions.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Trace Alpha-Beta Pruning on a 3-level game tree and explain why pruned nodes do not affect the root decision. (10 Marks)</div>
  <div class="qa-a">
    Alpha-Beta pruning computes the exact same minimax decision as standard Minimax without evaluating branches that cannot alter the final choice.<br>
    When a MIN node evaluates a child with value $v \le \alpha$, MIN will pick a value $\le v \le \alpha$. But MAX (higher in the tree) already has a confirmed choice with value $\alpha$. Hence MAX will never choose the branch leading to this MIN node, making further exploration of its remaining children mathematically pointless.
  </div>
</div>
"""
