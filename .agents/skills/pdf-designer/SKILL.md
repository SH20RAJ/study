---
name: pdf-designer
description: >-
  Publication-grade system for generating beautiful, error-free PDF documents in multiple creative aesthetic styles (Neuroscience Study Notes, Academic Textbook, Modern Minimalist, Dark Neon Cyberpunk, Executive Slate, Vibrant Creative). Includes KaTeX math support, inline SVG diagrams, @page pagination, and headless Chromium automation via Playwright.
---

# 🎨 PDF Designer Skill & Creative Generation Engine

This skill provides an end-to-end framework and automation patterns to design and compile publication-grade, error-free PDFs from semantic HTML/CSS using Headless Chromium and Playwright.

---

## 🌟 6 Creative Design Presets

| Theme Preset | Color Palette & Mood | Best Suited For | Key CSS Variables |
| :--- | :--- | :--- | :--- |
| **1. Neuroscience Study Guide** | Deep Navy (`#1e3a8a`), Sky Blue (`#0284c7`), Amber (`#d97706`), Emerald (`#059669`) | Exam notes, revision books, university study guides with callouts & PYQs | `--primary: #1e3a8a; --accent: #0284c7; --bg-page: #f8fafc;` |
| **2. Modern Minimalist (Nordic)** | Slate 900 (`#0f172a`), Cool Grey (`#64748b`), Soft Frost (`#f1f5f9`) | Research papers, technical whitepapers, clean reference summaries | `--primary: #0f172a; --accent: #3b82f6; --bg-page: #ffffff;` |
| **3. Dark Neon (Cyberpunk)** | Obsidian (`#090d16`), Neon Cyan (`#06b6d4`), Magenta (`#d946ef`), Violet (`#8b5cf6`) | Developer cheatsheets, algorithms, AI/ML deep dives, terminal notes | `--primary: #06b6d4; --accent: #d946ef; --bg-page: #090d16; --text: #e2e8f0;` |
| **4. Executive Slate** | Forest Emerald (`#064e3b`), Classic Slate (`#334155`), Rich Gold (`#b45309`) | Software Architecture proposals, engineering reviews, business reports | `--primary: #064e3b; --accent: #b45309; --bg-page: #f8fafc;` |
| **5. Academic Textbook** | Crimson Burgundy (`#881337`), Charcoal (`#1c1917`), Parchment (`#fffbeb`) | Formal lecture notes, mathematical proofs, classical academic syllabi | `--primary: #881337; --accent: #0284c7; --bg-page: #fdfbf7;` |
| **6. Vibrant Creative** | Indigo Violet (`#4f46e5`), Electric Fuchsia (`#c026d3`), Amber Glow (`#f59e0b`) | Elective subjects, interactive walkthroughs, modern student guides | `--primary: #4f46e5; --accent: #c026d3; --bg-page: #faf5ff;` |

---

## 🛠️ The Bulletproof CSS Print Engine

Always include these `@page` and print-media rules to guarantee flawless page breaks, zero text overlapping, and sharp vector rendering:

```css
@media print {
  body {
    background: #ffffff !important;
    font-size: 11.8px;
    color: #1e293b;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .page-container {
    padding: 0 !important;
    max-width: 100% !important;
    box-shadow: none !important;
  }
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
      content: attr(data-footer);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8px;
      color: #94a3b8;
    }
  }
  /* Prevent awkward mid-element page splits */
  .toc-box, .diagram-container, .callout, table, pre, .qa-card, .avoid-break {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  h2.section-title {
    page-break-after: avoid;
    break-after: avoid;
  }
}
```

---

## 📐 KaTeX Mathematical Typesetting Template

To render math ($$E = mc^2$$ or $\text{FIRST}(\alpha)$) cleanly without escaping errors in Python, use string template substitution:

```python
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"></script>
<style>__CUSTOM_CSS__</style>
</head>
<body>
<div class="page-container" data-footer="__FOOTER__">
  __BODY__
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
```

---

## 🚀 Playwright Chromium Rendering Pipeline

```python
from playwright.sync_api import sync_playwright

def render_pdf(html_path: str, pdf_path: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            headless=True
        )
        page = browser.new_page()
        page.goto(f"file://{html_path}", wait_until="networkidle")
        # Ensure KaTeX and fonts finish rendering
        page.wait_for_timeout(1500)
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"},
            prefer_css_page_size=True
        )
        browser.close()
```

---

## ⚡ Error Prevention & Best Practices Checklist

1. **Avoid Python f-string brace syntax collisions:** In Python generators, never use raw f-strings around JavaScript callbacks (`renderMathInElement({ ... })`) or CSS selectors with `{}`. Use `.replace("__MACRO__", val)` or raw docstrings.
2. **SVG ViewBox Scaling:** Always specify `viewBox="0 0 W H"` and `width="100%"` on inline SVGs so diagrams scale seamlessly across print and web formats.
3. **Table Column Constraints:** Always define `border-collapse: collapse` and give explicit percentage widths to primary columns (e.g. `<th style="width: 25%;">`).
4. **Active Recall Cards:** Group exam questions in `.qa-card` blocks with distinct colors for question heading and solution body to enhance recall.
