# NLP 10-Page Master Revision Exhaustive Content (CS24311)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

NLP_REVISION_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title">⚡ 10-Page Master Quick Revision — Natural Language Processing (CS24311)</div>
  <div class="toc-grid">
    <div>Page 1: Linguistic Levels, Byte-Pair Encoding & Levenshtein Edit Distance</div>
    <div>Page 2: N-gram Language Models, Perplexity & Kneser-Ney Smoothing Formulations</div>
    <div>Page 3: POS Tagging: Penn Treebank Tagset & Hidden Markov Models (HMM)</div>
    <div>Page 4: The Viterbi Dynamic Programming Algorithm & Trellis Tracing Math</div>
    <div>Page 5: Syntactic Parsing: CFG, Chomsky Normal Form (CNF) & CYK Dynamic Algorithm</div>
    <div>Page 6: Dependency Syntax: Shift-Reduce, Arc-Standard & Arc-Eager Parsing</div>
    <div>Page 7: Vector Space Models: TF-IDF, Positive PMI & WordNet Distance Metrics</div>
    <div>Page 8: Word2Vec: Skip-Gram with Negative Sampling (SGNS) Loss & GloVe Matrix Model</div>
    <div>Page 9: The Transformer Architecture: Scaled Dot-Product & Multi-Head Attention</div>
    <div>10: BERT vs. GPT Architectures & Machine Translation Evaluation (BLEU / ROUGE)</div>
  </div>
</div>

<h2 class="section-title">⚡ Master Formula, Algorithm & Loss Function Cheat Sheet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Topic / Model</th>
      <th style="width: 45%;">Core Mathematical Formulation / Rule</th>
      <th>Key Exam Takeaway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Perplexity ($\text{PPL}$)</strong></td>
      <td>$$\text{PPL}(W) = 2^{-\frac{1}{n} \sum_{i=1}^n \log_2 P(w_i \mid w_{i-1})}$$</td>
      <td>Lower is better; represents average branching factor of language model.</td>
    </tr>
    <tr>
      <td><strong>Viterbi Recurrence</strong></td>
      <td>$$v_t(j) = \max_i [v_{t-1}(i) \cdot a_{ij}] \cdot b_j(o_t)$$</td>
      <td>Finds globally optimal hidden state sequence in $O(N^2 T)$ time.</td>
    </tr>
    <tr>
      <td><strong>CYK Parsing Recurrence</strong></td>
      <td>$$P[i, j, A] = \bigvee_{k=i}^{j-1} \bigvee_{A \rightarrow BC} (P[i, k, B] \land P[k+1, j, C])$$</td>
      <td>Requires grammar strictly in Chomsky Normal Form (CNF); runs in $O(n^3 |P|)$.</td>
    </tr>
    <tr>
      <td><strong>Skip-Gram SGNS Loss</strong></td>
      <td>$$\mathcal{L} = \log \sigma(\mathbf{v}'_c \cdot \mathbf{v}_w) + \sum_{i=1}^k \mathbb{E}[\log \sigma(-\mathbf{v}'_{n_i} \cdot \mathbf{v}_w)]$$</td>
      <td>Maximizes true context dot product while pushing away $k$ negative noise samples.</td>
    </tr>
    <tr>
      <td><strong>Scaled Dot-Product Attention</strong></td>
      <td>$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$</td>
      <td>Scaling by $\frac{1}{\sqrt{d_k}}$ prevents vanishing softmax gradients.</td>
    </tr>
    <tr>
      <td><strong>BLEU Brevity Penalty</strong></td>
      <td>$$\text{BP} = \begin{cases} 1 & \text{if } c > r \\ e^{1 - r/c} & \text{if } c \le r \end{cases}$$</td>
      <td>Penalizes artificially short candidate translations that inflate precision.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🔥 Top 10 High-Yield BIT Mesra Exam Questions & Solutions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Given Query $Q$, Key $K$, Value $V$, trace the dimensions of the Transformer Multi-Head Attention operation with $d_{\text{model}} = 512, h = 8$. (8 Marks)</div>
  <div class="qa-a">
    1. Dimension per head: $d_k = d_v = \frac{d_{\text{model}}}{h} = \frac{512}{8} = \mathbf{64}$.<br>
    2. Projections: $Q W_i^Q \in \mathbb{R}^{n \times 64}, K W_i^K \in \mathbb{R}^{m \times 64}, V W_i^V \in \mathbb{R}^{m \times 64}$.<br>
    3. Attention Matrix: $\frac{Q_i K_i^T}{\sqrt{64}} \in \mathbb{R}^{n \times m}$. Softmax normalizes each row into attention weights.<br>
    4. Head Output: $\text{head}_i = \text{softmax}(\dots) V_i \in \mathbb{R}^{n \times 64}$.<br>
    5. Concatenation: $\text{Concat}(\text{head}_1 \dots \text{head}_8) \in \mathbb{R}^{n \times 512}$. Multiplying by $W^O \in \mathbb{R}^{512 \times 512}$ produces final output $\mathbb{R}^{n \times 512}$.
  </div>
</div>
"""
