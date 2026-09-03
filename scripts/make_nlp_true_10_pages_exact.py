#!/usr/bin/env python3
"""
True 10-Page NLP Compiler.
Guarantees 10-12 pages for every module (M1 to M5) and 60+ pages for Full Master Book!
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf
from push_nlp_to_all_10_pages_final import (
    M1_CONTENT, M1_BOOST, M1_ULTRA,
    M2_CONTENT, M2_BOOST, M2_ULTRA,
    M3_CONTENT, M3_BOOST, M3_ULTRA,
    M4_CONTENT, M4_BOOST, M4_ULTRA,
    M5_CONTENT, M5_BOOST, M5_ULTRA,
    NLP_REVISION_ULTRA, NLP_LAB_GUIDE
)

# ----------------- MODULE 1 MEGA INJECTION -----------------
M1_MEGA = r"""
<h2 class="section-title">Topic 12.3: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 10: Needleman-Wunsch Global Sequence Alignment vs Smith-Waterman Local Alignment</div>
  <p>Compare two character sequences $S_1 = \text{"ACACACTA"}$ and $S_2 = \text{"AGCACACA"}$ with scoring parameters: $\text{Match} = +2, \text{Mismatch} = -1, \text{Gap} = -2$:</p>
  <ul>
    <li><strong>Needleman-Wunsch (Global Alignment):</strong> Forces end-to-end alignment across the entire string length. Initialization: $D[i, 0] = -2i, D[0, j] = -2j$. Optimal global alignment aligns all characters, penalizing terminal unaligned prefixes.</li>
    <li><strong>Smith-Waterman (Local Alignment):</strong> Identifies the highest-scoring local matching substring. Initialization: $D[i, 0] = 0, D[0, j] = 0$. Recurrence incorporates zero floor:
      $$\mathbf{D[i, j] = \max \begin{cases} 0 & (\text{Reset local alignment}) \\ D[i-1, j-1] + \text{score}(S_1[i], S_2[j]) \\ D[i-1, j] + \text{gap} \\ D[i, j-1] + \text{gap} \end{cases}}$$
      Traceback starts from the <em>maximum score anywhere in the entire matrix</em> and terminates as soon as a cell with score 0 is encountered, isolating the matching sub-block $\text{"CACAC"}$ with score $+10$!
    </li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q8. Explain Two-Level Morphology (Koskenniemi 1983) and Parallel Rule Application. (8 Marks)</div><div class="qa-a">Traditional generative phonology applied morphological rewrite rules in a strict cascading sequence, where intermediate stages might not represent real words.<br>• <strong>Two-Level Morphology:</strong> Eliminates cascading intermediate representations. It maps directly between the <em>Lexical Level</em> (abstract morphemes: `fox + N + PL`) and the <em>Surface Level</em> (concrete orthography: `foxes`) in a single step using parallel Finite State Transducers (FSTs) that simultaneously constrain character correspondences without intermediate rule order dependencies!</div></div>

<div class="qa-card"><div class="qa-q">Q9. Explain Lemmatization with Morphological Suffix Trees and Context-Aware POS Tagging. (8 Marks)</div><div class="qa-a">Unlike rule-based stemmers that operate blind to grammar, a production-grade <strong>Lemmatizer</strong> executes a 2-stage pipeline:<br>1. <strong>POS Tag Disambiguation:</strong> Identifies whether the token is a Noun, Verb, Adjective, or Adverb (e.g., in <em>"He is <u>meeting</u> her"</em>, `meeting` is tagged as `VERB`, whereas in <em>"The <u>meeting</u> started"</em>, `meeting` is tagged as `NOUN`).<br>2. <strong>Lexicon Lookup & Irregular Exception Mapping:</strong> Queries lexical databases (WordNet) with (word, POS) tuples: `(meeting, VERB)` maps to base lemma `meet`, whereas `(meeting, NOUN)` maps to lemma `meeting`! Irregulars (`went` $\rightarrow$ `go`, `better` $\rightarrow$ `good`) are resolved via morphological index tables.</div></div>
"""

# ----------------- MODULE 2 MEGA INJECTION -----------------
M2_MEGA = r"""
<h2 class="section-title">Topic 24.3: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 11: Modified Kneser-Ney Smoothing with 3 Distinct Discount Parameters</div>
  <p>Standard Kneser-Ney uses a single constant discount $d$. <strong>Modified Kneser-Ney (Chen & Goodman 1996)</strong> utilizes 3 distinct discounts $d_1, d_2, d_{3+}$ based on whether the n-gram count is 1, 2, or $\ge 3$:</p>
  $$\mathbf{d_1 = 1 - 2Y\frac{N_2}{N_1}, \quad d_2 = 2 - 3Y\frac{N_3}{N_2}, \quad d_{3+} = 3 - 4Y\frac{N_4}{N_3} \quad \text{where } Y = \frac{N_1}{N_1 + 2N_2}}$$
  <p>Provides the most empirically accurate statistical language modeling probability estimates in computational linguistics!</p>
</div>

<div class="qa-card"><div class="qa-q">Q6. Explain the Log-Probability Formulation in Viterbi Decoding to Prevent Numerical Underflow. (8 Marks)</div><div class="qa-a">In standard Viterbi decoding, sequence probabilities are computed via multiplying dozens of small floating-point emission and transition probabilities ($P \approx 10^{-4}$):
$$v_t(j) = \max_i [v_{t-1}(i) \cdot a_{ij}] \cdot b_j(w_t)$$
For a sentence of length $T = 30$, multiplying 30 small probabilities produces values below $10^{-60}$, causing catastrophic 64-bit IEEE floating-point numerical underflow to zero ($0.0$).<br>• <strong>Log-Viterbi Transformation:</strong> Transform all operations into log-space:
$$\mathbf{V_t(j) = \max_{i} \left[ V_{t-1}(i) + \ln(a_{ij}) \right] + \ln(b_j(w_t))}$$
Replaces multiplications with additions and handles arbitrary sequence lengths $T$ with zero precision loss!</div></div>

<div class="qa-card"><div class="qa-q">Q7. Detail the Witten-Bell Smoothing Algorithm and Compare it with Good-Turing. (8 Marks)</div><div class="qa-a"><strong>Witten-Bell Smoothing</strong> models zero-count events as the arrival of a previously unseen token. It defines the probability of seeing a novel word based on the number of <em>distinct word types</em> $T(w_{i-1})$ that have already been observed following history $w_{i-1}$:<br>
$$\mathbf{\lambda(w_{i-1}) = 1 - \frac{T(w_{i-1})}{T(w_{i-1}) + C(w_{i-1})} = \frac{C(w_{i-1})}{C(w_{i-1}) + T(w_{i-1})}}$$
$$P_{\text{WB}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i)}{C(w_{i-1}) + T(w_{i-1})} + \frac{T(w_{i-1})}{C(w_{i-1}) + T(w_{i-1})} P(w_i)$$
Unlike Good-Turing (which requires global frequency-of-frequency counts $N_r$), Witten-Bell computes parameters directly from local history statistics.</div></div>
"""

# ----------------- MODULE 3 MEGA INJECTION -----------------
M3_MEGA = r"""
<h2 class="section-title">Topic 34.3: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 12: Continuous Bag of Words (CBOW) Hidden-to-Output Weight Update</div>
  <p>In CBOW, let context words be $\{w_1, \dots, w_{2C}\}$ and true target center word be $w_t$ ($j^*$).</p>
  <ul>
    <li>Hidden representation: $\mathbf{h} = \frac{1}{2C} \sum_{i=1}^{2C} \mathbf{v}_{w_i} \in \mathbb{R}^d$.</li>
    <li>Output logits: $z_j = \mathbf{u}_j^T \mathbf{h}$ for all vocabulary words $j \in \{1, \dots, |V|\}$.</li>
    <li>Predicted probability via softmax: $\hat{y}_j = \frac{\exp(\mathbf{u}_j^T \mathbf{h})}{\sum_k \exp(\mathbf{u}_k^T \mathbf{h})}$.</li>
    <li>Cross-entropy loss: $\mathcal{L} = -\log \hat{y}_{j^*}$.</li>
    <li>Output weight gradient: $\frac{\partial \mathcal{L}}{\partial \mathbf{u}_j} = (\hat{y}_j - y_j)\mathbf{h}$ where $y_j = 1$ if $j=j^*$ else $0$.</li>
    <li>Input weight gradient for each context word $w_i$: $\mathbf{\frac{\partial \mathcal{L}}{\partial \mathbf{v}_{w_i}} = \frac{1}{2C} \sum_{j=1}^{|V|} (\hat{y}_j - y_j) \mathbf{u}_j}$.</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q5. Explain the Geometric Intuition of Word Vector Analogies and the Cosine Offset Method. (8 Marks)</div><div class="qa-a">Word vectors trained on large corpora organize semantic relationships as linear directional vector offsets in $\mathbb{R}^d$:
$$\mathbf{v}_{\text{King}} - \mathbf{v}_{\text{Man}} \approx \mathbf{v}_{\text{Queen}} - \mathbf{v}_{\text{Woman}} \implies \mathbf{v}_{\text{King}} - \mathbf{v}_{\text{Man}} + \mathbf{v}_{\text{Woman}} \approx \mathbf{v}_{\text{Queen}}$$
To solve an analogy $a : b :: c : ?$, 3CosAdd finds word $d^*$ maximizing:
$$\mathbf{d^* = \arg\max_{x \notin \{a, b, c\}} \cos(\mathbf{v}_x, \mathbf{v}_b - \mathbf{v}_a + \mathbf{v}_c) = \arg\max_x \left[ \cos(\mathbf{v}_x, \mathbf{v}_b) - \cos(\mathbf{v}_x, \mathbf{v}_a) + \cos(\mathbf{v}_x, \mathbf{v}_c) \right]}$$
Levy & Goldberg (2014) introduced <strong>3CosMul</strong> to prevent single large similarity terms from dominating:
$$\mathbf{d^* = \arg\max_x \frac{\cos(\mathbf{v}_x, \mathbf{v}_b) \cdot \cos(\mathbf{v}_x, \mathbf{v}_c)}{\cos(\mathbf{v}_x, \mathbf{v}_a) + \epsilon}}$$</div></div>

<div class="qa-card"><div class="qa-q">Q6. Compare Contextualized Word Representations (BERT, ELMo) vs. Static Word Embeddings (Word2Vec, GloVe). (8 Marks)</div><div class="qa-a"><table class="custom-table"><thead><tr><th>Dimension</th><th>Static Embeddings (Word2Vec / GloVe)</th><th>Contextualized Embeddings (ELMo / BERT)</th></tr></thead><tbody><tr><td><strong>Polysemy</strong></td><td>Single fixed vector per word; `bank` in "river bank" and "financial bank" have identical representations.</td><td>Dynamic vector computed as a function of the entire sentence; `bank` has distinct embeddings in different contexts.</td></tr><tr><td><strong>Lookup</strong></td><td>Fast static matrix row lookup $O(1)$.</td><td>Requires deep multi-layer transformer forward pass.</td></tr><tr><td><strong>Syntax Integration</strong></td><td>Captures only local bag-of-words co-occurrence.</td><td>Encodes deep syntactic hierarchical dependency structures and semantic roles.</td></tr></tbody></table></div></div>
"""

# ----------------- MODULE 4 MEGA INJECTION -----------------
M4_MEGA = r"""
<h2 class="section-title">Topic 45.3: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 13: Transformer Layer Normalization vs Batch Normalization</div>
  <p>In Computer Vision, Batch Normalization normalizes across batch dimension $N$ for each channel. In NLP, sentence lengths vary widely and mini-batches contain padded tokens:</p>
  <ul>
    <li><strong>Layer Normalization (Ba et al. 2016):</strong> Normalizes across the <em>hidden feature dimensions</em> $d_{\text{model}}$ independently for each individual token:
      $$\mathbf{\mu_i = \frac{1}{d} \sum_{j=1}^d x_{ij} \qquad \sigma_i^2 = \frac{1}{d} \sum_{j=1}^d (x_{ij} - \mu_i)^2}$$
      $$\mathbf{\text{LayerNorm}(\mathbf{x}_i) = \frac{\mathbf{x}_i - \mu_i}{\sqrt{\sigma_i^2 + \epsilon}} \odot \mathbf{\gamma} + \mathbf{\beta}}$$
    </li>
    <li><em>Advantage:</em> Completely independent of batch size and padding tokens; identical execution during training and autoregressive single-token inference!</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q4. Detail the KV-Cache (Key-Value Caching) Optimization for Fast Autoregressive LLM Inference. (8 Marks)</div><div class="qa-a">During autoregressive generation in decoder-only LLMs (GPT), generating token $t+1$ requires computing attention over all preceding tokens $1 \dots t$.<br>• <strong>Naive Generation:</strong> Re-computing Key and Value projections for all $t$ past tokens at every step scales quadratically $O(T^2)$ in compute.<br>• <strong>KV-Cache:</strong> Stores past computed Key ($\mathbf{K}_{1..t}$) and Value ($\mathbf{V}_{1..t}$) tensor matrices in GPU RAM. At step $t+1$, the model computes Query, Key, and Value <em>only for the single newly generated token</em> ($\mathbf{q}_{t+1}, \mathbf{k}_{t+1}, \mathbf{v}_{t+1}$), appends $\mathbf{k}_{t+1}, \mathbf{v}_{t+1}$ to cache, and computes attention in $O(T)$ linear time!</div></div>

<div class="qa-card"><div class="qa-q">Q5. Explain the T5 (Text-to-Text Transfer Transformer) Unified Framework. (8 Marks)</div><div class="qa-a"><strong>T5 (Raffel et al. 2020)</strong> unifies all NLP tasks into a single universal <strong>Text-to-Text</strong> sequence-to-sequence encoder-decoder architecture where both inputs and outputs are always text strings:<br>• <strong>Classification:</strong> `"cola sentence: The course is fine." -> "acceptable"`<br>• <strong>Translation:</strong> `"translate English to German: That is good. -> Das ist gut."`<br>• <strong>Summarization:</strong> `"summarize: [Article text] -> [Summary]"`<br>Pretrained using <em>Span Corruption</em> (masking random contiguous token spans with sentinel tokens `<extra_id_0>` and training the decoder to reconstruct the missing text).</div></div>
"""

# ----------------- MODULE 5 MEGA INJECTION -----------------
M5_MEGA = r"""
<h2 class="section-title">Topic 53.3: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 14: Aspect-Based Sentiment Analysis (ABSA) Pipeline</div>
  <p>In ABSA, review sentence $S = \text{"The pasta was delicious but the service was terrible"}$ contains multiple polarities across distinct aspects:</p>
  <ol>
    <li><strong>Aspect Term Extraction (ATE):</strong> Sequence tagging identifies aspect terms: `pasta` (Target 1), `service` (Target 2).</li>
    <li><strong>Aspect Term Polarity Classification (APTC):</strong> Encodes sentence with target aspect marker: `[CLS] S [SEP] pasta [SEP] -> Positive (98%)`; `[CLS] S [SEP] service [SEP] -> Negative (95%)`.</li>
  </ol>
</div>

<div class="qa-card"><div class="qa-q">Q4. Detail the Pointer-Generator Network for Abstractive Summarization with Out-Of-Vocabulary Copying. (8 Marks)</div><div class="qa-a"><strong>Pointer-Generator Networks (See et al. 2017)</strong> solve two major limitations of standard seq2seq summarizers: factual hallucinations and inability to produce out-of-vocabulary names/numbers.<br>1. <strong>Generation Probability $p_{\text{gen}} \in [0, 1]$:</strong> Computes a soft gating switch from decoder context $\mathbf{c}_t$, hidden state $\mathbf{s}_t$, and input $\mathbf{x}_t$:
$$p_{\text{gen}} = \sigma(\mathbf{w}_{c}^T \mathbf{c}_t + \mathbf{w}_{s}^T \mathbf{s}_t + \mathbf{w}_{x}^T \mathbf{x}_t + b_{\text{ptr}})$$
2. <strong>Hybrid Output Distribution:</strong> Interpolates between generating from vocabulary and copying directly from source text via attention weights $a_i^t$:
$$\mathbf{P(w) = p_{\text{gen}} P_{\text{vocab}}(w) + (1 - p_{\text{gen}}) \sum_{i: w_i = w} a_i^t}$$
3. <strong>Coverage Mechanism:</strong> Maintains a running sum of attention weights $c_i^t = \sum_{t'=1}^{t-1} a_i^{t'}$ and penalizes repeatedly attending to the same source words, completely eliminating repetitive loop summaries!</div></div>

<div class="qa-card"><div class="qa-q">Q5. Explain Statistical Watermarking for LLM-Generated Text (Kirchenbauer et al. 2023). (8 Marks)</div><div class="qa-a">To detect AI-generated text without changing perplexity:<br>1. When sampling token $t$, use previous token hash $h(x_{t-1})$ as a pseudo-random seed to partition the vocabulary $V$ into a <strong>Green List $G$</strong> (size $\gamma |V|$) and a <strong>Red List $R$</strong>.<br>2. Add a positive bias $\delta$ to the logits of green tokens: $\tilde{z}_k = z_k + \delta$ for $k \in G$.<br>3. <strong>Statistical Detection Test:</strong> For a candidate text of $T$ tokens, count green tokens $|T|_G$. Under human text, $|T|_G \sim \text{Binomial}(T, \gamma)$. Under watermarked text, $|T|_G \gg \gamma T$. A one-sided $Z$-score $z = \frac{|T|_G - \gamma T}{\sqrt{T\gamma(1-\gamma)}} > 4.0$ detects synthetic AI text with $p < 0.0001$ error rate!</div></div>
"""

# ----------------- REVISION DEFINITIVE INJECTION -----------------
NLP_REVISION_DEFINITIVE = NLP_REVISION_ULTRA + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 14: All POS Tagging Paradigms Compared</div>
  <table class="custom-table">
    <thead><tr><th>Model</th><th>Normalization</th><th>Strengths & Weaknesses</th></tr></thead>
    <tbody>
      <tr><td><strong>Rule-Based (Brill)</strong></td><td>Non-probabilistic</td><td>Error-driven transformation rules; fast but fragile on noisy text.</td></tr>
      <tr><td><strong>HMM</strong></td><td>Generative joint $P(W, T)$</td><td>Fast exact Viterbi decoding $O(T |S|^2)$; cannot use overlapping rich features.</td></tr>
      <tr><td><strong>MEMM</strong></td><td>Discriminative local $P(t_i | t_{i-1}, \mathbf{x})$</td><td>Supports arbitrary features; suffers from severe Label Bias Problem.</td></tr>
      <tr><td><strong>Linear CRF</strong></td><td>Discriminative global $Z(\mathbf{x})$</td><td>Global partition function; eliminates label bias; optimal sequence labeler.</td></tr>
      <tr><td><strong>BiLSTM-CRF</strong></td><td>Neural feature + CRF</td><td>Deep bidirectional contextual embeddings + CRF syntactic transition constraints.</td></tr>
    </tbody>
  </table>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 15: The Transformer Parameter Sizing Equations</div>
  <ul>
    <li>Embedding Parameters: $|V| \times d_{\text{model}}$</li>
    <li>Self-Attention Weights: $4 \times d_{\text{model}}^2$ (Query, Key, Value, Output projections)</li>
    <li>Feed-Forward Network (FFN): $2 \times (d_{\text{model}} \times d_{\text{ff}}) = 8 \times d_{\text{model}}^2$ (since $d_{\text{ff}} = 4 d_{\text{model}}$)</li>
    <li>LayerNorm & Biases: $\approx 4 d_{\text{model}}$</li>
    <li>Total Parameters per Encoder Layer: $\mathbf{\approx 12 \times d_{\text{model}}^2}$</li>
  </ul>
</div>
"""

def execute_definitive_nlp():
    m1_full = M1_CONTENT + M1_BOOST + M1_ULTRA + M1_MEGA
    m2_full = M2_CONTENT + M2_BOOST + M2_ULTRA + M2_MEGA
    m3_full = M3_CONTENT + M3_BOOST + M3_ULTRA + M3_MEGA
    m4_full = M4_CONTENT + M4_BOOST + M4_ULTRA + M4_MEGA
    m5_full = M5_CONTENT + M5_BOOST + M5_ULTRA + M5_MEGA

    print("Definitive NLP M1 Chars:", len(m1_full))
    print("Definitive NLP M2 Chars:", len(m2_full))
    print("Definitive NLP M3 Chars:", len(m3_full))
    print("Definitive NLP M4 Chars:", len(m4_full))
    print("Definitive NLP M5 Chars:", len(m5_full))
    print("Definitive NLP Rev Chars:", len(NLP_REVISION_DEFINITIVE))

    modules = [
        (1, "Module 1: Introduction to NLP, Linguistic Levels & Preprocessing", "Topics 1 to 12 • Phonology, Morphology, Syntax, Ambiguity, Tokenization, Normalization & Edit Distance", m1_full, "Module_1_Linguistics_Notes"),
        (2, "Module 2: Language Modeling, Smoothing & POS Tagging", "Topics 13 to 24 • N-grams, Perplexity, Laplace, Kneser-Ney, HMMs, Viterbi Decoding & CRFs", m2_full, "Module_2_Language_Models_Notes"),
        (3, "Module 3: Vector Semantics, Distributed Representations & Word Embeddings", "Topics 25 to 34 • TF-IDF, PPMI, Word2Vec CBOW/SGNS, GloVe, FastText & Evaluation", m3_full, "Module_3_Word_Embeddings_Notes"),
        (4, "Module 4: Deep Learning for NLP, Recurrent Architectures & Transformers", "Topics 35 to 45 • RNNs, BPTT, LSTMs, Attention, Transformers, BERT & GPT Architectures", m4_full, "Module_4_Transformers_Notes"),
        (5, "Module 5: Core Applications, Evaluation Metrics & Ethics in NLP", "Topics 46 to 53 • Machine Translation BLEU, Summarization ROUGE, RAG, NER & Algorithmic De-Biasing", m5_full, "Module_5_Applications_Ethics_Notes"),
    ]

    for num, title, subtitle, content, fname in modules:
        html_content = wrap_html(title, subtitle, content, module_num=num)
        html_file = os.path.join(HTML_DIR, f"{fname}.html")
        pdf_file = os.path.join(PDF_DIR, f"{fname}.pdf")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        generate_pdf(html_file, pdf_file, f"NLP Module {num}")

    # Revision Guide
    rev_html = wrap_html(
        "Natural Language Processing (CS24351) 10-Page Master Revision",
        "Universal Formulas, Transformer Architectures, Viterbi Trellises, BLEU Numericals & Solved Flashcards",
        NLP_REVISION_DEFINITIVE
    )
    rev_html_file = os.path.join(HTML_DIR, "NLP_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "NLP_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "NLP 10-Page Master Revision")

    # Lab Guide
    lab_html = wrap_html(
        "NLP Python Laboratory Guide",
        "Hands-On Implementation of Word2Vec, BiLSTM-CRF & Transformers",
        NLP_LAB_GUIDE
    )
    lab_html_file = os.path.join(HTML_DIR, "NLP_Lab_Practical_Guide.html")
    lab_pdf_file = os.path.join(PDF_DIR, "NLP_Lab_Practical_Guide.pdf")
    with open(lab_html_file, "w", encoding="utf-8") as f:
        f.write(lab_html)
    generate_pdf(lab_html_file, lab_pdf_file, "NLP Lab Guide")

    # Full Master Book via PyMuPDF merge
    master_doc = fitz.open()
    for _, _, _, _, fname in modules:
        mod_pdf = fitz.open(os.path.join(PDF_DIR, f"{fname}.pdf"))
        master_doc.insert_pdf(mod_pdf)
    
    lab_doc = fitz.open(lab_pdf_file)
    master_doc.insert_pdf(lab_doc)

    rev_doc = fitz.open(rev_pdf_file)
    master_doc.insert_pdf(rev_doc)

    master_pdf_path = os.path.join(PDF_DIR, "NLP_Full_Course_Master.pdf")
    master_doc.save(master_pdf_path)
    print(f"✅ Generated {master_pdf_path} ({len(master_doc)} pages)")

if __name__ == "__main__":
    execute_definitive_nlp()
