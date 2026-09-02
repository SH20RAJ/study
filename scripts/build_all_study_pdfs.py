#!/usr/bin/env python3
"""
🎓 B.Tech CSE 5th Semester — Universal Master PDF Study Suite Builder
Birla Institute of Technology (BIT), Mesra | NEP Scheme (2024–25)

Usage:
  python3 build_all_study_pdfs.py --all                      # Compiles the entire 5th semester suite (all subjects, modules, and master books)
  python3 build_all_study_pdfs.py --subject compiler-design  # Compiles Compiler Design (CS24301)
  python3 build_all_study_pdfs.py --subject dccn             # Compiles DCCN (CS24305)
  python3 build_all_study_pdfs.py --subject ai               # Compiles Artificial Intelligence (CS24307)
  python3 build_all_study_pdfs.py --subject data-mining      # Compiles Data Mining (CS24303)
  python3 build_all_study_pdfs.py --subject nlp              # Compiles Natural Language Processing (CS24351)
  python3 build_all_study_pdfs.py --subject se               # Compiles Software Engineering (CS24353)
"""

import os
import sys
import argparse
import subprocess

SUBJECT_SCRIPTS = {
    "compiler-design": ("compiler-design/generate_cd_suite.py", "Compiler Design (CS24301)"),
    "cd": ("compiler-design/generate_cd_suite.py", "Compiler Design (CS24301)"),
    "dccn": ("data-communication-and-networks/generate_dccn_suite.py", "Data Communication & Computer Networks (CS24305)"),
    "data-communication-and-networks": ("data-communication-and-networks/generate_dccn_suite.py", "Data Communication & Computer Networks (CS24305)"),
    "ai": ("artificial-intelligence/generate_ai_suite.py", "Artificial Intelligence (CS24307)"),
    "artificial-intelligence": ("artificial-intelligence/generate_ai_suite.py", "Artificial Intelligence (CS24307)"),
    "data-mining": ("data-mining/generate_dm_suite.py", "Data Mining Concepts and Techniques (CS24303)"),
    "dm": ("data-mining/generate_dm_suite.py", "Data Mining Concepts and Techniques (CS24303)"),
    "nlp": ("natural-language-processing/generate_nlp_suite.py", "Natural Language Processing (CS24351)"),
    "natural-language-processing": ("natural-language-processing/generate_nlp_suite.py", "Natural Language Processing (CS24351)"),
    "software-engineering": ("software-engineering/generate_se_suite.py", "Software Engineering (CS24353)"),
    "se": ("software-engineering/generate_se_suite.py", "Software Engineering (CS24353)")
}

PRIMARY_SUBJECTS = ["compiler-design", "dccn", "ai", "data-mining", "nlp", "software-engineering"]

def run_suite(key):
    script_rel, name = SUBJECT_SCRIPTS[key]
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_rel)
    print(f"\n==================================================")
    print(f"🚀 Building Study Suite: {name}")
    print(f"📄 Executing: {script_rel}")
    print(f"==================================================")
    if not os.path.exists(script_path):
        print(f"❌ Error: Script not found at {script_path}")
        return False
    ret = subprocess.run([sys.executable, script_path])
    if ret.returncode == 0:
        print(f"✨ Successfully compiled {name} study suite!\n")
        return True
    else:
        print(f"❌ Failed compiling {name} (Exit code: {ret.returncode})\n")
        return False

def main():
    parser = argparse.ArgumentParser(description="Universal Master PDF Study Suite Builder for BIT Mesra 5th Semester B.Tech CSE")
    parser.add_argument("--all", action="store_true", help="Compile study suites for all 6 subjects")
    parser.add_argument("--subject", type=str, choices=list(SUBJECT_SCRIPTS.keys()), help="Compile a specific subject")
    args = parser.parse_args()

    if args.all or (not args.subject and len(sys.argv) == 1):
        print("\n🎓 Starting complete 5th Semester B.Tech CSE Master Study Suite Recompilation...\n")
        success_count = 0
        for subj in PRIMARY_SUBJECTS:
            if run_suite(subj):
                success_count += 1
        print(f"\n🎉 All tasks finished! {success_count}/{len(PRIMARY_SUBJECTS)} subjects compiled successfully.\n")
    elif args.subject:
        run_suite(args.subject.lower())

if __name__ == "__main__":
    main()
