# 🎓 B.Tech CSE 5th Semester — Master Study Guide & Syllabus
**Birla Institute of Technology (BIT), Mesra | NEP Scheme (2024–25)**

> **Student:** Shaswat Raj  
> **Academic Program:** B.Tech in Computer Science & Engineering (3rd Year, 5th Semester)  
> **Total Credits:** **26.0 Credits**  
> **Workspace Status:** Organized & Tracked across all Theory, Lab, and Elective Courses.

---

## 📌 Semester Structure & Subject Catalog

```
                               5TH SEMESTER CSE (26.0 CREDITS)
                                             |
         +-----------------------------------+-----------------------------------+
         |                                   |                                   |
   THEORY CORE (12.0 Cr)               LAB CORE (4.5 Cr)                ELECTIVES (6.0 Cr)
   • Compiler Design                   • Compiler Design Lab            • Natural Language Proc.
   • Data Comm. & Networks             • DCCN Lab                       • Software Engineering
   • Data Mining Concepts              • AI Lab                         • Open Elective - II
   • Artificial Intelligence           (Plus Project-I: 2.0 Cr)         (Comm. Skill-II: 1.5 Cr)
```

### 💎 Core Theory Courses (12.0 Credits)
| Course Code | Subject Title | Credits | Workspace Directory | Syllabus & Notes |
| :--- | :--- | :---: | :--- | :---: |
| **CS24301** | [Compiler Design](file:///Users/shaswatraj/Desktop/study/compiler-design/) | 3.0 | [`compiler-design/`](file:///Users/shaswatraj/Desktop/study/compiler-design/) | [View Syllabus](file:///Users/shaswatraj/Desktop/study/compiler-design/compiler_design_syllabus.md) |
| **CS24305** | [Data Communication and Computer Networks](file:///Users/shaswatraj/Desktop/study/data-communication-and-networks/) | 3.0 | [`data-communication-and-networks/`](file:///Users/shaswatraj/Desktop/study/data-communication-and-networks/) | [View Syllabus](file:///Users/shaswatraj/Desktop/study/data-communication-and-networks/dccn_syllabus.md) |
| **CS24303** | [Data Mining Concepts and Techniques](file:///Users/shaswatraj/Desktop/study/data-mining/) | 3.0 | [`data-mining/`](file:///Users/shaswatraj/Desktop/study/data-mining/) | [View Syllabus](file:///Users/shaswatraj/Desktop/study/data-mining/data_mining_syllabus.md) |
| **CS24307** | [Artificial Intelligence](file:///Users/shaswatraj/Desktop/study/artificial-intelligence/) | 3.0 | [`artificial-intelligence/`](file:///Users/shaswatraj/Desktop/study/artificial-intelligence/) | [View Syllabus](file:///Users/shaswatraj/Desktop/study/artificial-intelligence/ai_syllabus.md) |

### 🏷️ Practical / Laboratory Courses (4.5 Credits)
| Course Code | Lab Title | Credits | Workspace Directory | Syllabus & Practical Tasks |
| :--- | :--- | :---: | :--- | :---: |
| **CS24302** | [Compiler Design Lab](file:///Users/shaswatraj/Desktop/study/compiler-design/lab/) | 1.5 | [`compiler-design/lab/`](file:///Users/shaswatraj/Desktop/study/compiler-design/lab/) | [Lab Tasks](file:///Users/shaswatraj/Desktop/study/compiler-design/compiler_design_syllabus.md#-compiler-design-lab-cs24302) |
| **CS24306** | [Data Communication & Networks Lab](file:///Users/shaswatraj/Desktop/study/data-communication-and-networks/lab/) | 1.5 | [`data-communication-and-networks/lab/`](file:///Users/shaswatraj/Desktop/study/data-communication-and-networks/lab/) | [Lab Tasks](file:///Users/shaswatraj/Desktop/study/data-communication-and-networks/dccn_lab_syllabus.md) |
| **CS24308** | [Artificial Intelligence Lab](file:///Users/shaswatraj/Desktop/study/artificial-intelligence/lab/) | 1.5 | [`artificial-intelligence/lab/`](file:///Users/shaswatraj/Desktop/study/artificial-intelligence/lab/) | [Lab Tasks](file:///Users/shaswatraj/Desktop/study/artificial-intelligence/ai_lab_syllabus.md) |

### ❤️ Program Electives (3.0 Credits)
| Course Code | Elective Subject | Credits | Workspace Directory | Syllabus & Notes |
| :--- | :--- | :---: | :--- | :---: |
| **CS24351** | [Natural Language Processing](file:///Users/shaswatraj/Desktop/study/natural-language-processing/) | 3.0 | [`natural-language-processing/`](file:///Users/shaswatraj/Desktop/study/natural-language-processing/) | [View Syllabus](file:///Users/shaswatraj/Desktop/study/natural-language-processing/nlp_syllabus.md) |
| **CS24353** | [Software Engineering](file:///Users/shaswatraj/Desktop/study/software-engineering/) | 3.0 | [`software-engineering/`](file:///Users/shaswatraj/Desktop/study/software-engineering/) | [View Syllabus](file:///Users/shaswatraj/Desktop/study/software-engineering/software_engineering_syllabus.md) |

---

## 📖 Complete Syllabus Overview by Subject

### 1. 🏛️ Compiler Design (`CS24301` & `CS24302`)
- **Module I – Lexical Analysis:** Cousins of compiler, 6 Phases of compilation, Tokens/Patterns/Lexemes, Input buffering (Buffer Pairs & Sentinels), Regular Expressions, Thompson's Construction, Subset Construction, Hopcroft DFA Minimization, Direct DFA Construction (Syntax Tree Method: `nullable`, `firstpos`, `lastpos`, `followpos`).
- **Module II – Syntax Analysis:** Context-Free Grammars, Derivations, Ambiguity, Left Recursion elimination, Left Factoring, LL(1) Parsing Table construction, FIRST & FOLLOW sets, Shift-Reduce Parsing, LR(0), SLR(1), Canonical LR(1), LALR(1), Parsing conflicts, Error recovery (Panic mode, phrase level).
- **Module III – Semantic Analysis & Intermediate Code Generation:** SDD (S-attributed vs L-attributed), SDTS, Symbol Tables, Type systems & checking, Three Address Code (Quadruples, Triples, Indirect Triples), Array address calculations (Row-major & Column-major).
- **Module IV – Advanced Intermediate Code Generation & Runtime Environment:** Boolean expression translation (short-circuit), Control flow constructs (`if-else`, `while`), Backpatching (`makelist`, `merge`, `backpatch`), Procedure calls, Runtime storage layout, Activation Records (Dynamic/Static links, parameter passing).
- **Module V – Code Generation & Optimization:** Basic blocks, Leader statements, Control Flow Graphs (CFG), DAG representation, Machine-independent optimizations (Constant folding/propagation, Common subexpression elimination, Dead code elimination, Loop-invariant code motion), Target code emission, Register allocation, Peephole optimization.

---

### 2. 🌐 Data Communication and Computer Networks (`CS24305` & `CS24306`)
- **Module I – Data Communications & Networking Overview:** Communications model, Data transmission concepts, Analog vs Digital transmission, Transmission impairments (Attenuation, Delay distortion, Noise), Nyquist and Shannon channel capacity, OSI 7-Layer reference model, TCP/IP architecture, Standards & protocol layers.
- **Module II – Transmission Media & Signal Encoding:** Guided media (Twisted pair, Coaxial, Optical fiber), Wireless propagation (Ground, Sky, Line-of-sight), Digital signaling (NRZ-L, NRZ-I, Manchester, Differential Manchester), Analog signaling (ASK, FSK, PSK, QAM), Modulation techniques.
- **Module III – Error Handling, Data Link Control & Multiplexing:** Types of errors, Error detection (Parity, Checksum, CRC-12/16/32), Error correction (Hamming code), Flow control (Stop-and-Wait, Sliding Window), Error control (Go-Back-N, Selective Repeat ARQ), HDLC protocol, FDM, TDM, WDM.
- **Module IV – WANs, LANs & Cellular Systems:** Circuit switching vs Packet switching (Datagram vs Virtual Circuit), Principles of cellular networks, Cellular generations (1G to 5G), LAN architectures, Ethernet (IEEE 802.3), Wireless LAN (IEEE 802.11 Wi-Fi), VLANs.
- **Module V – Internetworking, Routing & Application Protocols:** IPv4/IPv6 addressing, Subnetting, CIDR, Transport protocols (TCP 3-way handshake, UDP), Routing algorithms (Dijkstra's shortest path, Distance Vector / Bellman-Ford, Link State / OSPF, BGP), Congestion control, Application protocols (DNS, DHCP, HTTP, SMTP, FTP).

---

### 3. ⛏️ Data Mining Concepts and Techniques (`CS24303`)
- **Module I – Introduction to Data Mining:** Data mining functionalities, Classification of data mining systems, Major issues in data mining, Relational databases, Data warehouses, Transactional databases, Data objects and attribute types (Nominal, Binary, Ordinal, Numeric), Statistical descriptions, Measuring similarity and dissimilarity (Euclidean, Manhattan, Cosine, Jaccard).
- **Module II – Data Preprocessing:** Data cleaning (Handling missing values, Smoothing noisy data), Data integration (Redundancy, Correlation analysis $\chi^2$), Data transformation (Normalization, Min-Max, Z-score), Data reduction (PCA, Sampling, Wavelets), Data discretization and concept hierarchy generation.
- **Module III – Data Warehousing & OLAP:** Data warehouse modeling, Data cube, Multidimensional data models (Star, Snowflake, Fact Constellation schemas), OLAP operations (Roll-up, Drill-down, Slice, Dice, Pivot), Data warehouse architecture & implementation, Attribute-Oriented Induction (AOI).
- **Module IV – Frequent Pattern Mining:** Basic concepts, Association rules, Support and Confidence metrics, Apriori algorithm, Apriori property, Join and Prune steps, FP-Growth algorithm (FP-Tree construction and conditional pattern bases), Pattern evaluation methods (Lift, Chi-Square).
- **Module V – Advanced Pattern Mining:** Multilevel pattern mining, Multidimensional association rule mining, Constraint-based mining, Mining high-dimensional data, Mining colossal patterns, Compressed and approximate patterns, Real-world applications.

---

### 4. 🤖 Artificial Intelligence (`CS24307` & `CS24308`)
- **Module I – Preliminaries & Intelligent Agents:** What is AI?, Turing Test, Evolution and Foundations of AI, Intelligent Agents, Rationality, PEAS description (Performance measure, Environment, Actuators, Sensors), Environment properties (Observable, Deterministic, Episodic, Static, Discrete, Single/Multi-agent), Agent architectures (Simple reflex, Model-based, Goal-based, Utility-based, Learning agents).
- **Module II – Problem Solving & Search Strategies:** Formulating search problems, State space search, Uninformed search (BFS, DFS, Uniform-Cost Search, Depth-Limited, Iterative Deepening), Informed (Heuristic) search ($A^*$, Greedy Best-First, Admissibility and Consistency of heuristics), Local search (Hill Climbing, Simulated Annealing, Genetic Algorithms), Adversarial Search (Game trees, Minimax algorithm, Alpha-Beta pruning).
- **Module III – Knowledge Representation & Reasoning:** Knowledge-based agents, Wumpus World environment, Propositional Logic (Syntax, Semantics, Entailment, Model checking), Inference rules, Resolution refutation in Propositional Logic, First-Order Predicate Logic (FOPL) syntax & semantics, Quantifiers, Knowledge engineering in FOPL, Forward chaining, Backward chaining, Resolution in FOL (Unification, Skolemization, Conjunctive Normal Form).
- **Module IV – Planning & Probabilistic Reasoning:** Classical Planning (STRIPS, PDDL representation), Components of planning problem, Goal Stack Planning, Planning Graph, Reasoning under uncertainty, Axioms of probability, Bayes' Rule, Bayesian Networks (Inference, Conditional Independence, D-separation), Exact and approximate probabilistic inference.
- **Module V – Machine Learning Foundations:** Forms of learning (Supervised, Unsupervised, Reinforcement), Rote learning, Inductive learning, Decision Trees (Entropy, Information Gain, ID3/C4.5), Formal learning theory (PAC learning, Occam's Razor), Neural network learning (Perceptron, Multi-Layer Perceptrons, Backpropagation), Overfitting, Underfitting, Regularization.

---

### 5. 🗣️ Natural Language Processing (`CS24351`)
- **Module I – Introduction to NLP & Text Preprocessing:** Definition and applications of NLP, Components of natural language (Morphology, Syntax, Semantics, Pragmatics), Text preprocessing pipeline (Tokenization, Sentence segmentation, Stemming / Porter Stemmer, Lemmatization, Stop-word removal, Normalization), Regular Expressions for NLP, Language models overview.
- **Module II – Syntax Analysis, Parsing & Language Models:** $N$-gram language models, Maximum Likelihood Estimation (MLE), Perplexity, Smoothing techniques (Laplace add-1, Add-$k$, Good-Turing, Kneser-Ney), Part-of-Speech (POS) Tagging (Rule-based, Hidden Markov Models, Viterbi algorithm), Syntactic parsing, Context-Free Grammars (CFGs), Top-down and bottom-up parsing, Probabilistic CFGs (PCFGs), Dependency Parsing, Evaluation metrics (Precision, Recall, F1-Score).
- **Module III – Semantics & Lexical Resources:** Lexical semantics, Word senses and relationships (Synonymy, Antonymy, Hyponymy, Hypernymy), Word Sense Disambiguation (WSD: Lesk algorithm, supervised WSD), WordNet database, Semantic similarity measures, Vector Space Models (Bag-of-Words, TF-IDF), Distributed representations, Word Embeddings (Word2Vec: Skip-gram & CBOW, GloVe, FastText).
- **Module IV – Neural Approaches to NLP:** Convolutional Neural Networks (CNNs) for text, Sequence modeling (Recurrent Neural Networks, Vanishing gradient problem, LSTMs, GRUs), Sequence-to-Sequence (Seq2Seq) models, Attention Mechanism, Transformer Architecture (Self-Attention, Multi-Head Attention, Positional Encoding), Pretrained Language Models (BERT, GPT, Transfer Learning in NLP).
- **Module V – NLP Applications & Ethics:** Text Classification, Sentiment Analysis, Named Entity Recognition (NER), Machine Translation (Rule-based, Statistical MT, Neural MT), Dialogue Systems & Conversational Chatbots, Ethics in NLP (Algorithmic bias, Fairness, Toxicity mitigation, Explainability).

---

### 6. ⚙️ Software Engineering (`CS24353`)
- **Module I – Introduction & Software Process Models:** Definitions of Software Engineering, Software crises and myths, Evolving role of software, Software Process Models (Linear Sequential / Waterfall, Prototyping, Incremental, RAD, Spiral, Agile methodologies: Scrum, XP, Kanban), Project management activities (Planning, Scheduling, Risk management, WBS, PERT/CPM charts).
- **Module II – Software Requirements Engineering:** Functional vs Non-Functional requirements, User vs System requirements, Software Requirements Specification (SRS), IEEE standard 830 for SRS, Requirements engineering process (Feasibility study, Requirements elicitation techniques, Requirements analysis and modeling, Requirements validation, Requirements management and traceability).
- **Module III – Software Design Engineering:** Design concepts (Abstraction, Modularity, Information Hiding, Refinement, Refactoring), Design quality guidelines, Architectural design styles, Component-level design, Object-Oriented Design principles (SOLID), Coupling and Cohesion metrics, Unified Modeling Language (UML: Use Case, Class, Sequence, Collaboration, Activity, Statechart diagrams).
- **Module IV – Verification, Validation & Software Testing:** V&V concepts, Software inspections and walkthroughs, Static vs Dynamic analysis, Testing taxonomy, Black-box testing (Equivalence Partitioning, Boundary Value Analysis, Cause-Effect graphing), White-box testing (Basis Path testing, Cyclomatic Complexity calculation, Control Structure testing, Dataflow testing), Testing levels (Unit testing, Integration testing: Top-down/Bottom-up, System testing, Acceptance testing), Regression testing, Software reliability metrics (MTTF, MTBF, Availability).
- **Module V – Project Estimation, Quality Assurance & Maintenance:** Software metrics (Process, Project, Product metrics), Project estimation techniques (LOC, Function Points analysis), Empirical estimation models (COCOMO I & COCOMO II), Software Quality Assurance (SQA plan, ISO 9000, SEI CMM / CMMI levels), Software Configuration Management (SCM: Version control, Change control), Software Maintenance (Corrective, Adaptive, Perfective, Preventive), Software Re-engineering and Reverse engineering.

---

## 📊 Comprehensive 5th Semester Study Tracker

| Subject Code | Subject Name | Type | Modules Tracked | Current Status |
| :---: | :--- | :---: | :---: | :---: |
| **CS24301** | Compiler Design | Theory | 5 Modules | 🟡 M1 Completed (Notes & PDF Generated) |
| **CS24302** | Compiler Design Lab | Practical | 5 Lab Modules | ⬜ Not Started |
| **CS24305** | Data Communication & Networks | Theory | 5 Modules | ⬜ Not Started |
| **CS24306** | Data Communication & Networks Lab | Practical | 5 Lab Modules | ⬜ Not Started |
| **CS24303** | Data Mining Concepts and Techniques | Theory | 5 Modules | ⬜ Not Started |
| **CS24307** | Artificial Intelligence | Theory | 5 Modules | ⬜ Not Started |
| **CS24308** | Artificial Intelligence Lab | Practical | 5 Lab Modules | ⬜ Not Started |
| **CS24351** | Natural Language Processing | Elective | 5 Modules | ⬜ Not Started |
| **CS24353** | Software Engineering | Elective | 5 Modules | ⬜ Not Started |

---
*Maintained for B.Tech Computer Science & Engineering 5th Semester — BIT Mesra.*
