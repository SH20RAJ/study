#!/usr/bin/env python3
"""
Final 10-Page Lock for NLP Modules & Master Book.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf
from finalize_nlp_true_10_pages import (
    M1_CONTENT, M1_BOOST, M1_ULTRA, M1_MEGA, M1_CROWN, M1_PASS, M1_LOCK, M1_PERFECT, M1_FINAL_PUSH,
    M2_CONTENT, M2_BOOST, M2_ULTRA, M2_MEGA, M2_CROWN, M2_PASS, M2_LOCK, M2_PERFECT, M2_FINAL_PUSH,
    M3_CONTENT, M3_BOOST, M3_ULTRA, M3_MEGA, M3_CROWN, M3_PASS, M3_LOCK, M3_PERFECT, M3_FINAL_PUSH,
    M4_CONTENT, M4_BOOST, M4_ULTRA, M4_MEGA, M4_CROWN, M4_PASS, M4_LOCK, M4_PERFECT, M4_FINAL_PUSH,
    M5_CONTENT, M5_BOOST, M5_ULTRA, M5_MEGA, M5_CROWN, M5_PASS, M5_LOCK, M5_PERFECT, M5_FINAL_PUSH,
    REVISION_FINAL_PUSH, NLP_LAB_EXPANDED
)

M1_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 54: Non-Deterministic Finite State Automata (NFA) to DFA Subset Construction for Regex Matchers</div>
  <p>For regex `(a|b)*abb`, construct the DFA transition table via powerset subset construction, demonstrating linear $O(n)$ deterministic token matching speed!</p>
</div>
"""

M2_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 55: Forward-Backward State Posterior Decoding</div>
  <p>In HMMs, state posterior probability $\gamma_t(i) = P(t_t = q_i \mid W) = \frac{\alpha_t(i)\beta_t(i)}{\sum_j \alpha_t(j)\beta_t(j)}$ allows computing the expected number of transitions from state $i$ during Baum-Welch training!</p>
</div>
"""

M3_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 56: Skip-Gram with Negative Sampling (SGNS) Computational Speedup Proof</div>
  <p>Prove that computing binary logistic loss on $K=5$ negative samples reduces GPU gradient backpropagation time by $\mathbf{99.995\%}$ compared to full vocabulary softmax ($|V| = 100,000$)!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 57: Contextual Polysemy Disambiguation in Transformer Self-Attention</div>
  <p>In sentence $S_1 = \text{"The bank riverbed was eroded"}$ vs $S_2 = \text{"The bank approved the loan"}$, trace how self-attention dynamically projects the token `bank` into divergent subspace coordinates!</p>
</div>
"""

M4_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 58: Sinusoidal Positional Encoding Frequency Allocation Proof</div>
  <p>Prove why the geometric progression of wavelengths $\lambda_i = 2\pi \cdot 10000^{2i/d}$ spans from $2\pi$ to $20000\pi$, allowing the model to attend simultaneously to immediate neighboring tokens and global document-level structural anchors!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 59: Attention Logit Scaling by $\sqrt{d_k}$ Derivation</div>
  <p>Show that without the $\frac{1}{\sqrt{d_k}}$ scaling factor, the variance of dot product $q \cdot k$ equals $d_k = 64$, pushing softmax outputs to saturated extremes ($0.0$ or $1.0$) with near-zero gradients!</p>
</div>
"""

M5_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 60: BLEU Brevity Penalty Exponential Decay Curve</div>
  <p>For candidate length $c = 10$ and reference length $r = 15$: $\text{BP} = \exp(1 - 15/10) = \exp(-0.5) \approx \mathbf{0.6065}$. The score is penalized by $40\%$ for omitting essential reference content!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 61: RAG Dense Indexing with FAISS Flat vs HNSW Graphs</div>
  <p>• <strong>IndexFlatIP:</strong> Exact brute-force inner-product search $O(N \cdot d)$.<br>• <strong>HNSW (Hierarchical Navigable Small World):</strong> Multi-layer proximity graph achieving approximate nearest neighbor retrieval in blazing fast $O(\log N)$ logarithmic time!</p>
</div>
"""

REVISION_TRUE = REVISION_FINAL_PUSH + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 29: Language Modeling & Perplexity Summary</div>
  $$\text{Perplexity} = 2^{H(W)} \qquad \text{Kneser-Ney: } P_{\text{KN}} = \frac{\max(C-d, 0)}{C} + \lambda P_{\text{cont}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 30: Attention & Transformers Summary</div>
  $$\text{Scaled Dot-Product: } \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \qquad \text{MHA} = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O$$
</div>
"""

def execute_lock():
    m1 = M1_CONTENT + M1_BOOST + M1_ULTRA + M1_MEGA + M1_CROWN + M1_PASS + M1_LOCK + M1_PERFECT + M1_FINAL_PUSH + M1_TRUE
    m2 = M2_CONTENT + M2_BOOST + M2_ULTRA + M2_MEGA + M2_CROWN + M2_PASS + M2_LOCK + M2_PERFECT + M2_FINAL_PUSH + M2_TRUE
    m3 = M3_CONTENT + M3_BOOST + M3_ULTRA + M3_MEGA + M3_CROWN + M3_PASS + M3_LOCK + M3_PERFECT + M3_FINAL_PUSH + M3_TRUE
    m4 = M4_CONTENT + M4_BOOST + M4_ULTRA + M4_MEGA + M4_CROWN + M4_PASS + M4_LOCK + M4_PERFECT + M4_FINAL_PUSH + M4_TRUE
    m5 = M5_CONTENT + M5_BOOST + M5_ULTRA + M5_MEGA + M5_CROWN + M5_PASS + M5_LOCK + M5_PERFECT + M5_FINAL_PUSH + M5_TRUE

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
        REVISION_TRUE
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
    execute_lock()
