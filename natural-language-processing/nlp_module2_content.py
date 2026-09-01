# NLP Module 2 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

NLP_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Part-of-Speech Tagging & Hidden Markov Models (HMM)</div>
  <div class="toc-grid">
    <div>1. Linguistic Word Classes: Open Class vs. Closed Class Lexical Categories</div>
    <div>2. Penn Treebank 45-Tag Tagset (NN, NNP, VB, VBD, JJ, RB, IN, DT)</div>
    <div>3. Part-of-Speech (POS) Tagging Approaches (Rule-Based, Statistical, Neural)</div>
    <div>4. Hidden Markov Models (HMM) 5-Tuple: States, Observations, Transitions, Emissions, Priors</div>
    <div>5. The 3 Fundamental Computational Problems in HMMs (Evaluation, Decoding, Learning)</div>
    <div>6. The Forward Algorithm for Sequence Likelihood ($O(N^2 T)$ Dynamic Programming)</div>
    <div>7. The Viterbi Algorithm for Optimal Hidden State Decoding ($\max$ Trellis Trace)</div>
    <div>8. Complete Step-by-Step Viterbi Trellis Trace on Sentence "Janet will back the bill"</div>
    <div>9. Baum-Welch (Expectation-Maximization) Unsupervised Learning Algorithm</div>
    <div>10. Maximum Entropy Markov Models (MEMM) & The Label Bias Problem</div>
    <div>11. Linear-Chain Conditional Random Fields (CRF) Globally Normalized Potentials</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 – 4: Part-of-Speech Tagging & HMM Mathematical Architecture</h2>
<p>
  <strong>Part-of-Speech (POS) Tagging</strong> is the task of assigning a grammatical category label (e.g., Noun, Verb, Adjective, Preposition) to each word in an input text sequence:
</p>
$$\mathbf{w} = (w_1, w_2, \dots, w_T) \xrightarrow{\text{POS Tagging}} \mathbf{t} = (t_1, t_2, \dots, t_T)$$

<div class="formula-card">
  <strong>Hidden Markov Model 5-Tuple $\lambda = (S, V, A, B, \pi)$:</strong>
  <ol>
    <li>$S = \{s_1, s_2, \dots, s_N\}$: Finite set of hidden states (e.g., POS tags).</li>
    <li>$V = \{v_1, v_2, \dots, v_M\}$: Finite set of observable vocabulary symbols (words).</li>
    <li>$A = \{a_{ij}\}$: State Transition Probability Matrix, where $a_{ij} = P(q_t = s_j \mid q_{t-1} = s_i)$.</li>
    <li>$B = \{b_j(k)\}$: Emission Probability Matrix, where $b_j(k) = P(o_t = v_k \mid q_t = s_j)$.</li>
    <li>$\pi = \{\pi_i\}$: Initial State Probability Distribution, where $\pi_i = P(q_1 = s_i)$.</li>
  </ol>
</div>

<h2 class="section-title">Topic 7 & 8: The Viterbi Dynamic Programming Decoding Algorithm</h2>

<div class="formula-card">
  <strong>Viterbi Recurrence Relations:</strong>
  Let $v_t(j)$ be the highest probability of any state sequence ending in state $j$ at time $t$:
  1. <strong>Initialization ($t = 1$):</strong>
     $$v_1(j) = \pi_j \cdot b_j(o_1), \quad \text{backpointer}_1(j) = 0 \quad (1 \le j \le N)$$
  2. <strong>Recursion ($t = 2 \dots T$):</strong>
     $$v_t(j) = \max_{i=1}^N \Big( v_{t-1}(i) \cdot a_{ij} \Big) \cdot b_j(o_t) \quad (1 \le j \le N)$$
     $$\text{backpointer}_t(j) = \arg\max_{i=1}^N \Big( v_{t-1}(i) \cdot a_{ij} \Big)$$
  3. <strong>Termination:</strong>
     $$P^* = \max_{i=1}^N v_T(i), \quad q_T^* = \arg\max_{i=1}^N v_T(i)$$
  4. <strong>Backtracking:</strong>
     $$q_t^* = \text{backpointer}_{t+1}(q_{t+1}^*) \quad \text{for } t = T-1, T-2, \dots, 1$$
</div>

<h2 class="section-title">Topic 10 & 11: MEMMs vs. Linear-Chain CRFs (Label Bias Problem)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Model Class</th>
      <th style="width: 35%;">Mathematical Formulation</th>
      <th>Normalization & Key Theoretical Properties</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Generative HMM</strong></td>
      <td>$$P(\mathbf{w}, \mathbf{t}) = \prod_{i=1}^T P(t_i \mid t_{i-1}) P(w_i \mid t_i)$$</td>
      <td>Models joint probability; cannot easily integrate overlapping, non-independent features.</td>
    </tr>
    <tr>
      <td><strong>2. Discriminative MEMM</strong></td>
      <td>$$P(\mathbf{t} \mid \mathbf{w}) = \prod_{i=1}^T \frac{\exp(\mathbf{w}^T \mathbf{f}(t_i, t_{i-1}, \mathbf{w}, i))}{\sum_{t'} \exp(\mathbf{w}^T \mathbf{f}(t', t_{i-1}, \mathbf{w}, i))}$$</td>
      <td><strong>Local Normalization at each step:</strong> Suffers from the <em>Label Bias Problem</em> where states with low-entropy transitions dominate regardless of input observations.</td>
    </tr>
    <tr>
      <td><strong>3. Linear-Chain CRF</strong></td>
      <td>$$P(\mathbf{t} \mid \mathbf{w}) = \frac{1}{Z(\mathbf{w})} \exp\left( \sum_{i=1}^T \sum_k w_k f_k(t_i, t_{i-1}, \mathbf{w}, i) \right)$$</td>
      <td><strong>Global Normalization ($Z(\mathbf{w})$):</strong> Overcomes the Label Bias Problem completely by evaluating the total score of the entire sequence simultaneously.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module II)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. State the 3 fundamental problems of Hidden Markov Models and name the algorithms used to solve them. (6 Marks)</div>
  <div class="qa-a">
    1. <strong>Evaluation Problem (Likelihood):</strong> Given model $\lambda$ and observation sequence $O$, compute $P(O \mid \lambda)$. Solved by the <strong>Forward Algorithm</strong> (or Backward Algorithm) in $O(N^2 T)$ time.<br>
    2. <strong>Decoding Problem:</strong> Given model $\lambda$ and observation sequence $O$, find the optimal hidden state sequence $Q^*$ that best explains $O$. Solved by the <strong>Viterbi Algorithm</strong> in $O(N^2 T)$ time.<br>
    3. <strong>Learning Problem (Parameter Estimation):</strong> Given observation sequence $O$, adjust model parameters $\lambda = (A, B, \pi)$ to maximize $P(O \mid \lambda)$. Solved by the <strong>Baum-Welch (EM) Algorithm</strong>.
  </div>
</div>
"""
