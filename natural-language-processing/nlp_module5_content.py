# Natural Language Processing Module 5 Exhaustive Content (10 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions & [UPLOADED PYQ]

NLP_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: NLP Applications, Dialogue Systems & AI Ethics — Complete 10-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 44:</strong> Text Classification (Document Categorization & Naive Bayes)</div>
    <div><strong>Topic 45:</strong> Sentiment Analysis (Document, Sentence & Aspect-Based)</div>
    <div><strong>Topic 46:</strong> Named Entity Recognition (NER Sequence Labeling vs. POS) [UPLOADED PYQ]</div>
    <div><strong>Topic 47:</strong> Machine Translation Overview & The Vauquois Triangle</div>
    <div><strong>Topic 48:</strong> Rule-Based Machine Translation (Direct, Transfer & Interlingua)</div>
    <div><strong>Topic 49:</strong> Statistical Machine Translation (SMT Noisy Channel Formulation)</div>
    <div><strong>Topic 50:</strong> Neural Machine Translation (End-to-End Transformer Seq2Seq)</div>
    <div><strong>Topic 51:</strong> Chatbots & Conversational Dialogue Systems (NLU-DM-NLG Pipeline)</div>
    <div><strong>Topic 52:</strong> Bias, Fairness & Stereotyping in Large Language Models</div>
    <div><strong>Topic 53:</strong> Model Explainability & Interpretability (Attention Heatmaps & LIME)</div>
  </div>
</div>

<h2 class="section-title">Topic 44 – 46: Text Classification, Sentiment Analysis & NER [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">Part-of-Speech (POS) Tagging</th>
      <th>Named Entity Recognition (NER) [UPLOADED PYQ — CS633]</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Objective</strong></td><td>Assigns syntactic grammatical word classes (`NN`, `VB`, `JJ`, `DT`).</td><td>Detects and classifies real-world semantic entity mentions.</td></tr>
    <tr><td><strong>Granularity</strong></td><td>Every single token in the sentence receives a tag.</td><td>Only specific entity spans receive labels (`PERSON`, `ORG`, `LOC`, `DATE`). Non-entities are tagged `O`.</td></tr>
    <tr><td><strong>Example</strong></td><td>`"Sundar [NNP] Pichai [NNP] leads [VBZ] Google [NNP]"`</td><td>`"Sundar Pichai [B-PER, I-PER] leads Google [B-ORG]"` (BIO tagging scheme).</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 47 – 50: Machine Translation (MT) Paradigm Evolution</h2>

<div class="diagram-container">
  <svg width="100%" height="80" viewBox="0 0 740 80" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="15" width="150" height="50" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="95" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">1. Rule-Based MT</text>
    <text x="95" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Dictionaries + Grammar</text>

    <path d="M 170 40 L 205 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="210" y="15" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="290" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">2. Statistical MT (SMT)</text>
    <text x="290" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#b45309" text-anchor="middle">Noisy Channel P(T|S)</text>

    <path d="M 370 40 L 405 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="410" y="15" width="180" height="50" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="500" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">3. Neural MT (NMT)</text>
    <text x="500" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Seq2Seq Transformer</text>

    <path d="M 590 40 L 625 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="630" y="15" width="95" height="50" rx="6" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="677" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#581c87" text-anchor="middle">4. LLMs</text>
    <text x="677" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#9333ea" text-anchor="middle">Zero-Shot MT</text>
  </svg>
  <div class="diagram-caption">Figure 5.1: The 70-Year Evolution of Machine Translation Paradigms</div>
</div>

<div class="formula-card">
  <strong>Statistical Machine Translation (Noisy Channel Model):</strong>
  $$\hat{T} = \arg\max_T P(T \mid S) = \arg\max_T \Big[ \underbrace{P(S \mid T)}_{\text{Translation Model (Fidelity)}} \times \underbrace{P(T)}_{\text{Language Model (Fluency)}} \Big]$$
</div>

<h2 class="section-title">Topic 51: Chatbots & Conversational Dialogue Architectures</h2>

<div class="callout callout-info">
  <div class="callout-title">The 3-Tier Task-Oriented Dialogue System Architecture</div>
  <ol>
    <li><strong>Natural Language Understanding (NLU):</strong> Converts user utterance into structured semantic frame: Intent Classification (e.g., `BookFlight`) + Slot Filling (e.g., `Origin: "Ranchi"`, `Destination: "Delhi"`).</li>
    <li><strong>Dialogue State Tracker (DST) & Policy Manager:</strong> Maintains conversation history state and selects the next system action (e.g., `AskDepartureDate` or `ExecuteBookingAPI`).</li>
    <li><strong>Natural Language Generation (NLG):</strong> Synthesizes natural, fluent response text from the structured action template.</li>
  </ol>
</div>

<h2 class="section-title">Topic 52 & 53: Ethics, Bias Mitigation & Model Explainability</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Ethical / Interpretability Challenge</th>
      <th style="width: 45%;">Manifestation in Language Models</th>
      <th>Engineering Mitigation Method</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Dataset & Representation Bias</strong></td>
      <td>Stereotypical associations in word embeddings (e.g., $\text{"doctor"} - \text{"man"} + \text{"woman"} \approx \text{"nurse"}$).</td>
      <td>Counterfactual data augmentation, debiasing projection subspaces.</td>
    </tr>
    <tr>
      <td><strong>2. Model Hallucination</strong></td>
      <td>Generating plausibly sounding but factually incorrect assertions with high confidence.</td>
      <td>Retrieval-Augmented Generation (RAG), RLHF with truthfulness reward models.</td>
    </tr>
    <tr>
      <td><strong>3. Black-Box Interpretability</strong></td>
      <td>Complex billions-parameter Transformer decisions cannot be audited for high-stakes healthcare/law.</td>
      <td><strong>LIME</strong> (Local Interpretable Model-agnostic Explanations), Integrated Gradients, Cross-Attention Heatmaps.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M5 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Compare Rule-Based, Statistical, and Neural Machine Translation systems across 4 dimensions. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Knowledge Representation:</strong> RBMT relies on explicit handwritten grammar rules and bilingual dictionaries; SMT uses phrase-based translation tables; NMT uses continuous distributed vector representations in a unified neural network.<br>
    2. <strong>Fluency & Context:</strong> RBMT produces robotic, literal translations; SMT handles local phrases well but struggles with long-distance reordering; NMT generates highly fluent translations with global sentence context.<br>
    3. <strong>Development Cost:</strong> RBMT requires decades of expert linguistic labor; SMT/NMT learn automatically from parallel sentence corpora.<br>
    4. <strong>Hardware Requirements:</strong> RBMT runs with low compute; NMT requires massive GPU accelerators for Transformer matrix multiplications.
  </div>
</div>
"""
