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
from lock_nlp_true_100 import (
    M1_CONTENT, M1_BOOST, M1_ULTRA, M1_MEGA, M1_CROWN, M1_PASS, M1_LOCK, M1_PERFECT, M1_FINAL_PUSH, M1_TRUE, M1_TOP,
    M2_CONTENT, M2_BOOST, M2_ULTRA, M2_MEGA, M2_CROWN, M2_PASS, M2_LOCK, M2_PERFECT, M2_FINAL_PUSH, M2_TRUE, M2_TOP, M2_CROWN2, M2_LOCK2, M2_FINAL, M2_LOCKED_TRUE,
    M3_CONTENT, M3_BOOST, M3_ULTRA, M3_MEGA, M3_CROWN, M3_PASS, M3_LOCK, M3_PERFECT, M3_FINAL_PUSH, M3_TRUE, M3_TOP, M3_CROWN2, M3_LOCK2, M3_FINAL, M3_LOCKED_TRUE,
    M4_CONTENT, M4_BOOST, M4_ULTRA, M4_MEGA, M4_CROWN, M4_PASS, M4_LOCK, M4_PERFECT, M4_FINAL_PUSH, M4_TRUE, M4_TOP, M4_CROWN2, M4_LOCK2, M4_FINAL, M4_LOCKED_TRUE,
    M5_CONTENT, M5_BOOST, M5_ULTRA, M5_MEGA, M5_CROWN, M5_PASS, M5_LOCK, M5_PERFECT, M5_FINAL_PUSH, M5_TRUE, M5_TOP, M5_CROWN2, M5_LOCK2, M5_FINAL, M5_LOCKED_TRUE,
    REVISION_LOCKED_TRUE, NLP_LAB_EXPANDED
)

M2_EXACT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 91: Trigram Witten-Bell Dynamic Weight Trace</div>
  <p>In Witten-Bell smoothing: $\lambda(w_{i-1}) = \frac{C(w_{i-1})}{C(w_{i-1}) + T(w_{i-1})}$. If history $w_{i-1}$ has count $C = 100$ and precedes $T = 20$ distinct word types, $\lambda = \frac{100}{120} = \mathbf{0.8333}$, reserving $16.67\%$ mass for novel unseen transitions!</p>
</div>
"""

M3_EXACT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 92: Word Embedding Intrinsic Analogies Benchmark Evaluation</div>
  <p>On the Google Analogy Test Set (19,544 questions across syntactic and semantic categories), Skip-Gram with Negative Sampling ($d=300$) achieves $\mathbf{74.2\%}$ accuracy, outperforming classical LSA by over $45\%$!</p>
</div>
"""

M4_EXACT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 93: FlashAttention-2 Work Partitioning & FLOP Utilization</div>
  <p>Dao (2023) redesigned FlashAttention loop nesting by swapping the outer loop to iterate over sequence blocks of $Q$, reducing non-matmul FLOPs and boosting tensor core utilization from $50\%$ to $\mathbf{73\%}$ on Nvidia A100/H100 GPUs!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 94: ALiBi (Attention with Linear Biases) Long-Context Extrapolation</div>
  <p>Press et al. (2022) replaced positional embeddings with fixed linear slope biases $m = 2^{-8i/h}$: $\text{softmax}(QK^T/\sqrt{d_k} - m \cdot |i - j|)$, training on 2048 tokens while extrapolating to $\mathbf{8192+}$ tokens with zero perplexity increase!</p>
</div>
"""

M5_EXACT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 95: Cross-Encoder vs Bi-Encoder RAG Reranking Pipeline</div>
  <p>• <strong>Bi-Encoder (Fast Retrieval):</strong> Projects query and documents into isolated vectors; searches top 100 documents via FAISS in 5ms.<br>• <strong>Cross-Encoder (High Precision Reranker):</strong> Concatenates query and document `[CLS] Query [SEP] Doc [SEP]` through full cross-attention layers, sorting the top 5 most relevant passages with $\mathbf{+12.4\% \text{ MRR@10}}$ accuracy boost!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 96: Watermark Detection Z-Score Calculation</div>
  <p>For text of $T = 200$ tokens with $\gamma = 0.5$, an AI detector observes $|T|_G = 160$ green tokens:</p>
  $$\mu = 200(0.5) = 100 \qquad \sigma = \sqrt{200(0.5)(0.5)} = \sqrt{50} \approx 7.071$$
  $$\mathbf{z = \frac{160 - 100}{7.071} = \frac{60}{7.071} = \mathbf{+8.485} \implies p < 10^{-16} \quad (\text{Definitive Proof of Synthetic AI Origin!})}$$
</div>
"""

REVISION_EXACT = REVISION_LOCKED_TRUE + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 41: Vector Retrieval Architectures</div>
  <ul>
    <li><strong>Bi-Encoder:</strong> Dot-product $\mathbf{q}^T \mathbf{p}$; $O(1)$ lookup via ANN index (FAISS, Chroma, Milvus).</li>
    <li><strong>Cross-Encoder:</strong> Full transformer cross-attention $\text{BERT}(q, p)$; high-precision reranker.</li>
    <li><strong>Hybrid Search:</strong> Reciprocal Rank Fusion (RRF) combining BM25 keyword matching with Dense Vector embeddings.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 42: Modern LLM Pretraining & Alignment Pipeline</div>
  $$\text{Raw Web Crawl} \xrightarrow{\text{Deduplication/Filtering}} \text{Pretraining (Next Token)} \xrightarrow{\text{Base LLM}} \xrightarrow{\text{SFT}} \xrightarrow{\text{DPO/RLHF}} \text{Aligned Assistant}$$
</div>
"""

def execute_exact_pass():
    m2 = M2_CONTENT + M2_BOOST + M2_ULTRA + M2_MEGA + M2_CROWN + M2_PASS + M2_LOCK + M2_PERFECT + M2_FINAL_PUSH + M2_TRUE + M2_TOP + M2_CROWN2 + M2_LOCK2 + M2_FINAL + M2_LOCKED_TRUE + M2_EXACT
    m3 = M3_CONTENT + M3_BOOST + M3_ULTRA + M3_MEGA + M3_CROWN + M3_PASS + M3_LOCK + M3_PERFECT + M3_FINAL_PUSH + M3_TRUE + M3_TOP + M3_CROWN2 + M3_LOCK2 + M3_FINAL + M3_LOCKED_TRUE + M3_EXACT
    m4 = M4_CONTENT + M4_BOOST + M4_ULTRA + M4_MEGA + M4_CROWN + M4_PASS + M4_LOCK + M4_PERFECT + M4_FINAL_PUSH + M4_TRUE + M4_TOP + M4_CROWN2 + M4_LOCK2 + M4_FINAL + M4_LOCKED_TRUE + M4_EXACT
    m5 = M5_CONTENT + M5_BOOST + M5_ULTRA + M5_MEGA + M5_CROWN + M5_PASS + M5_LOCK + M5_PERFECT + M5_FINAL_PUSH + M5_TRUE + M5_TOP + M5_CROWN2 + M5_LOCK2 + M5_FINAL + M5_LOCKED_TRUE + M5_EXACT

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
        REVISION_EXACT
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
    execute_exact_pass()
