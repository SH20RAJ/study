# NLP Module 4 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

NLP_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Lexical Semantics, Vector Space Models & Distributed Word Embeddings</div>
  <div class="toc-grid">
    <div>1. Lexical Semantics: Word Senses, Synonyms, Antonyms, Hypernyms & Hyponyms</div>
    <div>2. WordNet Ontology Architecture: Synsets, Taxonomic Distance & Similarity Metrics</div>
    <div>3. Distributional Hypothesis: "You shall know a word by the company it keeps"</div>
    <div>4. Term-Document Matrix & Term Frequency-Inverse Document Frequency (TF-IDF)</div>
    <div>5. Term-Context Matrices & Pointwise Mutual Information (PMI / Positive PMI)</div>
    <div>6. Dimensionality Reduction in Semantics: Latent Semantic Analysis (LSA / SVD)</div>
    <div>7. Word2Vec Architecture (Mikolov et al., 2013): Continuous Bag-of-Words (CBOW)</div>
    <div>8. Word2Vec Skip-Gram Model with Negative Sampling (SGNS) Mathematical Objective</div>
    <div>9. Vector Arithmetic & Analogical Reasoning ($\mathbf{v}_{\text{King}} - \mathbf{v}_{\text{Man}} + \mathbf{v}_{\text{Woman}} \approx \mathbf{v}_{\text{Queen}}$)</div>
    <div>10. GloVe (Global Vectors for Word Representation): Log-Bilinear Matrix Factorization</div>
    <div>11. FastText: Subword N-Gram Embeddings for Morphology & Out-of-Vocabulary (OOV)</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 4 & 5: Vector Space Models (TF-IDF & Positive PMI)</h2>

<div class="formula-card">
  <strong>1. Term Frequency-Inverse Document Frequency ($\text{TF-IDF}$):</strong>
  $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$
  $$\text{TF}(t, d) = \frac{f_{t, d}}{\sum_{t' \in d} f_{t', d}}, \quad \text{IDF}(t, D) = \log_{10}\left( \frac{|D|}{|\{d \in D : t \in d\}|} \right)$$
</div>

<div class="formula-card">
  <strong>2. Positive Pointwise Mutual Information ($\text{PPMI}$):</strong>
  $$\text{PMI}(w, c) = \log_2\left( \frac{P(w, c)}{P(w) P(c)} \right) = \log_2\left( \frac{C(w, c) \cdot N}{C(w) \cdot C(c)} \right)$$
  $$\text{PPMI}(w, c) = \max(\text{PMI}(w, c), 0)$$
</div>

<h2 class="section-title">Topic 7 & 8: Word2Vec (Skip-Gram with Negative Sampling - SGNS)</h2>

<p>
  <strong>Word2Vec</strong> learns dense low-dimensional continuous vector embeddings ($d \approx 300$) where semantically similar words are mapped to proximate points in vector space.
</p>

<div class="callout callout-info">
  <div class="callout-title">Skip-Gram with Negative Sampling (SGNS) Loss Function</div>
  For a target word $w$ with true context word $c_{\text{pos}}$ and $k$ randomly drawn negative words $c_{\text{neg}, 1 \dots k}$ from noise distribution $P_n(w) \propto f(w)^{3/4}$:
  $$\mathcal{L}_{\text{SGNS}} = \log \sigma(\mathbf{v}_{c_{\text{pos}}}^T \mathbf{v}_w) + \sum_{i=1}^k \mathbb{E}_{c_{\text{neg}, i} \sim P_n} \Big[ \log \sigma(-\mathbf{v}_{c_{\text{neg}, i}}^T \mathbf{v}_w) \Big]$$
  Where $\sigma(z) = \frac{1}{1 + e^{-z}}$ is the logistic sigmoid function. Maximizes dot product with actual context words while pushing away negative noise samples!
</div>

<h2 class="section-title">Topic 10: GloVe (Global Vectors for Word Representation)</h2>

<div class="formula-card">
  <strong>GloVe Log-Bilinear Objective Function (Pennington, Socher, Manning, 2014):</strong>
  $$J = \sum_{i, j=1}^V f(X_{ij}) \Big( \mathbf{w}_i^T \tilde{\mathbf{w}}_j + b_i + \tilde{b}_j - \log X_{ij} \Big)^2$$
  Where $X_{ij}$ is the co-occurrence count of word $i$ with context word $j$, and $f(X_{ij}) = \min(1, (X_{ij} / x_{\max})^\alpha)$ is a weighting function that caps the influence of extremely frequent stop words (with $\alpha = 0.75, x_{\max} = 100$).
</div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module IV)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Compare CBOW and Skip-Gram models in Word2Vec across 4 architectural parameters. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Prediction Task:</strong> CBOW predicts the target center word given a window of surrounding context words; Skip-Gram predicts the surrounding context words given the center word.<br>
    2. <strong>Training Speed:</strong> CBOW trains several times faster than Skip-Gram because context word vectors are averaged in a single forward pass.<br>
    3. <strong>Performance on Rare Words:</strong> Skip-Gram is substantially superior for rare words and small datasets because each target-context pair is treated as a separate training sample.<br>
    4. <strong>Vector Representations:</strong> CBOW smooths over context distribution; Skip-Gram preserves multi-sense representations.
  </div>
</div>
"""
