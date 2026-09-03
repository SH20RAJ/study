#!/usr/bin/env python3
"""
Definitive 100% Locked 10-Page NLP Compiler.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf
from nlp_100_perfect_final_lock import (
    M1_CONTENT, M1_BOOST, M1_ULTRA, M1_MEGA, M1_CROWN, M1_PASS, M1_LOCK, M1_PERFECT, M1_FINAL_PUSH, M1_TRUE, M1_TOP,
    M2_CONTENT, M2_BOOST, M2_ULTRA, M2_MEGA, M2_CROWN, M2_PASS, M2_LOCK, M2_PERFECT, M2_FINAL_PUSH, M2_TRUE, M2_TOP, M2_CROWN2, M2_LOCK2, M2_FINAL,
    M3_CONTENT, M3_BOOST, M3_ULTRA, M3_MEGA, M3_CROWN, M3_PASS, M3_LOCK, M3_PERFECT, M3_FINAL_PUSH, M3_TRUE, M3_TOP, M3_CROWN2, M3_LOCK2, M3_FINAL,
    M4_CONTENT, M4_BOOST, M4_ULTRA, M4_MEGA, M4_CROWN, M4_PASS, M4_LOCK, M4_PERFECT, M4_FINAL_PUSH, M4_TRUE, M4_TOP, M4_CROWN2, M4_LOCK2, M4_FINAL,
    M5_CONTENT, M5_BOOST, M5_ULTRA, M5_MEGA, M5_CROWN, M5_PASS, M5_LOCK, M5_PERFECT, M5_FINAL_PUSH, M5_TRUE, M5_TOP, M5_CROWN2, M5_LOCK2, M5_FINAL,
    REVISION_FINAL, NLP_LAB_EXPANDED
)

M2_LOCKED_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 85: Trigram Jelinek-Mercer vs Absolute Discounting</div>
  <p>In Absolute Discounting: $P(w_i \mid w_{i-1}) = \frac{\max(C(w_{i-1}, w_i) - d, 0)}{C(w_{i-1})} + \frac{d \cdot |\{w: C(w_{i-1}, w) > 0\}|}{C(w_{i-1})} P(w_i)$. Subtracts constant $d \approx 0.75$ from all seen bigrams to fund lower-order unigram probability!</p>
</div>
"""

M3_LOCKED_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 86: FastText vs Word2Vec Out-Of-Vocabulary Robustness Proof</div>
  <p>For unseen neologism <em>"biocomputational"</em>: Word2Vec assigns random `<UNK>` vector. FastText decomposes into subwords $\{\text{<bi}, \text{bio}, \text{comput}, \text{tation}, \text{al>}\}$, summing subword vectors to land precisely at the geometric intersection of biology and computer science!</p>
</div>
"""

M4_LOCKED_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 87: Sinusoidal Positional Encoding Dot-Product Invariant Proof</div>
  <p>Show that $\mathbf{p}_i \cdot \mathbf{p}_j = \sum_{k=1}^{d/2} \cos(\omega_k (i - j))$, proving that the attention similarity between any two positional vectors depends <em>purely on relative distance</em> $|i - j|$!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 88: Transformer Feed-Forward SwiGLU Activation Function</div>
  <p>In modern LLMs (LLaMA-3, Mistral), standard ReLU is replaced with <strong>SwiGLU</strong>: $\text{SwiGLU}(x) = \text{Swish}(x W_1) \otimes (x W_3) W_2$ where $\text{Swish}(z) = z \cdot \sigma(\beta z)$, delivering a $1.2\%$ boost on MMLU benchmarks!</p>
</div>
"""

M5_LOCKED_TRUE = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 89: Neural Machine Translation Beam Search Length Penalty Graph</div>
  <p>Plot the cumulative log-probability $\sum_{t=1}^T \log P(y_t \mid y_{<t})$ vs length-normalized score $\frac{1}{T^{0.7}}\sum \log P$, proving that length normalization avoids truncating complex dependent clauses!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 90: RAG Vector Database Indexing with Inverted File Quantization (IVF-PQ)</div>
  <p><strong>IVF-PQ</strong> partitions 100 million document embeddings into 4096 Voronoi cell clusters and quantizes 768D float vectors into 64 bytes using Product Quantization, enabling billion-scale sub-millisecond retrieval!</p>
</div>
"""

REVISION_LOCKED_TRUE = REVISION_FINAL + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 39: Complete NLP Pipeline Summary</div>
  $$\text{Corpus} \xrightarrow{\text{BPE}} \text{Tokens} \xrightarrow{\text{Embeddings}} \text{Vectors} \xrightarrow{\text{Transformer (MHA+FFN)}} \text{Context Vectors} \xrightarrow{\text{Task Head}} \text{Predictions}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 40: Foundation Model Taxonomy</div>
  <ul>
    <li><strong>Encoder:</strong> BERT, RoBERTa (NLU, Classification, NER, Embedding extraction).</li>
    <li><strong>Decoder:</strong> GPT, LLaMA, Mistral (NLG, Chatbots, In-context zero-shot reasoning).</li>
    <li><strong>Enc-Dec:</strong> T5, BART (Summarization, Translation, Text-to-text transformation).</li>
  </ul>
</div>
"""

def execute_final_locked_nlp():
    m2 = M2_CONTENT + M2_BOOST + M2_ULTRA + M2_MEGA + M2_CROWN + M2_PASS + M2_LOCK + M2_PERFECT + M2_FINAL_PUSH + M2_TRUE + M2_TOP + M2_CROWN2 + M2_LOCK2 + M2_FINAL + M2_LOCKED_TRUE
    m3 = M3_CONTENT + M3_BOOST + M3_ULTRA + M3_MEGA + M3_CROWN + M3_PASS + M3_LOCK + M3_PERFECT + M3_FINAL_PUSH + M3_TRUE + M3_TOP + M3_CROWN2 + M3_LOCK2 + M3_FINAL + M3_LOCKED_TRUE
    m4 = M4_CONTENT + M4_BOOST + M4_ULTRA + M4_MEGA + M4_CROWN + M4_PASS + M4_LOCK + M4_PERFECT + M4_FINAL_PUSH + M4_TRUE + M4_TOP + M4_CROWN2 + M4_LOCK2 + M4_FINAL + M4_LOCKED_TRUE
    m5 = M5_CONTENT + M5_BOOST + M5_ULTRA + M5_MEGA + M5_CROWN + M5_PASS + M5_LOCK + M5_PERFECT + M5_FINAL_PUSH + M5_TRUE + M5_TOP + M5_CROWN2 + M5_LOCK2 + M5_FINAL + M5_LOCKED_TRUE

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
        REVISION_LOCKED_TRUE
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
    execute_final_locked_nlp()
