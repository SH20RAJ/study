#!/usr/bin/env python3
"""
Master Build Pipeline for BIT Mesra CSE 5th Semester Study Suite.
Recompiles all practical lab manuals, HTML/PDF documents, and rich subject landing pages.
"""

import subprocess, sys, os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

BUILD_SCRIPTS = [
    ("Compiler Design Lab Manual", "build_cd_lab_master.py"),
    ("DCCN Lab Manual", "build_dccn_lab_master.py"),
    ("Artificial Intelligence Lab Manual", "build_ai_lab_master.py"),
    ("Data Mining Lab Manual", "build_dm_lab_master.py"),
    ("Natural Language Processing Lab Manual", "build_nlp_lab_master.py"),
    ("Software Engineering Lab Manual", "build_se_lab_master.py"),
    ("Rich Subject Landing Pages & TOC Sidebars", "build_rich_subject_pages.py"),
    ("Global Document Audit", "audit_suite.py")
]

def run_build():
    print("🚀 Starting Master Build Pipeline for B.Tech CSE 5th Sem Study Suite...\n")
    for desc, script_name in BUILD_SCRIPTS:
        script_path = os.path.join(SCRIPTS_DIR, script_name)
        print(f"▶️ Executing: {desc} ({script_name})...")
        res = subprocess.run([sys.executable, script_path], cwd=os.path.dirname(SCRIPTS_DIR))
        if res.returncode != 0:
            print(f"❌ Error during {script_name} execution (exit code {res.returncode})")
            sys.exit(res.returncode)
        print(f"✅ Finished: {desc}\n")
    print("🎉 All documents and portals compiled successfully!")

if __name__ == "__main__":
    run_build()
