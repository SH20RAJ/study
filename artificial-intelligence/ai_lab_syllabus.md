# 🧪 Artificial Intelligence Lab (CS24308)
**Practical Syllabus, Lab Assignments & Python Implementation Manual | BIT Mesra**

> **Course Code:** `CS24308`  
> **Course Title:** Artificial Intelligence Lab  
> **Credits:** **1.5 Credits**  
> **Programming Language:** Python 3.10+ (NumPy, SciPy, Matplotlib, pgmpy)

---

## 📌 Lab Schedule & Practical Assignments

```
+-----------+-----------------------------------------------------------+----------------+
| Module    | Practical Focus Area                                      | Target Weeks   |
+-----------+-----------------------------------------------------------+----------------+
| Lab M1    | Agent Architectures, Reflex & Goal-Based Simulations      | Weeks 1 - 2    |
| Lab M2    | Uninformed Search, A* 8-Puzzle, Minimax with Alpha-Beta   | Weeks 3 - 6    |
| Lab M3    | Knowledge Representation, Truth Tables, Logic Resolution  | Weeks 7 - 9    |
| Lab M4    | STRIPS Planning, Bayesian Network Modeling & Inference    | Weeks 10 - 11  |
| Lab M5    | ID3 Decision Tree & Multi-Layer Perceptron from Scratch   | Weeks 12 - 14  |
+-----------+-----------------------------------------------------------+----------------+
```

---

## 🧪 Detailed Lab Tasks Breakdown

### Lab Module I – Agent Modeling & Simulations
- [ ] **Task 1.1: Vacuum Cleaner Reflex Agent:**
  - Model a 2-room environment (`[Room A, Room B]`) with dirty/clean states.
  - Implement a Table-Driven Agent and Simple Reflex Agent.
  - Track performance metrics (number of clean rooms over $N$ time steps).
- [ ] **Task 1.2: Goal-Based Agent in Grid World:**
  - Create a 2D grid world ($N \times M$) with start position, target goal, and static wall obstacles.
  - Implement goal-checking and path planning to guide the agent to the goal.
- [ ] **Task 1.3: Observable vs. Partially Observable Environments:**
  - Compare agent decision-making when the full grid state is visible vs. when the agent has a limited sensor radius (fog of war).

---

### Lab Module II – Search Algorithms & Game Playing AI
- [ ] **Task 2.1: Graph Search Implementations:**
  - Implement Breadth-First Search (BFS) using `collections.deque`.
  - Implement Depth-First Search (DFS) using recursion / LIFO stack.
  - Implement Uniform-Cost Search (UCS) using `heapq` priority queue.
- [ ] **Task 2.2: $A^*$ Search for the 8-Puzzle Problem:**
  - State representation: $3 \times 3$ matrix of numbers $0-8$ ($0$ = blank).
  - Implement Manhattan Distance heuristic: $h_1(s) = \sum |x_i - x_i^*| + |y_i - y_i^*|$.
  - Implement Misplaced Tiles heuristic: $h_2(s) = \sum [s_i \ne s_i^*]$.
  - Compare nodes expanded and time taken between $h_1$ and $h_2$.
- [ ] **Task 2.3: Tic-Tac-Toe Game AI using Minimax:**
  - Board representation: 9 cells (`'X'`, `'O'`, `' '`).
  - Terminal state evaluator (+10 for AI win, -10 for Human win, 0 for Draw).
  - Recursive Minimax search exploring all legal moves.
- [ ] **Task 2.4: Alpha-Beta Pruning Enhancement:**
  - Enhance Minimax with $\alpha$ and $\beta$ bounding parameters.
  - Instrument counters to measure the reduction in evaluated nodes with Alpha-Beta pruning vs. standard Minimax.

---

### Lab Module III – Logic Inference & Knowledge Representation
- [ ] **Task 3.1: Propositional Logic Truth Table Generator:**
  - Parse propositional logic formulas (with $\land, \lor, \neg, \implies$).
  - Generate full truth tables and test for Tautology, Satisfiability, and Contradiction.
- [ ] **Task 3.2: Forward Chaining for Horn Clauses:**
  - Represent Knowledge Base as a set of definite clauses (e.g., $A \land B \implies C$).
  - Implement linear-time Forward Chaining algorithm answering queries $\text{KB} \vdash Q$.
- [ ] **Task 3.3: Propositional Resolution Refutation Solver:**
  - Convert propositional sentences into Conjunctive Normal Form (CNF).
  - Implement clause resolution and termination checking for empty clause ($\square$).
- [ ] **Task 3.4: First-Order Logic Unifier:**
  - Implement `unify(expr1, expr2)` supporting variable bindings and occur-check.

---

### Lab Module IV – Planning & Bayesian Networks
- [ ] **Task 4.1: STRIPS Planner for Blocks World:**
  - Define predicates: `ON(x, y)`, `ONTABLE(x)`, `CLEAR(x)`, `HOLDING(x)`, `ARMEMPTY`.
  - Actions: `STACK(x, y)`, `UNSTACK(x, y)`, `PICKUP(x)`, `PUTDOWN(x)`.
  - Implement forward state-space progression search to generate valid plan sequences.
- [ ] **Task 4.2: Bayesian Network Modeling with `pgmpy`:**
  - Model the classic Earthquake / Burglary / Alarm diagnostic network.
  - Define Directed Acyclic Graph structure and populate Conditional Probability Tables (CPTs).
  - Perform Exact Inference using Variable Elimination: Query $P(\text{Burglary} \mid \text{Alarm}=\text{True}, \text{JohnCalls}=\text{True})$.

---

### Lab Module V – Machine Learning Classifiers from Scratch
- [ ] **Task 5.1: ID3 Decision Tree Classifier (NumPy):**
  - Implement Entropy calculation: $H(S) = -\sum p_i \log_2(p_i)$.
  - Implement Information Gain computation for all features.
  - Recursively build decision tree and classify test samples.
- [ ] **Task 5.2: Perceptron from Scratch:**
  - Implement single-layer Perceptron learning rule for linear classification (AND, OR gates).
  - Demonstrate failure to converge on XOR gate (linear separability limit).
- [ ] **Task 5.3: Multi-Layer Perceptron (MLP) with Backpropagation:**
  - Implement 2-layer neural network with Sigmoid / ReLU activations.
  - Implement Forward propagation and Backpropagation gradient descent from scratch.
  - Train on non-linear datasets (e.g., XOR, Moon dataset) and plot decision boundaries.
- [ ] **Task 5.4: Overfitting & Underfitting Demonstration:**
  - Train polynomial regression / neural network models with varying capacity.
  - Plot Training Loss vs. Validation Loss curves to demonstrate overfitting regime.

---

## 📊 Lab Progress Tracker

| Module | Tasks Count | Completed | Status |
| :---: | :---: | :---: | :---: |
| **Lab M1** (Agents & Vacuum World) | 4 | 0 | ⬜ Not Started |
| **Lab M2** (BFS, A* 8-Puzzle, Minimax) | 6 | 0 | ⬜ Not Started |
| **Lab M3** (Truth Tables, Resolution, Unify) | 4 | 0 | ⬜ Not Started |
| **Lab M4** (STRIPS Planner, Bayesian Nets) | 5 | 0 | ⬜ Not Started |
| **Lab M5** (ID3 Tree, Perceptron, MLP) | 7 | 0 | ⬜ Not Started |
| **Total Practical Tasks** | **26** | **0** | **0% Complete** |

---
*Maintained for B.Tech CSE 5th Semester — CS24308 Artificial Intelligence Lab.*
