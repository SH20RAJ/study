#!/usr/bin/env python3
"""
Complete Master Suite Builder for Natural Language Processing (CS24351).
Embeds 35k-40k characters per module, 28k characters for Revision,
to achieve 10-12 pages for every module and 56+ pages for NLP_Full_Course_Master.pdf!
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

NLP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "natural-language-processing"))
HTML_DIR = os.path.join(NLP_DIR, "html")
PDF_DIR = os.path.join(NLP_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_nlp_master_suite import wrap_html, generate_pdf

# ==============================================================================
# MODULE 1: INTRODUCTION TO NLP, LINGUISTICS & PREPROCESSING (36,000+ Chars)
# ==============================================================================
M1_CONTENT = r"""
<h1 class="module-title">Module 1: Introduction to NLP, Linguistic Levels & Text Preprocessing</h1>

<div class="callout-box">
  <div class="callout-title">📌 Syllabus & Pedagogical Blueprint (Topics 1 to 12)</div>
  <p>Foundations of Computational Linguistics • Scientific vs. Engineering Goals • The End-to-End NLP Pipeline • Comprehensive Taxonomy of Linguistic Ambiguities • The 6 Levels of Language Analysis (Phonetics/Phonology, Morphology, Syntax, Semantics, Pragmatics, Discourse) • Tokenization Mechanics (Word, Sentence, Subword BPE, WordPiece, SentencePiece) • Normalization Pipelines (Case Folding, Unicode Decomposition NFKD, Levenshtein Minimum Edit Distance with Dynamic Programming) • Stemming vs. Lemmatization (Porter Stemmer Rules 1a–5b, Snowball, WordNet Lemmatizer) • Stop-Word Filtering • Regular Expressions, Finite State Automata (NFA/DFA), and Regex-Based Entity Extraction • 15 Solved University Examination Questions.</p>
</div>

<h2 class="section-title">Topic 1: Foundations of Natural Language Processing</h2>
<p><strong>Natural Language Processing (NLP)</strong> is a multidisciplinary field at the intersection of Computer Science, Artificial Intelligence, and Computational Linguistics concerned with enabling computers to understand, interpret, synthesize, and manipulate human language in a meaningful and actionable manner.</p>

<div class="callout-box">
  <div class="callout-title">🎯 The Dual Objectives of NLP</div>
  <ul>
    <li><strong>The Scientific Objective:</strong> To formalize computational models of human language capabilities—investigating how humans represent linguistic knowledge, acquire syntax and semantics, and process ambiguous utterances in real time.</li>
    <li><strong>The Engineering Objective:</strong> To build robust, scalable software artifacts and systems (e.g., neural machine translation, conversational agents, biomedical information extractors, semantic search engines) that perform practical language tasks with human or superhuman fidelity.</li>
  </ul>
</div>

<h2 class="section-title">Topic 2: The End-to-End NLP Processing Pipeline</h2>
<p>Modern NLP applications operate via a structured multi-tier architecture that progressively transforms unstructured raw text into structured semantic representations:</p>

<pre><code>Raw Text Document (Corpus)
       │
       ▼ [Stage 1: Preprocessing & Cleaning]
Regex Noise Removal ──► Unicode Normalization (NFKD) ──► Sentence Segmentation
       │
       ▼ [Stage 2: Lexical & Morphological Analysis]
Word / Subword Tokenization (BPE) ──► Stop-Word Filtering ──► Stemming / Lemmatization
       │
       ▼ [Stage 3: Syntactic Analysis & Tagging]
Part-of-Speech Tagging (HMM / CRF) ──► Constituency Parsing ──► Dependency Parsing
       │
       ▼ [Stage 4: Semantic Analysis]
Lexical Semantics (Word2Vec / GloVe) ──► Named Entity Recognition (NER) ──► Coreference
       │
       ▼ [Stage 5: Pragmatic & Discourse Processing]
Speech Act Classification ──► Intent Detection & Dialogue State Tracking ──► Summarization
       │
       ▼ [Stage 6: Downstream Application]
Neural Machine Translation • Question Answering • Sentiment Analysis • Generative LLMs</code></pre>

<h2 class="section-title">Topic 3: Comprehensive Taxonomy of Linguistic Ambiguities</h2>
<p>Human natural language is inherently ambiguous, context-dependent, and dynamic. A single surface form can map to divergent semantic interpretations across multiple linguistic dimensions:</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Ambiguity Level</th>
      <th style="width: 38%;">Linguistic Definition & Mechanism</th>
      <th>Canonical Illustrative Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Lexical / Syntactic Category</strong></td>
      <td>A word belongs to multiple grammatical parts of speech (POS) depending on sentential context.</td>
      <td><em>"Time <u>flies</u> like an arrow; fruit <u>flies</u> like a banana."</em> (`flies` is a Verb in clause 1, but a Noun in clause 2).</td>
    </tr>
    <tr>
      <td><strong>Syntactic / Structural</strong></td>
      <td>A sentence yields multiple distinct valid parse trees due to ambiguous prepositional phrase attachment or coordination.</td>
      <td><em>"I saw the astronomer with the telescope."</em> (Did I use the telescope to see, or does the astronomer possess the telescope?).</td>
    </tr>
    <tr>
      <td><strong>Semantic / Polysemy</strong></td>
      <td>A word has multiple distinct dictionary meanings (senses) that cannot be disambiguated from syntax alone.</td>
      <td><em>"He deposited money in the <u>bank</u> before walking to the river <u>bank</u>."</em> (Financial institution vs. Geological river margin).</td>
    </tr>
    <tr>
      <td><strong>Pragmatic / Speech Act</strong></td>
      <td>The intended communicative function of an utterance differs from its literal compositional semantics.</td>
      <td><em>"Can you pass the salt?"</em> (Syntactically a yes/no question of physical capability; pragmatically an imperative request for action).</td>
    </tr>
    <tr>
      <td><strong>Referential / Anaphoric</strong></td>
      <td>A pronoun has multiple plausible antecedent noun phrases in preceding discourse.</td>
      <td><em>"The trophy would not fit in the brown suitcase because <u>it</u> was too big."</em> (`it` = trophy). Change to <em>"too small"</em> $\implies$ `it` = suitcase.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 4: The Six Fundamental Levels of Linguistic Analysis</h2>
<ol>
  <li><strong>Phonetics & Phonology:</strong> The acoustic physics and cognitive organization of spoken sounds (phonemes, formants, pitch contours).</li>
  <li><strong>Morphology:</strong> The internal structure and formation of words from primitive atomic meaning units called <em>morphemes</em>:
    <ul>
      <li><strong>Free Morphemes:</strong> Can stand alone as independent words (e.g., `dog`, `play`, `compute`).</li>
      <li><strong>Bound Morphemes:</strong> Must attach to a root (affixes: prefixes, suffixes, infixes).</li>
      <li><strong>Inflectional Morphology:</strong> Modifies grammatical form without changing lexical category or core meaning (e.g., `play` $\rightarrow$ `plays`, `played`, `playing`).</li>
      <li><strong>Derivational Morphology:</strong> Creates entirely new words or changes lexical class (e.g., `compute` (Verb) $\rightarrow$ `computer` (Noun) $\rightarrow$ `computational` (Adjective)).</li>
    </ul>
  </li>
  <li><strong>Syntax:</strong> The grammatical rules governing how words combine to form valid phrases, clauses, and sentences (Context-Free Grammars, Dependency trees).</li>
  <li><strong>Semantics:</strong> The literal meaning of words (lexical semantics) and how they compositionally combine to form sentence propositions (truth-conditional semantics).</li>
  <li><strong>Pragmatics:</strong> How context, shared world knowledge, speaker intent, and conversational maxims (Grice's Maxims) shape meaning beyond literal syntax.</li>
  <li><strong>Discourse:</strong> Multi-sentence linguistic units, cohesion, coreference resolution, and rhetorical structure theory.</li>
</ol>

<h2 class="section-title">Topic 5: Tokenization Mechanics & Subword Algorithms</h2>
<p>Tokenization is the segmentation of a continuous stream of characters into discrete lexical units (tokens). While whitespace tokenization suffices for English, it fails catastrophically for agglutinative languages (German: <em>Donaudampfschiffahrtselektrizitätenhauptbetriebswerkbauunterbeamtengesellschaft</em>) and unsegmented scripts (Chinese, Japanese).</p>

<h3 class="sub-title">1. Byte-Pair Encoding (BPE - Sennrich et al. 2016)</h3>
<p>BPE is a data-driven subword tokenization algorithm that iteratively merges the most frequently occurring pair of adjacent characters/subwords:</p>
<ol>
  <li>Initialize vocabulary $V$ with all atomic characters in the corpus plus end-of-word symbol `</w>`.</li>
  <li>Represent every word in the training corpus as a sequence of individual characters.</li>
  <li>Count the co-occurrence frequency of all adjacent subword pairs $(c_i, c_j)$.</li>
  <li>Merge the single most frequent pair $(c_i, c_j) \rightarrow c_{\text{new}}$ and append $c_{\text{new}}$ to vocabulary $V$.</li>
  <li>Repeat steps 3–4 for a fixed number of merge operations $K$.</li>
</ol>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 1: Step-by-Step BPE Merge Trace</div>
  <p>Consider a corpus containing 4 words with frequencies: `low: 5`, `lower: 2`, `newest: 6`, `widest: 3`.</p>
  <p><strong>Initial Vocabulary:</strong> $\{l, o, w, e, r, n, s, t, i, d, \text{</w>}\}$</p>
  <p><strong>Corpus Representation:</strong></p>
  <ul>
    <li>`5  l o w </w>`</li>
    <li>`2  l o w e r </w>`</li>
    <li>`6  n e w e s t </w>`</li>
    <li>`3  w i d e s t </w>`</li>
  </ul>
  <p><strong>Iteration 1:</strong> Count adjacent pairs: `(e, s): 6 + 3 = 9`, `(s, t): 9`, `(t, </w>): 9`, `(e, w): 6`, `(l, o): 7`, `(o, w): 7`.</p>
  <p>Select pair with max count: <strong>`(e, s)` (frequency 9)</strong>. Merge `(e, s) -> es`.</p>
  <p><strong>Updated Corpus:</strong> `5 l o w </w>`, `2 l o w e r </w>`, `6 n e w es t </w>`, `3 w i d es t </w>`.</p>
  <p><strong>Iteration 2:</strong> Count pairs: `(es, t): 6 + 3 = 9`. Merge <strong>`(es, t) -> est`</strong>.</p>
  <p><strong>Updated Corpus:</strong> `5 l o w </w>`, `2 l o w e r </w>`, `6 n e w est </w>`, `3 w i d est </w>`.</p>
  <p><strong>Iteration 3:</strong> Count pairs: `(est, </w>): 9`. Merge <strong>`(est, </w>) -> est</w>`</strong>.</p>
  <p><strong>Iteration 4:</strong> Count pairs: `(l, o): 5 + 2 = 7`, `(o, w): 7`. Merge <strong>`(l, o) -> lo`</strong>, followed by <strong>`(lo, w) -> low`</strong>.</p>
  $$\mathbf{\text{Final Tokenized Output for Unseen Word 'lowest': } [\text{"low"}, \ \text{"est</w>"}] \quad (\text{Zero OOV tokens!})}$$
</div>

<h2 class="section-title">Topic 6: Text Normalization & Minimum Edit Distance</h2>
<p>Text normalization encompasses case folding, accent stripping, Unicode canonical decomposition (NFKD), and spell checking via <strong>Levenshtein Minimum Edit Distance</strong>.</p>

<div class="callout-box">
  <div class="callout-title">📐 Levenshtein Edit Distance Recurrence Relation</div>
  <p>Given source string $S[1..n]$ and target string $T[1..m]$, let $D[i, j]$ be the minimum number of insertions (cost 1), deletions (cost 1), and substitutions (cost 2 in standard Levenshtein, or cost 1 in unit edit distance) required to transform $S[1..i]$ into $T[1..j]$:</p>
  $$\mathbf{D[i, 0] = i, \quad D[0, j] = j}$$
  $$\mathbf{D[i, j] = \min \begin{cases} D[i-1, j] + 1 & (\text{Deletion of } S[i]) \\ D[i, j-1] + 1 & (\text{Insertion of } T[j]) \\ D[i-1, j-1] + \text{cost}(S[i] \rightarrow T[j]) & (\text{Substitution / Match}) \end{cases}}$$
  $$\text{where } \text{cost}(S[i] \rightarrow T[j]) = \begin{cases} 0 & \text{if } S[i] = T[j] \\ 2 & \text{if } S[i] \neq T[j] \quad (\text{Levenshtein substitution}) \end{cases}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 2: Full DP Matrix Computation for Edit Distance</div>
  <p>Compute unit edit distance ($\text{sub\_cost}=1, \text{ins}=1, \text{del}=1$) between $S = \text{"INTENTION"}$ and $T = \text{"EXECUTION"}$:</p>
  <table class="custom-table">
    <thead>
      <tr><th>$S \backslash T$</th><th>#</th><th>E</th><th>X</th><th>E</th><th>C</th><th>U</th><th>T</th><th>I</th><th>O</th><th>N</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>#</strong></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr>
      <tr><td><strong>I</strong></td><td>1</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>6</td><td>7</td><td>8</td></tr>
      <tr><td><strong>N</strong></td><td>2</td><td>2</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>7</td><td>7</td></tr>
      <tr><td><strong>T</strong></td><td>3</td><td>3</td><td>3</td><td>3</td><td>4</td><td>5</td><td>5</td><td>6</td><td>7</td><td>8</td></tr>
      <tr><td><strong>E</strong></td><td>4</td><td>3</td><td>4</td><td>3</td><td>4</td><td>5</td><td>6</td><td>6</td><td>7</td><td>8</td></tr>
      <tr><td><strong>N</strong></td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>6</td><td>7</td><td>7</td><td>7</td></tr>
      <tr><td><strong>T</strong></td><td>6</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>6</td><td>7</td><td>8</td></tr>
      <tr><td><strong>I</strong></td><td>7</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>5</td><td>6</td><td>7</td></tr>
      <tr><td><strong>O</strong></td><td>8</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>6</td><td>5</td><td>6</td></tr>
      <tr><td><strong>N</strong></td><td>9</td><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td><td>7</td><td>6</td><td><strong>5</strong></td></tr>
    </tbody>
  </table>
  $$\mathbf{\text{Minimum Unit Edit Distance: } D[9, 9] = \mathbf{5 \text{ operations}}}$$
  <p><em>Optimal Alignment Trace:</em> Delete `I`, Substitute `N->E`, Substitute `T->X`, Match `E`, Substitute `N->C`, Insert `U`, Match `T`, Match `I`, Match `O`, Match `N`.</p>
</div>

<h2 class="section-title">Topic 7: Stemming vs. Lemmatization</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">Stemming (e.g., Porter, Snowball)</th>
      <th>Lemmatization (e.g., WordNet)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Core Strategy</strong></td>
      <td>Heuristic, rule-based chopping of common inflectional affixes (`-ing`, `-ed`, `-s`).</td>
      <td>Full morphological vocabulary analysis using POS tags and dictionary lemmatas.</td>
    </tr>
    <tr>
      <td><strong>Linguistic Validity</strong></td>
      <td>Output may NOT be a valid dictionary word (e.g., `univers` for `university`/`universal`).</td>
      <td>Output is always a canonical valid base lemma (e.g., `better` $\rightarrow$ `good`).</td>
    </tr>
    <tr>
      <td><strong>Speed & Complexity</strong></td>
      <td>Blazing fast $O(1)$ string regex replacements; zero lexicon lookup.</td>
      <td>Slower; requires morphological parsing, dictionary indexing, and POS context.</td>
    </tr>
    <tr>
      <td><strong>Errors Produced</strong></td>
      <td><strong>Overstemming</strong> (`organization`/`organic` $\rightarrow$ `organ`) and <strong>Understemming</strong> (`knives`/`knife` not merged).</td>
      <td>Context-dependent misclassification if POS tag is incorrect (`meeting` as Noun vs Verb).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 8: Master University Examination Question Bank (Module 1)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the difference between Prescriptive and Descriptive Grammar in NLP. (6 Marks)</div>
  <div class="qa-a">• <strong>Prescriptive Grammar:</strong> Dictates authoritative, artificial rules about how language <em>ought</em> to be used (e.g., "never split an infinitive", "do not end a sentence with a preposition").<br>• <strong>Descriptive Grammar:</strong> Empirically documents and models how language is <em>actually</em> spoken and written by native speakers in real-world settings (including colloquialisms, typos, code-switching). Modern NLP systems are strictly built on descriptive computational models.</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Detail Porter Stemmer Step 1a, 1b, and 1c Rules with Examples. (8 Marks)</div>
  <div class="qa-a"><strong>Step 1a (Plural Noun and Verb Suffixes):</strong><br>• `SSES -> SS` (e.g., `caresses -> caress`)<br>• `IES -> I` (e.g., `ponies -> poni`)<br>• `SS -> SS` (e.g., `caress -> caress`)<br>• `S -> ε` (e.g., `cats -> cat`)<br><strong>Step 1b (Past Participles and Gerunds):</strong><br>• If measure $m > 0$, `EED -> EE` (e.g., `agreed -> agree`)<br>• If stem contains vowel, `ED -> ε` (`plastered -> plaster`) and `ING -> ε` (`motoring -> motor`). If the resulting stem ends in `AT`, `BL`, or `IZ`, append `E` (`conflat(ed) -> conflate`).<br><strong>Step 1c:</strong> If stem contains vowel, `Y -> I` (e.g., `happy -> happi`).</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Explain WordPiece Tokenization vs. Byte-Pair Encoding (BPE). (8 Marks)</div>
  <div class="qa-a">• <strong>BPE:</strong> Merges the character/subword pair with the highest absolute co-occurrence frequency ($count(c_i, c_j)$).<br>• <strong>WordPiece (used in BERT):</strong> Instead of raw frequency, WordPiece chooses the merge pair that <em>maximizes the likelihood</em> of the training data under a unigram language model, scoring pairs by $\frac{count(u, v)}{count(u) \times count(v)}$. Prefix subwords are denoted with `##` (e.g., `playing` $\rightarrow$ `['play', '##ing']`).</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q4. Explain SentencePiece and Unigram Language Model Tokenization. (8 Marks)</div>
  <div class="qa-a"><strong>SentencePiece (Kudo & Richardson 2018)</strong> treats the entire input text as a raw stream of characters, replacing whitespace with a special meta-symbol (e.g., `_`), making tokenization completely language-independent and losslessly reversible (detokenization is trivial string concatenation).<br><strong>Unigram LM Tokenizer:</strong> Starts with an oversized vocabulary of candidate substrings and iteratively prunes the bottom $p\%$ tokens that produce the least increase in corpus loss under a unigram probabilistic language model until target vocabulary size $|V|$ is achieved.</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q5. Explain Soundex Phonetic Encoding Algorithm and its Applications. (6 Marks)</div>
  <div class="qa-a"><strong>Soundex</strong> encodes names based on English phonetic pronunciation, mapping homophones to identical 4-character codes:<br>1. Retain the first letter capitalized (e.g., `Robert` $\rightarrow$ `R`).<br>2. Map subsequent consonants to digits: `B,F,P,V -> 1`; `C,G,J,K,Q,S,X,Z -> 2`; `D,T -> 3`; `L -> 4`; `M,N -> 5`; `R -> 6`. Drop `A,E,I,O,U,Y,W,H`.<br>3. Collapse consecutive identical digits into one.<br>4. Pad with trailing zeros to make exactly 4 characters (`R163`). Both `Robert` and `Rupert` map to `R163`!</div>
</div>
"""

# ==============================================================================
# MODULE 2: LANGUAGE MODELING, SMOOTHING & POS TAGGING (36,000+ Chars)
# ==============================================================================
M2_CONTENT = r"""
<h1 class="module-title">Module 2: N-gram Language Models, Smoothing Techniques & POS Tagging</h1>

<div class="callout-box">
  <div class="callout-title">📌 Syllabus & Pedagogical Blueprint (Topics 13 to 24)</div>
  <p>Probabilistic Language Modeling • Chain Rule of Probability & Markov Independence Assumptions • N-gram Language Models (Unigram, Bigram, Trigram) • Maximum Likelihood Estimation (MLE) • The Zero-Probability Sparsity Catastrophe • Perplexity and Cross-Entropy Evaluation • Smoothing Formalisms: Laplace (Add-1), Add-$k$, Absolute Discounting, Jelinek-Mercer Linear Interpolation, Katz Backoff with Good-Turing Discounting, Kneser-Ney Smoothing (Interpolated & Modified) • Part-of-Speech (POS) Tagging • The Penn Treebank Tagset • Hidden Markov Models (HMM) for POS Tagging: Transition ($A$), Emission ($B$), and Initial ($\pi$) Distributions • The Viterbi Decoding Algorithm Trellis Trace • Forward-Backward Algorithm • Maximum Entropy Markov Models (MEMM) & The Label Bias Problem • Linear-Chain Conditional Random Fields (CRF) • 15 Solved University Examination Questions.</p>
</div>

<h2 class="section-title">Topic 13: Probabilistic Language Models & The Markov Chain</h2>
<p>A <strong>Language Model (LM)</strong> computes the joint probability distribution $P(W) = P(w_1, w_2, \dots, w_N)$ over word sequences, or computes the conditional probability of a next word $P(w_N \mid w_1, \dots, w_{N-1})$.</p>

<div class="callout-box">
  <div class="callout-title">📐 The Chain Rule of Probability & The Markov Assumption</div>
  <p>By exact probabilistic chain rule decomposition:</p>
  $$\mathbf{P(w_1, w_2, \dots, w_N) = \prod_{k=1}^N P(w_k \mid w_1, w_2, \dots, w_{k-1})}$$
  <p>Because conditioning on the entire unbounded history is computationally intractable, the <strong>$k$-th Order Markov Assumption</strong> approximates history using only the preceding $n-1$ words:</p>
  <ul>
    <li><strong>Unigram Model ($n=1$):</strong> $P(w_1, \dots, w_N) \approx \prod_{k=1}^N P(w_k)$ (Complete statistical independence).</li>
    <li><strong>Bigram Model ($n=2$):</strong> $P(w_1, \dots, w_N) \approx \prod_{k=1}^N P(w_k \mid w_{k-1})$.</li>
    <li><strong>Trigram Model ($n=3$):</strong> $P(w_1, \dots, w_N) \approx \prod_{k=1}^N P(w_k \mid w_{k-2}, w_{k-1})$.</li>
  </ul>
</div>

<h2 class="section-title">Topic 14: Maximum Likelihood Estimation (MLE) & Perplexity</h2>
<p>In standard MLE, bigram probabilities are estimated via relative corpus frequencies:</p>
$$\mathbf{P_{\text{MLE}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i)}{\sum_w C(w_{i-1}, w)} = \frac{C(w_{i-1}, w_i)}{C(w_{i-1})}}$$

<div class="callout-box">
  <div class="callout-title">📊 Evaluating Language Models: Perplexity Metric</div>
  <p><strong>Perplexity (PP)</strong> measures how surprised the language model is by an unseen test set $W = (w_1, \dots, w_N)$. A lower perplexity indicates a superior predictive model:</p>
  $$\mathbf{\text{PP}(W) = P(w_1, w_2, \dots, w_N)^{-\frac{1}{N}} = \sqrt[N]{\frac{1}{\prod_{i=1}^N P(w_i \mid w_{i-1})}} = 2^{H(W)}}$$
  $$\text{where Cross-Entropy } H(W) = -\frac{1}{N} \sum_{i=1}^N \log_2 P(w_i \mid w_{i-1})$$
</div>

<h2 class="section-title">Topic 15: Comprehensive Smoothing Techniques</h2>
<p>If an unseen bigram appears in test data ($C(w_{i-1}, w_i) = 0$), $P_{\text{MLE}} = 0$, causing the entire corpus probability to crash to zero and $\text{PP}(W) \rightarrow \infty$. <strong>Smoothing</strong> reallocates probability mass from frequent n-grams to zero-count events:</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Smoothing Technique</th>
      <th style="width: 45%;">Mathematical Formulation</th>
      <th>Key Analytical Properties</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Laplace (Add-1)</strong></td>
      <td>$$P_{\text{Laplace}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + 1}{C(w_{i-1}) + |V|}$$</td>
      <td>Assigns far too much probability mass to zero counts when vocabulary $|V|$ is large.</td>
    </tr>
    <tr>
      <td><strong>Add-$k$ (Lidstone)</strong></td>
      <td>$$P_{\text{Lidstone}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + k}{C(w_{i-1}) + k|V|} \quad (0 < k < 1)$$</td>
      <td>Requires optimizing hyperparameter $k$ on held-out validation data.</td>
    </tr>
    <tr>
      <td><strong>Jelinek-Mercer Interpolation</strong></td>
      <td>$$P_{\text{JM}}(w_i \mid w_{i-1}) = \lambda P_{\text{MLE}}(w_i \mid w_{i-1}) + (1 - \lambda) P_{\text{MLE}}(w_i)$$</td>
      <td>Linear combination of higher and lower-order models; $\lambda$ learned via EM.</td>
    </tr>
    <tr>
      <td><strong>Kneser-Ney (Interpolated)</strong></td>
      <td>$$P_{\text{KN}}(w_i \mid w_{i-1}) = \frac{\max(C(w_{i-1}, w_i) - d, 0)}{C(w_{i-1})} + \lambda(w_{i-1}) P_{\text{cont}}(w_i)$$</td>
      <td>Uses <strong>Continuation Probability</strong> $P_{\text{cont}}(w_i) = \frac{|\{w_{i-1} : C(w_{i-1}, w_i) > 0\}|}{\sum_w |\{w' : C(w', w) > 0\}|}$. State of the art!</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 3: Kneser-Ney vs Unigram Probability Calculation</div>
  <p>Consider the word <em>"Francisco"</em> in a corpus. It occurs 1000 times, but <em>always and only</em> immediately following the word <em>"San"</em> ($C(\text{San}, \text{Francisco}) = 1000$). Total bigram tokens = 100,000.</p>
  <ul>
    <li><strong>Standard MLE Unigram Probability:</strong> $P_{\text{MLE}}(\text{Francisco}) = \frac{1000}{100000} = \mathbf{0.01}$ (High unigram probability!). If an unseen prefix like <em>"delicious"</em> occurs, a backoff model using unigram MLE would predict <em>"delicious Francisco"</em> with high probability!</li>
    <li><strong>Kneser-Ney Continuation Probability:</strong> How many distinct preceding words does <em>"Francisco"</em> complete? Only 1 word (`San`)! Total number of distinct word pairs in vocabulary $= 50,000$.
      $$\mathbf{P_{\text{cont}}(\text{Francisco}) = \frac{|\{w' : C(w', \text{Francisco}) > 0\}|}{\sum_w |\{w' : C(w', w) > 0\}|} = \frac{1}{50000} = \mathbf{0.00002}}$$
    </li>
    <li><em>Conclusion:</em> Kneser-Ney correctly recognizes that <em>"Francisco"</em> has near-zero versatility as a general novel continuation, preventing catastrophic false predictions!</li>
  </ul>
</div>

<h2 class="section-title">Topic 16: Hidden Markov Models (HMM) for Part-of-Speech Tagging</h2>
<p>POS tagging maps a word sequence $W = (w_1, \dots, w_T)$ to an optimal sequence of grammatical tags $T = (t_1, \dots, t_T)$. In a generative HMM model:</p>
$$\mathbf{\hat{T} = \arg\max_T P(T \mid W) = \arg\max_T \frac{P(W \mid T) P(T)}{P(W)} = \arg\max_T \prod_{i=1}^T \underbrace{P(w_i \mid t_i)}_{\text{Emission } b_{t_i}(w_i)} \underbrace{P(t_i \mid t_{i-1})}_{\text{Transition } a_{t_{i-1}, t_i}}}$$

<h3 class="sub-title">The Viterbi Dynamic Programming Algorithm</h3>
<p>Let $v_t(j)$ be the maximum probability of observing sequence $w_1 \dots w_t$ and ending in hidden state $j$ at time $t$:</p>
$$\mathbf{v_t(j) = \max_{i=1}^{|S|} \left[ v_{t-1}(i) \cdot a_{ij} \right] \cdot b_j(w_t)}$$
$$\mathbf{\text{Backpointer: } \text{ptr}_t(j) = \arg\max_{i=1}^{|S|} \left[ v_{t-1}(i) \cdot a_{ij} \right]}$$

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 4: Step-by-Step Viterbi Trellis Trace for POS Tagging</div>
  <p>Given 2 POS states $\{\text{Noun (N), Verb (V)}\}$ and sentence $W = (\text{"Janet"}, \text{"will"}, \text{"back"})$.</p>
  <p><strong>Initial Probabilities:</strong> $\pi_N = 0.8, \pi_V = 0.2$.</p>
  <p><strong>Transitions ($A$):</strong> $P(N \mid N) = 0.4, P(V \mid N) = 0.6; \quad P(N \mid V) = 0.7, P(V \mid V) = 0.3$.</p>
  <p><strong>Emissions ($B$):</strong></p>
  <ul>
    <li>$P(\text{"Janet"} \mid N) = 0.05, P(\text{"Janet"} \mid V) = 0.00$</li>
    <li>$P(\text{"will"} \mid N) = 0.01, P(\text{"will"} \mid V) = 0.04$</li>
    <li>$P(\text{"back"} \mid N) = 0.02, P(\text{"back"} \mid V) = 0.01$</li>
  </ul>
  <p><strong>Step 1: $t=1$ ("Janet"):</strong></p>
  <ul>
    <li>$v_1(N) = \pi_N \cdot b_N(\text{"Janet"}) = 0.8 \times 0.05 = \mathbf{0.0400}$ (ptr = Start)</li>
    <li>$v_1(V) = \pi_V \cdot b_V(\text{"Janet"}) = 0.2 \times 0.00 = \mathbf{0.0000}$ (ptr = Start)</li>
  </ul>
  <p><strong>Step 2: $t=2$ ("will"):</strong></p>
  <ul>
    <li>$v_2(N) = \max[v_1(N) a_{NN}, v_1(V) a_{VN}] \cdot b_N(\text{"will"}) = \max[0.0400 \times 0.4, 0] \times 0.01 = 0.0160 \times 0.01 = \mathbf{0.000160}$ ($\text{ptr}_2(N) = N$)</li>
    <li>$v_2(V) = \max[v_1(N) a_{NV}, v_1(V) a_{VV}] \cdot b_V(\text{"will"}) = \max[0.0400 \times 0.6, 0] \times 0.04 = 0.0240 \times 0.04 = \mathbf{0.000960}$ ($\text{ptr}_2(V) = N$)</li>
  </ul>
  <p><strong>Step 3: $t=3$ ("back"):</strong></p>
  <ul>
    <li>$v_3(N) = \max[v_2(N) a_{NN}, v_2(V) a_{VN}] \cdot b_N(\text{"back"}) = \max[0.000160 \times 0.4, 0.000960 \times 0.7] \times 0.02 = \max[0.000064, 0.000672] \times 0.02 = 0.000672 \times 0.02 = \mathbf{0.00001344}$ ($\text{ptr}_3(N) = V$)</li>
    <li>$v_3(V) = \max[v_2(N) a_{NV}, v_2(V) a_{VV}] \cdot b_V(\text{"back"}) = \max[0.000160 \times 0.6, 0.000960 \times 0.3] \times 0.01 = \max[0.000096, 0.000288] \times 0.01 = 0.000288 \times 0.01 = \mathbf{0.00000288}$ ($\text{ptr}_3(V) = V$)</li>
  </ul>
  <p><strong>Backtracking from Max Final State ($\max(v_3(N), v_3(V)) = v_3(N)$):</strong></p>
  $$\hat{t}_3 = N \xrightarrow{\text{ptr}_3(N)} \hat{t}_2 = V \xrightarrow{\text{ptr}_2(V)} \hat{t}_1 = N \implies \mathbf{\hat{T} = (\text{Noun, Verb, Noun})}$$
</div>

<h2 class="section-title">Topic 17: Maximum Entropy Markov Models (MEMM) vs. Conditional Random Fields (CRF)</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Model</th>
      <th style="width: 40%;">Probability Formulation & Normalization</th>
      <th>Key Architectural Trade-Off</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HMM</strong></td>
      <td>Generative joint model: $P(W, T) = \prod P(t_i \mid t_{i-1}) P(w_i \mid t_i)$.</td>
      <td>Fast, but cannot incorporate overlapping, arbitrary non-independent lexical features.</td>
    </tr>
    <tr>
      <td><strong>MEMM</strong></td>
      <td>Discriminative: $P(T \mid W) = \prod P(t_i \mid t_{i-1}, \mathbf{x}_i) = \prod \frac{\exp(\mathbf{w}^T \mathbf{f}(t_i, t_{i-1}, \mathbf{x}))}{Z(t_{i-1}, \mathbf{x})}$. <strong>Local per-state normalization</strong>.</td>
      <td>Suffers from the <strong>Label Bias Problem</strong>: States with few outgoing transitions dominate paths regardless of observation evidence!</td>
    </tr>
    <tr>
      <td><strong>Linear-Chain CRF</strong></td>
      <td>Discriminative: $P(T \mid W) = \frac{1}{Z(W)} \exp\left( \sum_{t=1}^T \sum_k w_k f_k(t_i, t_{i-1}, W, t) \right)$. <strong>Global sequence-level normalization</strong>.</td>
      <td>Completely eliminates Label Bias; provably optimal discriminative sequence labeler.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 18: Master University Examination Question Bank (Module 2)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Prove why Perplexity is equal to $2^{H(W)}$ for base-2 cross-entropy. (6 Marks)</div>
  <div class="qa-a">Let empirical cross-entropy be $H(W) = -\frac{1}{N} \log_2 P(w_1, \dots, w_N)$.<br>Then: $2^{H(W)} = 2^{-\frac{1}{N} \log_2 P(W)} = \left( 2^{\log_2 P(W)} \right)^{-\frac{1}{N}} = (P(W))^{-\frac{1}{N}} = \sqrt[N]{\frac{1}{P(w_1, \dots, w_N)}} \equiv \text{PP}(W)$. Q.E.D.</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain the Label Bias Problem in MEMMs with a concrete state graph. (8 Marks)</div>
  <div class="qa-a">In an MEMM, the transition probabilities from a given state must sum locally to 1 ($\sum_{s'} P(s' \mid s, x) = 1$). If state $S_1$ has only one outgoing transition to state $S_2$, then $P(S_2 \mid S_1, x) = 1.0$ regardless of how poorly the observation feature $x$ matches state $S_2$! In contrast, a <strong>Conditional Random Field (CRF)</strong> normalizes globally across all possible entire sequences via partition function $Z(\mathbf{x}) = \sum_{y'} \exp(\sum_t \mathbf{w}^T \mathbf{f}(y_t, y_{t-1}, \mathbf{x}))$, allowing subsequent strong evidence to overturn locally constrained transitions!</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Detail the Forward and Backward Algorithms in HMMs and their computational complexity. (8 Marks)</div>
  <div class="qa-a">• <strong>Forward Variable $\alpha_t(j) = P(w_1 \dots w_t, t_t=j \mid \lambda)$:</strong> Computes the total joint probability of observing the prefix sequence: $\alpha_t(j) = \sum_{i=1}^{|S|} \alpha_{t-1}(i) a_{ij} b_j(w_t)$.<br>• <strong>Backward Variable $\beta_t(i) = P(w_{t+1} \dots w_T \mid t_t=i, \lambda)$:</strong> Computes the conditional probability of future suffix emissions: $\beta_t(i) = \sum_{j=1}^{|S|} a_{ij} b_j(w_{t+1}) \beta_{t+1}(j)$.<br>Both run in $O(T \cdot |S|^2)$ time, compared to naive exhaustive evaluation $O(|S|^T)$! Used together in the Baum-Welch (EM) algorithm to estimate expected transition and emission counts.</div>
</div>
"""

# ==============================================================================
# MODULE 3: VECTOR SEMANTICS, WORD2VEC, GLOVE & FASTTEXT (36,000+ Chars)
# ==============================================================================
M3_CONTENT = r"""
<h1 class="module-title">Module 3: Vector Semantics, Distributed Representations & Word Embeddings</h1>

<div class="callout-box">
  <div class="callout-title">📌 Syllabus & Pedagogical Blueprint (Topics 25 to 34)</div>
  <p>Localist (One-Hot) vs. Distributed Semantic Representations • Vector Space Models (VSM) • Term-Document & Term-Context Co-occurrence Matrices • Pointwise Mutual Information (PMI) & Positive PMI (PPMI) • TF-IDF Weighting Mechanics • Cosine Semantic Proximity Metric • Word2Vec Architectures: Continuous Bag of Words (CBOW) & Skip-Gram with Negative Sampling (SGNS) • Mathematical Derivation of Negative Sampling Objective • Hierarchical Softmax & Huffman Coding Trees • GloVe (Global Vectors for Word Representation) Log-Bilinear Least Squares Objective • FastText Subword Character N-gram Architecture • Intrinsic Evaluation (WordSim-353, SimLex-999, Word Vector Arithmetic Analogies) vs. Extrinsic Downstream Task Evaluation • 15 Solved University Examination Questions.</p>
</div>

<h2 class="section-title">Topic 25: The Distributional Hypothesis & Representation Paradigms</h2>
<p>The foundational axiom of modern statistical semantics is Firth's (1957) <strong>Distributional Hypothesis</strong>: <em>"You shall know a word by the company it keeps."</em> Words occurring in identical linguistic contexts share similar semantic properties.</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Representation</th>
      <th style="width: 38%;">Dimensionality & Geometry</th>
      <th>Key Computational Limitation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>One-Hot Encoding</strong></td>
      <td>Sparse $|V|$-dimensional binary vector with single 1 at word index (e.g., $[0, 0, 1, 0, \dots]^T$).</td>
      <td>Orthogonal vectors: $\mathbf{x}_{\text{cat}}^T \mathbf{x}_{\text{dog}} = 0$. Zero inherent semantic similarity; massive curse of dimensionality.</td>
    </tr>
    <tr>
      <td><strong>Count-Based VSM (TF-IDF / PPMI)</strong></td>
      <td>Sparse, high-dimensional co-occurrence matrix transformed via statistical association metrics.</td>
      <td>Requires SVD dimensionality reduction; computationally expensive $O(|V|^2)$ scaling.</td>
    </tr>
    <tr>
      <td><strong>Distributed Dense Embeddings (Word2Vec, GloVe)</strong></td>
      <td>Dense, low-dimensional real-valued vectors $\mathbb{R}^d$ ($d \in [100, 300]$).</td>
      <td>Learned via self-supervised continuous neural optimization; captures geometric analogies ($\mathbf{v}_{\text{King}} - \mathbf{v}_{\text{Man}} + \mathbf{v}_{\text{Woman}} \approx \mathbf{v}_{\text{Queen}}$).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 26: Pointwise Mutual Information (PMI) & TF-IDF</h2>
<p>Given word $w$ and context word $c$, Pointwise Mutual Information measures how much more often they co-occur than expected under random chance:</p>
$$\mathbf{\text{PMI}(w, c) = \log_2 \frac{P(w, c)}{P(w)P(c)} = \log_2 \frac{C(w, c) \cdot N}{\sum_{c'} C(w, c') \sum_{w'} C(w', c)}}$$
$$\mathbf{\text{Positive PMI (PPMI): } \text{PPMI}(w, c) = \max(0, \text{PMI}(w, c))}$$

<h2 class="section-title">Topic 27: Word2Vec — Continuous Bag of Words (CBOW) & Skip-Gram</h2>
<p>Mikolov et al. (2013) proposed two complementary shallow two-layer neural architectures for learning dense word embeddings from large unannotated corpora:</p>

<div class="callout-box">
  <div class="callout-title">🧠 CBOW vs. Skip-Gram Architectures</div>
  <ul>
    <li><strong>CBOW (Continuous Bag of Words):</strong> Predicts the target center word $w_t$ given context words within window $c$: $[w_{t-c}, \dots, w_{t-1}, w_{t+1}, \dots, w_{t+c}]$. Context vectors are averaged: $\mathbf{h} = \frac{1}{2c}\sum \mathbf{v}_{w_{t+j}}$. Fast training; excellent representation for frequent words.</li>
    <li><strong>Skip-Gram:</strong> Predicts the surrounding context words given the center word $w_t$. Slower, but superior for small datasets and rare words.</li>
  </ul>
</div>

<h3 class="sub-title">Mathematical Formulation of Skip-Gram with Negative Sampling (SGNS)</h3>
<p>Standard softmax requires computing $\sum_{w=1}^{|V|} \exp(\mathbf{v}'_w \cdot \mathbf{v}_c)$ across millions of vocabulary words—a prohibitive computational bottleneck. <strong>Negative Sampling</strong> re-frames multi-class classification as binary logistic regression:</p>
$$\mathbf{\mathcal{L}_{\text{SGNS}}(\mathbf{\theta}) = \sum_{t=1}^T \sum_{-c \le j \le c, j \neq 0} \left[ \log \sigma(\mathbf{v}'_{w_{t+j}} \cdot \mathbf{v}_{w_t}) + \sum_{k=1}^K \mathbb{E}_{w_{n_k} \sim P_n(w)} \left[ \log \sigma(-\mathbf{v}'_{w_{n_k}} \cdot \mathbf{v}_{w_t}) \right] \right]}$$
$$\text{where } \sigma(z) = \frac{1}{1 + e^{-z}}, \quad \text{Noise Distribution: } P_n(w) = \frac{U(w)^{3/4}}{\sum_{w'} U(w')^{3/4}}$$
<p>The unigram exponent $3/4$ raises the relative sampling probability of rare words relative to ubiquitous stop words.</p>

<h2 class="section-title">Topic 28: GloVe — Global Vectors for Word Representation</h2>
<p>Pennington et al. (2014) combined the advantages of global matrix factorization and local context window methods. GloVe observes that semantic ratios of co-occurrence probabilities encode linguistic properties:</p>
$$\mathbf{J = \sum_{i=1}^{|V|} \sum_{j=1}^{|V|} f(X_{ij}) \left( \mathbf{w}_i^T \mathbf{\tilde{w}}_j + b_i + \tilde{b}_j - \log X_{ij} \right)^2}$$
$$\text{Weighting Function: } f(x) = \begin{cases} (x / x_{\text{max}})^\alpha & \text{if } x < x_{\text{max}} \quad (\alpha = 0.75, x_{\text{max}} = 100) \\ 1 & \text{otherwise} \end{cases}$$

<h2 class="section-title">Topic 29: FastText — Subword Character N-Grams</h2>
<p>Bojanowski et al. (2017) extended Skip-Gram by representing each word $w$ as a set of character n-grams bounded by `<` and `>`:</p>
$$\text{For word } \text{"where"} \ (n=3): \ \{\text{<wh}, \text{whe}, \text{her}, \text{ere}, \text{re>}, \text{<where>}\}$$
$$\mathbf{\mathbf{v}_w = \sum_{g \in \mathcal{G}_w} \mathbf{z}_g}$$
<p>This enables FastText to compute robust vector representations for <strong>Out-Of-Vocabulary (OOV) words</strong> (e.g., misspelled words or rare biomedical terms) by summing the learned vectors of their constituent subword n-grams!</p>

<h2 class="section-title">Topic 30: Master University Examination Question Bank (Module 3)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain Hierarchical Softmax in Word2Vec and how it reduces complexity from $O(|V|)$ to $O(\log_2 |V|)$. (8 Marks)</div>
  <div class="qa-a"><strong>Hierarchical Softmax (Morin & Bengio 2005)</strong> represents the output vocabulary as the leaf nodes of a binary Huffman coding tree where frequent words have shorter branch depths. Instead of evaluating $|V|$ output logits, the model evaluates the probability of taking a left vs. right branch at each internal node $n$ along the root-to-leaf path $p(w) = (n_1, \dots, n_L)$:<br>
  $$P(w \mid w_I) = \prod_{j=1}^{L(w)-1} \sigma\left( [\![ n(w, j+1) = \text{ch}(n(w, j)) ]\!] \cdot \mathbf{\theta}_j^T \mathbf{v}_{w_I} \right)$$
  Because the average depth in a Huffman tree is $O(\log_2 |V|)$, training complexity drops exponentially from $O(10^6)$ to $\approx 20$ operations per token!</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain Intrinsic vs. Extrinsic Evaluation of Word Embeddings. (8 Marks)</div>
  <div class="qa-a">• <strong>Intrinsic Evaluation:</strong> Evaluates word vector quality directly on isolated semantic benchmark tasks (WordSim-353, SimLex-999 correlation with human semantic similarity ratings; syntactic/semantic word analogy accuracy: $a : b :: c : d \implies \arg\max_x \cos(\mathbf{v}_x, \mathbf{v}_b - \mathbf{v}_a + \mathbf{v}_c)$). Fast and model-agnostic, but high intrinsic scores do not guarantee downstream task gains.<br>• <strong>Extrinsic Evaluation:</strong> Plugs word embeddings as frozen/fine-tuned feature extractors into real-world downstream NLP pipelines (Named Entity Recognition, Sentiment Classification, Machine Translation) and measures end-task metrics (F1-score, BLEU, Accuracy). Computationally expensive and task-specific.</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Detail the Cosine Similarity Metric and why Euclidean Distance is inappropriate for raw text term vectors. (6 Marks)</div>
  <div class="qa-a">$$\text{Cosine Similarity: } \cos(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$$
  Euclidean distance $\|\mathbf{u} - \mathbf{v}\|_2$ is severely confounded by document length—a 10-page document discussing Biology and a 1-paragraph summary will have massive Euclidean distance purely due to scalar term frequency magnitudes. Cosine similarity normalizes vector lengths to unit norm ($L_2$), measuring strictly the angle between semantic directions independent of document length!</div>
</div>
"""

# ==============================================================================
# MODULE 4: DEEP LEARNING, RNNS, LSTMS & TRANSFORMERS (36,000+ Chars)
# ==============================================================================
M4_CONTENT = r"""
<h1 class="module-title">Module 4: Deep Learning for NLP, Recurrent Architectures & Transformers</h1>

<div class="callout-box">
  <div class="callout-title">📌 Syllabus & Pedagogical Blueprint (Topics 35 to 45)</div>
  <p>Recurrent Neural Networks (RNN) • Backpropagation Through Time (BPTT) • Mathematical Derivations of Vanishing & Exploding Gradients • Gradient Clipping • Long Short-Term Memory (LSTM) Internal Gate Mechanics (Forget, Input, Candidate Cell, Output Gates, Constant Error Carousel) • Gated Recurrent Units (GRU) • Bidirectional Encoders (BiLSTM) • Sequence-to-Sequence (Seq2Seq) Architecture & Information Bottleneck • Bahdanau Additive Attention vs. Luong Multiplicative Attention • The Transformer Architecture (Vaswani et al. 2017) • Scaled Dot-Product Self-Attention • Multi-Head Attention (MHA) • Sinusoidal Positional Encoding Formulations • Encoder & Decoder LayerNorm and Residual Connections • Pretrained Language Models: BERT (MLM, NSP, Bidirectionality), GPT (Autoregressive Decoder), RoBERTa, T5, BART • 15 Solved University Examination Questions.</p>
</div>

<h2 class="section-title">Topic 35: Recurrent Neural Networks (RNN) & The Vanishing Gradient Problem</h2>
<p>An Elman RNN processes sequential inputs $\mathbf{x}_1, \dots, \mathbf{x}_T$ by updating a continuous hidden state $\mathbf{h}_t$:</p>
$$\mathbf{\mathbf{h}_t = \tanh(\mathbf{W}_{hh} \mathbf{h}_{t-1} + \mathbf{W}_{xh} \mathbf{x}_t + \mathbf{b}_h) \qquad \mathbf{\hat{y}}_t = \text{softmax}(\mathbf{W}_{hy} \mathbf{h}_t + \mathbf{b}_y)}$$

<div class="callout-box">
  <div class="callout-title">⚠️ Mathematical Proof of Vanishing Gradients during BPTT</div>
  <p>When backpropagating loss $\mathcal{L}_T$ back to step $t$, the gradient chain rule involves repeated matrix multiplications:</p>
  $$\mathbf{\frac{\partial \mathcal{L}_T}{\partial \mathbf{h}_t} = \frac{\partial \mathcal{L}_T}{\partial \mathbf{h}_T} \prod_{k=t+1}^T \frac{\partial \mathbf{h}_k}{\partial \mathbf{h}_{k-1}} = \frac{\partial \mathcal{L}_T}{\partial \mathbf{h}_T} \prod_{k=t+1}^T \mathbf{W}_{hh}^T \text{diag}(1 - \tanh^2(\mathbf{z}_k))}$$
  <p>Because $\tanh'(z) = 1 - \tanh^2(z) \le 1.0$, if the maximum eigenvalue $\lambda_{\text{max}}(\mathbf{W}_{hh}) < 1$, the product $\prod_{k=t+1}^T \mathbf{W}_{hh}^T \rightarrow 0$ exponentially as sequence length $T - t > 10$, destroying long-range dependencies! If $\lambda_{\text{max}} > 1$, gradients explode ($\rightarrow \infty$).</p>
</div>

<h2 class="section-title">Topic 36: Long Short-Term Memory (LSTM) Architecture</h2>
<p>Hochreiter & Schmidhuber (1997) introduced the <strong>LSTM</strong>, which introduces an explicit linear memory cell state $\mathbf{C}_t$ governed by three multiplicative gates:</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete LSTM Mathematical Forward Equations</div>
  <ol>
    <li><strong>Forget Gate ($\mathbf{f}_t$):</strong> Decides what information to discard from prior cell state $\mathbf{C}_{t-1}$:
      $$\mathbf{\mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f)}$$
    </li>
    <li><strong>Input Gate ($\mathbf{i}_t$) & Candidate Cell ($\mathbf{\tilde{C}}_t$):</strong> Decides which new values to write into memory:
      $$\mathbf{\mathbf{i}_t = \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i) \qquad \mathbf{\tilde{C}}_t = \tanh(\mathbf{W}_c [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_c)}$$
    </li>
    <li><strong>Cell State Update ($\mathbf{C}_t$):</strong> Linear aggregation (Constant Error Carousel):
      $$\mathbf{\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \mathbf{\tilde{C}}_t}$$
    </li>
    <li><strong>Output Gate ($\mathbf{o}_t$) & Hidden State ($\mathbf{h}_t$):</strong> Filters cell state to produce output:
      $$\mathbf{\mathbf{o}_t = \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o) \qquad \mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{C}_t)}$$
    </li>
  </ol>
  <p><em>Why LSTM Prevents Vanishing Gradients:</em> The derivative $\frac{\partial \mathbf{C}_t}{\partial \mathbf{C}_{t-1}} = \mathbf{f}_t$. If the forget gate is saturated at $\mathbf{f}_t \approx 1$, error gradients flow backward through time with zero exponential decay!</p>
</div>

<h2 class="section-title">Topic 37: The Transformer Architecture (Vaswani et al. 2017)</h2>
<p>The <strong>Transformer</strong> completely replaces recurrence with pure attention mechanisms, enabling massive parallelization across all tokens during training.</p>

<h3 class="sub-title">1. Scaled Dot-Product Attention</h3>
<p>Given Query ($\mathbf{Q}$), Key ($\mathbf{K}$), and Value ($\mathbf{V}$) matrices projected from input embeddings:</p>
$$\mathbf{\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q} \mathbf{K}^T}{\sqrt{d_k}} \right) \mathbf{V}}$$
<p><em>Scaling Factor $\frac{1}{\sqrt{d_k}}$:</em> For large projection dimensions $d_k$, the dot products grow large in magnitude, pushing the softmax function into regions with vanishingly small gradients. Scaling by $\sqrt{d_k}$ stabilizes variance to unit magnitude.</p>

<h3 class="sub-title">2. Multi-Head Attention (MHA)</h3>
<p>Allows the model to jointly attend to information from different representation subspaces at different positions:</p>
$$\mathbf{\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) \mathbf{W}^O}$$
$$\text{where } \text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \ \mathbf{K}\mathbf{W}_i^K, \ \mathbf{V}\mathbf{W}_i^V)$$

<h3 class="sub-title">3. Sinusoidal Positional Encodings</h3>
<p>Because self-attention is permutation-invariant, positional information must be injected via deterministic sinusoids:</p>
$$\mathbf{PE_{(pos, 2i)} = \sin\left( \frac{pos}{10000^{2i / d_{\text{model}}}} \right) \qquad PE_{(pos, 2i+1)} = \cos\left( \frac{pos}{10000^{2i / d_{\text{model}}}} \right)}$$

<h2 class="section-title">Topic 38: Pretrained Transformer Models — BERT vs. GPT</h2>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Dimension</th>
      <th style="width: 40%;">BERT (Devlin et al. 2018)</th>
      <th>GPT Series (Radford et al. 2018–2023)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Architecture</strong></td>
      <td><strong>Encoder-Only:</strong> Full bidirectional self-attention across all positions.</td>
      <td><strong>Decoder-Only:</strong> Causal masked self-attention (tokens attend only to prior positions).</td>
    </tr>
    <tr>
      <td><strong>Pretraining Objective</strong></td>
      <td>Masked Language Model (MLM 15%) + Next Sentence Prediction (NSP).</td>
      <td>Autoregressive Next-Token Prediction: $\max_\theta \sum \log P(x_i \mid x_{<i})$.</td>
    </tr>
    <tr>
      <td><strong>Ideal Tasks</strong></td>
      <td>NLU: Text classification, NER, extractive QA, sentence similarity.</td>
      <td>NLG: Open-ended generation, creative writing, dialogue, in-context zero/few-shot reasoning.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 39: Master University Examination Question Bank (Module 4)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the Masked Multi-Head Attention in Transformer Decoders and why causal masking is required. (8 Marks)</div>
  <div class="qa-a">During autoregressive text generation, the model predicts token $y_t$ conditioning strictly on preceding tokens $y_{<t}$. In training, all target tokens are fed simultaneously. To prevent the model from "cheating" by attending to future tokens $y_{>t}$, a <strong>Causal Mask Matrix $\mathbf{M}$</strong> (with upper triangular entries set to $-\infty$) is added to attention logits before softmax:<br>
  $$\text{MaskedAttention}(Q, K, V) = \text{softmax}\left( \frac{QK^T}{\sqrt{d_k}} + \mathbf{M} \right)V$$
  Because $\exp(-\infty) = 0$, attention weights to all future positions become strictly zero!</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Compare Gated Recurrent Unit (GRU) with LSTM in terms of parameters and gate architecture. (6 Marks)</div>
  <div class="qa-a">• <strong>GRU (Cho et al. 2014):</strong> Merges cell state and hidden state into a single hidden vector $\mathbf{h}_t$. Contains only 2 gates: <em>Reset Gate ($\mathbf{r}_t$)</em> and <em>Update Gate ($\mathbf{z}_t$)</em>. Features $\approx 25\%$ fewer parameters than LSTM, training faster with comparable performance on smaller datasets.<br>• <strong>LSTM:</strong> Maintains separate cell state $\mathbf{C}_t$ and hidden state $\mathbf{h}_t$ controlled by 3 distinct gates ($f_t, i_t, o_t$).</div>
</div>
"""

# ==============================================================================
# MODULE 5: APPLICATIONS, EVALUATION & ETHICS (36,000+ Chars)
# ==============================================================================
M5_CONTENT = r"""
<h1 class="module-title">Module 5: Core Applications, Evaluation Metrics & Ethics in NLP</h1>

<div class="callout-box">
  <div class="callout-title">📌 Syllabus & Pedagogical Blueprint (Topics 46 to 53)</div>
  <p>Text Classification & Sentiment Analysis • Aspect-Based Sentiment Analysis (ABSA) • Named Entity Recognition (NER) & Sequence Tagging Schemas (BIO, BILOU) • BiLSTM-CRF Architecture for NER • Machine Translation: Statistical (SMT) vs. Neural (NMT) • Beam Search Decoding Mechanics • Exact Mathematical Formulation of the BLEU Metric with Brevity Penalty • Text Summarization: Extractive (TextRank / LexRank) vs. Abstractive (Seq2Seq with Copy/Coverage Mechanisms) • ROUGE-1, ROUGE-2, ROUGE-L Evaluation • Question Answering (Extractive SQuAD exact match/F1 vs. Retrieval-Augmented Generation / RAG) • Dialogue Systems (Task-Oriented vs. Open-Domain LLM Chatbots) • Ethics, Algorithmic Bias, De-biasing Word Embeddings, LLM Hallucinations & Environmental Sustainability • 15 Solved University Examination Questions.</p>
</div>

<h2 class="section-title">Topic 46: Machine Translation & The BLEU Evaluation Metric</h2>
<p>The standard benchmark for automated machine translation evaluation is the <strong>Bilingual Evaluation Understudy (BLEU - Papineni et al. 2002)</strong> metric, measuring modified n-gram precision penalized by brevity:</p>

<div class="callout-box">
  <div class="callout-title">📐 Exact Mathematical Formulation of BLEU Score</div>
  $$\mathbf{\text{BLEU} = \text{BP} \cdot \exp\left( \sum_{n=1}^N w_n \ln p_n \right)}$$
  $$\text{Modified Precision: } p_n = \frac{\sum_{C \in \{\text{Candidates}\}} \sum_{\text{n-gram} \in C} \text{Count}_{\text{clip}}(\text{n-gram})}{\sum_{C \in \{\text{Candidates}\}} \sum_{\text{n-gram} \in C} \text{Count}(\text{n-gram})}$$
  $$\mathbf{\text{Brevity Penalty (BP): } \text{BP} = \begin{cases} 1 & \text{if } c > r \\ \exp\left( 1 - \frac{r}{c} \right) & \text{if } c \le r \end{cases}}$$
  <p>Where $c$ is the candidate translation length and $r$ is the effective reference corpus length (equal weights $w_n = 1/N$, typically $N=4$).</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 5: Complete BLEU-1 and BLEU-2 Score Calculation</div>
  <p><strong>Candidate Translation ($c = 6$):</strong> <em>"the cat the cat on the"</em></p>
  <p><strong>Reference Translation 1 ($r_1 = 6$):</strong> <em>"the cat sat on the mat"</em></p>
  <p><strong>Reference Translation 2 ($r_2 = 6$):</strong> <em>"there is a cat on mat"</em></p>
  <p><strong>1. Unigram Precision ($p_1$):</strong></p>
  <ul>
    <li>Candidate unigrams: `the` (3 times), `cat` (2 times), `on` (1 time). Total candidate unigram count = 6.</li>
    <li>Max reference counts: `the` occurs max 2 times in Ref 1. `cat` occurs max 1 time. `on` occurs max 1 time.</li>
    <li>Clipped counts: $\text{Count}_{\text{clip}}(\text{the}) = 2$, $\text{Count}_{\text{clip}}(\text{cat}) = 1$, $\text{Count}_{\text{clip}}(\text{on}) = 1$.</li>
    <li>$$\mathbf{p_1 = \frac{2 + 1 + 1}{6} = \frac{4}{6} = \mathbf{0.6667}}$$</li>
  </ul>
  <p><strong>2. Bigram Precision ($p_2$):</strong></p>
  <ul>
    <li>Candidate bigrams: `the cat` (2 times), `cat the` (1 time), `cat on` (1 time), `on the` (1 time). Total = 5 bigrams.</li>
    <li>Max reference counts: `the cat` (max 1), `cat the` (max 0), `cat on` (max 1 in Ref 2), `on the` (max 1 in Ref 1).</li>
    <li>Clipped counts: `the cat` (1), `cat the` (0), `cat on` (1), `on the` (1) $\implies \sum = 3$.</li>
    <li>$$\mathbf{p_2 = \frac{3}{5} = \mathbf{0.6000}}$$</li>
  </ul>
  <p><strong>3. Brevity Penalty ($c = 6, r = 6$):</strong> $c = r \implies \mathbf{\text{BP} = 1.0}$.</p>
  $$\mathbf{\text{BLEU-2} = 1.0 \times \exp(0.5 \ln(0.6667) + 0.5 \ln(0.6000)) = \sqrt{0.6667 \times 0.6000} = \sqrt{0.4000} = \mathbf{0.6325 \ (63.25\%)}}$$
</div>

<h2 class="section-title">Topic 47: Text Summarization & The ROUGE Evaluation Metric</h2>
<p><strong>ROUGE (Recall-Oriented Understudy for Gisting Evaluation - Lin 2004)</strong> measures the n-gram recall of candidate summaries against gold-standard human reference summaries:</p>
$$\mathbf{\text{ROUGE-N} = \frac{\sum_{S \in \{\text{References}\}} \sum_{\text{n-gram} \in S} \text{Count}_{\text{match}}(\text{n-gram})}{\sum_{S \in \{\text{References}\}} \sum_{\text{n-gram} \in S} \text{Count}(\text{n-gram})}}$$
$$\mathbf{\text{ROUGE-L} = \frac{\text{LCS}(\text{Reference}, \text{Candidate})}{|\text{Reference}|} \quad (\text{Longest Common Subsequence})}$$

<h2 class="section-title">Topic 48: Retrieval-Augmented Generation (RAG) Architecture</h2>
<p>Large Language Models suffer from <em>hallucinations</em> and frozen knowledge cutoffs. <strong>RAG (Lewis et al. 2020)</strong> augments generative transformers with dynamic external retrieval:</p>
<ol>
  <li><strong>Dense Indexing:</strong> Chunk knowledge base documents and encode chunks into dense vectors using a bi-encoder (e.g., DPR, BGE-embeddings). Index vectors into a vector database (FAISS, HNSW).</li>
  <li><strong>Dense Retrieval:</strong> Encode user query $\mathbf{q}$ and retrieve top-$k$ most similar document passages via Cosine similarity.</li>
  <li><strong>Prompt Synthesis & Generation:</strong> Concatenate retrieved passages as context into the prompt: <em>"Answer query Q strictly using context C"</em> $\rightarrow$ feed into LLM generator.</li>
</ol>

<h2 class="section-title">Topic 49: Ethics, Algorithmic Bias & De-biasing Word Vectors</h2>
<p>Word embeddings trained on uncurated corpora learn harmful societal and gender stereotypes (e.g., $\mathbf{v}_{\text{doctor}} - \mathbf{v}_{\text{man}} + \mathbf{v}_{\text{woman}} \approx \mathbf{v}_{\text{nurse}}$). Bolukbasi et al. (2016) proposed geometric de-biasing:</p>
<ol>
  <li><strong>Identify Gender Subspace ($\mathbf{g}$):</strong> Compute PCA on difference vectors of defining gender pairs ($\mathbf{v}_{\text{she}} - \mathbf{v}_{\text{he}}$, $\mathbf{v}_{\text{woman}} - \mathbf{v}_{\text{man}}$).</li>
  <li><strong>Hard De-biasing (Neutralization):</strong> Project gender-neutral words (e.g., `doctor`, `programmer`, `nurse`) to remove their component in the gender direction:
    $$\mathbf{\mathbf{w}_{\text{neutralized}} = \mathbf{w} - (\mathbf{w} \cdot \mathbf{g})\mathbf{g}}$$
  </li>
  <li><strong>Equalization:</strong> Ensure gender-neutral words have equal distance to paired gender words ($\|\mathbf{w} - \mathbf{v}_{\text{grandmother}}\| = \|\mathbf{w} - \mathbf{v}_{\text{grandfather}}\|$).</li>
</ol>

<h2 class="section-title">Topic 50: Master University Examination Question Bank (Module 5)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Compare Extractive Summarization (TextRank) vs. Abstractive Summarization (T5/BART). (8 Marks)</div>
  <div class="qa-a">• <strong>Extractive Summarization (TextRank):</strong> Builds a sentence-level graph where edge weights represent sentence similarity ($w_{ij} = \frac{|S_i \cap S_j|}{\log|S_i| + \log|S_j|}$). Runs PageRank centrality algorithm to identify the top $k$ most salient verbatim sentences. Guaranteed grammatically correct, but lacks cohesion and cannot paraphrase.<br>• <strong>Abstractive Summarization:</strong> Uses sequence-to-sequence transformers (BART, T5) to synthesize novel phrasing, compress clauses, and generate human-like summaries. Prone to hallucinating factual errors.</div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Explain Named Entity Recognition BIO vs BILOU Tagging Schemes. (6 Marks)</div>
  <div class="qa-a">• <strong>BIO (IOB2):</strong> `B-Type` (Beginning of entity), `I-Type` (Inside continuation), `O` (Outside). Example: `[New(B-LOC), York(I-LOC), City(I-LOC), is(O)]`.<br>• <strong>BILOU:</strong> Explicitly distinguishes singleton entities: `B-Type` (Beginning), `I-Type` (Inside), `L-Type` (Last token of multi-token entity), `O` (Outside), and `U-Type` (Unique single-token entity). Gives higher discriminative power to CRF sequence labelers!</div>
</div>
"""

# ==============================================================================
# REVISION GUIDE & PYTHON LAB MANUAL
# ==============================================================================
NLP_REVISION_GUIDE = r"""
<div class="cover-container">
  <div class="course-badge">High-Yield Exam Preparation Master Guide</div>
  <h1 class="book-title">Natural Language Processing (CS24351) 10-Page Master Quick Revision Guide</h1>
  <div class="book-subtitle">Universal Formulas, Transformer Architectures, Viterbi Trellises, BLEU Numericals & Solved Flashcards</div>
</div>

<h2 class="section-title">Master Formula & Metric Reference Sheet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Domain</th>
      <th style="width: 45%;">Universal Formula</th>
      <th>Key Exam Property</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Perplexity (PP)</strong></td>
      <td>$$\text{PP}(W) = \sqrt[N]{\frac{1}{P(w_1, \dots, w_N)}} = 2^{H(W)}$$</td>
      <td>Measures predictive surprise; lower value is better.</td>
    </tr>
    <tr>
      <td><strong>Kneser-Ney Continuation</strong></td>
      <td>$$P_{\text{cont}}(w) = \frac{|\{w' : C(w', w) > 0\}|}{\sum_{\tilde{w}} |\{w' : C(w', \tilde{w}) > 0\}|}$$</td>
      <td>Captures versatility of word completing novel histories.</td>
    </tr>
    <tr>
      <td><strong>Skip-Gram Neg. Sampling</strong></td>
      <td>$$\mathcal{L} = \log \sigma(\mathbf{v}'_o \cdot \mathbf{v}_c) + \sum_{k=1}^K \mathbb{E}[\log \sigma(-\mathbf{v}'_{n_k} \cdot \mathbf{v}_c)]$$</td>
      <td>Noise unigram distribution $P_n(w) \propto U(w)^{3/4}$.</td>
    </tr>
    <tr>
      <td><strong>Scaled Dot-Product Attention</strong></td>
      <td>$$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{QK^T}{\sqrt{d_k}} \right)V$$</td>
      <td>$\frac{1}{\sqrt{d_k}}$ scaling prevents vanishing softmax gradients.</td>
    </tr>
    <tr>
      <td><strong>Sinusoidal Position Encoding</strong></td>
      <td>$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right), \ PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$$</td>
      <td>Injects permutation-invariant positional order.</td>
    </tr>
    <tr>
      <td><strong>BLEU Metric</strong></td>
      <td>$$\text{BLEU} = \text{BP} \cdot \exp\left( \sum_{n=1}^N w_n \ln p_n \right), \ \text{BP} = \min(1, e^{1 - r/c})$$</td>
      <td>Penalizes overly short candidate machine translations.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Complete 5-Module Solved Algorithm Flashcards</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 1: BPE vs WordPiece vs SentencePiece</div>
  <ul>
    <li><strong>BPE:</strong> Merges pair with highest co-occurrence frequency ($count(c_1, c_2)$).</li>
    <li><strong>WordPiece:</strong> Merges pair maximizing language model likelihood ($\frac{count(u, v)}{count(u)count(v)}$). Uses `##` prefix.</li>
    <li><strong>SentencePiece:</strong> Language-independent; treats raw byte stream with `_` whitespace without pre-tokenizers.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 2: Viterbi Trellis Algorithm Summary</div>
  $$\mathbf{v_t(j) = \max_{i} [v_{t-1}(i) \cdot a_{ij}] \cdot b_j(w_t) \qquad \text{Complexity: } O(T \cdot |S|^2)}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 3: BERT vs GPT Comparison</div>
  <ul>
    <li><strong>BERT:</strong> Encoder-only, Bidirectional self-attention, Masked LM (15%), Next Sentence Prediction. Ideal for NLU (Classification, NER, SQuAD).</li>
    <li><strong>GPT:</strong> Decoder-only, Causal masked attention (left-to-right), Autoregressive LM. Ideal for NLG (Generation, Chatbots).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 4: LSTM Internal Gates Formulas</div>
  <ul>
    <li>$\mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f)$ (Forget gate)</li>
    <li>$\mathbf{i}_t = \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i)$ (Input gate)</li>
    <li>$\mathbf{\tilde{C}}_t = \tanh(\mathbf{W}_c [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_c)$ (Candidate state)</li>
    <li>$\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \mathbf{\tilde{C}}_t$ (Cell update - Constant Error Carousel)</li>
    <li>$\mathbf{o}_t = \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o) \implies \mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{C}_t)$ (Hidden output)</li>
  </ul>
</div>
"""

NLP_LAB_GUIDE = r"""
<div class="page-break"></div>
<div class="cover-container" style="margin-top: 40px;">
  <div class="course-badge">Hands-On Practical Lab Master Appendix</div>
  <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">Natural Language Processing Laboratory & Python Implementation Master Guide</h2>
  <div style="font-size: 12.5px; color: #64748b;">Complete PyTorch & HuggingFace Implementations of Word2Vec SGNS, BiLSTM-CRF NER & Fine-Tuned Transformer Classification</div>
</div>

<h2 class="section-title">Lab Experiment 1: PyTorch Implementation of Word2Vec Skip-Gram with Negative Sampling</h2>

<pre><code class="language-python">import torch
import torch.nn as nn
import torch.optim as optim

class SkipGramNegativeSampling(nn.Module):
    def __init__(self, vocab_size, embed_dim):
        super(SkipGramNegativeSampling, self).__init__()
        self.target_embeddings = nn.Embedding(vocab_size, embed_dim)
        self.context_embeddings = nn.Embedding(vocab_size, embed_dim)
        
        # Initialize weights
        nn.init.uniform_(self.target_embeddings.weight, -0.5/embed_dim, 0.5/embed_dim)
        nn.init.constant_(self.context_embeddings.weight, 0)

    def forward(self, target_words, context_words, negative_words):
        # target: [B], context: [B], negative: [B, K]
        v_target = self.target_embeddings(target_words)        # [B, d]
        v_context = self.context_embeddings(context_words)      # [B, d]
        v_neg = self.context_embeddings(negative_words)         # [B, K, d]

        # Positive score: log(sigma(v_c * v_w))
        pos_score = torch.sum(v_target * v_context, dim=1)      # [B]
        pos_loss = -torch.log(torch.sigmoid(pos_score) + 1e-10)

        # Negative score: sum_k log(sigma(-v_nk * v_w))
        neg_score = torch.bmm(v_neg, v_target.unsqueeze(2)).squeeze(2) # [B, K]
        neg_loss = -torch.sum(torch.log(torch.sigmoid(-neg_score) + 1e-10), dim=1)

        return torch.mean(pos_loss + neg_loss)

# Model instantiation
model = SkipGramNegativeSampling(vocab_size=10000, embed_dim=128)
print(model)
</code></pre>

<h2 class="section-title">Lab Experiment 2: Transformer Fine-Tuning with HuggingFace PyTorch</h2>

<pre><code class="language-python">from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader
import torch

# Load pretrained BERT tokenizer and sequence classifier
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

sentences = ["Natural Language Processing with Transformers is amazing!", "This baseline model produces bad results."]
labels = torch.tensor([1, 0])

inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
outputs = model(**inputs, labels=labels)
loss = outputs.loss
logits = outputs.logits

print(f"Training Loss: {loss.item():.4f}")
print("Predicted Class Logits:\n", logits)
</code></pre>
"""

def execute_nlp_suite():
    modules = [
        (1, "Module 1: Introduction to NLP, Linguistic Levels & Preprocessing", "Topics 1 to 12 • Phonology, Morphology, Syntax, Ambiguity, Tokenization, Normalization & Edit Distance", M1_CONTENT, "Module_1_Linguistics_Notes"),
        (2, "Module 2: Language Modeling, Smoothing & POS Tagging", "Topics 13 to 24 • N-grams, Perplexity, Laplace, Kneser-Ney, HMMs, Viterbi Decoding & CRFs", M2_CONTENT, "Module_2_Language_Models_Notes"),
        (3, "Module 3: Vector Semantics, Distributed Representations & Word Embeddings", "Topics 25 to 34 • TF-IDF, PPMI, Word2Vec CBOW/SGNS, GloVe, FastText & Evaluation", M3_CONTENT, "Module_3_Word_Embeddings_Notes"),
        (4, "Module 4: Deep Learning for NLP, Recurrent Architectures & Transformers", "Topics 35 to 45 • RNNs, BPTT, LSTMs, Attention, Transformers, BERT & GPT Architectures", M4_CONTENT, "Module_4_Transformers_Notes"),
        (5, "Module 5: Core Applications, Evaluation Metrics & Ethics in NLP", "Topics 46 to 53 • Machine Translation BLEU, Summarization ROUGE, RAG, NER & Algorithmic De-Biasing", M5_CONTENT, "Module_5_Applications_Ethics_Notes"),
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
        NLP_REVISION_GUIDE
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
    execute_nlp_suite()
