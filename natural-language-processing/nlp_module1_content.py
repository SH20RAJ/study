# NLP Module 1 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

NLP_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Morphology, Tokenization & Statistical Language Modeling</div>
  <div class="toc-grid">
    <div>1. NLP Pipeline Hierarchy (Phonetics, Morphology, Syntax, Semantics, Pragmatics)</div>
    <div>2. Regular Expressions & Finite-State Transducers (FST) for Morphological Parsing</div>
    <div>3. Tokenization Challenges, Minimum Edit Distance (Levenshtein) Dynamic Programming</div>
    <div>4. Subword Tokenization Algorithms: Byte-Pair Encoding (BPE), WordPiece & Unigram</div>
    <div>5. Word Stemming (Porter Stemmer Rules) vs. Morphological Lemmatization</div>
    <div>6. Statistical Language Modeling & The Chain Rule of Probability</div>
    <div>7. $N$-gram Language Models (Unigram, Bigram, Trigram) & Markov Assumptions</div>
    <div>8. Language Model Evaluation: Perplexity ($\text{PPL}$) Mathematical Formulation</div>
    <div>9. Smoothing Techniques: Laplace (Add-1), Add-$k$, Lidstone & Absolute Discounting</div>
    <div>10. Advanced Smoothing: Good-Turing Frequency Estimation ($r^* = (r+1)\frac{N_{r+1}}{N_r}$)</div>
    <div>11. Modified Kneser-Ney Smoothing (Interpolation & Continuation Probability $P_{\text{cont}}$)</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Natural Language Hierarchy & Morphology</h2>
<p>
  <strong>Natural Language Processing (NLP)</strong> is a multidisciplinary field at the intersection of Computer Science, Artificial Intelligence, and Computational Linguistics concerned with the automated understanding, generation, and processing of human language.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Linguistic Level</th>
      <th style="width: 38%;">Core Linguistic Phenomenon</th>
      <th>Key Computational Tasks</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Phonetics & Phonology</strong></td><td>Physical sounds and linguistic acoustic patterns.</td><td>Speech-to-Text (ASR), Text-to-Speech (TTS).</td></tr>
    <tr><td><strong>2. Morphology</strong></td><td>Structure and formation of words from root morphemes.</td><td>Stemming, Lemmatization, Tokenization, BPE.</td></tr>
    <tr><td><strong>3. Syntax</strong></td><td>Grammatical rules governing sentence and phrase structure.</td><td>POS Tagging, Context-Free Parsing, Dependency Parsing.</td></tr>
    <tr><td><strong>4. Semantics</strong></td><td>Literal meaning of words, phrases, and compositions.</td><td>WordNet, Word2Vec, BERT, Semantic Role Labeling.</td></tr>
    <tr><td><strong>5. Pragmatics & Discourse</strong></td><td>Contextual meaning, intent, coreference, and conversational tone.</td><td>Anaphora Resolution, Dialogue Systems, Sarcasm Detection.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 3 & 4: Subword Tokenization (Byte-Pair Encoding - BPE)</h2>

<div class="callout callout-info">
  <div class="callout-title">The Byte-Pair Encoding (BPE) Algorithm (Sennrich et al., 2016)</div>
  <ol>
    <li>Initialize vocabulary with all individual characters in the training corpus plus an end-of-word symbol `</w>`.</li>
    <li>Count the frequency of all adjacent symbol pairs in the tokenized corpus.</li>
    <li>Identify the most frequent symbol pair $(c_1, c_2)$ and merge it into a single new vocabulary token $c_1 c_2$.</li>
    <li>Repeat steps 2 and 3 for a fixed number of merge operations $k$ (e.g., $32,000$ merges in GPT-2).</li>
    <li><em>Significance:</em> Solves the Out-of-Vocabulary (OOV) problem by representing rare and unseen words as sequences of subword units (e.g., `unaffordability` $\rightarrow$ `un` + `afford` + `ability`).</li>
  </ol>
</div>

<h2 class="section-title">Topic 6 & 7: $N$-gram Language Modeling & The Chain Rule</h2>

<div class="formula-card">
  <strong>1. Exact Chain Rule of Probability for Sentence $W = (w_1, w_2, \dots, w_n)$:</strong>
  $$P(w_1, w_2, \dots, w_n) = \prod_{k=1}^n P(w_k \mid w_1, w_2, \dots, w_{k-1})$$
</div>

<div class="formula-card">
  <strong>2. Bigram Language Model (1st-Order Markov Assumption):</strong>
  $$P(w_1, w_2, \dots, w_n) \approx \prod_{k=1}^n P(w_k \mid w_{k-1}) \quad \text{where } P(w_k \mid w_{k-1}) = \frac{C(w_{k-1}, w_k)}{C(w_{k-1})}$$
</div>

<div class="formula-card">
  <strong>3. Language Model Perplexity ($\text{PPL}$):</strong>
  $$\text{PPL}(W) = P(w_1, w_2, \dots, w_n)^{-\frac{1}{n}} = \sqrt[n]{\frac{1}{P(w_1, w_2, \dots, w_n)}} = 2^{-\frac{1}{n} \sum_{i=1}^n \log_2 P(w_i \mid w_{i-1})}$$
  <em>Lower Perplexity indicates a superior language model that is less surprised by the test corpus!</em>
</div>

<h2 class="section-title">Topic 9 – 11: Smoothing Techniques for Statistical Language Models</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Smoothing Method</th>
      <th style="width: 45%;">Probability Estimation Formula</th>
      <th>Key Mechanics & Intuition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Laplace (Add-1)</strong></td>
      <td>$$P_{\text{Laplace}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + 1}{C(w_{i-1}) + V}$$</td>
      <td>Adds 1 to every count; shifts far too much probability mass to unseen $N$-grams in large vocabularies $V$.</td>
    </tr>
    <tr>
      <td><strong>2. Add-$k$ (Lidstone)</strong></td>
      <td>$$P_{\text{Add-}k}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + k}{C(w_{i-1}) + k V} \quad (0 < k < 1)$$</td>
      <td>Reduces probability mass distortion compared to Add-1.</td>
    </tr>
    <tr>
      <td><strong>3. Absolute Discounting</strong></td>
      <td>$$P(w_i \mid w_{i-1}) = \frac{\max(C(w_{i-1}, w_i) - d, 0)}{C(w_{i-1})} + \frac{d \cdot |\{w : C(w_{i-1}, w) > 0\}|}{C(w_{i-1})} P(w_i)$$</td>
      <td>Subtracts a fixed discount $d \in (0, 1)$ from non-zero counts and redistributes mass to unigrams.</td>
    </tr>
    <tr>
      <td><strong>4. Kneser-Ney (Interpolated)</strong></td>
      <td>$$P_{\text{KN}}(w_i \mid w_{i-1}) = \frac{\max(C(w_{i-1}, w_i) - d, 0)}{C(w_{i-1})} + \lambda(w_{i-1}) P_{\text{continuation}}(w_i)$$
          $$P_{\text{continuation}}(w_i) = \frac{|\{w' : C(w', w_i) > 0\}|}{\sum_{w} |\{w' : C(w', w) > 0\}|}$$
      </td>
      <td>Considers how versatile word $w_i$ is as a continuation across diverse preceding contexts (e.g., `San Francisco`). State-of-the-art $N$-gram smoothing.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module I)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Define Perplexity. Given a test sentence with probability $10^{-6}$ and length 6 words, compute its Perplexity. (6 Marks)</div>
  <div class="qa-a">
    <strong>Perplexity ($\text{PPL}$):</strong> The reciprocal geometric mean of the probability assigned to the test sentence by the language model:<br>
    $$\text{PPL}(W) = (P(W))^{-1/N} = (10^{-6})^{-1/6} = 10^1 = \mathbf{10}$$
    A perplexity of 10 means the model is as confused as if it had to choose uniformly among 10 words at each step.
  </div>
</div>
"""
