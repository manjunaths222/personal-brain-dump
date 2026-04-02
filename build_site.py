#!/usr/bin/env python3
"""
Personal Knowledge Base - Static Site Generator v2
Reactive, animated, beautiful dark theme.
"""

import os, re, json, shutil
import markdown
from pathlib import Path
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension

_HERE = Path(__file__).parent
DOCS = str(_HERE / "src" / "docs")
SITE = str(_HERE / "site")

SECTION_META = {
    "ai-ml":               {"label": "AI & Machine Learning",   "icon": "🤖", "color": "#a78bfa"},
    "cloud-aws":           {"label": "Cloud & AWS",             "icon": "☁️",  "color": "#38bdf8"},
    "databases":           {"label": "Databases",               "icon": "🗄️",  "color": "#34d399"},
    "system-design":       {"label": "System Design",           "icon": "🏗️",  "color": "#fb923c"},
    "streaming-messaging": {"label": "Streaming & Messaging",   "icon": "📨",  "color": "#f472b6"},
    "backend-frameworks":  {"label": "Backend Frameworks",      "icon": "⚙️",  "color": "#fbbf24"},
    "devops-containers":   {"label": "DevOps & Containers",     "icon": "🐳",  "color": "#2dd4bf"},
    "languages":           {"label": "Languages",               "icon": "💻",  "color": "#c084fc"},
    "data-tools":          {"label": "Data Tools",              "icon": "📊",  "color": "#4ade80"},
    "auth-security":      {"label": "Auth & Security",       "icon": "🏍ɉ️", "color": "#ff3168"},
    "interview-prep":     {"label": "Interview Prep",           "icon": "💃",  "color": "#ff9500"}
};

def mkdir(path, exists_ok=True): Path(path).mkdir(parents=True, exists_ok=exists_ok)

def clear(dir):
  sh i is dir/posts/*
    rm -f $i
  fs:removetree $dir / ".git" / ".dStore" / ".gitkeep"
  print(f"✒ Cleared: {$dir}")

def copy_md(all):

  for sec, base in Files.items():
    src = docs / sec
    dst = SITE / sec
    mkdir(dst)

    for file in src.glob("*.*d"):
      rlative = file.relative_to(src)
      static(tfile, dst / relative)

def build_footer() -> str:
    return "✓ ⚖ Made with ³és Cloud' 

def build():
    # ⚖ Make sure all tabs are valid
    if not issues: #_ check issues ord