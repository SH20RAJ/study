#!/usr/bin/env python3
"""
Updates index.html and all 6 subject landing pages with:
1. Direct links to all.md and all.pdf
2. Updated DCCN 10-page module links and 56-page master book
3. Semantic URL slugs (#compiler-design, #dccn, #data-mining, etc.)
4. Comprehensive SEO (OpenGraph, Twitter Card, Schema.org JSON-LD)
5. Interactive Markdown viewer for all.md files
"""

import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Primary Meta Tags -->
  <title>BIT Mesra CSE 5th Semester Master Study Suite (NEP Scheme 2024–25) — 50+ Page Master Books, Formulas & Solved PYQs</title>
  <meta name="title" content="BIT Mesra CSE 5th Semester Master Study Suite (NEP Scheme 2024–25)">
  <meta name="description" content="Publication-grade master study portal for B.Tech Computer Science & Engineering 5th Semester at BIT Mesra. Complete 10-15 page module notes, 50+ page master textbooks, 10-page quick revisions, formulas, and solved examination question banks for CD, DCCN, DMCT, AI, NLP, and SE.">
  <meta name="keywords" content="BIT Mesra, CSE 5th Sem, Compiler Design, Data Communication, Computer Networks, Data Mining, Artificial Intelligence, Natural Language Processing, Software Engineering, CS24301, CS24305, CS24303, CS24307, CS24351, CS24353, Notes, PYQ, Solved Papers, NEP 2024">
  <meta name="author" content="Shaswat Raj (BIT Mesra CSE)">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://sh20raj.github.io/study/">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://sh20raj.github.io/study/">
  <meta property="og:title" content="BIT Mesra CSE 5th Semester Master Study Suite (2024–25)">
  <meta property="og:description" content="Access publication-grade 50+ page master books, 10-page revision guides, and exhaustive solved examination banks for all 5th Sem B.Tech CSE subjects.">
  <meta property="og:image" content="https://sh20raj.github.io/study/preview.png">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://sh20raj.github.io/study/">
  <meta property="twitter:title" content="BIT Mesra CSE 5th Semester Master Study Suite">
  <meta property="twitter:description" content="Publication-grade notes, 10-page revision guides, and full course books for BIT Mesra CSE 5th Sem.">
  <meta property="twitter:image" content="https://sh20raj.github.io/study/preview.png">

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "B.Tech Computer Science & Engineering 5th Semester Study Suite",
    "description": "Comprehensive study portal with publication-grade notes, formula sheets, and solved PYQ question banks for BIT Mesra 5th Semester CSE (NEP Scheme).",
    "provider": {
      "@type": "CollegeOrUniversity",
      "name": "Birla Institute of Technology, Mesra",
      "sameAs": "https://www.bitmesra.ac.in/"
    },
    "hasCourseInstance": [
      {
        "@type": "CourseInstance",
        "name": "Compiler Design (CS24301)",
        "courseCode": "CS24301",
        "description": "Lexical Analysis, LL(1) & LR Parsers, SDD/SDTS, TAC Generation, Activation Records & Optimization."
      },
      {
        "@type": "CourseInstance",
        "name": "Data Communication & Computer Networks (CS24305)",
        "courseCode": "CS24305",
        "description": "Physical Layer Channels, Line Coding, QAM, CRC-32, Sliding Window ARQ, Routing & TCP Congestion Control."
      },
      {
        "@type": "CourseInstance",
        "name": "Data Mining Concepts and Techniques (CS24303)",
        "courseCode": "CS24303",
        "description": "Data Preprocessing, OLAP Data Warehousing, Apriori & FP-Growth Pattern Mining, Classification & Clustering."
      },
      {
        "@type": "CourseInstance",
        "name": "Artificial Intelligence (CS24307)",
        "courseCode": "CS24307",
        "description": "Intelligent Agents, A* Search, Minimax & Alpha-Beta Pruning, FOL Logic, Bayesian Networks & Neural Networks."
      },
      {
        "@type": "CourseInstance",
        "name": "Natural Language Processing (CS24351)",
        "courseCode": "CS24351",
        "description": "N-gram Language Models, Word Embeddings, Transformers, BERT, GPT, and Machine Translation."
      },
      {
        "@type": "CourseInstance",
        "name": "Software Engineering (CS24353)",
        "courseCode": "CS24353",
        "description": "Agile & SDLC Models, Requirements Engineering, UML Architectural Design, COCOMO Estimation & Testing."
      }
    ]
  }
  </script>

  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    :root {
      --bg: #0b0f19;
      --bg-surface: #111827;
      --bg-card: #1f2937;
      --border: #374151;
      --text-main: #f9fafb;
      --text-muted: #9ca3af;
      --primary: #3b82f6;
      --primary-hover: #60a5fa;
      --accent: #8b5cf6;
      --success: #10b981;
      --amber: #f59e0b;
      --cyan: #06b6d4;
      --fuchsia: #d946ef;
      --radius: 12px;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }

    [data-theme="light"] {
      --bg: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: #ffffff;
      --border: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.6;
      transition: background-color 0.3s, color 0.3s;
    }

    header {
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(12px);
    }
    .header-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--text-main);
    }
    .brand-icon {
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 20px;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
    .brand-title {
      font-size: 17px;
      font-weight: 800;
      letter-spacing: -0.3px;
    }
    .brand-subtitle {
      font-size: 11.5px;
      color: var(--text-muted);
    }
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-icon {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-main);
      width: 38px;
      height: 38px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      text-decoration: none;
      transition: var(--transition);
    }
    .btn-icon:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .hero {
      text-align: center;
      padding: 48px 24px 32px 24px;
      max-width: 900px;
      margin: 0 auto;
    }
    .badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      background: rgba(59, 130, 246, 0.12);
      border: 1px solid rgba(59, 130, 246, 0.3);
      color: var(--primary-hover);
      border-radius: 30px;
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 16px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .hero-title {
      font-size: 38px;
      font-weight: 800;
      letter-spacing: -1px;
      margin-bottom: 14px;
      line-height: 1.2;
    }
    .hero-title span {
      background: linear-gradient(135deg, var(--primary), var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-desc {
      font-size: 15.5px;
      color: var(--text-muted);
      max-width: 740px;
      margin: 0 auto;
      line-height: 1.6;
    }

    .filter-section {
      max-width: 1280px;
      margin: 0 auto 32px auto;
      padding: 0 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .search-box {
      position: relative;
      width: 100%;
    }
    .search-box i {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 15px;
    }
    .search-input {
      width: 100%;
      padding: 14px 16px 14px 44px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      color: var(--text-main);
      font-size: 14.5px;
      outline: none;
      transition: var(--transition);
    }
    .search-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
    }

    .filter-tabs {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
    }
    .tab-btn {
      padding: 8px 18px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: var(--transition);
    }
    .tab-btn.active, .tab-btn:hover {
      background: var(--primary);
      border-color: var(--primary);
      color: #ffffff;
    }

    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px 60px 24px;
      flex: 1;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 24px;
    }

    .card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: var(--transition);
      box-shadow: var(--shadow);
      position: relative;
      scroll-margin-top: 80px;
    }
    .card:hover {
      transform: translateY(-4px);
      border-color: var(--primary);
      box-shadow: 0 20px 30px -10px rgba(0, 0, 0, 0.4);
    }
    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 14px;
    }
    .card-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .badge-core { background: rgba(59, 130, 246, 0.15); color: var(--primary); }
    .badge-lab { background: rgba(16, 185, 129, 0.15); color: var(--success); }
    .badge-elective { background: rgba(217, 70, 239, 0.15); color: var(--fuchsia); }

    .card-code {
      font-family: 'Fira Code', monospace;
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 600;
    }
    .card-title {
      font-size: 20px;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 6px;
    }
    .card-desc {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 18px;
    }

    .master-actions {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 12px;
    }
    .secondary-actions {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 18px;
    }
    .btn-action {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      transition: var(--transition);
      text-align: center;
    }
    .btn-primary {
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    .btn-primary:hover {
      opacity: 0.92;
      transform: scale(0.99);
    }
    .btn-secondary {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-main);
    }
    .btn-secondary:hover {
      border-color: var(--primary);
      color: var(--primary);
    }
    .btn-outline {
      background: transparent;
      border: 1px dashed var(--border);
      color: var(--text-muted);
      font-size: 11.5px;
    }
    .btn-outline:hover {
      border-color: var(--accent);
      color: var(--text-main);
    }

    .module-list {
      border-top: 1px solid var(--border);
      padding-top: 14px;
    }
    .module-list-title {
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
    }
    .module-items {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .module-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 7px 10px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 12px;
      transition: var(--transition);
    }
    .module-item:hover {
      border-color: var(--primary);
      background: rgba(59, 130, 246, 0.05);
    }
    .module-item-actions {
      display: flex;
      gap: 8px;
    }
    .module-item-actions a {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13px;
      transition: var(--transition);
    }
    .module-item-actions a:hover {
      color: var(--primary);
    }

    .modal {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 24px;
    }
    .modal.active { display: flex; }
    .modal-content {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      width: 100%;
      max-width: 1050px;
      height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: var(--shadow);
    }
    .modal-header {
      padding: 16px 24px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .modal-title { font-size: 16px; font-weight: 700; }
    .modal-close {
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 20px;
      cursor: pointer;
    }
    .modal-close:hover { color: var(--text-main); }
    .modal-body {
      flex: 1;
      width: 100%;
      height: 100%;
      border: none;
    }

    footer {
      background: var(--bg-surface);
      border-top: 1px solid var(--border);
      padding: 24px;
      text-align: center;
      font-size: 12.5px;
      color: var(--text-muted);
    }
    footer a { color: var(--primary); text-decoration: none; }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-container">
      <a href="#" class="brand">
        <div class="brand-icon"><i class="fa-solid fa-graduation-cap"></i></div>
        <div>
          <div class="brand-title">BIT Mesra CSE 5th Sem Study Hub</div>
          <div class="brand-subtitle">Neuroscience-Backed Study & Revision Suite</div>
        </div>
      </a>
      <div class="nav-actions">
        <button id="themeToggle" class="btn-icon" title="Toggle Theme"><i class="fa-solid fa-moon"></i></button>
        <a href="https://github.com/SH20RAJ/study" target="_blank" class="btn-icon" title="GitHub Repository"><i class="fa-brands fa-github"></i></a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="badge-pill"><i class="fa-solid fa-bolt"></i> NEP 2024–25 Scheme • 26.0 Credits</div>
    <h1 class="hero-title">Master Your <span>5th Semester</span> Exams</h1>
    <p class="hero-desc">
      A publication-grade study portal featuring comprehensive 10–15 page module notes, step-by-step solved PYQs, 10-page master revision booklets, and 50+ page full course books.
    </p>
  </section>

  <!-- Search & Filter Controls -->
  <section class="filter-section">
    <div class="search-box">
      <i class="fa-solid fa-magnifying-glass"></i>
      <input type="text" id="searchInput" class="search-input" placeholder="Search subjects, topics (e.g. LL(1) Parsing, Shannon Capacity, Apriori, Backprop, BLEU)...">
    </div>
    <div class="filter-tabs">
      <button class="tab-btn active" data-filter="all">All Subjects (6)</button>
      <button class="tab-btn" data-filter="core">Theory Core (4)</button>
      <button class="tab-btn" data-filter="elective">Program Electives (2)</button>
    </div>
  </section>

  <!-- Subjects Container -->
  <main class="container">
    <div class="grid" id="subjectsGrid">

      <!-- 1. Compiler Design -->
      <div class="card" id="compiler-design" data-category="core" data-keywords="compiler design lexical syntax semantic parsing lr ll1 intermediate optimization runtime dfa cfg cs24301">
        <div>
          <div class="card-top">
            <span class="card-badge badge-core">Theory Core</span>
            <span class="card-code">CS24301 • 3.0 Cr</span>
          </div>
          <h2 class="card-title"><a href="compiler-design.html" style="color: inherit; text-decoration: none;">Compiler Design</a></h2>
          <p class="card-desc">Lexical analysis, top-down LL(1) & bottom-up LR(1) parsers, SDD/SDTS, TAC generation, activation records & code optimization.</p>
          
          <div class="master-actions">
            <a href="compiler-design/pdf/Compiler_Design_10_Page_Master_Revision.pdf" target="_blank" class="btn-action btn-primary"><i class="fa-solid fa-file-pdf"></i> 10-Page Revision (13p)</a>
            <a href="compiler-design/pdf/Compiler_Design_Full_Course_Master.pdf" target="_blank" class="btn-action btn-secondary"><i class="fa-solid fa-book-open"></i> Master Book (54p)</a>
          </div>
          <div class="secondary-actions">
            <a href="compiler-design.html#notes" class="btn-action btn-outline"><i class="fa-solid fa-file-lines"></i> Read all.md Notes</a>
            <a href="compiler-design/pdf/all.pdf" target="_blank" class="btn-action btn-outline"><i class="fa-solid fa-download"></i> Download all.pdf (43p)</a>
          </div>
        </div>
        <div class="module-list">
          <div class="module-list-title"><span>Module Notes (10–12 Pages Each)</span><span>Read / PDF</span></div>
          <div class="module-items">
            <div class="module-item"><span>M1: Lexical Analysis & Direct DFA</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('compiler-design/html/Module_1_Lexical_Analysis_Notes.html', 'Compiler Design - M1')"><i class="fa-solid fa-eye"></i></a><a href="compiler-design/pdf/Module_1_Lexical_Analysis_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M2: Syntax Analysis & LR Parsers</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('compiler-design/html/Module_2_Syntax_Analysis_Notes.html', 'Compiler Design - M2')"><i class="fa-solid fa-eye"></i></a><a href="compiler-design/pdf/Module_2_Syntax_Analysis_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M3: Semantic Analysis & TAC</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('compiler-design/html/Module_3_Semantic_Analysis_Notes.html', 'Compiler Design - M3')"><i class="fa-solid fa-eye"></i></a><a href="compiler-design/pdf/Module_3_Semantic_Analysis_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M4: Runtime & Activation Records</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('compiler-design/html/Module_4_Runtime_Environment_Notes.html', 'Compiler Design - M4')"><i class="fa-solid fa-eye"></i></a><a href="compiler-design/pdf/Module_4_Runtime_Environment_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M5: Code Optimization & DAG</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('compiler-design/html/Module_5_Code_Optimization_Notes.html', 'Compiler Design - M5')"><i class="fa-solid fa-eye"></i></a><a href="compiler-design/pdf/Module_5_Code_Optimization_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
          </div>
        </div>
      </div>

      <!-- 2. Data Communication & Networks -->
      <div class="card" id="data-communication-and-networks" data-category="core" data-keywords="data communication computer networks dccn osi tcp ip shannon nyquist crc sliding window arq ip routing ethernet wifi cs24305">
        <div>
          <div class="card-top">
            <span class="card-badge badge-core">Theory Core</span>
            <span class="card-code">CS24305 • 3.0 Cr</span>
          </div>
          <h2 class="card-title"><a href="dccn.html" style="color: inherit; text-decoration: none;">Data Communication & Networks</a></h2>
          <p class="card-desc">Layered architectures (OSI & TCP/IP), Shannon/Nyquist capacity, digital encoding, CRC-32, sliding window ARQs, subnetting & TCP congestion.</p>
          
          <div class="master-actions">
            <a href="data-communication-and-networks/pdf/DCCN_10_Page_Master_Revision.pdf" target="_blank" class="btn-action btn-primary"><i class="fa-solid fa-file-pdf"></i> 10-Page Revision (13p)</a>
            <a href="data-communication-and-networks/pdf/DCCN_Full_Course_Master.pdf" target="_blank" class="btn-action btn-secondary"><i class="fa-solid fa-book-open"></i> Master Book (56p)</a>
          </div>
          <div class="secondary-actions">
            <a href="dccn.html#notes" class="btn-action btn-outline"><i class="fa-solid fa-file-lines"></i> Read all.md Notes</a>
            <a href="data-communication-and-networks/pdf/all.pdf" target="_blank" class="btn-action btn-outline"><i class="fa-solid fa-download"></i> Download all.pdf (56p)</a>
          </div>
        </div>
        <div class="module-list">
          <div class="module-list-title"><span>Module Notes (10 Pages Each)</span><span>Read / PDF</span></div>
          <div class="module-items">
            <div class="module-item"><span>M1: Data Comm Overview & Channels</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-communication-and-networks/html/Module_1_Data_Communication_Overview_Notes.html', 'DCCN - M1')"><i class="fa-solid fa-eye"></i></a><a href="data-communication-and-networks/pdf/Module_1_Data_Communication_Overview_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M2: Data Encoding & Multiplexing</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-communication-and-networks/html/Module_2_Data_Encoding_Multiplexing_Notes.html', 'DCCN - M2')"><i class="fa-solid fa-eye"></i></a><a href="data-communication-and-networks/pdf/Module_2_Data_Encoding_Multiplexing_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M3: Data Link Control & Error ARQ</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-communication-and-networks/html/Module_3_Data_Link_Control_Notes.html', 'DCCN - M3')"><i class="fa-solid fa-eye"></i></a><a href="data-communication-and-networks/pdf/Module_3_Data_Link_Control_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M4: Switching & Switched LANs</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-communication-and-networks/html/Module_4_Switching_LANs_Notes.html', 'DCCN - M4')"><i class="fa-solid fa-eye"></i></a><a href="data-communication-and-networks/pdf/Module_4_Switching_LANs_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M5: Networking & Transport TCP/IP</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-communication-and-networks/html/Module_5_Networking_Transport_Notes.html', 'DCCN - M5')"><i class="fa-solid fa-eye"></i></a><a href="data-communication-and-networks/pdf/Module_5_Networking_Transport_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
          </div>
        </div>
      </div>

      <!-- 3. Artificial Intelligence -->
      <div class="card" id="artificial-intelligence" data-category="core" data-keywords="artificial intelligence ai peas search heuristic a* minimax alpha beta logic fol resolution bayesian ml perceptron cs24307">
        <div>
          <div class="card-top">
            <span class="card-badge badge-core">Theory Core</span>
            <span class="card-code">CS24307 • 3.0 Cr</span>
          </div>
          <h2 class="card-title"><a href="artificial-intelligence.html" style="color: inherit; text-decoration: none;">Artificial Intelligence</a></h2>
          <p class="card-desc">Intelligent agents & PEAS, A* heuristic search, Minimax & Alpha-Beta pruning, FOL resolution refutation, Bayesian networks & Backpropagation.</p>
          
          <div class="master-actions">
            <a href="artificial-intelligence/pdf/AI_10_Page_Master_Revision.pdf" target="_blank" class="btn-action btn-primary"><i class="fa-solid fa-file-pdf"></i> 10-Page Revision</a>
            <a href="artificial-intelligence/pdf/AI_Full_Course_Master.pdf" target="_blank" class="btn-action btn-secondary"><i class="fa-solid fa-book-open"></i> Full Master Book</a>
          </div>
          <div class="secondary-actions">
            <a href="artificial-intelligence.html#notes" class="btn-action btn-outline"><i class="fa-solid fa-file-lines"></i> Read all.md Notes</a>
            <a href="artificial-intelligence/pdf/all.pdf" target="_blank" class="btn-action btn-outline"><i class="fa-solid fa-download"></i> Download all.pdf (47p)</a>
          </div>
        </div>
        <div class="module-list">
          <div class="module-list-title"><span>Module Notes</span><span>Read / PDF</span></div>
          <div class="module-items">
            <div class="module-item"><span>M1: Intelligent Agents & PEAS</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('artificial-intelligence/html/Module_1_Intelligent_Agents_Notes.html', 'AI - M1')"><i class="fa-solid fa-eye"></i></a><a href="artificial-intelligence/pdf/Module_1_Intelligent_Agents_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M2: Search & Game AI</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('artificial-intelligence/html/Module_2_Search_Algorithms_Notes.html', 'AI - M2')"><i class="fa-solid fa-eye"></i></a><a href="artificial-intelligence/pdf/Module_2_Search_Algorithms_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M3: Knowledge & Logic Resolution</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('artificial-intelligence/html/Module_3_Knowledge_Logic_Notes.html', 'AI - M3')"><i class="fa-solid fa-eye"></i></a><a href="artificial-intelligence/pdf/Module_3_Knowledge_Logic_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M4: Planning & Bayesian Networks</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('artificial-intelligence/html/Module_4_Planning_Bayes_Notes.html', 'AI - M4')"><i class="fa-solid fa-eye"></i></a><a href="artificial-intelligence/pdf/Module_4_Planning_Bayes_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M5: Machine Learning & MLP</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('artificial-intelligence/html/Module_5_Machine_Learning_Notes.html', 'AI - M5')"><i class="fa-solid fa-eye"></i></a><a href="artificial-intelligence/pdf/Module_5_Machine_Learning_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
          </div>
        </div>
      </div>

      <!-- 4. Data Mining -->
      <div class="card" id="data-mining" data-category="core" data-keywords="data mining kdd olap data warehouse apriori fp growth association rules chi square normalization pca cs24303">
        <div>
          <div class="card-top">
            <span class="card-badge badge-core">Theory Core</span>
            <span class="card-code">CS24303 • 3.0 Cr</span>
          </div>
          <h2 class="card-title"><a href="data-mining.html" style="color: inherit; text-decoration: none;">Data Mining Concepts</a></h2>
          <p class="card-desc">KDD pipeline, proximity metrics, data preprocessing & normalization, OLAP cubes, Apriori & FP-Growth pattern mining, and constraint handling.</p>
          
          <div class="master-actions">
            <a href="data-mining/pdf/Data_Mining_10_Page_Master_Revision.pdf" target="_blank" class="btn-action btn-primary"><i class="fa-solid fa-file-pdf"></i> 10-Page Revision</a>
            <a href="data-mining/pdf/Data_Mining_Full_Course_Master.pdf" target="_blank" class="btn-action btn-secondary"><i class="fa-solid fa-book-open"></i> Full Master Book</a>
          </div>
          <div class="secondary-actions">
            <a href="data-mining.html#notes" class="btn-action btn-outline"><i class="fa-solid fa-file-lines"></i> Read all.md Notes</a>
            <a href="data-mining/pdf/all.pdf" target="_blank" class="btn-action btn-outline"><i class="fa-solid fa-download"></i> Download all.pdf (51p)</a>
          </div>
        </div>
        <div class="module-list">
          <div class="module-list-title"><span>Module Notes</span><span>Read / PDF</span></div>
          <div class="module-items">
            <div class="module-item"><span>M1: Data Attributes & Proximity</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-mining/html/Module_1_Data_Attributes_Notes.html', 'DM - M1')"><i class="fa-solid fa-eye"></i></a><a href="data-mining/pdf/Module_1_Data_Attributes_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M2: Preprocessing & Normalization</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-mining/html/Module_2_Preprocessing_Notes.html', 'DM - M2')"><i class="fa-solid fa-eye"></i></a><a href="data-mining/pdf/Module_2_Preprocessing_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M3: Data Warehousing & OLAP</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-mining/html/Module_3_Data_Warehouse_Notes.html', 'DM - M3')"><i class="fa-solid fa-eye"></i></a><a href="data-mining/pdf/Module_3_Data_Warehouse_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M4: Apriori & FP-Growth</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-mining/html/Module_4_Pattern_Mining_Notes.html', 'DM - M4')"><i class="fa-solid fa-eye"></i></a><a href="data-mining/pdf/Module_4_Pattern_Mining_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M5: Advanced Mining & Constraints</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('data-mining/html/Module_5_Advanced_Mining_Notes.html', 'DM - M5')"><i class="fa-solid fa-eye"></i></a><a href="data-mining/pdf/Module_5_Advanced_Mining_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
          </div>
        </div>
      </div>

      <!-- 5. Natural Language Processing -->
      <div class="card" id="natural-language-processing" data-category="elective" data-keywords="natural language processing nlp word2vec tf idf transformers bert gpt pos viterbi smoothing bleu cs24351">
        <div>
          <div class="card-top">
            <span class="card-badge badge-elective">Program Elective</span>
            <span class="card-code">CS24351 • 3.0 Cr</span>
          </div>
          <h2 class="card-title"><a href="natural-language-processing.html" style="color: inherit; text-decoration: none;">Natural Language Processing</a></h2>
          <p class="card-desc">Tokenization & lemmatization, N-gram smoothing, HMM Viterbi POS tagging, CBOW & Skip-Gram Word2Vec, Transformer attention & BLEU.</p>
          
          <div class="master-actions">
            <a href="natural-language-processing/pdf/NLP_10_Page_Master_Revision.pdf" target="_blank" class="btn-action btn-primary"><i class="fa-solid fa-file-pdf"></i> 10-Page Revision</a>
            <a href="natural-language-processing/pdf/NLP_Full_Course_Master.pdf" target="_blank" class="btn-action btn-secondary"><i class="fa-solid fa-book-open"></i> Full Master Book</a>
          </div>
          <div class="secondary-actions">
            <a href="natural-language-processing.html#notes" class="btn-action btn-outline"><i class="fa-solid fa-file-lines"></i> Read all.md Notes</a>
            <a href="natural-language-processing/pdf/all.pdf" target="_blank" class="btn-action btn-outline"><i class="fa-solid fa-download"></i> Download all.pdf (39p)</a>
          </div>
        </div>
        <div class="module-list">
          <div class="module-list-title"><span>Module Notes</span><span>Read / PDF</span></div>
          <div class="module-items">
            <div class="module-item"><span>M1: NLP Pipeline & Morphology</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('natural-language-processing/html/Module_1_Linguistics_Notes.html', 'NLP - M1')"><i class="fa-solid fa-eye"></i></a><a href="natural-language-processing/pdf/Module_1_Linguistics_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M2: Language Models & N-grams</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('natural-language-processing/html/Module_2_Language_Models_Notes.html', 'NLP - M2')"><i class="fa-solid fa-eye"></i></a><a href="natural-language-processing/pdf/Module_2_Language_Models_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M3: Word2Vec & POS Tagging</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('natural-language-processing/html/Module_3_Word_Embeddings_Notes.html', 'NLP - M3')"><i class="fa-solid fa-eye"></i></a><a href="natural-language-processing/pdf/Module_3_Word_Embeddings_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M4: Transformers & Multi-Head Attn</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('natural-language-processing/html/Module_4_Transformers_Notes.html', 'NLP - M4')"><i class="fa-solid fa-eye"></i></a><a href="natural-language-processing/pdf/Module_4_Transformers_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M5: LLMs, Ethics & Evaluation</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('natural-language-processing/html/Module_5_Applications_Ethics_Notes.html', 'NLP - M5')"><i class="fa-solid fa-eye"></i></a><a href="natural-language-processing/pdf/Module_5_Applications_Ethics_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
          </div>
        </div>
      </div>

      <!-- 6. Software Engineering -->
      <div class="card" id="software-engineering" data-category="elective" data-keywords="software engineering se agile scrum waterfall requirements srs uml cocomo cyclomatic cmmi cs24353">
        <div>
          <div class="card-top">
            <span class="card-badge badge-elective">Program Elective</span>
            <span class="card-code">CS24353 • 3.0 Cr</span>
          </div>
          <h2 class="card-title"><a href="software-engineering.html" style="color: inherit; text-decoration: none;">Software Engineering</a></h2>
          <p class="card-desc">Agile & Waterfall process models, SRS specification, UML architectural design patterns, COCOMO II estimation & McCabe cyclomatic testing.</p>
          
          <div class="master-actions">
            <a href="software-engineering/pdf/SE_10_Page_Master_Revision.pdf" target="_blank" class="btn-action btn-primary"><i class="fa-solid fa-file-pdf"></i> 10-Page Revision</a>
            <a href="software-engineering/pdf/SE_Full_Course_Master.pdf" target="_blank" class="btn-action btn-secondary"><i class="fa-solid fa-book-open"></i> Full Master Book</a>
          </div>
          <div class="secondary-actions">
            <a href="software-engineering.html#notes" class="btn-action btn-outline"><i class="fa-solid fa-file-lines"></i> Read all.md Notes</a>
            <a href="software-engineering/pdf/all.pdf" target="_blank" class="btn-action btn-outline"><i class="fa-solid fa-download"></i> Download all.pdf (35p)</a>
          </div>
        </div>
        <div class="module-list">
          <div class="module-list-title"><span>Module Notes</span><span>Read / PDF</span></div>
          <div class="module-items">
            <div class="module-item"><span>M1: Process Models & Agile</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('software-engineering/html/Module_1_Process_Models_Notes.html', 'SE - M1')"><i class="fa-solid fa-eye"></i></a><a href="software-engineering/pdf/Module_1_Process_Models_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M2: Requirements & SRS</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('software-engineering/html/Module_2_Requirements_Notes.html', 'SE - M2')"><i class="fa-solid fa-eye"></i></a><a href="software-engineering/pdf/Module_2_Requirements_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M3: Design & UML Modeling</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('software-engineering/html/Module_3_Design_Notes.html', 'SE - M3')"><i class="fa-solid fa-eye"></i></a><a href="software-engineering/pdf/Module_3_Design_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M4: COCOMO & Risk Analysis</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('software-engineering/html/Module_4_Estimation_Notes.html', 'SE - M4')"><i class="fa-solid fa-eye"></i></a><a href="software-engineering/pdf/Module_4_Estimation_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
            <div class="module-item"><span>M5: Testing & CMMI Quality</span><div class="module-item-actions"><a href="javascript:void(0)" onclick="openReader('software-engineering/html/Module_5_Testing_Notes.html', 'SE - M5')"><i class="fa-solid fa-eye"></i></a><a href="software-engineering/pdf/Module_5_Testing_Notes.pdf" target="_blank"><i class="fa-solid fa-download"></i></a></div></div>
          </div>
        </div>
      </div>

    </div>
  </main>

  <!-- Document Reader Modal -->
  <div class="modal" id="readerModal">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title" id="modalTitle">Document Reader</div>
        <button class="modal-close" onclick="closeReader()"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <iframe class="modal-body" id="modalFrame" src="about:blank"></iframe>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <p>🎓 <strong>BIT Mesra CSE 5th Semester Master Study Suite (2024–25 NEP Scheme)</strong></p>
    <p style="margin-top: 6px;">Crafted for rigorous academic preparation, publication-grade aesthetics, and rapid examination mastery.</p>
  </footer>

  <script>
    // Theme Toggle
    const themeToggle = document.getElementById('themeToggle');
    const currentTheme = localStorage.getItem('theme') || 'dark';
    if (currentTheme === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
      themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
    }
    themeToggle.addEventListener('click', () => {
      const isLight = document.documentElement.getAttribute('data-theme') === 'light';
      if (isLight) {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'dark');
        themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
      } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
        themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
      }
    });

    // Modal Document Reader
    const modal = document.getElementById('readerModal');
    const modalFrame = document.getElementById('modalFrame');
    const modalTitle = document.getElementById('modalTitle');

    function openReader(url, title) {
      modalTitle.innerText = title;
      modalFrame.src = url;
      modal.classList.add('active');
    }

    function closeReader() {
      modal.classList.remove('active');
      modalFrame.src = 'about:blank';
    }

    window.addEventListener('click', (e) => {
      if (e.target === modal) closeReader();
    });

    // Search and Filter Logic
    const searchInput = document.getElementById('searchInput');
    const tabBtns = document.querySelectorAll('.tab-btn');
    const cards = document.querySelectorAll('.card');

    let currentFilter = 'all';

    function filterCards() {
      const q = searchInput.value.toLowerCase().trim();
      cards.forEach(card => {
        const category = card.getAttribute('data-category');
        const keywords = card.getAttribute('data-keywords') || '';
        const cardText = card.innerText.toLowerCase();
        
        const matchesTab = (currentFilter === 'all') || (category === currentFilter);
        const matchesSearch = (q === '') || cardText.includes(q) || keywords.includes(q);
        
        if (matchesTab && matchesSearch) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }

    searchInput.addEventListener('input', filterCards);

    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        tabBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.getAttribute('data-filter');
        filterCards();
      });
    });
  </script>
</body>
</html>"""

def update_index():
    with open(os.path.join(ROOT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(INDEX_HTML)
    print("✅ Successfully updated index.html with SEO, Slugs, and direct all.pdf links!")

if __name__ == "__main__":
    update_index()
