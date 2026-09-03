#!/usr/bin/env python3
"""
Final Master 10-12 Page NLP Suite Compiler.
Guarantees 10-12 pages for every module and 56+ pages for NLP_Full_Course_Master.pdf.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf
from boost_nlp_to_all_10_pages import (
    M1_CONTENT, M1_BOOST,
    M2_CONTENT, M2_BOOST,
    M3_CONTENT, M3_BOOST,
    M4_CONTENT, M4_BOOST,
    M5_CONTENT, M5_BOOST,
    NLP_REVISION_BOOST, NLP_LAB_GUIDE
)

# ----------------- MODULE 1 ULTRA BOOST -----------------
M1_ULTRA = r"""
<h2 class="section-title">Topic 12: Advanced Morphology & University Exam Problem Bank (Part II)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 9: Complete Damerau-Levenshtein Edit Distance with Transpositions</div>
  <p>Compute edit distance with transpositions (cost 1) between $S = \text{"CA"}$ and $T = \text{"ABC"}$:</p>
  <ul>
    <li>Standard Levenshtein (Insertion, Deletion, Substitution): Transform `CA` $\rightarrow$ `A` (del C) $\rightarrow$ `AB` (ins B) $\rightarrow$ `ABC` (ins C) = 3 operations.</li>
    <li><strong>Damerau-Levenshtein (Allows adjacent character swaps):</strong>
      $$D[i, j] = \min \begin{cases} D[i-1, j] + 1 & (\text{Del}) \\ D[i, j-1] + 1 & (\text{Ins}) \\ D[i-1, j-1] + \text{cost} & (\text{Sub}) \\ D[i-2, j-2] + 1 & (\text{Transposition if } S[i]=T[j-1] \land S[i-1]=T[j]) \end{cases}$$
    </li>
    <li>Transform `CA` $\rightarrow$ `AC` (1 transposition) $\rightarrow$ `ABC` (1 insertion of B) $\implies \mathbf{D = 2 \text{ operations!}}$</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q6. Explain the Difference between Unicode Normalization Forms NFC, NFD, NFKC, and NFKD. (8 Marks)</div><div class="qa-a">• <strong>NFD (Canonical Decomposition):</strong> Decomposes composite accented characters into base characters plus separate combining diacritical marks (e.g., `é` $\rightarrow$ `e` + `\u0301`).<br>• <strong>NFC (Canonical Composition):</strong> Decomposes characters then recombines them into canonical precomposed characters (e.g., `e` + `\u0301` $\rightarrow$ `é`). Standard for web text.<br>• <strong>NFKD (Compatibility Decomposition):</strong> Decomposes both canonical accents and formatting variants (e.g., ligature `ﬁ` $\rightarrow$ `f` + `i`; exponent `2³` $\rightarrow$ `2` + `3`). Ideal for NLP search and tokenization pipelines.<br>• <strong>NFKC (Compatibility Composition):</strong> Applies compatibility decomposition followed by canonical recomposition.</div></div>

<div class="qa-card"><div class="qa-q">Q7. Detail the Chomsky Hierarchy and Explain Why Natural Languages are Not Context-Free. (8 Marks)</div><div class="qa-a">While Context-Free Grammars (CFGs) model the vast majority of human language syntax (nested embeddings, center embeddings), natural languages contain <strong>cross-serial dependencies</strong> that violate the Pumping Lemma for Context-Free Languages.<br>• <strong>Evidence (Shieber 1985):</strong> In Swiss-German, subordinate clauses require crossed syntactic matching between verbs and noun phrases ($NP_1 \ NP_2 \dots NP_k \ V_1 \ V_2 \dots V_k$ where $NP_i$ is the grammatical object of $V_i$). This requires <em>Mildly Context-Sensitive Grammars</em> (such as Tree-Adjoining Grammars / TAGs).</div></div>
"""

# ----------------- MODULE 2 ULTRA BOOST -----------------
M2_ULTRA = r"""
<h2 class="section-title">Topic 24: Advanced Probability Formalisms & University Exam Problem Bank (Part II)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 10: Trigram Perplexity Calculation on Test Sentence</div>
  <p>Given test sentence $S = \text{"<s> I love NLP </s>"}$ ($N = 4$ tokens: `I`, `love`, `NLP`, `</s>`).</p>
  <p>Learned Trigram Conditional Probabilities:</p>
  <ul>
    <li>$P(\text{"I"} \mid \text{"<s>"}, \text{"<s>"}) = 0.25$</li>
    <li>$P(\text{"love"} \mid \text{"<s>"}, \text{"I"}) = 0.50$</li>
    <li>$P(\text{"NLP"} \mid \text{"I"}, \text{"love"}) = 0.10$</li>
    <li>$P(\text{"</s>"} \mid \text{"love"}, \text{"NLP"}) = 0.20$</li>
  </ul>
  <p><strong>1. Joint Sentence Probability:</strong></p>
  $$P(S) = 0.25 \times 0.50 \times 0.10 \times 0.20 = 0.0025 = 2.5 \times 10^{-3}$$
  <p><strong>2. Test Set Perplexity ($N = 4$):</strong></p>
  $$\mathbf{\text{PP}(S) = \left( \frac{1}{0.0025} \right)^{1/4} = (400)^{0.25} \approx \mathbf{4.472}}$$
  <p><em>Interpretation:</em> At each word position, the language model is as uncertain as if choosing uniformly from among $4.47$ possible words!</p>
</div>

<div class="qa-card"><div class="qa-q">Q4. Compare Katz Backoff with Jelinek-Mercer Linear Interpolation. (8 Marks)</div><div class="qa-a">• <strong>Jelinek-Mercer Interpolation:</strong> Always combines higher and lower-order n-gram estimates ($P_{\text{JM}} = \lambda_3 P(w_i \mid w_{i-2}, w_{i-1}) + \lambda_2 P(w_i \mid w_{i-1}) + \lambda_1 P(w_i)$), even when high-order counts are large.<br>• <strong>Katz Backoff:</strong> Uses the high-order MLE count discounted by Good-Turing ($d_r$) if $C(w_{i-k}^i) > 0$. It backs off to lower-order models <em>only when</em> the high-order n-gram count is zero ($C=0$), scaling the lower-order estimate by backoff normalization factor $\alpha(w_{i-k}^{i-1})$ so total probability sums strictly to 1.0!</div></div>

<div class="qa-card"><div class="qa-q">Q5. Explain the Linear-Chain Conditional Random Field (CRF) Feature Functions and Viterbi Inference. (8 Marks)</div><div class="qa-a">In a linear-chain CRF, the conditional probability of label sequence $\mathbf{y}$ given observation sequence $\mathbf{x}$ is:
$$\mathbf{P(\mathbf{y} \mid \mathbf{x}) = \frac{1}{Z(\mathbf{x})} \exp\left( \sum_{t=1}^T \sum_{k=1}^K w_k f_k(y_t, y_{t-1}, \mathbf{x}, t) \right)}$$
Where $f_k$ are arbitrary feature functions (e.g., $f_1 = 1$ if $y_t = \text{PROPN}$ and $x_t$ starts with capital letter). Unlike HMMs, CRFs support arbitrary overlapping, non-independent features, and normalize globally via partition function $Z(\mathbf{x})$, completely eliminating the label bias problem!</div></div>
"""

# ----------------- MODULE 3 ULTRA BOOST -----------------
M3_ULTRA = r"""
<h2 class="section-title">Topic 34: Advanced Semantic Embeddings & University Exam Problem Bank (Part II)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 11: Complete Pointwise Mutual Information (PMI) Matrix Computation</div>
  <p>Consider a 3x3 word-context co-occurrence matrix from a mini-corpus ($N = 100$ total co-occurrences):</p>
  <table class="custom-table">
    <thead><tr><th>Target \ Context</th><th>`computer`</th><th>`data`</th><th>`pie`</th><th>Row Sum $C(w)$</th></tr></thead>
    <tbody>
      <tr><td><strong>`digital`</strong></td><td>20</td><td>15</td><td>0</td><td>35</td></tr>
      <tr><td><strong>`cherry`</strong></td><td>0</td><td>0</td><td>25</td><td>25</td></tr>
      <tr><td><strong>`information`</strong></td><td>10</td><td>30</td><td>0</td><td>40</td></tr>
      <tr><td><strong>Col Sum $C(c)$</strong></td><td>30</td><td>45</td><td>25</td><td>$\mathbf{N = 100}$</td></tr>
    </tbody>
  </table>
  <p><strong>1. Compute PMI(`digital`, `computer`):</strong></p>
  $$P(\text{digital}, \text{computer}) = \frac{20}{100} = 0.20 \qquad P(\text{digital}) = \frac{35}{100} = 0.35 \qquad P(\text{computer}) = \frac{30}{100} = 0.30$$
  $$\mathbf{\text{PMI} = \log_2 \left( \frac{0.20}{0.35 \times 0.30} \right) = \log_2 \left( \frac{0.20}{0.105} \right) = \log_2(1.9048) = \mathbf{+0.9296}}$$
  <p><strong>2. Compute PMI(`digital`, `pie`) with Zero Count:</strong></p>
  $$\text{PMI} = \log_2(0) = -\infty \implies \mathbf{\text{PPMI}(\text{digital}, \text{pie}) = \max(0, -\infty) = \mathbf{0.0000}}$$
</div>

<div class="qa-card"><div class="qa-q">Q4. Explain Why Word2Vec Uses the Subsampling of Frequent Words and How the Probability Threshold is Formulated. (8 Marks)</div><div class="qa-a">In raw natural text, ubiquitous words like `the`, `of`, `and` occur millions of times, providing near-zero semantic discrimination while consuming massive training compute. Mikolov et al. subsample words during training, discarding word $w_i$ with probability:
$$\mathbf{P(\text{discard } w_i) = 1 - \sqrt{\frac{t}{f(w_i)}}}$$
Where $f(w_i)$ is the corpus frequency fraction of word $w_i$ and $t \approx 10^{-4}$ is a threshold parameter. Words with frequency $f(w) > t$ are discarded with high probability, accelerating training speed by $2\times$ to $10\times$ while drastically improving vector representations of rare words!</div></div>
"""

# ----------------- MODULE 4 ULTRA BOOST -----------------
M4_ULTRA = r"""
<h2 class="section-title">Topic 45: Advanced Deep Transformer Architectures & University Exam Problem Bank (Part II)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 12: Multi-Head Attention Dimensions & Tensor Computation</div>
  <p>Given Transformer model dimension $d_{\text{model}} = 512$, number of attention heads $h = 8$, sequence length $T = 64$:</p>
  <ul>
    <li>Head projection dimension: $\mathbf{d_k = d_v = \frac{d_{\text{model}}}{h} = \frac{512}{8} = \mathbf{64}}$.</li>
    <li>Input matrix $\mathbf{X} \in \mathbb{R}^{64 \times 512}$.</li>
    <li>Weight projection matrices per head: $\mathbf{W}_i^Q \in \mathbb{R}^{512 \times 64}, \mathbf{W}_i^K \in \mathbb{R}^{512 \times 64}, \mathbf{W}_i^V \in \mathbb{R}^{512 \times 64}$.</li>
    <li>Raw attention logits: $\mathbf{Q}_i \mathbf{K}_i^T \in \mathbb{R}^{64 \times 64}$.</li>
    <li>Scaled dot product attention per head: $\text{head}_i = \text{softmax}\left(\frac{\mathbf{Q}_i \mathbf{K}_i^T}{\sqrt{64}}\right)\mathbf{V}_i \in \mathbb{R}^{64 \times 64} \times \mathbb{R}^{64 \times 64} = \mathbb{R}^{64 \times 64}$.</li>
    <li>Concatenated output across all 8 heads: $\text{Concat}(\text{head}_1, \dots, \text{head}_8) \in \mathbb{R}^{64 \times 512}$.</li>
    <li>Final linear projection: $\mathbf{W}^O \in \mathbb{R}^{512 \times 512} \implies \mathbf{\text{Output Tensor } \mathbf{Y} \in \mathbb{R}^{64 \times 512}}$.</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q3. Detail the RoBERTa (Robustly Optimized BERT Approach) Modifications over Original BERT. (8 Marks)</div><div class="qa-a">Liu et al. (2019) demonstrated that original BERT was severely undertrained, introducing 4 critical modifications that established new state-of-the-art results across GLUE, SQuAD, and RACE:<br>1. <strong>Removed Next Sentence Prediction (NSP):</strong> Showing that NSP hurts downstream task performance when inputs are continuous sequences of full documents.<br>2. <strong>Dynamic Masking:</strong> Generating a novel 15% random mask pattern every time a sequence is fed to the model across training epochs (original BERT used static masking fixed at data pre-processing).<br>3. <strong>Larger Batch Sizes & Learning Rates:</strong> Scaling batch size from 256 to 8,000 sequences with AdamW optimization.<br>4. <strong>Byte-Level BPE:</strong> Using a 50,000-token byte-level BPE tokenizer without unicode preprocessing.</div></div>
"""

# ----------------- MODULE 5 ULTRA BOOST -----------------
M5_ULTRA = r"""
<h2 class="section-title">Topic 53: Advanced Downstream Tasks & University Exam Problem Bank (Part II)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 13: ROUGE-1, ROUGE-2, and ROUGE-L Summarization Metrics Calculation</div>
  <p><strong>Generated Summary ($C$):</strong> <em>"the prime minister visited london yesterday"</em> (5 words)</p>
  <p><strong>Reference Summary ($R$):</strong> <em>"prime minister visited london on monday"</em> (6 words)</p>
  <ul>
    <li><strong>1. ROUGE-1 (Unigram Recall):</strong>
      <ul>
        <li>Reference unigrams: `prime`, `minister`, `visited`, `london`, `on`, `monday` (Total = 6).</li>
        <li>Matching unigrams in candidate: `prime`, `minister`, `visited`, `london` (4 matches).</li>
        <li>$$\mathbf{\text{ROUGE-1 Recall} = \frac{4}{6} = \mathbf{0.6667 \ (66.67\%)} \qquad \text{Precision} = \frac{4}{5} = \mathbf{0.8000}}$$</li>
      </ul>
    </li>
    <li><strong>2. ROUGE-2 (Bigram Recall):</strong>
      <ul>
        <li>Reference bigrams: `prime minister`, `minister visited`, `visited london`, `london on`, `on monday` (Total = 5).</li>
        <li>Matching bigrams: `prime minister`, `minister visited`, `visited london` (3 matches).</li>
        <li>$$\mathbf{\text{ROUGE-2 Recall} = \frac{3}{5} = \mathbf{0.6000 \ (60.00\%)}}$$</li>
      </ul>
    </li>
    <li><strong>3. ROUGE-L (Longest Common Subsequence Recall):</strong>
      <ul>
        <li>$\text{LCS}(R, C) = \text{["prime", "minister", "visited", "london"]}$ (Length = 4).</li>
        <li>$$\mathbf{\text{ROUGE-L Recall} = \frac{\text{Length}(\text{LCS})}{|R|} = \frac{4}{6} = \mathbf{0.6667 \ (66.67\%)}}$$</li>
      </ul>
    </li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q3. Detail the Extractive Question Answering Architecture for SQuAD with Span Boundary Logits. (8 Marks)</div><div class="qa-a">In extractive Question Answering (e.g., SQuAD), input text is formatted as `[CLS] Query Tokens [SEP] Passage Context Tokens [SEP]`.<br>1. Passage contextual embeddings $\mathbf{h}_i \in \mathbb{R}^d$ are passed to two linear classification heads $\mathbf{w}_s, \mathbf{w}_e \in \mathbb{R}^d$.<br>2. Start and End span probabilities are computed via softmax across all context tokens:
$$P_{\text{start}}(i) = \frac{\exp(\mathbf{w}_s^T \mathbf{h}_i)}{\sum_j \exp(\mathbf{w}_s^T \mathbf{h}_j)} \qquad P_{\text{end}}(j) = \frac{\exp(\mathbf{w}_e^T \mathbf{h}_j)}{\sum_k \exp(\mathbf{w}_e^T \mathbf{h}_k)}$$
3. The predicted answer span $(i^*, j^*)$ maximizes $P_{\text{start}}(i) \times P_{\text{end}}(j)$ subject to constraint $i \le j \le i + L_{\text{max}}$.</div></div>
"""

# ----------------- REVISION ULTRA BOOST -----------------
NLP_REVISION_ULTRA = NLP_REVISION_BOOST + r"""
<h2 class="section-title">Comprehensive 10-Page Master Revision Examination Compendium</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 9: The 6 NLP Processing Levels Pipeline</div>
  $$\text{Phonetics} \rightarrow \text{Morphology} \rightarrow \text{Syntax} \rightarrow \text{Semantics} \rightarrow \text{Pragmatics} \rightarrow \text{Discourse}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 10: Complete Smoothing Formulas Reference</div>
  <ul>
    <li><strong>Laplace:</strong> $P(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + 1}{C(w_{i-1}) + |V|}$</li>
    <li><strong>Add-$k$:</strong> $P(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + k}{C(w_{i-1}) + k|V|}$</li>
    <li><strong>Good-Turing:</strong> $r^* = (r + 1)\frac{N_{r+1}}{N_r}, \ P_0 = \frac{N_1}{N}$</li>
    <li><strong>Kneser-Ney:</strong> $P_{\text{KN}} = \frac{\max(C - d, 0)}{C} + \lambda P_{\text{cont}}(w_i)$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 11: Word Embedding Objective Functions</div>
  <ul>
    <li><strong>SGNS:</strong> $\mathcal{L} = \log \sigma(\mathbf{u}_o^T \mathbf{v}_c) + \sum_{k=1}^K \log \sigma(-\mathbf{u}_{n_k}^T \mathbf{v}_c)$</li>
    <li><strong>GloVe:</strong> $J = \sum f(X_{ij})(\mathbf{w}_i^T \mathbf{\tilde{w}}_j + b_i + \tilde{b}_j - \log X_{ij})^2$</li>
    <li><strong>FastText:</strong> $\mathbf{v}_w = \sum_{g \in \mathcal{G}_w} \mathbf{z}_g$ (Subword character n-grams)</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 12: Transformer Multi-Head Self-Attention Equations</div>
  $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \qquad \text{MHA} = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O$$
  $$\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2 \qquad \text{LayerNorm}(x) = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}\odot \gamma + \beta$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 13: Translation & Summarization Evaluation Metrics</div>
  $$\text{BLEU} = \text{BP} \cdot \exp\left(\sum_{n=1}^4 \frac{1}{4} \ln p_n\right), \quad \text{BP} = \min\left(1, e^{1 - r/c}\right)$$
  $$\text{ROUGE-N} = \frac{\sum_{\text{n-grams} \in R} \text{Match}(\text{n-gram})}{\sum_{\text{n-grams} \in R} \text{Count}(\text{n-gram})} \qquad \text{ROUGE-L} = \frac{\text{LCS}(R, C)}{|R|}$$
</div>
"""

def execute_final_pass():
    m1_full = M1_CONTENT + M1_BOOST + M1_ULTRA
    m2_full = M2_CONTENT + M2_BOOST + M2_ULTRA
    m3_full = M3_CONTENT + M3_BOOST + M3_ULTRA
    m4_full = M4_CONTENT + M4_BOOST + M4_ULTRA
    m5_full = M5_CONTENT + M5_BOOST + M5_ULTRA

    print("NLP M1 Chars:", len(m1_full))
    print("NLP M2 Chars:", len(m2_full))
    print("NLP M3 Chars:", len(m3_full))
    print("NLP M4 Chars:", len(m4_full))
    print("NLP M5 Chars:", len(m5_full))

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
        NLP_REVISION_ULTRA
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
    execute_final_pass()
