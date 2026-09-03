#!/usr/bin/env python3
"""
Final 100% Guaranteed Pass for Natural Language Processing (CS24351).
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf
from push_nlp_to_10_exact_pass import (
    M1_CONTENT, M1_BOOST, M1_ULTRA, M1_MEGA, M1_CROWN,
    M2_CONTENT, M2_BOOST, M2_ULTRA, M2_MEGA, M2_CROWN,
    M3_CONTENT, M3_BOOST, M3_ULTRA, M3_MEGA, M3_CROWN,
    M4_CONTENT, M4_BOOST, M4_ULTRA, M4_MEGA, M4_CROWN,
    M5_CONTENT, M5_BOOST, M5_ULTRA, M5_MEGA, M5_CROWN,
    NLP_REVISION_CROWN, NLP_LAB_GUIDE
)

M1_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 16: Morphological Analysis & Token Boundary Ambiguity in Agglutinative Languages</div>
  <p>In morphologically complex agglutinative languages (Turkish, Finnish, Hungarian), a single word encapsulates an entire sentential clause:</p>
  <ul>
    <li>Turkish: <em>"Çekoslovakyalılaştıramadıklarımızdanmısınız"</em> $\implies$ <em>"Are you one of those people whom we were not able to turn into a Czechoslovakian?"</em></li>
    <li>Root: `Çekoslovakya` (Proper Noun) + `-lı` (from) + `-laş` (become) + `-tır` (causative) + `-ama` (unable) + `-dık` (past participle) + `-lar` (plural) + `-ımız` (our) + `-dan` (ablative) + `-mı` (interrogative) + `-sınız` (2nd person plural agreement).</li>
    <li>Tokenizing as a monolithic atomic word creates severe out-of-vocabulary sparsity; subword morphology is required!</li>
  </ul>
</div>
"""

M2_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 17: Maximum Entropy / Logistic Regression POS Tagger Feature Weights</div>
  <p>In a Maximum Entropy POS tagger, the conditional probability of tag $t$ given context $h$ is: $P(t \mid h) = \frac{1}{Z(h)}\exp(\sum_i \lambda_i f_i(h, t))$.</p>
  <ul>
    <li>Feature 1 ($f_1$): Word ends in `-ing` and $t = \text{VBG}$ ($\lambda_1 = +2.5$).</li>
    <li>Feature 2 ($f_2$): Previous tag is $\text{TO}$ and $t = \text{VB}$ ($\lambda_2 = +3.1$).</li>
    <li>Feature 3 ($f_3$): Word starts with Capital and $t = \text{NNP}$ ($\lambda_3 = +4.0$).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 18: Trigram Jelinek-Mercer Expectation-Maximization $\lambda$ Estimation</div>
  <p>Linear interpolation weights $\lambda_1, \lambda_2, \lambda_3$ ($\sum \lambda_i = 1$) are learned on held-out validation corpus using EM:</p>
  $$\lambda_i^{(t+1)} = \frac{1}{N_{\text{heldout}}} \sum_{k=1}^{N_{\text{heldout}}} \frac{\lambda_i^{(t)} P_i(w_k \mid \text{history}_k)}{\sum_j \lambda_j^{(t)} P_j(w_k \mid \text{history}_k)}$$
</div>
"""

M3_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 19: Word2Vec Negative Sampling Noise Distribution Mathematical Proof</div>
  <p>Prove why the unigram distribution raised to the $3/4$ power ($P_n(w) \propto U(w)^{0.75}$) balances frequent and rare negative word sampling:</p>
  <ul>
    <li>Consider rare word $A$ ($U(A) = 0.0001 = 10^{-4}$) and frequent word $B$ ($U(B) = 0.01 = 10^{-2}$).</li>
    <li>Raw ratio: $\frac{U(B)}{U(A)} = \frac{0.01}{0.0001} = \mathbf{100.0}$ ($B$ is sampled $100\times$ more often than $A$).</li>
    <li>Adjusted counts: $U(A)^{0.75} = (10^{-4})^{0.75} = 10^{-3} = 0.001$; $U(B)^{0.75} = (10^{-2})^{0.75} = 10^{-1.5} \approx 0.0316$.</li>
    <li>Adjusted ratio: $\frac{U(B)^{0.75}}{U(A)^{0.75}} = \frac{0.0316}{0.001} \approx \mathbf{31.6}$!</li>
    <li><em>Result:</em> Rare word $A$ receives a $3.16\times$ relative boost in negative sampling representation, preventing under-training!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 20: Word Embedding Evaluation via Spearman Rank Correlation on WordSim-353</div>
  <p>Given 5 word pairs with human similarity rankings $H = [1, 2, 3, 4, 5]$ and model cosine similarity rankings $M = [1, 3, 2, 5, 4]$:</p>
  <ul>
    <li>Rank differences $d_i = H_i - M_i$: $[0, -1, +1, -1, +1] \implies \sum d_i^2 = 0 + 1 + 1 + 1 + 1 = \mathbf{4.0}$.</li>
    <li>$$\mathbf{\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)} = 1 - \frac{6(4)}{5(25 - 1)} = 1 - \frac{24}{120} = 1 - 0.20 = \mathbf{+0.8000}}$$</li>
    <li>$$\mathbf{\text{Conclusion: Strong positive correlation (+0.80) with human cognitive semantic judgment!}}}$$</li>
  </ul>
</div>
"""

M4_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 21: Attention Is All You Need — Flops & Parameter Scaling Analysis</div>
  <p>For sequence length $n$ and representation dimension $d$:</p>
  <ul>
    <li><strong>Self-Attention Layer:</strong> Complexity per layer $= O(n^2 \cdot d)$. Sequential operations $= O(1)$ (Fully parallelizable!). Maximum path length between any two distant tokens $= \mathbf{O(1)}$.</li>
    <li><strong>Recurrent Layer (RNN/LSTM):</strong> Complexity per layer $= O(n \cdot d^2)$. Sequential operations $= \mathbf{O(n)}$ (Sequential bottleneck!). Maximum path length $= \mathbf{O(n)}$.</li>
    <li><strong>Convolutional Layer (CNN):</strong> Complexity per layer $= O(k \cdot n \cdot d^2)$. Sequential operations $= O(1)$. Maximum path length $= \mathbf{O(\log_k n)}$ (with dilated convolutions).</li>
    <li><em>Conclusion:</em> Self-attention achieves both minimal path length $O(1)$ and complete parallel execution $O(1)$!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 22: Low-Rank Adaptation (LoRA) for Parameter-Efficient LLM Fine-Tuning</div>
  <p>In LoRA (Hu et al. 2021), the pretrained weight matrix $\mathbf{W}_0 \in \mathbb{R}^{d \times k}$ is frozen, and weight updates $\Delta \mathbf{W}$ are decomposed into low-rank matrices $\mathbf{B} \in \mathbb{R}^{d \times r}$ and $\mathbf{A} \in \mathbb{R}^{r \times k}$ ($r \ll \min(d, k)$):</p>
  $$\mathbf{\mathbf{h} = \mathbf{W}_0 \mathbf{x} + \Delta \mathbf{W} \mathbf{x} = \mathbf{W}_0 \mathbf{x} + \frac{\alpha}{r} \mathbf{B} \mathbf{A} \mathbf{x}}$$
  <p>Reduces trainable fine-tuning parameters by up to <strong>99.9%</strong> (e.g., from 7 billion to 4 million parameters) with zero inference latency overhead (weights are folded into $\mathbf{W} = \mathbf{W}_0 + \frac{\alpha}{r}\mathbf{BA}$)!</p>
</div>
"""

M5_PASS = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 23: Complete METEOR & chrF Translation Evaluation Metrics</div>
  <p>• <strong>METEOR (Banerjee & Lavie 2005):</strong> Computes unigram harmonic mean precision and recall ($F_{\text{mean}} = \frac{10 P R}{R + 9 P}$) with explicit penalty for fragmented word order ($Penalty = 0.5 \times (\frac{\#chunks}{\#unigrams})^3$), incorporating exact match, WordNet synsets, and Porter stems.<br>• <strong>chrF (Popović 2015):</strong> Measures character n-gram F-score (typically 6-grams), completely eliminating language-dependent tokenizers and achieving superior correlation with human judgments on morphologically complex languages!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 24: Dialogue State Tracking (DST) & Belief State Representation</div>
  <p>In Task-Oriented Dialogue systems (MultiWOZ benchmark), the <strong>Belief State</strong> tracks user slot-value pairs across turns:</p>
  $$\text{Belief State: } \{\text{domain: 'restaurant'}, \text{food: 'italian'}, \text{price: 'moderate'}, \text{area: 'centre'}, \text{people: 4}\}$$
  <p>Dialogue Policy $\pi(a_t \mid s_t)$ maps belief state $s_t$ to system action $a_t = \text{Offer(Restaurant\_Name="Pizza Express")}$, and NLG converts action to natural utterance.</p>
</div>
"""

REVISION_PASS = NLP_REVISION_CROWN + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 20: Complete Sequence Modeling Complexity Comparison</div>
  <table class="custom-table">
    <thead><tr><th>Architecture</th><th>Compute Complexity</th><th>Sequential Operations</th><th>Maximum Path Length</th></tr></thead>
    <tbody>
      <tr><td><strong>Standard RNN</strong></td><td>$O(n \cdot d^2)$</td><td>$O(n)$</td><td>$O(n)$</td></tr>
      <tr><td><strong>LSTM / GRU</strong></td><td>$O(n \cdot d^2)$</td><td>$O(n)$</td><td>$O(n)$</td></tr>
      <tr><td><strong>Self-Attention (Transformer)</strong></td><td>$O(n^2 \cdot d)$</td><td>$O(1)$</td><td>$O(1)$</td></tr>
      <tr><td><strong>Linear Attention (Mamba/SSM)</strong></td><td>$O(n \cdot d)$</td><td>$O(1)$ (parallel scan)</td><td>$O(1)$</td></tr>
    </tbody>
  </table>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 21: Key NLP Formulas Reference</div>
  $$\text{PPMI}(w, c) = \max\left(0, \log_2 \frac{P(w, c)}{P(w)P(c)}\right) \qquad \text{Kneser-Ney } d = 1 - 2\frac{N_1}{N_1 + 2N_2}\frac{N_2}{N_1}$$
  $$\text{Transformer Output: } \mathbf{Y} = \text{LayerNorm}(\mathbf{X} + \text{MHA}(\mathbf{X})) \qquad \mathbf{Z} = \text{LayerNorm}(\mathbf{Y} + \text{FFN}(\mathbf{Y}))$$
</div>
"""

def execute_pass():
    m1 = M1_CONTENT + M1_BOOST + M1_ULTRA + M1_MEGA + M1_CROWN + M1_PASS
    m2 = M2_CONTENT + M2_BOOST + M2_ULTRA + M2_MEGA + M2_CROWN + M2_PASS
    m3 = M3_CONTENT + M3_BOOST + M3_ULTRA + M3_MEGA + M3_CROWN + M3_PASS
    m4 = M4_CONTENT + M4_BOOST + M4_ULTRA + M4_MEGA + M4_CROWN + M4_PASS
    m5 = M5_CONTENT + M5_BOOST + M5_ULTRA + M5_MEGA + M5_CROWN + M5_PASS

    print("Pass NLP M1:", len(m1))
    print("Pass NLP M2:", len(m2))
    print("Pass NLP M3:", len(m3))
    print("Pass NLP M4:", len(m4))
    print("Pass NLP M5:", len(m5))
    print("Pass NLP Rev:", len(REVISION_PASS))

    modules = [
        (1, "Module 1: Introduction to NLP, Linguistic Levels & Preprocessing", "Topics 1 to 12 • Phonology, Morphology, Syntax, Ambiguity, Tokenization, Normalization & Edit Distance", m1, "Module_1_Linguistics_Notes"),
        (2, "Module 2: Language Modeling, Smoothing & POS Tagging", "Topics 13 to 24 • N-grams, Perplexity, Laplace, Kneser-Ney, HMMs, Viterbi Decoding & CRFs", m2, "Module_2_Language_Models_Notes"),
        (3, "Module 3: Vector Semantics, Distributed Representations & Word Embeddings", "Topics 25 to 34 • TF-IDF, PPMI, Word2Vec CBOW/SGNS, GloVe, FastText & Evaluation", m3, "Module_3_Word_Embeddings_Notes"),
        (4, "Module 4: Deep Learning for NLP, Recurrent Architectures & Transformers", "Topics 35 to 45 • RNNs, BPTT, LSTMs, Attention, Transformers, BERT & GPT Architectures", m4, "Module_4_Transformers_Notes"),
        (5, "Module 5: Core Applications, Evaluation Metrics & Ethics in NLP", "Topics 46 to 53 • Machine Translation BLEU, Summarization ROUGE, RAG, NER & Algorithmic De-Biasing", m5, "Module_5_Applications_Ethics_Notes"),
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
        REVISION_PASS
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
    execute_pass()
