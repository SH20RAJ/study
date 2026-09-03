#!/usr/bin/env python3
"""
Final 100% Locked 10-Page NLP Compiler.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf
from lock_nlp_to_10_pages_final import (
    M1_CONTENT, M1_BOOST, M1_ULTRA, M1_MEGA, M1_CROWN, M1_PASS, M1_LOCK, M1_PERFECT, M1_FINAL_PUSH, M1_TRUE,
    M2_CONTENT, M2_BOOST, M2_ULTRA, M2_MEGA, M2_CROWN, M2_PASS, M2_LOCK, M2_PERFECT, M2_FINAL_PUSH, M2_TRUE,
    M3_CONTENT, M3_BOOST, M3_ULTRA, M3_MEGA, M3_CROWN, M3_PASS, M3_LOCK, M3_PERFECT, M3_FINAL_PUSH, M3_TRUE,
    M4_CONTENT, M4_BOOST, M4_ULTRA, M4_MEGA, M4_CROWN, M4_PASS, M4_LOCK, M4_PERFECT, M4_FINAL_PUSH, M4_TRUE,
    M5_CONTENT, M5_BOOST, M5_ULTRA, M5_MEGA, M5_CROWN, M5_PASS, M5_LOCK, M5_PERFECT, M5_FINAL_PUSH, M5_TRUE,
    REVISION_TRUE, NLP_LAB_EXPANDED
)

M1_TOP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 62: Morphological Suffix Analyzer on Compound Agglutinations</div>
  <p>Deconstruct the compound word <em>"antidisestablishmentarianism"</em> ($28$ characters) into prefix, root, and suffix morphemes:</p>
  $$\text{anti (prefix)} + \text{dis (prefix)} + \text{establish (root)} + \text{ment (suffix)} + \text{arian (suffix)} + \text{ism (suffix)}$$
</div>
"""

M2_TOP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 63: Trigram Good-Turing Discounting on Sparse Web Corpora</div>
  <p>In a 1-billion-word web crawl, $N_1 = 40,000,000$ singleton trigrams, $N_2 = 10,000,000$ doubletons. $P_0 = \frac{40M}{1B} = \mathbf{0.040 = 4.0\%}$ total probability mass is safely reserved for previously unseen novel trigram sequences!</p>
</div>
"""

M3_TOP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 64: Continuous Bag of Words (CBOW) vs Skip-Gram Negative Sampling Convergence</div>
  <p>CBOW averages context embeddings, smoothing out stochastic noise and converging in $3\times$ fewer epochs on large dense corpora. Skip-Gram treats each (target, context) pair independently, giving rare words repeated training updates!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 65: GloVe Weighting Function Optimization Properties</div>
  <p>Show that when $X_{ij} \ge x_{\text{max}} = 100$, $f(X_{ij}) = 1.0$ caps the loss contribution, preventing extremely frequent pairs like `(of, the)` from warping semantic distances!</p>
</div>
"""

M4_TOP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 66: Multi-Head Self-Attention Projection Matrix Gradient Derivations</div>
  <p>For output loss $\mathcal{L}$, the gradient with respect to Value weight matrix $\mathbf{W}^V$ is $\frac{\partial \mathcal{L}}{\partial \mathbf{W}^V} = \mathbf{X}^T \mathbf{A}^T \frac{\partial \mathcal{L}}{\partial \mathbf{Y}}$ where $\mathbf{A} = \text{softmax}(QK^T/\sqrt{d_k})$.</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 67: Rotary Position Embedding (RoPE) Invariance Proof</div>
  <p>Show that $\mathbf{R}_{\Theta, m}^T \mathbf{R}_{\Theta, n} = \mathbf{R}_{\Theta, n-m}$, proving that the attention score between query at position $m$ and key at position $n$ depends purely on relative distance $n-m$!</p>
</div>
"""

M5_TOP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 68: Complete 4-Gram BLEU Score Calculation Trace</div>
  <p>Given candidate $c=12$, reference $r=14$, clipped precisions: $p_1 = 0.833, p_2 = 0.636, p_3 = 0.500, p_4 = 0.333$:</p>
  $$\text{BP} = \exp(1 - 14/12) = \exp(-0.1667) = \mathbf{0.8465}$$
  $$\mathbf{\text{BLEU-4} = 0.8465 \times \exp\left( \frac{\ln(0.833) + \ln(0.636) + \ln(0.500) + \ln(0.333)}{4} \right) = 0.8465 \times 0.545 = \mathbf{0.4613 \ (46.13\%)}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 69: ROUGE-L Longest Common Subsequence Dynamic Programming Recurrence</div>
  <p>For reference $R[1..m]$ and candidate $C[1..n]$:</p>
  $$\mathbf{\text{LCS}[i, j] = \begin{cases} \text{LCS}[i-1, j-1] + 1 & \text{if } R[i] = C[j] \\ \max(\text{LCS}[i-1, j], \text{LCS}[i, j-1]) & \text{if } R[i] \neq C[j] \end{cases}}$$
</div>
"""

REVISION_TOP = REVISION_TRUE + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 31: Complete Word Embedding Architectures</div>
  <ul>
    <li><strong>Word2Vec:</strong> CBOW (predicts center word) & Skip-Gram (predicts context words with negative sampling).</li>
    <li><strong>GloVe:</strong> Global co-occurrence matrix factorization with log-bilinear model.</li>
    <li><strong>FastText:</strong> Subword character n-grams; handles Out-Of-Vocabulary words.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 32: Transformer Layer Operations Cheat-Sheet</div>
  $$\mathbf{X} \xrightarrow{\text{MHA}} \mathbf{Y}_1 \xrightarrow{\text{Add \& LayerNorm}} \mathbf{Z}_1 \xrightarrow{\text{FFN}} \mathbf{Y}_2 \xrightarrow{\text{Add \& LayerNorm}} \mathbf{Z}_2$$
</div>
"""

def lock_pass():
    m1 = M1_CONTENT + M1_BOOST + M1_ULTRA + M1_MEGA + M1_CROWN + M1_PASS + M1_LOCK + M1_PERFECT + M1_FINAL_PUSH + M1_TRUE + M1_TOP
    m2 = M2_CONTENT + M2_BOOST + M2_ULTRA + M2_MEGA + M2_CROWN + M2_PASS + M2_LOCK + M2_PERFECT + M2_FINAL_PUSH + M2_TRUE + M2_TOP
    m3 = M3_CONTENT + M3_BOOST + M3_ULTRA + M3_MEGA + M3_CROWN + M3_PASS + M3_LOCK + M3_PERFECT + M3_FINAL_PUSH + M3_TRUE + M3_TOP
    m4 = M4_CONTENT + M4_BOOST + M4_ULTRA + M4_MEGA + M4_CROWN + M4_PASS + M4_LOCK + M4_PERFECT + M4_FINAL_PUSH + M4_TRUE + M4_TOP
    m5 = M5_CONTENT + M5_BOOST + M5_ULTRA + M5_MEGA + M5_CROWN + M5_PASS + M5_LOCK + M5_PERFECT + M5_FINAL_PUSH + M5_TRUE + M5_TOP

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
        REVISION_TOP
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
    lock_pass()
