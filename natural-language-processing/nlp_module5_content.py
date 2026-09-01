# NLP Module 5 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

NLP_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Transformers, Large Language Models & Generation Evaluation</div>
  <div class="toc-grid">
    <div>1. Limitations of Recurrent Architectures (RNN, LSTM, GRU) & Sequential Bottleneck</div>
    <div>2. The Transformer Architecture (Vaswani et al., 2017: "Attention Is All You Need")</div>
    <div>3. Scaled Dot-Product Self-Attention Mechanism & Softmax Normalization ($\sqrt{d_k}$)</div>
    <div>4. Multi-Head Attention Formulations ($\text{Concat}(\text{head}_1 \dots \text{head}_h)W^O$)</div>
    <div>5. Positional Encoding Schemes: Fixed Sinusoidal Waves vs. Rotary Embeddings (RoPE)</div>
    <div>6. Transformer Encoder Blocks (LayerNorm, Residual Additions & Multi-Layer Feedforward)</div>
    <div>7. Transformer Decoder Blocks (Masked Causal Self-Attention & Cross-Attention)</div>
    <div>8. BERT Architecture: Bidirectional Transformer Encoders (Masked LM & NSP Tasks)</div>
    <div>9. GPT Family: Autoregressive Decoder Models, In-Context Learning & Prompting</div>
    <div>10. Text Generation Decoding: Greedy, Beam Search, Top-$k$ & Top-$p$ (Nucleus) Sampling</div>
    <div>11. NLP Evaluation Metrics: BLEU Score (with Brevity Penalty) & ROUGE-1/2/L Math</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 2 – 4: The Transformer & Scaled Dot-Product Attention</h2>

<div class="formula-card">
  <strong>1. Scaled Dot-Product Attention:</strong>
  $$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V$$
  Where $Q \in \mathbb{R}^{n \times d_k}$ is the Query matrix, $K \in \mathbb{R}^{m \times d_k}$ is the Key matrix, and $V \in \mathbb{R}^{m \times d_v}$ is the Value matrix.<br>
  <em>Why Scale by $\frac{1}{\sqrt{d_k}}$?</em> For large values of $d_k$, dot products grow large in magnitude, pushing the softmax function into regions with extremely small gradients. Dividing by $\sqrt{d_k}$ stabilizes gradient backpropagation!
</div>

<div class="formula-card">
  <strong>2. Multi-Head Attention:</strong>
  $$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \text{head}_2, \dots, \text{head}_h) W^O$$
  $$\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$
  Where projection parameter matrices $W_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}, W_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}, W_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}$, and $W^O \in \mathbb{R}^{h d_v \times d_{\text{model}}}$.
</div>

<h2 class="section-title">Topic 8 & 9: BERT vs. GPT Architectural Comparison</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">BERT (Devlin et al., 2018)</th>
      <th>GPT (Radford et al., OpenAI)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Core Architecture</strong></td>
      <td>Transformer <strong>Encoder-Only</strong> (Bidirectional attention).</td>
      <td>Transformer <strong>Decoder-Only</strong> (Causal left-to-right masked attention).</td>
    </tr>
    <tr>
      <td><strong>Pre-Training Objectives</strong></td>
      <td>1. <strong>Masked Language Model (MLM):</strong> Predict 15% masked tokens.<br>2. <strong>Next Sentence Prediction (NSP):</strong> Binary classification.</td>
      <td><strong>Autoregressive Language Modeling:</strong> Predict next token $P(w_t \mid w_{<t})$ given past context.</td>
    </tr>
    <tr>
      <td><strong>Context Flow</strong></td>
      <td>Full bidirectional visibility across future and past tokens.</td>
      <td>Strictly unidirectional past context (future tokens masked out).</td>
    </tr>
    <tr>
      <td><strong>Primary Strength</strong></td>
      <td>NLU (Classification, Named Entity Recognition, Extractive QA).</td>
      <td>NLG (Text Generation, Summarization, Code Synthesis, Chatbots).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 11: Text Generation Evaluation Metrics (BLEU & ROUGE)</h2>

<div class="formula-card">
  <strong>1. Bilingual Evaluation Understudy ($\text{BLEU}$) Metric:</strong>
  $$\text{BLEU} = \text{BP} \times \exp\left( \sum_{n=1}^N w_n \log p_n \right)$$
  Where $p_n$ is the modified $n$-gram precision, and $\text{BP}$ is the <strong>Brevity Penalty</strong> to penalize artificially short candidate outputs:
  $$\text{BP} = \begin{cases} 1 & \text{if } c > r \\ e^{1 - r/c} & \text{if } c \le r \end{cases}$$
  Where $c$ is candidate length and $r$ is reference length.
</div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module V)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain why Self-Attention overcomes the fundamental sequential bottleneck of RNNs and LSTMs. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Massive Parallelization:</strong> RNNs compute hidden state $h_t = f(h_{t-1}, x_t)$ sequentially, requiring $O(n)$ sequential time steps that cannot be parallelized across GPU cores. Self-Attention computes all pairwise token interactions simultaneously via matrix multiplications ($QK^T$) in $O(1)$ sequential operations.<br>
    2. <strong>Direct Long-Range Paths:</strong> In RNNs, information must travel step-by-step through $n$ recurrent transitions, causing vanishing gradients for distant words. Self-Attention connects any two positions in the sequence with a direct $O(1)$ path length, enabling instantaneous long-range context resolution.
  </div>
</div>
"""
