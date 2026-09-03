#!/usr/bin/env python3
"""
Generates rich, publication-grade interactive landing pages with live all.md viewers
for all 6 subjects:
- compiler-design.html
- dccn.html
- data-mining.html
- artificial-intelligence.html
- natural-language-processing.html
- software-engineering.html
"""

import os, json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SUBJECTS = [
    {
        "file": "compiler-design.html",
        "slug": "compiler-design",
        "code": "CS24301",
        "name": "Compiler Design",
        "credits": "3.0 Credits",
        "type": "Theory Core",
        "desc": "Exhaustive coverage of Lexical Analysis (DFA/NFA, Thompson's Construction), Top-Down LL(1) Parsing, Bottom-Up LR(0)/SLR(1)/CLR(1)/LALR(1) Parsing, Syntax Directed Definitions (SDD/SDTS), Intermediate 3-Address Code Generation, Runtime Activation Records, Dynamic Memory Heap, Basic Block Control Flow Graphs (CFG), and Global Loop Optimization.",
        "folder": "compiler-design",
        "master_pdf": "compiler-design/pdf/Compiler_Design_Full_Course_Master.pdf",
        "master_pages": "54 Pages",
        "rev_pdf": "compiler-design/pdf/Compiler_Design_10_Page_Master_Revision.pdf",
        "rev_pages": "13 Pages",
        "all_pdf": "compiler-design/pdf/all.pdf",
        "all_pages": "43 Pages",
        "all_md": "compiler-design/all.md",
        "modules": [
            ("Module 1", "Lexical Analysis & Direct DFA", "compiler-design/html/Module_1_Lexical_Analysis_Notes.html", "compiler-design/pdf/Module_1_Lexical_Analysis_Notes.pdf", "12 Pages"),
            ("Module 2", "Syntax Analysis & LR Parsers", "compiler-design/html/Module_2_Syntax_Analysis_Notes.html", "compiler-design/pdf/Module_2_Syntax_Analysis_Notes.pdf", "11 Pages"),
            ("Module 3", "Semantic Analysis & TAC", "compiler-design/html/Module_3_Semantic_Analysis_Notes.html", "compiler-design/pdf/Module_3_Semantic_Analysis_Notes.pdf", "10 Pages"),
            ("Module 4", "Runtime & Activation Records", "compiler-design/html/Module_4_Runtime_Environment_Notes.html", "compiler-design/pdf/Module_4_Runtime_Environment_Notes.pdf", "10 Pages"),
            ("Module 5", "Code Optimization & DAG", "compiler-design/html/Module_5_Code_Optimization_Notes.html", "compiler-design/pdf/Module_5_Code_Optimization_Notes.pdf", "10 Pages"),
        ]
    },
    {
        "file": "dccn.html",
        "slug": "data-communication-and-networks",
        "code": "CS24305",
        "name": "Data Communication & Computer Networks",
        "credits": "3.0 Credits",
        "type": "Theory Core",
        "desc": "Exhaustive coverage of Data Communication Models, Physical Media & Signal Attenuation, Nyquist & Shannon Limits, Line Coding (Manchester, 4B/5B), Carrier Modulation (QAM, BPSK), Multiplexing (FDM, TDM, WDM), Error Control (CRC-32, Hamming Codes), Sliding Window ARQ (GBN, Selective Repeat), CSMA/CD & Ethernet, Spanning Tree Protocol (STP), IPv4/IPv6 Subnetting & CIDR, Dijkstra/Bellman-Ford Routing, TCP Congestion Control (AIMD, Reno), and Socket Programming.",
        "folder": "data-communication-and-networks",
        "master_pdf": "data-communication-and-networks/pdf/DCCN_Full_Course_Master.pdf",
        "master_pages": "56 Pages",
        "rev_pdf": "data-communication-and-networks/pdf/DCCN_10_Page_Master_Revision.pdf",
        "rev_pages": "13 Pages",
        "all_pdf": "data-communication-and-networks/pdf/all.pdf",
        "all_pages": "56 Pages",
        "all_md": "data-communication-and-networks/all.md",
        "modules": [
            ("Module 1", "Data Communication Overview & Channels", "data-communication-and-networks/html/Module_1_Data_Communication_Overview_Notes.html", "data-communication-and-networks/pdf/Module_1_Data_Communication_Overview_Notes.pdf", "10 Pages"),
            ("Module 2", "Data Encoding & Multiplexing", "data-communication-and-networks/html/Module_2_Data_Encoding_Multiplexing_Notes.html", "data-communication-and-networks/pdf/Module_2_Data_Encoding_Multiplexing_Notes.pdf", "10 Pages"),
            ("Module 3", "Data Link Control & Error ARQ", "data-communication-and-networks/html/Module_3_Data_Link_Control_Notes.html", "data-communication-and-networks/pdf/Module_3_Data_Link_Control_Notes.pdf", "10 Pages"),
            ("Module 4", "Switching & Switched LANs", "data-communication-and-networks/html/Module_4_Switching_LANs_Notes.html", "data-communication-and-networks/pdf/Module_4_Switching_LANs_Notes.pdf", "10 Pages"),
            ("Module 5", "Networking & Transport TCP/IP", "data-communication-and-networks/html/Module_5_Networking_Transport_Notes.html", "data-communication-and-networks/pdf/Module_5_Networking_Transport_Notes.pdf", "10 Pages"),
        ]
    },
    {
        "file": "data-mining.html",
        "slug": "data-mining",
        "code": "CS24303",
        "name": "Data Mining Concepts and Techniques",
        "credits": "3.0 Credits",
        "type": "Theory Core",
        "desc": "Exhaustive coverage of KDD Pipeline, Attribute Types & Proximity Dissimilarity Measures, Data Cleaning & Normalization (Z-score, Min-Max, Decimal Scaling), OLAP Data Warehousing (Star, Snowflake, Constellation Schemas), Frequent Itemset Mining (Apriori Algorithm, FP-Growth Tree, ECLAT), Association Rules, Correlation Metrics (Chi-Square, Lift), Constraint-Based Mining, Classification, and Clustering.",
        "folder": "data-mining",
        "master_pdf": "data-mining/pdf/Data_Mining_Full_Course_Master.pdf",
        "master_pages": "15 Pages",
        "rev_pdf": "data-mining/pdf/Data_Mining_10_Page_Master_Revision.pdf",
        "rev_pages": "5 Pages",
        "all_pdf": "data-mining/pdf/all.pdf",
        "all_pages": "51 Pages",
        "all_md": "data-mining/all.md",
        "modules": [
            ("Module 1", "Data Attributes & Proximity Metrics", "data-mining/html/Module_1_Data_Attributes_Notes.html", "data-mining/pdf/Module_1_Data_Attributes_Notes.pdf", "4 Pages"),
            ("Module 2", "Preprocessing & Normalization", "data-mining/html/Module_2_Preprocessing_Notes.html", "data-mining/pdf/Module_2_Preprocessing_Notes.pdf", "3 Pages"),
            ("Module 3", "Data Warehousing & OLAP Cubes", "data-mining/html/Module_3_Data_Warehouse_Notes.html", "data-mining/pdf/Module_3_Data_Warehouse_Notes.pdf", "3 Pages"),
            ("Module 4", "Apriori & FP-Growth Pattern Mining", "data-mining/html/Module_4_Pattern_Mining_Notes.html", "data-mining/pdf/Module_4_Pattern_Mining_Notes.pdf", "3 Pages"),
            ("Module 5", "Advanced Mining & Constraints", "data-mining/html/Module_5_Advanced_Mining_Notes.html", "data-mining/pdf/Module_5_Advanced_Mining_Notes.pdf", "3 Pages"),
        ]
    },
    {
        "file": "artificial-intelligence.html",
        "slug": "artificial-intelligence",
        "code": "CS24307",
        "name": "Artificial Intelligence",
        "credits": "3.0 Credits",
        "type": "Theory Core",
        "desc": "Exhaustive coverage of Intelligent Agents & PEAS Environments, Uninformed vs Informed Search (BFS, DFS, Uniform Cost, A*, IDA*), Game Playing (Minimax Algorithm, Alpha-Beta Pruning), Propositional & First-Order Logic (FOL Resolution Refutation, Unification), Classical Planning (STRIPS, PDDL), Probabilistic Reasoning (Bayesian Networks, Conditional Independence), and Machine Learning Foundations (Perceptrons, Multi-Layer Perceptrons, Backpropagation).",
        "folder": "artificial-intelligence",
        "master_pdf": "artificial-intelligence/pdf/AI_Full_Course_Master.pdf",
        "master_pages": "12 Pages",
        "rev_pdf": "artificial-intelligence/pdf/AI_10_Page_Master_Revision.pdf",
        "rev_pages": "4 Pages",
        "all_pdf": "artificial-intelligence/pdf/all.pdf",
        "all_pages": "47 Pages",
        "all_md": "artificial-intelligence/all.md",
        "modules": [
            ("Module 1", "Intelligent Agents & PEAS Framework", "artificial-intelligence/html/Module_1_Intelligent_Agents_Notes.html", "artificial-intelligence/pdf/Module_1_Intelligent_Agents_Notes.pdf", "3 Pages"),
            ("Module 2", "Search Strategies & Game Trees", "artificial-intelligence/html/Module_2_Search_Algorithms_Notes.html", "artificial-intelligence/pdf/Module_2_Search_Algorithms_Notes.pdf", "2 Pages"),
            ("Module 3", "Knowledge & Logic Resolution", "artificial-intelligence/html/Module_3_Knowledge_Logic_Notes.html", "artificial-intelligence/pdf/Module_3_Knowledge_Logic_Notes.pdf", "3 Pages"),
            ("Module 4", "Planning & Bayesian Networks", "artificial-intelligence/html/Module_4_Planning_Bayes_Notes.html", "artificial-intelligence/pdf/Module_4_Planning_Bayes_Notes.pdf", "2 Pages"),
            ("Module 5", "Machine Learning & MLP Networks", "artificial-intelligence/html/Module_5_Machine_Learning_Notes.html", "artificial-intelligence/pdf/Module_5_Machine_Learning_Notes.pdf", "2 Pages"),
        ]
    },
    {
        "file": "natural-language-processing.html",
        "slug": "natural-language-processing",
        "code": "CS24351",
        "name": "Natural Language Processing",
        "credits": "3.0 Credits",
        "type": "Program Elective",
        "desc": "Exhaustive coverage of NLP Pipelines (Tokenization, Lemmatization, Stemming, Regex), N-Gram Statistical Language Modeling & Smoothing (Laplace, Good-Turing, Kneser-Ney), Hidden Markov Models & Viterbi POS Tagging, Word Embeddings (TF-IDF, CBOW, Skip-Gram Word2Vec, GloVe), Recurrent Neural Networks (LSTM, GRU), Transformer Multi-Head Self-Attention Architecture, Pre-Trained LLMs (BERT, GPT), and Machine Translation Evaluation (BLEU, ROUGE).",
        "folder": "natural-language-processing",
        "master_pdf": "natural-language-processing/pdf/NLP_Full_Course_Master.pdf",
        "master_pages": "12 Pages",
        "rev_pdf": "natural-language-processing/pdf/NLP_10_Page_Master_Revision.pdf",
        "rev_pages": "6 Pages",
        "all_pdf": "natural-language-processing/pdf/all.pdf",
        "all_pages": "39 Pages",
        "all_md": "natural-language-processing/all.md",
        "modules": [
            ("Module 1", "NLP Pipeline & Morphology", "natural-language-processing/html/Module_1_Linguistics_Notes.html", "natural-language-processing/pdf/Module_1_Linguistics_Notes.pdf", "3 Pages"),
            ("Module 2", "Language Models & N-grams", "natural-language-processing/html/Module_2_Language_Models_Notes.html", "natural-language-processing/pdf/Module_2_Language_Models_Notes.pdf", "3 Pages"),
            ("Module 3", "Word2Vec & POS Tagging", "natural-language-processing/html/Module_3_Word_Embeddings_Notes.html", "natural-language-processing/pdf/Module_3_Word_Embeddings_Notes.pdf", "2 Pages"),
            ("Module 4", "Transformers & Multi-Head Attn", "natural-language-processing/html/Module_4_Transformers_Notes.html", "natural-language-processing/pdf/Module_4_Transformers_Notes.pdf", "2 Pages"),
            ("Module 5", "LLMs, Ethics & Evaluation", "natural-language-processing/html/Module_5_Applications_Ethics_Notes.html", "natural-language-processing/pdf/Module_5_Applications_Ethics_Notes.pdf", "2 Pages"),
        ]
    },
    {
        "file": "software-engineering.html",
        "slug": "software-engineering",
        "code": "CS24353",
        "name": "Software Engineering",
        "credits": "3.0 Credits",
        "type": "Program Elective",
        "desc": "Exhaustive coverage of Software Process Models (Waterfall, Prototyping, Spiral, RAD, Incremental, Agile Scrum/Kanban), Requirements Engineering & SRS (IEEE 830 Standard), UML Architectural Modeling & Design Patterns, Software Project Estimation (COCOMO I/II, Function Point Analysis), Risk Management (RMMM Plan), Software Quality Assurance (CMMI, ISO 9001), Software Testing (Black-Box Equivalence/BVA, White-Box Basis Path Cyclomatic Complexity), and Maintenance.",
        "folder": "software-engineering",
        "master_pdf": "software-engineering/pdf/SE_Full_Course_Master.pdf",
        "master_pages": "59 Pages",
        "rev_pdf": "software-engineering/pdf/SE_10_Page_Master_Revision.pdf",
        "rev_pages": "6 Pages",
        "all_pdf": "software-engineering/pdf/all.pdf",
        "all_pages": "36 Pages",
        "all_md": "software-engineering/all.md",
        "modules": [
            ("Module 1", "Process Models & Agile", "software-engineering/html/Module_1_Process_Models_Notes.html", "software-engineering/pdf/Module_1_Process_Models_Notes.pdf", "10 Pages"),
            ("Module 2", "Requirements Engineering & SRS", "software-engineering/html/Module_2_Requirements_Notes.html", "software-engineering/pdf/Module_2_Requirements_Notes.pdf", "10 Pages"),
            ("Module 3", "Design Engineering & UML 2.5", "software-engineering/html/Module_3_Design_UML_Notes.html", "software-engineering/pdf/Module_3_Design_UML_Notes.pdf", "10 Pages"),
            ("Module 4", "Testing Methodologies & Reliability", "software-engineering/html/Module_4_Testing_QA_Notes.html", "software-engineering/pdf/Module_4_Testing_QA_Notes.pdf", "10 Pages"),
            ("Module 5", "Project Estimation & CMMI Quality", "software-engineering/html/Module_5_Estimation_CMMI_Notes.html", "software-engineering/pdf/Module_5_Estimation_CMMI_Notes.pdf", "10 Pages"),
        ]
    }
]

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>{name} ({code}) | BIT Mesra CSE 5th Semester Master Study Suite</title>
  <meta name="title" content="{name} ({code}) — Master Study Notes, PDF Books & Solved PYQs">
  <meta name="description" content="Publication-grade master study guide for {name} ({code}) at BIT Mesra. Complete 10-15 page module notes, {master_pages} full textbook, 10-page master revision, formulas, and solved university exam bank.">
  <meta name="keywords" content="{name}, {code}, BIT Mesra, CSE 5th Sem, Study Notes, Formula Sheet, PYQ Solutions, Master PDF, all.pdf">
  <meta name="author" content="Shaswat Raj (BIT Mesra CSE)">
  <link rel="canonical" href="https://sh20raj.github.io/study/{file}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://sh20raj.github.io/study/{file}">
  <meta property="og:title" content="{name} ({code}) | BIT Mesra Study Suite">
  <meta property="og:description" content="{desc}">
  
  <!-- Fonts & KaTeX & Markdown Rendering -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

  <style>
    :root {{
      --bg: #0b0f19;
      --bg-surface: #111827;
      --bg-card: #1f2937;
      --border: #374151;
      --text-main: #f9fafb;
      --text-muted: #9ca3af;
      --primary: #3b82f6;
      --primary-hover: #60a5fa;
      --accent: #8b5cf6;
      --radius: 12px;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    [data-theme="light"] {{
      --bg: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: #ffffff;
      --border: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.6;
      transition: background-color 0.3s, color 0.3s;
    }}
    header {{
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(12px);
    }}
    .header-container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}
    .brand {{ display: flex; align-items: center; gap: 12px; text-decoration: none; color: var(--text-main); }}
    .brand-icon {{
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 20px;
    }}
    .brand-title {{ font-size: 17px; font-weight: 800; }}
    .brand-subtitle {{ font-size: 11.5px; color: var(--text-muted); }}
    .nav-actions {{ display: flex; align-items: center; gap: 10px; }}
    .nav-btn {{
      padding: 8px 14px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--text-main);
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
    }}
    .nav-btn:hover {{ border-color: var(--primary); color: var(--primary); }}
    
    .main-container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 32px 24px 60px 24px;
      flex: 1;
      width: 100%;
    }}
    
    .subject-hero {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 32px;
      box-shadow: var(--shadow);
    }}
    .badge-row {{ display: flex; gap: 10px; margin-bottom: 12px; align-items: center; }}
    .badge {{ font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; }}
    .badge-primary {{ background: rgba(59, 130, 246, 0.15); color: var(--primary); }}
    .badge-code {{ font-family: 'Fira Code', monospace; background: var(--bg-card); border: 1px solid var(--border); color: var(--text-muted); }}
    
    .subject-title {{ font-size: 32px; font-weight: 800; margin-bottom: 12px; letter-spacing: -0.5px; }}
    .subject-desc {{ font-size: 14.5px; color: var(--text-muted); line-height: 1.65; max-width: 950px; margin-bottom: 24px; }}
    
    .downloads-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}
    .download-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      text-decoration: none;
      color: var(--text-main);
      transition: var(--transition);
    }}
    .download-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px -6px rgba(0,0,0,0.3);
    }}
    .download-info h4 {{ font-size: 14px; font-weight: 700; margin-bottom: 4px; }}
    .download-info p {{ font-size: 11.5px; color: var(--text-muted); }}
    .download-icon {{ font-size: 20px; color: var(--primary); }}

    .modules-section {{ margin-bottom: 36px; }}
    .section-heading {{ font-size: 20px; font-weight: 800; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
    .modules-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
      gap: 14px;
    }}
    .mod-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 10px;
      transition: var(--transition);
    }}
    .mod-card:hover {{ border-color: var(--primary); }}
    .mod-card-title {{ font-size: 13px; font-weight: 700; }}
    .mod-card-sub {{ font-size: 11px; color: var(--text-muted); }}
    .mod-actions {{ display: flex; gap: 8px; margin-top: 4px; }}
    .mod-btn {{
      flex: 1;
      padding: 6px;
      text-align: center;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-main);
      text-decoration: none;
      transition: var(--transition);
    }}
    .mod-btn:hover {{ border-color: var(--primary); color: var(--primary); }}

    /* Markdown Reader Section */
    .notes-viewer {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      box-shadow: var(--shadow);
    }}
    .notes-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
      margin-bottom: 24px;
    }}
    .markdown-body {{
      font-size: 13.5px;
      line-height: 1.7;
      color: var(--text-main);
    }}
    .markdown-body h1 {{ font-size: 24px; margin: 24px 0 14px 0; color: var(--primary); border-bottom: 1px solid var(--border); padding-bottom: 8px; }}
    .markdown-body h2 {{ font-size: 19px; margin: 22px 0 10px 0; color: var(--primary-hover); border-bottom: 1px solid var(--border); padding-bottom: 6px; }}
    .markdown-body h3 {{ font-size: 16px; margin: 18px 0 8px 0; color: var(--text-main); }}
    .markdown-body p {{ margin-bottom: 12px; text-align: justify; }}
    .markdown-body pre {{ background: #0f172a; color: #f8fafc; padding: 14px 18px; border-radius: 8px; overflow-x: auto; margin: 14px 0; font-family: 'Fira Code', monospace; font-size: 12px; }}
    .markdown-body code {{ font-family: 'Fira Code', monospace; font-size: 12px; background: var(--bg-card); color: var(--primary); padding: 2px 6px; border-radius: 4px; }}
    .markdown-body pre code {{ background: transparent; color: inherit; padding: 0; }}
    .markdown-body table {{ width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 12.5px; }}
    .markdown-body th, .markdown-body td {{ border: 1px solid var(--border); padding: 8px 12px; text-align: left; }}
    .markdown-body th {{ background: var(--bg-card); color: var(--text-main); font-weight: 700; }}
    .markdown-body blockquote {{ border-left: 4px solid var(--primary); background: rgba(59, 130, 246, 0.08); padding: 12px 18px; border-radius: 6px; margin: 14px 0; }}
    .markdown-body ul, .markdown-body ol {{ padding-left: 24px; margin-bottom: 14px; }}
    .markdown-body li {{ margin-bottom: 6px; }}
    
    footer {{ background: var(--bg-surface); border-top: 1px solid var(--border); padding: 24px; text-align: center; font-size: 12.5px; color: var(--text-muted); }}
  </style>
</head>
<body>

  <header>
    <div class="header-container">
      <a href="index.html" class="brand">
        <div class="brand-icon"><i class="fa-solid fa-arrow-left"></i></div>
        <div>
          <div class="brand-title">{name} ({code})</div>
          <div class="brand-subtitle">BIT Mesra CSE 5th Semester Master Portal</div>
        </div>
      </a>
      <div class="nav-actions">
        <button id="themeToggle" class="nav-btn"><i class="fa-solid fa-moon"></i></button>
        <a href="index.html" class="nav-btn"><i class="fa-solid fa-house"></i> All Courses</a>
        <a href="https://github.com/SH20RAJ/study" target="_blank" class="nav-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </header>

  <main class="main-container">
    <div class="subject-hero">
      <div class="badge-row">
        <span class="badge badge-primary">{type}</span>
        <span class="badge badge-code">{code} • {credits}</span>
      </div>
      <h1 class="subject-title">{name}</h1>
      <p class="subject-desc">{desc}</p>
      
      <div class="downloads-grid">
        <a href="{master_pdf}" target="_blank" class="download-card">
          <div class="download-info">
            <h4><i class="fa-solid fa-book-open"></i> Full Course Master Book</h4>
            <p>{master_pages} • Complete Syllabus + Solved PYQs</p>
          </div>
          <div class="download-icon"><i class="fa-solid fa-file-pdf"></i></div>
        </a>
        <a href="{rev_pdf}" target="_blank" class="download-card">
          <div class="download-info">
            <h4><i class="fa-solid fa-bolt"></i> 10-Page Master Quick Revision</h4>
            <p>{rev_pages} • Formulas, Matrices & Flashcards</p>
          </div>
          <div class="download-icon"><i class="fa-solid fa-file-pdf"></i></div>
        </a>
        <a href="{all_pdf}" target="_blank" class="download-card">
          <div class="download-info">
            <h4><i class="fa-solid fa-download"></i> Download all.pdf</h4>
            <p>{all_pages} • Compiled Master Notes</p>
          </div>
          <div class="download-icon"><i class="fa-solid fa-file-arrow-down"></i></div>
        </a>
      </div>
    </div>

    <!-- Modules Section -->
    <section class="modules-section">
      <h2 class="section-heading"><i class="fa-solid fa-folder-open"></i> Individual Module Notes</h2>
      <div class="modules-grid">
        {module_cards}
      </div>
    </section>

    <!-- Master Markdown Reader Section -->
    <section class="notes-viewer" id="notes">
      <div class="notes-header">
        <div>
          <h2 style="font-size: 18px; font-weight: 800;"><i class="fa-solid fa-file-lines"></i> Complete Master Notes (all.md)</h2>
          <p style="font-size: 12px; color: var(--text-muted);">Rendered live with KaTeX mathematical formulas & code syntax</p>
        </div>
        <div>
          <a href="{all_pdf}" target="_blank" class="nav-btn" style="background: var(--primary); color: #fff; border-color: var(--primary);"><i class="fa-solid fa-file-pdf"></i> Get PDF</a>
        </div>
      </div>
      <div class="markdown-body" id="markdownContent">
        <p style="text-align: center; color: var(--text-muted); padding: 40px 0;"><i class="fa-solid fa-spinner fa-spin"></i> Loading master notes...</p>
      </div>
    </section>
  </main>

  <footer>
    <p>🎓 <strong>BIT Mesra CSE 5th Semester Study Hub</strong> • {name} ({code})</p>
  </footer>

  <script>
    // Theme Toggle
    const themeToggle = document.getElementById('themeToggle');
    const currentTheme = localStorage.getItem('theme') || 'dark';
    if (currentTheme === 'light') {{
      document.documentElement.setAttribute('data-theme', 'light');
      themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
    }}
    themeToggle.addEventListener('click', () => {{
      const isLight = document.documentElement.getAttribute('data-theme') === 'light';
      if (isLight) {{
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'dark');
        themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
      }} else {{
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
        themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
      }}
    }});

    // Fetch and render all.md
    fetch('{all_md}')
      .then(res => res.text())
      .then(text => {{
        const contentDiv = document.getElementById('markdownContent');
        contentDiv.innerHTML = marked.parse(text);
        if (window.renderMathInElement) {{
          renderMathInElement(contentDiv, {{
            delimiters: [
              {{left: '$$', right: '$$', display: true}},
              {{left: '$', right: '$', display: false}}
            ]
          }});
        }}
      }})
      .catch(err => {{
        document.getElementById('markdownContent').innerHTML = '<p style="color: #ef4444;">Failed to load markdown content.</p>';
      }});
  </script>
</body>
</html>"""

def build_subject_pages():
    for sub in SUBJECTS:
        mod_cards = []
        for mod_num, mod_title, mod_html, mod_pdf, pages in sub["modules"]:
            mod_cards.append(f"""
            <div class="mod-card">
              <div>
                <div class="mod-card-title">{mod_num}: {mod_title}</div>
                <div class="mod-card-sub">{pages}</div>
              </div>
              <div class="mod-actions">
                <a href="{mod_html}" target="_blank" class="mod-btn"><i class="fa-solid fa-eye"></i> View</a>
                <a href="{mod_pdf}" target="_blank" class="mod-btn"><i class="fa-solid fa-download"></i> PDF</a>
              </div>
            </div>
            """)
        
        page_html = PAGE_TEMPLATE.format(
            file=sub["file"],
            slug=sub["slug"],
            code=sub["code"],
            name=sub["name"],
            credits=sub["credits"],
            type=sub["type"],
            desc=sub["desc"],
            master_pdf=sub["master_pdf"],
            master_pages=sub["master_pages"],
            rev_pdf=sub["rev_pdf"],
            rev_pages=sub["rev_pages"],
            all_pdf=sub["all_pdf"],
            all_pages=sub["all_pages"],
            all_md=sub["all_md"],
            module_cards="".join(mod_cards)
        )
        
        out_path = os.path.join(ROOT_DIR, sub["file"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"✅ Generated rich subject landing page: {sub['file']}")

if __name__ == "__main__":
    build_subject_pages()
