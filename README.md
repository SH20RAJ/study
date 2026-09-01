# 🎓 B.Tech CSE 5th Semester Study Suite
**Birla Institute of Technology (BIT), Mesra | NEP Scheme (2024–25)**

[![GitHub Pages](https://img.shields.io/badge/Live%20Web%20Portal-GitHub%20Pages-blue?style=for-the-badge&logo=github)](https://sh20raj.github.io/study/)
[![Antigravity Skill](https://img.shields.io/badge/Antigravity%20Skill-pdf--designer-purple?style=for-the-badge&logo=sparkles)](.agents/skills/pdf-designer/SKILL.md)
[![Total Credits](https://img.shields.io/badge/Semester%20Credits-26.0%20Credits-emerald?style=for-the-badge)](5th_Semester_BTech_CSE_Master_Syllabus.md)

Welcome to the centralized, neuroscience-backed study and revision repository for **B.Tech Computer Science & Engineering — 5th Semester**.

> 🌐 **Live Web Portal & Reader:** [**https://sh20raj.github.io/study/**](https://sh20raj.github.io/study/)  
> 👤 **Student:** Shaswat Raj  
> 📑 **Master Syllabus Index:** [`5th_Semester_BTech_CSE_Master_Syllabus.md`](5th_Semester_BTech_CSE_Master_Syllabus.md)  
> 🎨 **PDF Designer Skill:** [`.agents/skills/pdf-designer/SKILL.md`](.agents/skills/pdf-designer/SKILL.md)  
> 🛠️ **Universal Recompilation CLI:** [`build_all_study_pdfs.py`](build_all_study_pdfs.py)

---

## ⚡ Master PDF Download Hub & Study Guides

All materials are publication-grade A4 printable PDFs with KaTeX math rendering, color-coded callouts, and vector diagrams:

| Subject & Code | Credits | 📄 10-Page Exam Revision PDF | 📚 Full Course Master Book | 📦 In-Depth Module PDFs |
| :--- | :---: | :--- | :--- | :--- |
| **Compiler Design** (`CS24301`) | 3.0 | [10-Page Revision PDF](compiler-design/pdf/Compiler_Design_10_Page_Master_Revision.pdf) | [Full Master Book](compiler-design/pdf/Compiler_Design_Full_Course_Master.pdf) | [M1](compiler-design/pdf/Module_1_Lexical_Analysis_Notes.pdf) • [M2](compiler-design/pdf/Module_2_Syntax_Analysis_Notes.pdf) • [M3](compiler-design/pdf/Module_3_Semantic_Analysis_Notes.pdf) • [M4](compiler-design/pdf/Module_4_Runtime_Environment_Notes.pdf) • [M5](compiler-design/pdf/Module_5_Code_Optimization_Notes.pdf) |
| **Data Communication & Networks** (`CS24305`) | 3.0 | [10-Page Revision PDF](data-communication-and-networks/pdf/DCCN_10_Page_Master_Revision.pdf) | [Full Master Book](data-communication-and-networks/pdf/DCCN_Full_Course_Master.pdf) | [M1](data-communication-and-networks/pdf/Module_1_Overview_Notes.pdf) • [M2](data-communication-and-networks/pdf/Module_2_Physical_Media_Notes.pdf) • [M3](data-communication-and-networks/pdf/Module_3_Data_Link_Notes.pdf) • [M4](data-communication-and-networks/pdf/Module_4_LAN_Switching_Notes.pdf) • [M5](data-communication-and-networks/pdf/Module_5_Routing_TCP_Notes.pdf) |
| **Artificial Intelligence** (`CS24307`) | 3.0 | [10-Page Revision PDF](artificial-intelligence/pdf/AI_10_Page_Master_Revision.pdf) | [Full Master Book](artificial-intelligence/pdf/AI_Full_Course_Master.pdf) | [M1](artificial-intelligence/pdf/Module_1_Intelligent_Agents_Notes.pdf) • [M2](artificial-intelligence/pdf/Module_2_Search_Algorithms_Notes.pdf) • [M3](artificial-intelligence/pdf/Module_3_Knowledge_Logic_Notes.pdf) • [M4](artificial-intelligence/pdf/Module_4_Planning_Bayes_Notes.pdf) • [M5](artificial-intelligence/pdf/Module_5_Machine_Learning_Notes.pdf) |
| **Data Mining Concepts** (`CS24303`) | 3.0 | [10-Page Revision PDF](data-mining/pdf/Data_Mining_10_Page_Master_Revision.pdf) | [Full Master Book](data-mining/pdf/Data_Mining_Full_Course_Master.pdf) | [M1](data-mining/pdf/Module_1_Data_Attributes_Notes.pdf) • [M2](data-mining/pdf/Module_2_Preprocessing_Notes.pdf) • [M3](data-mining/pdf/Module_3_Data_Warehouse_Notes.pdf) • [M4](data-mining/pdf/Module_4_Pattern_Mining_Notes.pdf) • [M5](data-mining/pdf/Module_5_Advanced_Mining_Notes.pdf) |
| **Natural Language Processing** (`CS24351`) | 3.0 | [10-Page Revision PDF](natural-language-processing/pdf/NLP_10_Page_Master_Revision.pdf) | [Full Master Book](natural-language-processing/pdf/NLP_Full_Course_Master.pdf) | [M1](natural-language-processing/pdf/Module_1_Linguistics_Notes.pdf) • [M2](natural-language-processing/pdf/Module_2_Language_Models_Notes.pdf) • [M3](natural-language-processing/pdf/Module_3_Word_Embeddings_Notes.pdf) • [M4](natural-language-processing/pdf/Module_4_Transformers_Notes.pdf) • [M5](natural-language-processing/pdf/Module_5_Applications_Ethics_Notes.pdf) |
| **Software Engineering** (`CS24353`) | 3.0 | [10-Page Revision PDF](software-engineering/pdf/SE_10_Page_Master_Revision.pdf) | [Full Master Book](software-engineering/pdf/SE_Full_Course_Master.pdf) | [M1](software-engineering/pdf/Module_1_Process_Models_Notes.pdf) • [M2](software-engineering/pdf/Module_2_Requirements_Notes.pdf) • [M3](software-engineering/pdf/Module_3_Design_UML_Notes.pdf) • [M4](software-engineering/pdf/Module_4_Testing_QA_Notes.pdf) • [M5](software-engineering/pdf/Module_5_Estimation_CMMI_Notes.pdf) |

---

## 🎨 Antigravity Skill: `pdf-designer`

This repository includes a reusable, built-in Antigravity Skill located at [`.agents/skills/pdf-designer/SKILL.md`](.agents/skills/pdf-designer/SKILL.md).

### Capabilities:
- **6 Creative Presets:** Neuroscience Study Guide, Modern Minimalist (Nordic), Dark Neon (Cyberpunk), Executive Slate, Academic Textbook, and Vibrant Creative.
- **Math Formatting:** KaTeX auto-rendering for complex mathematical proofs, theorems, and algorithms.
- **Bulletproof Pagination:** Custom CSS print engine preventing awkward element breaks across pages.
- **Headless Chromium Automation:** Flawless rendering via Playwright.

---

## 🛠️ CLI Recompilation Commands

You can edit any HTML note or source text and rebuild PDFs anytime with the universal builder:

```bash
# Recompile everything (all 6 subjects, 30 module PDFs + 6 revision guides + 6 master books)
python3 build_all_study_pdfs.py --all

# Recompile a specific subject
python3 build_all_study_pdfs.py --subject compiler-design
python3 build_all_study_pdfs.py --subject dccn
python3 build_all_study_pdfs.py --subject ai
python3 build_all_study_pdfs.py --subject data-mining
python3 build_all_study_pdfs.py --subject nlp
python3 build_all_study_pdfs.py --subject se
```

---

## 🏷️ Laboratory Manuals & Practicals (4.5 Credits)

| Course Code | Practical Lab | Credits | Lab Syllabus & Manual |
| :--- | :--- | :---: | :--- |
| **CS24302** | [Compiler Design Lab](compiler-design/) | 1.5 | [Lab Guide](compiler-design/compiler_design_syllabus.md#-compiler-design-lab-cs24302) |
| **CS24306** | [Data Communication & Networks Lab](data-communication-and-networks/) | 1.5 | [Lab Guide](data-communication-and-networks/dccn_lab_syllabus.md) |
| **CS24308** | [Artificial Intelligence Lab](artificial-intelligence/) | 1.5 | [Lab Guide](artificial-intelligence/ai_lab_syllabus.md) |

---
*Created and maintained by Shaswat Raj | BIT Mesra B.Tech CSE (NEP Scheme 2024–25).*
