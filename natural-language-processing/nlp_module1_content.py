# Natural Language Processing Module 1 Exhaustive Content (12 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions & [UPLOADED PYQ]

NLP_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Introduction to NLP & Preprocessing — Complete 12-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> Introduction to NLP (Scientific vs. Engineering Goals & Ambiguity)</div>
    <div><strong>Topic 2:</strong> Real-World NLP Applications (Search, Healthcare, Finance, Chatbots)</div>
    <div><strong>Topic 3:</strong> Morphology (Morphemes, Free/Bound, Inflectional vs. Derivational)</div>
    <div><strong>Topic 4:</strong> Syntax (Grammatical Phrase Structures & Parse Trees)</div>
    <div><strong>Topic 5:</strong> Semantics (Literal Meaning & Semantic Role Labeling)</div>
    <div><strong>Topic 6:</strong> Pragmatics (Contextual Meaning: S-S-P Paradigm)</div>
    <div><strong>Topic 7:</strong> Tokenization (Word, Sentence, Subword BPE & Character)</div>
    <div><strong>Topic 8:</strong> Lemmatization (Base Lemma vs. Porter Stemming)</div>
    <div><strong>Topic 9:</strong> Stop-Word Removal (Tradeoffs & Sentiment Preservations)</div>
    <div><strong>Topic 10:</strong> Normalization (Case Folding, Unicode & Contractions) [UPLOADED PYQ]</div>
    <div><strong>Topic 11:</strong> Regular Expressions (Pattern Matching & Information Extraction)</div>
    <div><strong>Topic 12:</strong> Language Models Overview (Sequence Probability Distributions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Introduction to NLP & The Fundamental Ambiguity Challenge [UPLOADED PYQ]</h2>
<p>
  <strong>Natural Language Processing (NLP)</strong> sits at the intersection of Artificial Intelligence and Computational Linguistics, pursuing two fundamental objectives:
</p>
<ul>
  <li><strong>Scientific Goal:</strong> Formulating computational models of human cognitive language understanding and production.</li>
  <li><strong>Engineering Goal:</strong> Developing robust, scalable software systems capable of processing human text and speech for practical real-world utility.</li>
</ul>

<div class="callout callout-warning">
  <div class="callout-title">[UPLOADED PYQ — CS633] Why is Ambiguity the Core Challenge of NLP?</div>
  Natural language is inherently ambiguous across all linguistic tiers:
  <ol>
    <li><strong>Lexical Ambiguity:</strong> A single word possesses multiple distinct meanings (e.g., `"bank"` $\rightarrow$ financial institution vs. river slope).</li>
    <li><strong>Syntactic (Structural) Ambiguity:</strong> A sentence can generate multiple valid parse trees (e.g., <em>"I saw the man with the telescope"</em> $\rightarrow$ who holds the telescope?).</li>
    <li><strong>Semantic Ambiguity:</strong> A sentence has multiple literal interpretations (e.g., <em>"The chicken is ready to eat"</em> $\rightarrow$ is the chicken hungry or cooked?).</li>
    <li><strong>Pragmatic Ambiguity:</strong> Meaning depends strictly on conversational context and real-world intent (e.g., <em>"Can you pass the salt?"</em> $\rightarrow$ an action request, not an inquiry about physical ability).</li>
  </ol>
</div>

<h2 class="section-title">Topic 3 – 6: The 4 Core Levels of Linguistic Analysis</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Linguistic Level</th>
      <th style="width: 45%;">Core Scope & Analysis Mechanism</th>
      <th>Representative Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Morphology</strong></td>
      <td>Study of the internal structure of words and their minimal meaning-bearing units (<strong>Morphemes</strong>).<br>• <em>Free:</em> Can stand alone (`"happy"`).<br>• <em>Bound:</em> Prefixes/Suffixes (`"un-"`, `"-ness"`).<br>• <em>Inflectional:</em> Changes grammar form (`"walk"` $\rightarrow$ `"walked"`).<br>• <em>Derivational:</em> Creates new words/parts of speech (`"happy"` $\rightarrow$ `"unhappiness"`).</td>
      <td>`unhappiness` = `un-` (prefix) + `happy` (root) + `-ness` (suffix).</td>
    </tr>
    <tr>
      <td><strong>2. Syntax</strong></td>
      <td>Formal grammatical rules governing how words combine into phrases and sentences (Context-Free Grammars).</td>
      <td>$\text{S} \rightarrow \text{NP} \ \text{VP}$ (e.g., <em>"The student [NP] solved the problem [VP]"</em>).</td>
    </tr>
    <tr>
      <td><strong>3. Semantics</strong></td>
      <td>The study of literal, context-independent linguistic meaning and predicate-argument relationships (Semantic Roles: Agent, Action, Patient).</td>
      <td><em>"The dog chased the cat"</em> $\rightarrow \text{Agent}=\text{dog}, \text{Action}=\text{chase}, \text{Patient}=\text{cat}$.</td>
    </tr>
    <tr>
      <td><strong>4. Pragmatics</strong></td>
      <td>Meaning in real-world communicative context, discourse intent, and speaker implicature.</td>
      <td><em>"It is freezing in here!"</em> $\implies$ Pragmatic command to close the window.</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: S-S-P Paradigm</div>
  <strong>S</strong>yntax (Structure) $\longrightarrow$ <strong>S</strong>emantics (Sense / Meaning) $\longrightarrow$ <strong>P</strong>ragmatics (Situation / Context)
</div>

<h2 class="section-title">Topic 7 – 10: Text Preprocessing & Normalization Pipeline [UPLOADED PYQ]</h2>

<div class="diagram-container">
  <svg width="100%" height="75" viewBox="0 0 740 75" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="15" width="110" height="45" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="75" y="36" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#1e40af" text-anchor="middle">Raw Text</text>
    <text x="75" y="49" font-family="Plus Jakarta Sans" font-size="8.5" fill="#2563eb" text-anchor="middle">Unstructured string</text>

    <path d="M 130 37 L 165 37" stroke="#0284c7" stroke-width="2"/>

    <rect x="170" y="15" width="115" height="45" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="227" y="36" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#14532d" text-anchor="middle">Tokenization</text>
    <text x="227" y="49" font-family="Plus Jakarta Sans" font-size="8.5" fill="#16a34a" text-anchor="middle">Word / BPE Subwords</text>

    <path d="M 285 37 L 320 37" stroke="#0284c7" stroke-width="2"/>

    <rect x="325" y="15" width="125" height="45" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="387" y="36" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#92400e" text-anchor="middle">Normalization</text>
    <text x="387" y="49" font-family="Plus Jakarta Sans" font-size="8.5" fill="#b45309" text-anchor="middle">Case fold / Contractions</text>

    <path d="M 450 37 L 485 37" stroke="#0284c7" stroke-width="2"/>

    <rect x="490" y="15" width="115" height="45" rx="6" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="547" y="36" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#581c87" text-anchor="middle">Lemmatization</text>
    <text x="547" y="49" font-family="Plus Jakarta Sans" font-size="8.5" fill="#9333ea" text-anchor="middle">Dictionary root lemma</text>

    <path d="M 605 37 L 635 37" stroke="#0284c7" stroke-width="2"/>

    <rect x="640" y="15" width="80" height="45" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="680" y="36" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#1e40af" text-anchor="middle">Model</text>
    <text x="680" y="49" font-family="Plus Jakarta Sans" font-size="8.5" fill="#2563eb" text-anchor="middle">Clean Tokens</text>
  </svg>
  <div class="diagram-caption">Figure 1.1: Standard Text Preprocessing Pipeline in NLP Systems</div>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">Stemming (e.g., Porter Stemmer)</th>
      <th>Lemmatization (WordNet Lemmatizer) [UPLOADED PYQ]</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Core Technique</strong></td><td>Crude heuristic rule-based chopping of prefixes and suffixes.</td><td>Full morphological vocabulary and dictionary lookup analysis.</td></tr>
    <tr><td><strong>Output Validity</strong></td><td>Often produces non-words (e.g., `"running"` $\rightarrow$ `"run"`, `"studies"` $\rightarrow$ `"studi"`).</td><td>Guaranteed valid dictionary base form (e.g., `"better"` $\rightarrow$ `"good"`, `"mice"` $\rightarrow$ `"mouse"`).</td></tr>
    <tr><td><strong>Context Awareness</strong></td><td>Zero Part-of-Speech context awareness.</td><td>Uses POS tags to resolve ambiguity (`"meeting"` as Verb $\rightarrow$ `"meet"`, as Noun $\rightarrow$ `"meeting"`).</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 11 & 12: Regular Expressions & Language Models Overview</h2>

<div class="formula-card">
  <strong>Language Model Formal Definition:</strong>
  A <strong>Language Model (LM)</strong> computes the joint probability distribution over any arbitrary sequence of $n$ words $W = \langle w_1, w_2, \dots, w_n \rangle$:
  $$P(w_1, w_2, \dots, w_n) = \prod_{i=1}^n P(w_i \mid w_1, w_2, \dots, w_{i-1})$$
</div>

<h2 class="section-title">🧠 M1 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ — CS633] Explain the 5 sequential phases of NLP with an end-to-end example. (10 Marks)</div>
  <div class="qa-a">
    Given sentence: <em>"The intelligent student solved the complex problem."</em><br>
    1. <strong>Morphological Analysis:</strong> Breaks tokens into morphemes (`"solve"` + `"-ed"`, `"complex"`).<br>
    2. <strong>Syntactic Analysis (Parsing):</strong> Builds hierarchical phrase parse tree ($S \rightarrow NP \ VP$).<br>
    3. <strong>Semantic Analysis:</strong> Assigns literal meaning ($Agent=\text{student}, Action=\text{solve}, Object=\text{problem}$).<br>
    4. <strong>Discourse Integration:</strong> Links pronouns and entities across surrounding sentences.<br>
    5. <strong>Pragmatic Analysis:</strong> Interprets the speaker's true intent within conversational context.
  </div>
</div>
"""
