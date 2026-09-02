# Natural Language Processing Module 3 Exhaustive Content (11 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions & [UPLOADED PYQ]

NLP_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Semantics & Lexical Vector Resources — Complete 11-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 25:</strong> Lexical Semantics (Synonymy, Antonymy, Hyponymy, Meronymy)</div>
    <div><strong>Topic 26:</strong> Word Sense Disambiguation (Simplified Lesk & Supervised WSD)</div>
    <div><strong>Topic 27 & 28:</strong> WordNet Lexical Database (Synsets & Hypernym Hierarchies)</div>
    <div><strong>Topic 29:</strong> Semantic Similarity (Shortest Path Length in WordNet)</div>
    <div><strong>Topic 30:</strong> Cosine Similarity Formulation in Vector Spaces</div>
    <div><strong>Topic 31:</strong> Vector Space Models (Term-Document & Term-Term Matrices)</div>
    <div><strong>Topic 32:</strong> TF-IDF Weighting Formulation & Numerical Analysis [UPLOADED PYQ]</div>
    <div><strong>Topic 33:</strong> Word2Vec Embeddings (CBOW vs. Skip-Gram Architectures) [UPLOADED PYQ]</div>
    <div><strong>Topic 34:</strong> GloVe (Global Vectors from Word-Word Co-Occurrence Counts)</div>
    <div><strong>Topic 35:</strong> FastText (Subword Character N-Gram Vector Representations)</div>
  </div>
</div>

<h2 class="section-title">Topic 25 – 29: Lexical Semantics, WordNet & WSD Algorithms</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Lexical Relation</th>
      <th style="width: 45%;">Formal Definition</th>
      <th>Representative Example</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Synonymy</strong></td><td>Different words expressing the identical or near-identical concept ($A \approx B$).</td><td>`"large"` $\leftrightarrow$ `"big"`, `"automobile"` $\leftrightarrow$ `"car"`.</td></tr>
    <tr><td><strong>2. Antonymy</strong></td><td>Words expressing opposite semantic meanings along a spectrum ($A \leftrightarrow -A$).</td><td>`"hot"` $\leftrightarrow$ `"cold"`, `"increase"` $\leftrightarrow$ `"decrease"`.</td></tr>
    <tr><td><strong>3. Hyponymy / Hypernymy</strong></td><td>$\text{IS-A}$ class-subclass hierarchical relationship ($A$ is a subtype of $B$).</td><td>`"sparrow"` is a hyponym of `"bird"`; `"animal"` is a hypernym of `"dog"`.</td></tr>
    <tr><td><strong>4. Meronymy / Holonymy</strong></td><td>$\text{PART-OF}$ compositional relationship ($A$ is a physical component of $B$).</td><td>`"wheel"` is a meronym of `"car"`; `"car"` is a holonym of `"wheel"`.</td></tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">The Simplified Lesk WSD Algorithm (Lesk, 1986)</div>
  Given target ambiguous word $w$ in context sentence $C$:
  <ol>
    <li>Retrieve all dictionary definitions (glosses) and usage examples for each synset sense $S_i$ of $w$ in WordNet.</li>
    <li>Compute the word token overlap score between the context sentence $C$ and the gloss/examples of sense $S_i$: $\text{Overlap}(S_i, C) = | \text{Words}(S_i.\text{gloss}) \cap \text{Words}(C) |$.</li>
    <li>Select the sense $\hat{S} = \arg\max_{S_i} \text{Overlap}(S_i, C)$ with the highest word overlap count.</li>
  </ol>
</div>

<h2 class="section-title">Topic 30 – 32: Vector Space Models & TF-IDF Weighting [UPLOADED PYQ]</h2>

<div class="formula-card">
  <strong>1. Term Frequency-Inverse Document Frequency (TF-IDF) [UPLOADED PYQ]:</strong>
  $$\text{TF}(t, d) = \frac{\text{Count}(t, d)}{\sum_{t' \in d} \text{Count}(t', d)}$$
  $$\text{IDF}(t, D) = \log_{10} \left( \frac{N}{\text{DF}(t)} \right)$$
  $$\mathbf{\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)}$$
  Where $N$ is total documents in corpus, and $\text{DF}(t)$ is number of documents containing term $t$.
</div>

<div class="formula-card">
  <strong>2. Vector Cosine Similarity Metric:</strong>
  $$\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum_{i=1}^d u_i^2} \sqrt{\sum_{i=1}^d v_i^2}}$$
</div>

<h2 class="section-title">Topic 33 – 35: Neural Word Embeddings (Word2Vec, GloVe, FastText) [UPLOADED PYQ]</h2>

<div class="callout callout-info">
  <div class="callout-title">The Distributional Hypothesis (J.R. Firth, 1957)</div>
  <em>"You shall know a word by the company it keeps!"</em> Words appearing in similar contextual distributions acquire geometrically close spatial representations in $d$-dimensional embedding space.
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Embedding Model</th>
      <th style="width: 45%;">Training Objective & Operational Mechanism</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Word2Vec: CBOW [UPLOADED PYQ]</strong></td>
      <td><strong>Continuous Bag-of-Words:</strong> Predicts current center target word $w_t$ given surrounding context window words: $\arg\max \log P(w_t \mid w_{t-c}, \dots, w_{t+c})$.</td>
      <td>Fast to train; higher accuracy for frequent words; smooths over distributional noise.</td>
    </tr>
    <tr>
      <td><strong>2. Word2Vec: Skip-Gram [UPLOADED PYQ]</strong></td>
      <td>Predicts surrounding context words given center word $w_t$: $\arg\max \sum \log P(w_{t+j} \mid w_t)$ using Negative Sampling.</td>
      <td>Superb for capturing subtle semantic nuances of rare words; slower to train.</td>
    </tr>
    <tr>
      <td><strong>3. GloVe</strong></td>
      <td><strong>Global Vectors (Stanford):</strong> Factorizes global log-co-occurrence matrix: $J = \sum f(X_{ij}) (w_i^T \tilde{w}_j + b_i + \tilde{b}_j - \log X_{ij})^2$.</td>
      <td>Combines global matrix factorization statistics with local context window advantages.</td>
    </tr>
    <tr>
      <td><strong>4. FastText (Meta AI)</strong></td>
      <td>Represents each word as a bag of <strong>Character $n$-Grams</strong> (e.g., `"<wh"`, `"whe"`, `"hee"`, `"eel>"`, `"<wheel>"`).</td>
      <td>Seamlessly computes embeddings for <strong>Out-of-Vocabulary (OOV)</strong> and morphologically complex words!</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M3 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Explain the Continuous Bag of Words (CBOW) and Skip-Gram models of Word2Vec with neat network diagrams. (10 Marks)</div>
  <div class="qa-a">
    - <strong>CBOW Architecture:</strong> Input layer takes $2C$ context word one-hot vectors $\rightarrow$ Projection layer averages context embeddings $\rightarrow$ Softmax output layer predicts the single probability distribution of center target word $w_t$.<br>
    - <strong>Skip-Gram Architecture:</strong> Input layer takes 1 center word one-hot vector $w_t \rightarrow$ Projection layer retrieves embedding $\rightarrow$ Output layer simultaneously predicts $2C$ context word probability distributions $\langle w_{t-C}, \dots, w_{t+C} \rangle$ using Negative Sampling ($\log \sigma(v'_{w_O}{}^T v_{w_I}) + \sum_{i=1}^k \mathbb{E}[\log \sigma(-v'_{w_{i}}{}^T v_{w_I})]$).
  </div>
</div>
"""
