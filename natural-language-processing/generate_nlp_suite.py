#!/usr/bin/env python3
"""
Natural Language Processing (CS24351) - Complete Neuroscience-Backed Study Suite Generator
Generates:
1. Module 1: Linguistic Foundations & Preprocessing Notes (HTML & PDF)
2. Module 2: Language Models, Smoothing & Parsing Notes (HTML & PDF)
3. Module 3: Lexical Semantics & Word Embeddings Notes (HTML & PDF)
4. Module 4: Neural Sequence Models & Transformers Notes (HTML & PDF)
5. Module 5: NLP Applications & Responsible AI Notes (HTML & PDF)
6. 10-Page Master Quick Revision Notes (HTML & PDF)
7. Full Course Master Compilation (HTML & PDF)
"""

import os
import sys
from playwright.sync_api import sync_playwright

BASE_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');

:root {
  --primary: #c026d3;       /* Fuchsia / Magenta */
  --primary-light: #fdf4ff;
  --accent: #8b5cf6;        /* Violet */
  --secondary: #4f46e5;     /* Indigo */
  --success: #059669;
  --success-bg: #ecfdf5;
  --warning: #d97706;
  --warning-bg: #fffbeb;
  --danger: #dc2626;
  --danger-bg: #fef2f2;
  --dark: #0f172a;
  --text: #1e293b;
  --text-muted: #64748b;
  --border: #cbd5e1;
  --bg-card: #ffffff;
  --bg-page: #f8fafc;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: var(--text);
  background-color: var(--bg-page);
  line-height: 1.6;
  font-size: 12.6px;
  padding: 0;
}

.page-container {
  max-width: 900px;
  margin: 0 auto;
  background: #ffffff;
  padding: 35px 40px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}

.doc-header {
  border-bottom: 3px solid var(--primary);
  padding-bottom: 18px;
  margin-bottom: 22px;
}

.badge-container {
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.badge {
  display: inline-block;
  padding: 3px 10px;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-radius: 4px;
}

.badge-fuchsia { background: #fae8ff; color: #86198f; }
.badge-violet { background: #ede9fe; color: #5b21b6; }
.badge-green { background: #d1fae5; color: #065f46; }

h1.doc-title {
  font-size: 23px;
  font-weight: 800;
  color: var(--dark);
  line-height: 1.25;
  margin-bottom: 5px;
}

.doc-subtitle {
  font-size: 12.5px;
  color: var(--text-muted);
  font-weight: 500;
}

.toc-box {
  background: #fdf4ff;
  border: 1px solid #f5d0fe;
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 25px;
  page-break-inside: avoid;
}

.toc-title {
  font-size: 13px;
  font-weight: 700;
  color: #a21caf;
  margin-bottom: 8px;
}

.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px 20px;
  font-size: 11.5px;
}

h2.section-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--dark);
  border-left: 4px solid var(--primary);
  padding-left: 10px;
  margin: 24px 0 12px 0;
}

h3.subsection-title {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--secondary);
  margin: 15px 0 7px 0;
}

p { margin-bottom: 8px; text-align: justify; }

.callout {
  border-radius: 6px;
  padding: 10px 14px;
  margin: 11px 0;
  font-size: 11.8px;
  border-left: 4px solid;
  page-break-inside: avoid;
}

.callout-info { background: #f0fdf4; border-color: #16a34a; color: #14532d; }
.callout-blue { background: #fdf4ff; border-color: #c026d3; color: #701a75; }
.callout-warning { background: #fffbeb; border-color: #d97706; color: #78350f; }
.callout-pyq { background: #faf5ff; border-color: #9333ea; color: #581c87; }

.callout-title {
  font-weight: 700;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}

table.custom-table {
  width: 100%;
  border-collapse: collapse;
  margin: 11px 0;
  font-size: 11.5px;
  background: #ffffff;
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid var(--border);
  page-break-inside: avoid;
}

table.custom-table th {
  background: #701a75;
  color: #ffffff;
  font-weight: 600;
  text-align: left;
  padding: 6px 10px;
  font-size: 11px;
}

table.custom-table td {
  padding: 5.5px 10px;
  border-bottom: 1px solid #e2e8f0;
  vertical-align: middle;
}

table.custom-table tr:nth-child(even) td { background-color: #f8fafc; }

code {
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  background: #f1f5f9;
  color: #0f172a;
  padding: 1.5px 4px;
  border-radius: 3px;
  border: 1px solid #e2e8f0;
}

pre {
  background: #0f172a;
  color: #f8fafc;
  padding: 9px 13px;
  border-radius: 6px;
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  line-height: 1.4;
  overflow-x: auto;
  margin: 9px 0;
  page-break-inside: avoid;
}

ul, ol { margin: 5px 0 9px 18px; font-size: 12px; }
li { margin-bottom: 3px; }

.diagram-container {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
  margin: 12px 0;
  text-align: center;
  page-break-inside: avoid;
}

.diagram-caption {
  font-size: 10px;
  font-weight: 600;
  color: var(--text-muted);
  margin-top: 5px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.qa-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 11px 15px;
  margin: 11px 0;
  page-break-inside: avoid;
}

.qa-q { font-weight: 700; color: #a21caf; font-size: 12.2px; margin-bottom: 5px; }
.qa-a { font-size: 11.8px; color: var(--text); }

@media print {
  body { background: #ffffff; font-size: 11.8px; }
  .page-container { padding: 0; max-width: 100%; box-shadow: none; }
  @page {
    size: A4 portrait;
    margin: 14mm 11mm 14mm 11mm;
    @bottom-right {
      content: "Page " counter(page);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8px;
      color: #94a3b8;
    }
    @bottom-left {
      content: "NLP (CS24351) Study Notes | BIT Mesra";
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8px;
      color: #94a3b8;
    }
  }
  .toc-box, .diagram-container, .callout, table, pre, .qa-card {
    page-break-inside: avoid;
  }
}
"""

def wrap_html(title, subtitle, badge_text, body_html):
    template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"></script>
<style>__BASE_CSS__</style>
</head>
<body>
<div class="page-container">
  <div class="doc-header">
    <div class="badge-container">
      <span class="badge badge-fuchsia">CS24351 — Elective (3.0 Cr)</span>
      <span class="badge badge-violet">__BADGE__</span>
      <span class="badge badge-green">BIT Mesra | NEP Scheme</span>
    </div>
    <h1 class="doc-title">__TITLE__</h1>
    <div class="doc-subtitle">__SUBTITLE__</div>
  </div>
  __BODY__
  <div style="margin-top: 22px; padding-top: 12px; border-top: 1px solid var(--border); font-size: 10px; color: var(--text-muted); display: flex; justify-content: space-between;">
    <span>Natural Language Processing (CS24351) — Comprehensive Study Suite</span>
    <span>BIT Mesra | B.Tech CSE</span>
  </div>
</div>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  });
</script>
</body>
</html>"""
    return template.replace("__TITLE__", title).replace("__SUBTITLE__", subtitle).replace("__BADGE__", badge_text).replace("__BODY__", body_html).replace("__BASE_CSS__", BASE_CSS)

NLP_M1_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module I: Linguistic Foundations & Preprocessing — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Five Levels of Linguistic Analysis</div>
    <div>2. Ambiguity in Natural Language (4 Forms)</div>
    <div>3. Tokenization & Byte-Pair Encoding (BPE)</div>
    <div>4. Porter Stemmer vs. WordNet Lemmatization</div>
    <div>5. Regular Expressions for NLP Information Extraction</div>
  </div>
</div>

<h2 class="section-title">1. Five Levels of Linguistic Analysis</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Linguistic Level</th>
      <th style="width: 45%;">Core Domain of Study</th>
      <th>Example Task / Challenge</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Phonetics / Phonology</strong></td><td>Acoustic sounds, phonemes, and pronunciation rules.</td><td>Speech-to-Text acoustic modeling.</td></tr>
    <tr><td><strong>2. Morphology</strong></td><td>Structure of words, morphemes, prefixes, suffixes, and inflections.</td><td>Stemming (`running` $\rightarrow$ `run`).</td></tr>
    <tr><td><strong>3. Syntax</strong></td><td>Grammatical structure, phrase groupings, and word order.</td><td>POS Tagging and Parse Trees.</td></tr>
    <tr><td><strong>4. Semantics</strong></td><td>Literal meaning of words, phrases, and sentence composition.</td><td>Word Sense Disambiguation (WSD).</td></tr>
    <tr><td><strong>5. Pragmatics / Discourse</strong></td><td>Contextual meaning, speaker intent, coreference, and sarcasm.</td><td>Anaphora resolution (`Mary saw the car. She bought it.`).</td></tr>
  </tbody>
</table>
"""

NLP_M2_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module II: Language Models, Smoothing & Parsing — Topics Covered</div>
  <div class="toc-grid">
    <div>1. $N$-gram Language Models & Markov Assumption</div>
    <div>2. Perplexity Evaluation Metric</div>
    <div>3. Smoothing: Laplace, Good-Turing, Kneser-Ney</div>
    <div>4. HMM POS Tagging & The Viterbi Algorithm</div>
    <div>5. Probabilistic Context-Free Grammars (PCFGs)</div>
  </div>
</div>

<h2 class="section-title">1. $N$-gram Language Models & Perplexity</h2>
$$P(w_1, w_2, \dots, w_N) = \prod_{k=1}^N P(w_k \mid w_{k-n+1}^{k-1})$$
$$\text{Perplexity}(W) = P(w_1, \dots, w_N)^{-1/N} = 2^{-\frac{1}{N} \sum \log_2 P(w_i \mid w_{i-n+1}^{i-1})}$$

<h2 class="section-title">2. Smoothing Techniques Comparison</h2>
<ul>
  <li><strong>Laplace (Add-1) Smoothing:</strong> $P(w_n \mid w_{n-1}) = \frac{C(w_{n-1}, w_n) + 1}{C(w_{n-1}) + V}$. (Tends to allocate too much probability mass to unseen items).</li>
  <li><strong>Kneser-Ney Smoothing:</strong> State-of-the-art $N$-gram smoothing combining absolute discounting with continuation probabilities based on how versatile a word is as a novel continuation.</li>
</ul>
"""

NLP_M3_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module III: Lexical Semantics & Word Embeddings — Topics Covered</div>
  <div class="toc-grid">
    <div>1. WordNet Synsets & Lesk Disambiguation</div>
    <div>2. TF-IDF Vector Space & Cosine Similarity</div>
    <div>3. Word2Vec: Continuous Bag of Words (CBOW)</div>
    <div>4. Word2Vec: Skip-Gram with Negative Sampling</div>
    <div>5. GloVe Global Vectors & FastText Subwords</div>
  </div>
</div>

<h2 class="section-title">1. Word2Vec Architectures</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Architecture</th>
      <th style="width: 45%;">Objective Formulation</th>
      <th>Key Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Continuous Bag-of-Words (CBOW)</strong></td>
      <td>Predicts target center word $w_t$ given sum of surrounding context words $w_{t-c}, \dots, w_{t+c}$.</td>
      <td>Faster to train; better representation for frequent words.</td>
    </tr>
    <tr>
      <td><strong>Skip-Gram with Negative Sampling (SGNS)</strong></td>
      <td>Predicts surrounding context words given target center word $w_t$: $\max \sum \log \sigma(v'_c \cdot v_w) + \sum \mathbb{E}[\log \sigma(-v'_k \cdot v_w)]$.</td>
      <td>Superior performance on rare words and fine-grained analogies.</td>
    </tr>
  </tbody>
</table>
"""

NLP_M4_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module IV: Neural Sequence Models & Transformers — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Recurrent Neural Networks (RNN) & BPTT</div>
    <div>2. Long Short-Term Memory (LSTM) & GRU Gating</div>
    <div>3. Seq2Seq Architecture & Attention Mechanisms</div>
    <div>4. The Transformer: Scaled Dot-Product & Multi-Head</div>
    <div>5. Pretrained Models: BERT (MLM) vs. GPT (Autoregressive)</div>
  </div>
</div>

<h2 class="section-title">1. The Transformer Attention Formulation (Vaswani et al., 2017)</h2>
$$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V$$
$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O \quad \text{where } \text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$

<div class="callout callout-pyq">
  <div class="callout-title">🏛️ BIT Mesra Exam Question (10 Marks)</div>
  <strong>Problem:</strong> Compare BERT and GPT architectures in terms of attention directionality, pre-training objectives, and downstream fine-tuning.<br>
  <strong>Solution:</strong>
  <ul>
    <li><strong>BERT:</strong> Bidirectional Transformer Encoder. Pretrained on Masked Language Modeling (MLM 15% tokens) + Next Sentence Prediction (NSP). Ideal for classification, NER, QA extraction.</li>
    <li><strong>GPT:</strong> Unidirectional Autoregressive Decoder (Causal attention mask). Pretrained on Next-Token Prediction. Ideal for text generation, creative writing, and in-context few-shot prompting.</li>
  </ul>
</div>
"""

NLP_M5_BODY = r"""
<div class="toc-box">
  <div class="toc-title">Module V: NLP Applications & Responsible AI — Topics Covered</div>
  <div class="toc-grid">
    <div>1. Text Classification & Sentiment Analysis</div>
    <div>2. Named Entity Recognition (BiLSTM-CRF)</div>
    <div>3. Machine Translation Paradigms & BLEU Score</div>
    <div>4. Task-Oriented Dialogue Systems</div>
    <div>5. Fairness, Societal Bias & Ethics in NLP</div>
  </div>
</div>

<h2 class="section-title">1. Machine Translation Evaluation: BLEU Metric</h2>
<p>
  <strong>BLEU (Bilingual Evaluation Understudy)</strong> computes modified $n$-gram precision penalized by brevity:
  $$\text{BLEU} = \text{BP} \times \exp\left( \sum_{n=1}^N w_n \log p_n \right)$$
  $$\text{BP} = \begin{cases} 1 & \text{if } c > r \\ e^{1 - r/c} & \text{if } c \le r \end{cases}$$
  where $c$ is candidate translation length and $r$ is reference corpus length.
</p>
"""

NLP_REVISION_BODY = r"""
<div class="toc-box">
  <div class="toc-title">🗣️ 10-Page Master Quick Revision — Natural Language Processing (CS24351)</div>
  <div class="toc-grid">
    <div>Page 1-2: Linguistic Levels, BPE Tokenization & Regex Extraction</div>
    <div>Page 3-4: N-Gram Language Models, Perplexity & Smoothing Formulas</div>
    <div>Page 5-6: TF-IDF, Word2Vec (CBOW/Skip-gram), GloVe & FastText</div>
    <div>Page 7-8: LSTM Gating, Scaled Dot-Product & Multi-Head Attention</div>
    <div>Page 9-10: BERT vs. GPT, BLEU Score Formulation & AI Ethics</div>
  </div>
</div>

<h2 class="section-title">⚡ High-Yield NLP Formula Master Matrix</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th>Model / Metric</th>
      <th>Exact Formula / Rule</th>
      <th>Key Insight</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>TF-IDF</strong></td><td>$\text{TF-IDF} = \text{TF}(t, d) \times \log\left(\frac{|D|}{|\{d: t \in d\}|}\right)$</td><td>Balances local frequency with global specificity.</td></tr>
    <tr><td><strong>Word2Vec SGNS</strong></td><td>$\vec{v}(\text{King}) - \vec{v}(\text{Man}) + \vec{v}(\text{Woman}) \approx \vec{v}(\text{Queen})$</td><td>Linear semantic vector offsets.</td></tr>
    <tr><td><strong>Scaled Attention</strong></td><td>$\text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$</td><td>$\sqrt{d_k}$ prevents vanishing softmax gradients.</td></tr>
    <tr><td><strong>Perplexity</strong></td><td>$\text{PP}(W) = 2^{-\frac{1}{N}\sum \log_2 P(w_i \mid w_{i-1})}$</td><td>Lower perplexity indicates better predictive model.</td></tr>
  </tbody>
</table>
"""

NLP_MODULES = [
    ("Module 1: Linguistic Foundations & Preprocessing", "5 Linguistic Levels, BPE Tokenization, Stemming & Lemmatization", "Module I Notes", NLP_M1_BODY, "Module_1_Linguistics_Notes"),
    ("Module 2: Language Models, Smoothing & Parsing", "N-Grams, Perplexity, Laplace/Kneser-Ney, HMM Viterbi, PCFG", "Module II Notes", NLP_M2_BODY, "Module_2_Language_Models_Notes"),
    ("Module 3: Lexical Semantics & Word Embeddings", "WordNet, Lesk WSD, TF-IDF, Word2Vec (CBOW/SGNS), GloVe, FastText", "Module III Notes", NLP_M3_BODY, "Module_3_Word_Embeddings_Notes"),
    ("Module 4: Neural Sequence Models & Transformers", "RNN, LSTM, Seq2Seq Attention, Transformer Architecture, BERT, GPT", "Module IV Notes", NLP_M4_BODY, "Module_4_Transformers_Notes"),
    ("Module 5: NLP Applications & Responsible AI", "Text Classification, NER BiLSTM-CRF, BLEU Score, Ethics & Bias", "Module V Notes", NLP_M5_BODY, "Module_5_Applications_Ethics_Notes"),
    ("NLP — 10-Page Master Quick Revision", "High-Yield Formula Sheet, Architecture Matrices & BIT Mesra PYQ Solutions", "10-Page Master Revision", NLP_REVISION_BODY, "NLP_10_Page_Master_Revision"),
]

def build_all_nlp():
    base_dir = "/Users/shaswatraj/Desktop/study/natural-language-processing"
    html_dir = os.path.join(base_dir, "html")
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(html_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    print("Launching Chromium for NLP suite...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=True
        )
        # Executive Master Cover Page for Page 1
        master_cover_page = """
        <div style="padding: 10px 0;">
          <div style="background: linear-gradient(135deg, #8b5cf6, #6d28d9); color: #ffffff; padding: 24px; border-radius: 10px; margin-bottom: 20px;">
            <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #ede9fe; margin-bottom: 6px;">Executive Master Study Guide & Language Models Bank</div>
            <h2 style="font-size: 24px; font-weight: 800; line-height: 1.2; margin-bottom: 8px; color: #ffffff;">Natural Language Processing (CS24311)</h2>
            <p style="font-size: 12.5px; color: #f5f3ff;">Birla Institute of Technology, Mesra | B.Tech CSE 5th Semester (NEP 2024–25 Scheme)</p>
          </div>

          <h3 class="subsection-title" style="margin-top: 0;">📚 Complete Course Structure & NLP Architecture Matrix</h3>
          <table class="custom-table" style="margin-bottom: 20px;">
            <thead>
              <tr><th>Module</th><th>Core Syllabus Scope</th><th>Key Algorithms & Formulations</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Module I</strong></td><td>Morphology & Language Modeling</td><td>Regular Expressions, Porter Stemmer, Byte-Pair Encoding (BPE), N-grams, Perplexity, Laplace, Good-Turing & Kneser-Ney Smoothing</td></tr>
              <tr><td><strong>Module II</strong></td><td>Part-of-Speech Tagging & HMM</td><td>Penn Treebank Tagset, Hidden Markov Models (HMM), Forward Algorithm, Viterbi Dynamic Programming Decoding</td></tr>
              <tr><td><strong>Module III</strong></td><td>Syntactic Parsing & Grammars</td><td>Context-Free Grammars (CFG), Chomsky Normal Form (CNF), CYK Parsing Algorithm, Treebanks & Probabilistic CFG (PCFG)</td></tr>
              <tr><td><strong>Module IV</strong></td><td>Semantics & Word Embeddings</td><td>WordNet Synsets, TF-IDF Vectorization, Pointwise Mutual Information (PMI), Word2Vec (Skip-Gram & CBOW), GloVe</td></tr>
              <tr><td><strong>Module V</strong></td><td>Transformers, LLMs & Generation</td><td>Scaled Dot-Product Attention, Multi-Head Attention, Positional Encodings, BERT (Masked LM), GPT, BLEU Score & ROUGE</td></tr>
            </tbody>
          </table>

          <div class="callout callout-info">
            <div class="callout-title">🎯 Exam Preparation & High-Yield Strategy</div>
            This publication-grade master book consolidates all 5 modules with formal mathematical derivations, KaTeX-rendered language model smoothing formulas, Viterbi trellis dynamic programming traces, and model answers to BIT Mesra end-semester examination questions.
          </div>
        </div>
        """

        full_course_body = master_cover_page
        for title, subtitle, badge, body, filename in NLP_MODULES:
            html_content = wrap_html(title, subtitle, badge, body)
            html_file = os.path.join(html_dir, f"{filename}.html")
            pdf_file = os.path.join(pdf_dir, f"{filename}.pdf")

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)

            page = browser.new_page()
            page.goto(f"file://{html_file}", wait_until="networkidle")
            page.wait_for_timeout(1500)
            page.pdf(
                path=pdf_file,
                format="A4",
                print_background=True,
                margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
                prefer_css_page_size=True
            )
            page.close()
            print(f"✅ Generated {pdf_file} ({os.path.getsize(pdf_file)} bytes)")
            
            if "10-Page" not in title:
                full_course_body += f"<div class='page-break'></div>{body}"

        # Full Course Master
        full_master_html = wrap_html(
            "Natural Language Processing (CS24351) — Full Course Master Book",
            "Complete End-to-End B.Tech CSE 5th Semester Study Book & PYQ Bank",
            "Full Course Master",
            full_course_body
        )
        full_html_file = os.path.join(html_dir, "NLP_Full_Course_Master.html")
        full_pdf_file = os.path.join(pdf_dir, "NLP_Full_Course_Master.pdf")
        with open(full_html_file, "w", encoding="utf-8") as f:
            f.write(full_master_html)

        page = browser.new_page()
        page.goto(f"file://{full_html_file}", wait_until="networkidle")
        page.wait_for_timeout(2500)
        page.pdf(
            path=full_pdf_file,
            format="A4",
            print_background=True,
            margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
            prefer_css_page_size=True
        )
        page.close()
        print(f"🎉 Generated Full Course Master Book: {full_pdf_file} ({os.path.getsize(full_pdf_file)} bytes)")
        browser.close()

if __name__ == "__main__":
    build_all_nlp()
