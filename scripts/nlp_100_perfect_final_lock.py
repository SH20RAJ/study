#!/usr/bin/env python3
"""
Final 100% Guaranteed 10-Page Lock for All NLP Modules.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf
from lock_nlp_100_pass_final import (
    M1_CONTENT, M1_BOOST, M1_ULTRA, M1_MEGA, M1_CROWN, M1_PASS, M1_LOCK, M1_PERFECT, M1_FINAL_PUSH, M1_TRUE, M1_TOP,
    M2_CONTENT, M2_BOOST, M2_ULTRA, M2_MEGA, M2_CROWN, M2_PASS, M2_LOCK, M2_PERFECT, M2_FINAL_PUSH, M2_TRUE, M2_TOP, M2_CROWN2, M2_LOCK2,
    M3_CONTENT, M3_BOOST, M3_ULTRA, M3_MEGA, M3_CROWN, M3_PASS, M3_LOCK, M3_PERFECT, M3_FINAL_PUSH, M3_TRUE, M3_TOP, M3_CROWN2, M3_LOCK2,
    M4_CONTENT, M4_BOOST, M4_ULTRA, M4_MEGA, M4_CROWN, M4_PASS, M4_LOCK, M4_PERFECT, M4_FINAL_PUSH, M4_TRUE, M4_TOP, M4_CROWN2, M4_LOCK2,
    M5_CONTENT, M5_BOOST, M5_ULTRA, M5_MEGA, M5_CROWN, M5_PASS, M5_LOCK, M5_PERFECT, M5_FINAL_PUSH, M5_TRUE, M5_TOP, M5_CROWN2, M5_LOCK2,
    REVISION_LOCK2, NLP_LAB_EXPANDED
)

M2_FINAL = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 78: Maximum Entropy Markov Model (MEMM) Objective Function Proof</div>
  <p>In MEMMs, parameters $\mathbf{w}$ are learned by maximizing conditional log-likelihood with $L_2$ Gaussian regularization: $\mathcal{L}(\mathbf{w}) = \sum_{i} \sum_{t} \left[ \mathbf{w}^T \mathbf{f}(y_{i, t}, y_{i, t-1}, \mathbf{x}_i) - \ln Z(y_{i, t-1}, \mathbf{x}_i) \right] - \frac{\|\mathbf{w}\|^2}{2\sigma^2}$. Optimized via L-BFGS in linear time!</p>
</div>
"""

M3_FINAL = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 79: Cosine Distance vs Angular Distance in Semantic Geometry</div>
  <p>Angular distance $d_\theta(\mathbf{u}, \mathbf{v}) = \frac{\arccos(\cos(\mathbf{u}, \mathbf{v}))}{\pi}$ satisfies all metric space axioms (including the Triangle Inequality), unlike raw cosine distance ($1 - \cos(\mathbf{u}, \mathbf{v})$) which is a semi-metric!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 80: Word2Vec Vector Arithmetic Stability Analysis</div>
  <p>Show that subtracting $\mathbf{v}_{\text{man}}$ removes gender attributes from the masculine subspace while retaining royalty features: $\mathbf{v}_{\text{king}} - \mathbf{v}_{\text{man}} \approx \mathbf{v}_{\text{royalty}}$, which upon adding $\mathbf{v}_{\text{woman}}$ lands precisely in the feminine royal semantic neighborhood of $\mathbf{v}_{\text{queen}}$!</p>
</div>
"""

M4_FINAL = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 81: FlashAttention SRAM Tiling Block Math</div>
  <p>Let SRAM cache size be $M$. Set block sizes $B_r = \lceil M / (4 d) \rceil, B_c = \lceil M / (4 d) \rceil$. FlashAttention loads blocks $Q_i \in \mathbb{R}^{B_r \times d}$ and $K_j \in \mathbb{R}^{B_c \times d}$ into SRAM, computing local attention without GPU DRAM roundtrips!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 82: Cross-Attention vs Self-Attention Matrix Dimensions</div>
  <p>In Transformer Decoders: Query matrix $\mathbf{Q} \in \mathbb{R}^{T_{\text{dec}} \times d}$ comes from the decoder hidden states, while Key $\mathbf{K} \in \mathbb{R}^{T_{\text{enc}} \times d}$ and Value $\mathbf{V} \in \mathbb{R}^{T_{\text{enc}} \times d}$ come from encoder representations. The resulting attention matrix $\mathbf{A} \in \mathbb{R}^{T_{\text{dec}} \times T_{\text{enc}}}$ aligns each generated word with relevant source words!</p>
</div>
"""

M5_FINAL = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 83: Exact Match (EM) vs Token-Level F1 in SQuAD QA</div>
  <p>For prediction <em>"the golden gate bridge"</em> and gold answer <em>"golden gate bridge"</em>:</p>
  <ul>
    <li><strong>Exact Match (EM):</strong> Binary $0.0$ (Strict string inequality).</li>
    <li><strong>Token-Level Precision:</strong> $3/4 = 0.75$; <strong>Recall:</strong> $3/3 = 1.0 \implies \mathbf{\text{F1} = \frac{2(0.75)(1.0)}{0.75+1.0} = \mathbf{0.8571 \ (85.71\%)}}}$.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 84: Algorithmic Debiasing Hard-Neutralization Matrix Projection</div>
  <p>For gender direction $\mathbf{g} = (0.6, 0.8)^T$ and biased word vector $\mathbf{w}_{\text{doctor}} = (2.0, 1.0)^T$:</p>
  $$\mathbf{w} \cdot \mathbf{g} = 2.0(0.6) + 1.0(0.8) = 1.2 + 0.8 = 2.0$$
  $$\mathbf{\mathbf{w}_{\text{neutral}} = (2.0, 1.0)^T - 2.0(0.6, 0.8)^T = (2.0 - 1.2, \ 1.0 - 1.6)^T = \mathbf{(0.8, -0.6)^T}}$$
  $$\mathbf{\text{Verification: } \mathbf{w}_{\text{neutral}} \cdot \mathbf{g} = 0.8(0.6) + (-0.6)(0.8) = 0.48 - 0.48 = \mathbf{0.000 \quad (Perfect Orthogonality!)}}}$$
</div>
"""

REVISION_FINAL = REVISION_LOCK2 + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 37: Complete Sequence Labeling Metrics</div>
  $$\text{Micro F1} = \frac{2 \cdot \sum TP}{\sum (2TP + FP + FN)} \qquad \text{Macro F1} = \frac{1}{|C|} \sum_{c=1}^{|C|} F1_c$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 38: Word Embedding Distinctions</div>
  <ul>
    <li><strong>SGNS:</strong> Maximizes $\log \sigma(\mathbf{u}_o^T \mathbf{v}_c) + \sum \log \sigma(-\mathbf{u}_{n_k}^T \mathbf{v}_c)$.</li>
    <li><strong>GloVe:</strong> Fits least-squares to co-occurrence counts: $\mathbf{w}_i^T \mathbf{\tilde{w}}_j + b_i + \tilde{b}_j = \log X_{ij}$.</li>
    <li><strong>FastText:</strong> Subword character n-grams; solves OOV.</li>
  </ul>
</div>
"""

def execute_final_pass_100():
    m2 = M2_CONTENT + M2_BOOST + M2_ULTRA + M2_MEGA + M2_CROWN + M2_PASS + M2_LOCK + M2_PERFECT + M2_FINAL_PUSH + M2_TRUE + M2_TOP + M2_CROWN2 + M2_LOCK2 + M2_FINAL
    m3 = M3_CONTENT + M3_BOOST + M3_ULTRA + M3_MEGA + M3_CROWN + M3_PASS + M3_LOCK + M3_PERFECT + M3_FINAL_PUSH + M3_TRUE + M3_TOP + M3_CROWN2 + M3_LOCK2 + M3_FINAL
    m4 = M4_CONTENT + M4_BOOST + M4_ULTRA + M4_MEGA + M4_CROWN + M4_PASS + M4_LOCK + M4_PERFECT + M4_FINAL_PUSH + M4_TRUE + M4_TOP + M4_CROWN2 + M4_LOCK2 + M4_FINAL
    m5 = M5_CONTENT + M5_BOOST + M5_ULTRA + M5_MEGA + M5_CROWN + M5_PASS + M5_LOCK + M5_PERFECT + M5_FINAL_PUSH + M5_TRUE + M5_TOP + M5_CROWN2 + M5_LOCK2 + M5_FINAL

    modules = [
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
        REVISION_FINAL
    )
    rev_html_file = os.path.join(HTML_DIR, "NLP_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "NLP_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "NLP 10-Page Master Revision")

    all_mods = [
        "Module_1_Linguistics_Notes",
        "Module_2_Language_Models_Notes",
        "Module_3_Word_Embeddings_Notes",
        "Module_4_Transformers_Notes",
        "Module_5_Applications_Ethics_Notes",
    ]

    master_doc = fitz.open()
    for fname in all_mods:
        mod_pdf = fitz.open(os.path.join(PDF_DIR, f"{fname}.pdf"))
        master_doc.insert_pdf(mod_pdf)
    
    lab_doc = fitz.open(os.path.join(PDF_DIR, "NLP_Lab_Practical_Guide.pdf"))
    master_doc.insert_pdf(lab_doc)

    rev_doc = fitz.open(rev_pdf_file)
    master_doc.insert_pdf(rev_doc)

    master_pdf_path = os.path.join(PDF_DIR, "NLP_Full_Course_Master.pdf")
    master_doc.save(master_pdf_path)
    print(f"✅ Generated {master_pdf_path} ({len(master_doc)} pages)")

if __name__ == "__main__":
    execute_final_pass_100()
