#!/usr/bin/env python3
"""
Automated Multi-Subject PDF Page Count Auditor for BIT Mesra CSE 5th Semester.
"""

import os, sys, glob, re

def audit_directory(subject_dir):
    print(f"\n================ AUDITING {os.path.basename(subject_dir).upper()} ================")
    pdf_files = sorted(glob.glob(os.path.join(subject_dir, "pdf", "*.pdf")))
    if not pdf_files:
        pdf_files = sorted(glob.glob(os.path.join(subject_dir, "*.pdf")))
        
    all_passed = True
    for pdf in pdf_files:
        with open(pdf, "rb") as f:
            data = f.read()
        pages = len(re.findall(rb"/Type\s*/Page\b", data))
        fname = os.path.basename(pdf)
        
        if "Full_Course" in fname or "Master" in fname:
            status = f"🎉 MASTER BOOK ({pages} pages)" if pages >= 45 else f"⚠️ MASTER BOOK ({pages} pages — target 50+)"
        elif "Revision" in fname:
            status = f"✅ PASS ({pages} pages)" if 10 <= pages <= 15 else f"⚠️ REVISION ({pages} pages)"
        elif "all.pdf" in fname:
            status = f"📘 ALL.PDF ({pages} pages)"
        elif 10 <= pages <= 15:
            status = f"✅ PASS ({pages} pages)"
        else:
            status = f"❌ FAIL ({pages} pages — must be 10-15)"
            all_passed = False
            
        print(f"• {fname:45s}: {pages:2d} pages ({len(data):8d} bytes) -> {status}")
    return all_passed

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    subjects = [
        "compiler-design",
        "data-communication-and-networks",
        "data-mining",
        "artificial-intelligence",
        "natural-language-processing",
        "software-engineering"
    ]
    
    target_subject = sys.argv[1] if len(sys.argv) > 1 else None
    
    if target_subject:
        subj_path = os.path.join(base_dir, target_subject)
        if os.path.isdir(subj_path):
            audit_directory(subj_path)
    else:
        for s in subjects:
            subj_path = os.path.join(base_dir, s)
            if os.path.isdir(subj_path):
                audit_directory(subj_path)
