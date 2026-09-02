# Natural Language Processing Module 2 Exhaustive Content (12 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions & [UPLOADED PYQ]

NLP_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Language Models, POS Tagging & Parsing — Complete 12-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 13:</strong> N-Gram Language Models (Unigram, Bigram & Trigram Probabilities)</div>
    <div><strong>Topic 14:</strong> Smoothing & Perplexity (Laplace Add-1 & Kneser-Ney Backoff)</div>
    <div><strong>Topic 15:</strong> Rule-Based Part-of-Speech Tagging (Morphological Rules)</div>
    <div><strong>Topic 16:</strong> HMM POS Tagging & The Viterbi Algorithm [UPLOADED PYQ]</div>
    <div><strong>Topic 17:</strong> Context-Free Grammars (CFG Formal Definition & Parse Trees)</div>
    <div><strong>Topic 18:</strong> Recursive Descent Parsing (Top-Down Backtracking Search)</div>
    <div><strong>Topic 19:</strong> Probabilistic Parsing (PCFG, CNF & CKY Algorithm) [UPLOADED PYQ]</div>
    <div><strong>Topic 20:</strong> Dependency Parsing (Typed Dependency Trees & Arc-Standard)</div>
    <div><strong>Topic 21:</strong> Precision Metric Formulation in NLP Evaluation</div>
    <div><strong>Topic 22:</strong> Recall Metric Formulation in Information Extraction</div>
    <div><strong>Topic 23:</strong> F1-Score Harmonic Mean Formulation</div>
    <div><strong>Topic 24:</strong> Parsing Evaluation Metrics (UAS & LAS Attachment Scores)</div>
  </div>
</div>

<h2 class="section-title">Topic 13 & 14: N-Gram Models, Laplace Smoothing & Perplexity [UPLOADED PYQ]</h2>

<div class="formula-card">
  <strong>1. Bigram Maximum Likelihood Estimation (MLE):</strong>
  $$P(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})}$$
</div>

<div class="formula-card">
  <strong>2. Laplace (Add-1) Smoothing Formula [UPLOADED PYQ]:</strong>
  $$P_{\text{Laplace}}(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i) + 1}{\text{Count}(w_{i-1}) + |V|}$$
  Where $|V|$ is the total vocabulary size. Guarantees zero-probability events never crash sentence likelihoods!
</div>

<div class="formula-card">
  <strong>3. Model Perplexity Metric ($PP$):</strong>
  $$PP(W) = P(w_1, w_2, \dots, w_N)^{-\frac{1}{N}} = \sqrt[N]{\frac{1}{P(w_1, w_2, \dots, w_N)}}$$
  <em>Interpretation:</em> The average branching factor of the language model (Lower Perplexity $\implies$ Higher Predictive Accuracy).
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ [UPLOADED PYQ] Solved Problem: Bigram Probability with Laplace Smoothing</div>
  <p>Given corpus counts: $\text{Count}(\text{"want", "to"}) = 600$, $\text{Count}(\text{"want"}) = 1200$, Vocabulary $|V| = 5000$.</p>
  <ol>
    <li>MLE Probability: $P_{\text{MLE}}(\text{"to"} \mid \text{"want"}) = \frac{600}{1200} = \mathbf{0.500}$.</li>
    <li>Laplace Smoothed Probability: $P_{\text{Laplace}}(\text{"to"} \mid \text{"want"}) = \frac{600 + 1}{1200 + 5000} = \frac{601}{6200} \approx \mathbf{0.0969}$.</li>
  </ol>
</div>

<h2 class="section-title">Topic 15 & 16: HMM POS Tagging & The Viterbi Algorithm [UPLOADED PYQ]</h2>

<p>
  A <strong>Hidden Markov Model (HMM)</strong> models Part-of-Speech tagging as finding the most probable hidden sequence of POS tags $T = \langle t_1, \dots, t_n \rangle$ given observed words $W = \langle w_1, \dots, w_n \rangle$:
</p>
$$\hat{T} = \arg\max_T P(T \mid W) = \arg\max_T \prod_{i=1}^n P(t_i \mid t_{i-1}) \cdot P(w_i \mid t_i)$$

<div class="callout callout-info">
  <div class="callout-title">The Viterbi Dynamic Programming Algorithm [UPLOADED PYQ]</div>
  $$\mathbf{V_t(j) = \max_{i=1}^N \Big[ V_{t-1}(i) \cdot a_{ij} \Big] \cdot b_j(o_t)}$$
  $$\mathbf{\text{Backpointer: } B_t(j) = \arg\max_{i=1}^N \Big[ V_{t-1}(i) \cdot a_{ij} \Big]}$$
  Where $a_{ij} = P(t_j \mid t_i)$ is Tag Transition probability, and $b_j(o_t) = P(w_t \mid t_j)$ is Word Emission probability.
</div>

<h2 class="section-title">Topic 17 – 20: Syntactic Parsing (CFG, PCFG, CKY & Dependency Parsing) [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Parsing Paradigm</th>
      <th style="width: 45%;">Grammar & Structural Formulation</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Context-Free Grammar (CFG)</strong></td>
      <td>$G = (V, \Sigma, R, S)$ where productions have form $A \rightarrow \alpha$ ($A \in V$). Recursive descent expands rules top-down.</td>
      <td>Precise; vulnerable to left-recursion infinite loops and combinatorial ambiguity explosions.</td>
    </tr>
    <tr>
      <td><strong>2. Probabilistic CFG (PCFG) [UPLOADED PYQ]</strong></td>
      <td>Assigns probability to each rule: $P(A \rightarrow \alpha)$, where $\sum_\alpha P(A \rightarrow \alpha) = 1$. Parse probability is product of rule probabilities.</td>
      <td>Ranks multiple ambiguous parse trees and selects the mathematically most probable syntactic structure!</td>
    </tr>
    <tr>
      <td><strong>3. CKY Dynamic Programming [UPLOADED PYQ]</strong></td>
      <td>Requires grammar in <strong>Chomsky Normal Form (CNF)</strong>: $A \rightarrow B C$ or $A \rightarrow a$. Fills triangular table $O(n^3 \cdot |R|)$.</td>
      <td>Guaranteed polynomial $O(n^3)$ parsing time for all ambiguous sentences!</td>
    </tr>
    <tr>
      <td><strong>4. Dependency Parsing</strong></td>
      <td>Connects words directly with labeled binary grammatical dependency links (e.g., $\text{nsubj}$, $\text{dobj}$, $\text{amod}$).</td>
      <td>Directly captures predicate-argument relationships; excellent for free-word-order languages.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 21 – 24: Parsing & Classification Evaluation Metrics</h2>

<div class="formula-card">
  <strong>1. Classification / Parsing Core Metrics:</strong>
  $$\text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall} = \frac{TP}{TP + FN}, \quad F_1\text{-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
  - <strong>Unlabeled Attachment Score (UAS):</strong> Percentage of words assigned the correct syntactic head governor.
  - <strong>Labeled Attachment Score (LAS):</strong> Percentage of words assigned both the correct head governor AND the correct dependency relation label.
</div>

<h2 class="section-title">🧠 M2 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Explain the working of HMM-based POS Tagging. Define Transition and Emission Probabilities. (10 Marks)</div>
  <div class="qa-a">
    HMM treats POS tags as hidden Markov states generating observable surface words:<br>
    1. <strong>Transition Probability $P(t_i \mid t_{i-1})$:</strong> The probability of transitioning from tag $t_{i-1}$ to tag $t_i$: $P(t_i \mid t_{i-1}) = \frac{C(t_{i-1}, t_i)}{C(t_{i-1})}$.<br>
    2. <strong>Emission Probability $P(w_i \mid t_i)$:</strong> The probability that hidden tag $t_i$ emits the observable word $w_i$: $P(w_i \mid t_i) = \frac{C(t_i, w_i)}{C(t_i)}$.<br>
    3. <strong>Viterbi Algorithm:</strong> Computes the global optimal sequence of tags in $O(T \cdot N^2)$ time using dynamic programming lattice trellis!
  </div>
</div>
"""
