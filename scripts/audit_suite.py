#!/usr/bin/env python3
"""
Comprehensive Audit Script for BIT Mesra CSE 5th Semester Study Suite.
Verifies existence, integrity, and page counts across all 57 PDF deliverables.
"""

import os, glob, fitz

SUBJECTS = [
    ("Compiler Design (CS24301 / CS24302)", "compiler-design"),
    ("Data Communication & Networks (CS24305 / CS24306)", "data-communication-and-networks"),
    ("Artificial Intelligence (CS24307 / CS24308)", "artificial-intelligence"),
    ("Data Mining Concepts (CS24303 / CS24304)", "data-mining"),
    ("Natural Language Processing (CS24351 / CS24352)", "natural-language-processing"),
    ("Software Engineering (CS24353 / CS24354)", "software-engineering")
]

def audit():
    total_docs = 0
    total_pages = 0
    errors = 0

    print("=" * 80)
    print("      BIT MESRA B.TECH CSE 5TH SEMESTER — MASTER DOCUMENT AUDIT")
    print("=" * 80)

    for title, folder in SUBJECTS:
        print(f"\n📚 {title}")
        pdf_files = sorted(glob.glob(os.path.join(folder, "pdf", "*.pdf")))
        if not pdf_files:
            print(f"   ❌ No PDF documents found in {folder}/pdf/")
            errors += 1
            continue

        for pdf_path in pdf_files:
            fname = os.path.basename(pdf_path)
            try:
                doc = fitz.open(pdf_path)
                pages = len(doc)
                size_kb = os.path.getsize(pdf_path) / 1024
                total_docs += 1
                total_pages += pages
                status = "✅ PASS" if pages >= 10 or "all.pdf" in fname or "Master" in fname else "🟡 OK"
                print(f"   • {status} {fname:48} : {pages:2d} pages ({size_kb:6.1f} KB)")
            except Exception as e:
                print(f"   • ❌ ERROR reading {fname}: {e}")
                errors += 1

    print("\n" + "=" * 80)
    print(f"📊 SUMMARY: {total_docs} Total Documents | {total_pages} Total Pages | {errors} Errors")
    print("=" * 80)

if __name__ == "__main__":
    audit()
