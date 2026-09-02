# Natural Language Processing Module 4 Exhaustive Content (8 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions & [UPLOADED PYQ]

NLP_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Deep Learning & Neural Architectures in NLP — Complete 8-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 36:</strong> Convolutional Neural Networks (CNNs) for Text Classification</div>
    <div><strong>Topic 37:</strong> Recurrent Neural Networks (RNNs) & Vanishing Gradients</div>
    <div><strong>Topic 38:</strong> Long Short-Term Memory (LSTM Gate Formulations & Memory Cells)</div>
    <div><strong>Topic 39:</strong> The Transformer Architecture (Scaled Dot-Product Self-Attention)</div>
    <div><strong>Topic 40:</strong> Sequence-to-Sequence Encoder-Decoder with Cross-Attention</div>
    <div><strong>Topic 41:</strong> Transfer Learning in NLP (Pre-Training + Task Fine-Tuning)</div>
    <div><strong>Topic 42:</strong> BERT (Bidirectional Encoder Representations from Transformers)</div>
    <div><strong>Topic 43:</strong> GPT (Generative Pre-Trained Causal Autoregressive Decoders)</div>
  </div>
</div>

<h2 class="section-title">Topic 36 – 38: Sequential Neural Models (CNN, RNN, LSTM)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Neural Model</th>
      <th style="width: 45%;">Mathematical Formulation & Architecture</th>
      <th>Key Advantage & Failure Mode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. CNN for NLP</strong></td>
      <td>1D convolution filters slide across embedding matrices capturing local $n$-gram phrase features: $c_i = f(\mathbf{w}^T \mathbf{x}_{i:i+h-1} + b) \rightarrow$ Max-Pooling over time.</td>
      <td>Highly parallelizable; fails to model long-range sequential syntax dependencies.</td>
    </tr>
    <tr>
      <td><strong>2. Vanilla RNN</strong></td>
      <td>Recurrent hidden state: $\mathbf{h}_t = \tanh(\mathbf{W}_{hh} \mathbf{h}_{t-1} + \mathbf{W}_{xh} \mathbf{x}_t + \mathbf{b}_h)$. Unrolls across variable sentence lengths.</td>
      <td>Models sequential history; severely suffers from <strong>Vanishing and Exploding Gradients</strong> over $>10$ tokens.</td>
    </tr>
    <tr>
      <td><strong>3. LSTM (Hochreiter, 1997)</strong></td>
      <td>Regulates information flow using <strong>3 Gates + Constant Error Carousel Cell State $C_t$</strong>: Forget Gate $f_t$, Input Gate $i_t$, Output Gate $o_t$.</td>
      <td>Maintains long-range gradient highway over hundreds of tokens; sequential processing inhibits GPU scaling.</td>
    </tr>
  </tbody>
</table>

<div class="formula-card">
  <strong>Complete LSTM Mathematical Gate Formulations:</strong>
  $$\text{Forget Gate: } \mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f)$$
  $$\text{Input Gate: } \mathbf{i}_t = \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i), \quad \tilde{\mathbf{C}}_t = \tanh(\mathbf{W}_c [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_c)$$
  $$\text{Cell State Update: } \mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$$
  $$\text{Output Gate: } \mathbf{o}_t = \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o), \quad \mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{C}_t)$$
</div>

<h2 class="section-title">Topic 39 & 40: The Transformer Architecture (Vaswani et al., 2017)</h2>

<div class="formula-card">
  <strong>1. Scaled Dot-Product Attention Equation:</strong>
  $$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q} \mathbf{K}^T}{\sqrt{d_k}} \right) \mathbf{V}$$
  Where $\mathbf{Q}$ (Query), $\mathbf{K}$ (Key), and $\mathbf{V}$ (Value) are linear projections of input embeddings. Division by $\sqrt{d_k}$ prevents gradient saturation in large dimensions!
</div>

<div class="formula-card">
  <strong>2. Multi-Head Attention (MHA):</strong>
  $$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) \mathbf{W}^O, \quad \text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V)$$
</div>

<h2 class="section-title">Topic 41 – 43: Pre-Trained Transformers: BERT vs. GPT</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">BERT (Devlin et al., Google)</th>
      <th>GPT Series (Radford et al., OpenAI)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Core Architecture</strong></td><td>Transformer <strong>Encoder Only</strong> (Bidirectional self-attention).</td><td>Transformer <strong>Decoder Only</strong> (Autoregressive causal masked attention).</td></tr>
    <tr><td><strong>Pretraining Objective</strong></td><td>1. Masked LM (MLM: predicts 15% `[MASK]` tokens).<br>2. Next Sentence Prediction (NSP).</td><td>Standard Left-to-Right Causal Language Modeling: $\max \sum \log P(w_t \mid w_{<t})$.</td></tr>
    <tr><td><strong>Optimal Tasks</strong></td><td>NLU, Text Classification, Named Entity Recognition, Question Answering.</td><td>NLG, Creative Writing, Chatbots, Open-Domain Reasoning, Code Generation.</td></tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M4 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the working of the Scaled Dot-Product Self-Attention mechanism in Transformers with a diagram. (10 Marks)</div>
  <div class="qa-a">
    Self-attention calculates pairwise relational affinities between every pair of tokens in parallel:<br>
    1. <strong>Linear Projections:</strong> Input matrix $\mathbf{X}$ is multiplied by weight matrices $\mathbf{W}^Q, \mathbf{W}^K, \mathbf{W}^V$ to generate $\mathbf{Q}, \mathbf{K}, \mathbf{V}$.<br>
    2. <strong>Score Calculation:</strong> Computes dot-product similarity matrix $\mathbf{S} = \mathbf{Q}\mathbf{K}^T$, reflecting how much each token attends to all other tokens.<br>
    3. <strong>Scaling & Normalization:</strong> Divides by $\sqrt{d_k}$ to stabilize gradients and applies row-wise $\text{softmax}(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}})$.<br>
    4. <strong>Weighted Aggregation:</strong> Multiplies attention weights by value matrix $\mathbf{V}$ to output contextualized embeddings!
  </div>
</div>
"""
