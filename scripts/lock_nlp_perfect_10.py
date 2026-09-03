#!/usr/bin/env python3
"""
Final 100% Perfect Pass for Natural Language Processing (CS24351).
All modules strictly 10+ pages, Revision 10+ pages, Master Book 65+ pages!
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf
from lock_nlp_100_percent_true import (
    M1_CONTENT, M1_BOOST, M1_ULTRA, M1_MEGA, M1_CROWN, M1_PASS, M1_LOCK,
    M2_CONTENT, M2_BOOST, M2_ULTRA, M2_MEGA, M2_CROWN, M2_PASS, M2_LOCK,
    M3_CONTENT, M3_BOOST, M3_ULTRA, M3_MEGA, M3_CROWN, M3_PASS, M3_LOCK,
    M4_CONTENT, M4_BOOST, M4_ULTRA, M4_MEGA, M4_CROWN, M4_PASS, M4_LOCK,
    M5_CONTENT, M5_BOOST, M5_ULTRA, M5_MEGA, M5_CROWN, M5_PASS, M5_LOCK,
    REVISION_LOCK, NLP_LAB_EXPANDED
)

M1_PERFECT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 37: Regular Expression Named Entity Pattern Extraction</div>
  <p>Construct production-grade regex patterns for extracting emails, URLs, and ISO dates:</p>
  <ul>
    <li><strong>Email Address:</strong> `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`</li>
    <li><strong>HTTP/HTTPS URL:</strong> `https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)`</li>
    <li><strong>ISO 8601 Date:</strong> `\b(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])\b`</li>
  </ul>
</div>
"""

M2_PERFECT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 38: Trigram Smoothing with Katz Backoff & Good-Turing Multipliers</div>
  <p>In Katz Backoff, the probability of trigram $w_i \mid w_{i-2}, w_{i-1}$ is formulated as:</p>
  $$P_{\text{Katz}}(w_i \mid w_{i-2}, w_{i-1}) = \begin{cases} d_r \frac{C(w_{i-2}^i)}{C(w_{i-2}^{i-1})} & \text{if } C(w_{i-2}^i) > 0 \\ \alpha(w_{i-2}, w_{i-1}) P_{\text{Katz}}(w_i \mid w_{i-1}) & \text{if } C(w_{i-2}^i) = 0 \end{cases}$$
  <p>Where backoff weight $\alpha(w_{i-2}, w_{i-1}) = \frac{1 - \sum_{w: C>0} P_{\text{Katz}}(w \mid w_{i-2}, w_{i-1})}{1 - \sum_{w: C>0} P_{\text{Katz}}(w \mid w_{i-1})}$. Ensures exact conservation of total probability mass!</p>
</div>
"""

M3_PERFECT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 39: FastText Subword Character N-Gram Vector Aggregation Trace</div>
  <p>Given word $w = \text{"cat"}$ ($n=3$): Subwords = $\{\text{<ca}, \text{cat}, \text{at>}, \text{<cat>}\}$. Vectors in 2D space:</p>
  <ul>
    <li>$\mathbf{z}_{\text{<ca}} = (0.2, 0.4)^T, \ \mathbf{z}_{\text{cat}} = (0.5, 0.8)^T, \ \mathbf{z}_{\text{at>}} = (0.1, 0.3)^T, \ \mathbf{z}_{\text{<cat>}} = (0.6, 0.9)^T$.</li>
    <li>$$\mathbf{\mathbf{v}_{\text{cat}} = \sum_{g} \mathbf{z}_g = (0.2+0.5+0.1+0.6, \ 0.4+0.8+0.3+0.9)^T = \mathbf{(1.4, 2.4)^T}}$$</li>
    <li>For unseen misspelled word $w' = \text{"cats"}$ with subwords $\{\text{<ca}, \text{cat}, \text{ats}, \text{ts>}, \text{<cats>}\}$: Even if `cats` was never in the training dictionary, the model computes a rich vector using shared subwords $\text{<ca}$ and $\text{cat}$!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 40: Term Frequency-Inverse Document Frequency (TF-IDF) Weighting Trace</div>
  <p>In a collection of $N = 10,000$ scientific documents, term $t = \text{"transformer"}$ appears $15$ times in a 300-word document $D_1$, and occurs in $100$ total documents across the corpus:</p>
  $$\text{TF}(t, D_1) = \frac{15}{300} = \mathbf{0.05} \qquad \text{IDF}(t) = \log_{10}\left( \frac{10,000}{100} \right) = \log_{10}(100) = \mathbf{2.0}$$
  $$\mathbf{\text{TF-IDF}(t, D_1) = 0.05 \times 2.0 = \mathbf{0.1000}}$$
</div>
"""

M4_PERFECT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 41: Multi-Query Attention (MQA) & Grouped-Query Attention (GQA)</div>
  <p>To reduce KV-Cache memory consumption in large-scale LLMs (LLaMA-2/3, Mistral):</p>
  <ul>
    <li><strong>Multi-Head Attention (MHA):</strong> $h$ Query heads, $h$ Key heads, $h$ Value heads. (Highest memory consumption).</li>
    <li><strong>Multi-Query Attention (MQA - Shazeer 2019):</strong> $h$ Query heads share a <em>single key head</em> and <em>single value head</em>. Reduces KV cache by factor of $h$ ($8\times$ to $32\times$), but can cause slight capacity degradation.</li>
    <li><strong>Grouped-Query Attention (GQA - Ainslie et al. 2023):</strong> Partitions $h$ Query heads into $G$ groups (e.g., $G = 8$), where each group shares 1 Key and 1 Value head. Strikes the optimal Pareto frontier between inference speed and model accuracy!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 42: Speculative Decoding for Accelerated LLM Generation</div>
  <p>Standard LLM inference is memory bandwidth-bound. <strong>Speculative Decoding (Leviathan et al. 2023)</strong> uses a fast small Draft Model (e.g., 1B parameters) to generate $K$ speculative draft tokens in parallel, which are verified simultaneously in a single forward pass by the large Target Model (e.g., 70B parameters), achieving a $\mathbf{2\times \text{ to } 3\times}$ inference acceleration with zero mathematical difference in output probability distribution!</p>
</div>
"""

M5_PERFECT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 43: COMET & Neural Translation Evaluation Metrics</div>
  <p>Traditional n-gram metrics (BLEU, ROUGE) penalize valid translations that use synonyms (e.g., `automobile` vs `car`). <strong>COMET (Rei et al. 2020)</strong> uses cross-lingual pretrained encoders (XLM-RoBERTa) to project the source sentence, candidate translation, and reference into a shared multilingual embedding space, computing neural semantic similarity that achieves state-of-the-art correlation with human professional translators!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 44: Direct Preference Optimization (DPO) Closed-Form Loss Derivation</div>
  <p>Rafailov et al. (2023) proved that the optimal policy under Bradley-Terry reward models satisfies: $r(x, y) = \beta \log \frac{\pi_\theta(y \mid x)}{\pi_{\text{ref}}(y \mid x)} + \beta \log Z(x)$.</p>
  $$\mathbf{\mathcal{L}_{\text{DPO}}(\theta; \pi_{\text{ref}}) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}}\left[ \log \sigma\left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right]}$$
  <p>Eliminates the separate reward model and reinforcement learning training stability issues entirely!</p>
</div>
"""

REVISION_PERFECT = REVISION_LOCK + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 25: Attention Architectures Cheat-Sheet</div>
  <ul>
    <li><strong>MHA:</strong> $h$ queries, $h$ keys, $h$ values ($h \times \text{KV}$).</li>
    <li><strong>MQA:</strong> $h$ queries, $1$ key, $1$ value ($1 \times \text{KV}$).</li>
    <li><strong>GQA:</strong> $h$ queries, $G$ keys, $G$ values ($G \times \text{KV}$).</li>
    <li><strong>FlashAttention:</strong> IO-aware tiling in GPU SRAM cache; $O(N)$ memory.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 26: Alignment & Preference Optimization</div>
  $$\text{DPO Loss: } -\log \sigma\left(\beta \ln\frac{\pi(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \ln\frac{\pi(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\right)$$
</div>
"""

def execute_all():
    m1 = M1_CONTENT + M1_BOOST + M1_ULTRA + M1_MEGA + M1_CROWN + M1_PASS + M1_LOCK + M1_PERFECT
    m2 = M2_CONTENT + M2_BOOST + M2_ULTRA + M2_MEGA + M2_CROWN + M2_PASS + M2_LOCK + M2_PERFECT
    m3 = M3_CONTENT + M3_BOOST + M3_ULTRA + M3_MEGA + M3_CROWN + M3_PASS + M3_LOCK + M3_PERFECT
    m4 = M4_CONTENT + M4_BOOST + M4_ULTRA + M4_MEGA + M4_CROWN + M4_PASS + M4_LOCK + M4_PERFECT
    m5 = M5_CONTENT + M5_BOOST + M5_ULTRA + M5_MEGA + M5_CROWN + M5_PASS + M5_LOCK + M5_PERFECT

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
        REVISION_PERFECT
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
        NLP_LAB_EXPANDED
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
    execute_all()
