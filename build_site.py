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
    "databases":           {"label": "Databases",               "icon": "🗆️",  "color": "#34d399"},
    "system-design":       {"label": "System Design",           "icon": "🏗️",  "color": "#fb923c"},
    "streaming-messaging": {"label": "Streaming & Messaging",   "icon": "📨",  "color": "#f472b6"},
    "backend-frameworks":  {"label": "Backend Frameworks",      "icon": "⚙️",  "color": "#fbbf24"},
    "devops-containers":   {"label": "DevOps & Containers",     "icon": "🐳",  "color": "#2dd4bf"},
    "languages":           {"label": "Languages",               "icon": "💻",  "color": "#c084fc"},
    "data-tools":          {"label": "Data Tools",              "icon": "📊",  "color": "#4ade80"},
    "auth-security":       {"label": "Auth & Security",         "icon": "🔐",  "color": "#f87171"},
    "frontend-web":        {"label": "Frontend & Web",          "icon": "🌐",  "color": "#60a5fa"},
    "interview-prep":      {"label": "Interview Prep",          "icon": "🎯",  "color": "#e879f9"},
    "quick-references":    {"label": "Quick References",        "icon": "📌",  "color": "#94a3b8"},
}

def preprocess_markdown(text):
    """Ensure blank lines around bullet list blocks for proper rendering."""
    import re
    # Add blank line before first bullet item in each block
    text = re.sub(r'(?m)^(?![ \t]*[\*\-] )(.+)\n([ \t]*[\*\-] )', r'\1\n\n\2', text)
    # Add blank line after last bullet item before non-bullet, non-blank line
    text = re.sub(r'(?m)^([ \t]*[\*\-] [^\n]+)\n(?![ \t]*[\*\-] )(?!\n)(.)', r'\1\n\n\2', text)
    return text

def fix_mojibake(text):
    """Fix Windows-1252 mojibake from Apple Notes/clipboard exports."""
    try:
        return text.encode('cp1252').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text

md_proc = markdown.Markdown(extensions=[
    FencedCodeExtension(),
    'markdown.extensions.nl2br',
    CodeHiliteExtension(linenums=False, css_class='highlight'),
    TableExtension(),
    TocExtension(permalink=True),
])

def md_to_html(text):
    md_proc.reset()
    text = fix_mojibake(text)
    text = preprocess_markdown(text)
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    html = md_proc.convert(text)
    # Auto-link bare URLs that aren't already inside href/src attributes
    html = re.sub(
        r'(?<!["\'=>])(https?://[^\s<>"\')\]]+)',
        r'<a href="\1" target="_blank" rel="noopener noreferrer">\1</a>',
        html
    )
    return html

def extract_title(text):
    fm = re.search(r'^---\ntitle: "(.+?)"\n---', text, re.DOTALL)
    if fm: return fm.group(1)
    h1 = re.search(r'^# (.+)$', text, re.MULTILINE)
    if h1: return h1.group(1)
    return "Untitled"

# ── Global CSS ────────────────────────────────────────────────────────────────
GLOBAL_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --bg:        #0a0c10;
  --bg2:       #111318;
  --bg3:       #1c1f2e;
  --bg4:       #252840;
  --border:    #2a2d45;
  --border2:   #3d4166;
  --accent:    #7c6af7;
  --accent2:   #56c8d8;
  --accent3:   #f472b6;
  --text:      #e2e8f0;
  --text2:     #94a3b8;
  --text3:     #64748b;
  --code-bg:   #0d1117;
  --sidebar-w: 285px;
  --topbar-h:  58px;
  --radius:    10px;
  --radius-lg: 16px;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.75;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg2); }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

/* ── Topbar ── */
.topbar {
  position: fixed; top: 0; left: 0; right: 0;
  height: var(--topbar-h);
  background: rgba(10,12,16,0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  z-index: 200;
  display: flex; align-items: center;
  padding: 0 20px; gap: 16px;
}

.topbar .logo {
  font-weight: 800; font-size: 1.1rem;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  text-decoration: none; white-space: nowrap;
  letter-spacing: -0.3px;
}

.search-wrap { flex: 1; max-width: 480px; position: relative; }
#search-input {
  width: 100%; padding: 9px 16px 9px 42px;
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 24px;
  color: var(--text); font-size: 0.875rem;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s, background 0.2s;
}
#search-input::placeholder { color: var(--text3); }
#search-input:focus {
  border-color: var(--accent);
  background: var(--bg4);
  box-shadow: 0 0 0 3px rgba(124,106,247,0.15);
}
.search-icon {
  position: absolute; left: 14px; top: 50%;
  transform: translateY(-50%); opacity: 0.45; font-size: 1rem;
  pointer-events: none;
}
.kbd-hint {
  position: absolute; right: 12px; top: 50%;
  transform: translateY(-50%);
  font-size: 0.7rem; color: var(--text3);
  background: var(--bg4); border: 1px solid var(--border2);
  padding: 1px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace;
}

#search-results {
  position: absolute; top: calc(100% + 8px); left: 0; right: 0;
  background: var(--bg2);
  border: 1px solid var(--border2);
  border-radius: var(--radius);
  max-height: 420px; overflow-y: auto;
  z-index: 300; display: none;
  box-shadow: 0 16px 48px rgba(0,0,0,0.6);
  animation: dropIn 0.15s ease;
}
@keyframes dropIn {
  from { opacity: 0; transform: translateY(-8px); }
  to   { opacity: 1; transform: translateY(0); }
}
.search-result {
  padding: 12px 16px; border-bottom: 1px solid var(--border);
  cursor: pointer; transition: background 0.12s;
  display: flex; flex-direction: column; gap: 3px;
}
.search-result:last-child { border-bottom: none; }
.search-result:hover { background: var(--bg3); }
.sr-title { font-weight: 600; font-size: 0.88rem; color: var(--text); }
.sr-section {
  font-size: 0.72rem; color: var(--accent2);
  text-transform: uppercase; letter-spacing: 0.5px;
}
.sr-snippet { font-size: 0.78rem; color: var(--text2); line-height: 1.4; }
.sr-highlight { color: var(--accent3); font-weight: 600; }
.search-empty { padding: 20px; text-align: center; color: var(--text3); font-size: 0.85rem; }

#hamburger {
  display: none; background: none; border: none;
  color: var(--text); font-size: 1.3rem; cursor: pointer;
  padding: 6px 8px; border-radius: 6px;
  transition: background 0.15s;
}
#hamburger:hover { background: var(--bg3); }

/* ── Layout ── */
.layout { display: flex; margin-top: var(--topbar-h); min-height: calc(100vh - var(--topbar-h)); }

/* ── Sidebar ── */
.sidebar {
  width: var(--sidebar-w);
  background: var(--bg2);
  border-right: 1px solid var(--border);
  position: fixed; top: var(--topbar-h); left: 0; bottom: 0;
  overflow-y: auto; padding: 20px 0 40px;
  transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);
  z-index: 100;
}

.sidebar-section { margin-bottom: 4px; }
.sidebar-section-header {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 16px 6px;
  font-size: 0.7rem; font-weight: 700;
  color: var(--text3);
  text-transform: uppercase; letter-spacing: 1px;
  cursor: pointer; user-select: none;
  transition: color 0.15s;
}
.sidebar-section-header:hover { color: var(--text2); }
.sidebar-section-header .sec-icon { font-size: 0.95rem; }
.sidebar-section-header .chevron {
  margin-left: auto; font-size: 0.65rem;
  transition: transform 0.25s; color: var(--text3);
}
.sidebar-section.collapsed .chevron { transform: rotate(-90deg); }
.sidebar-section.collapsed .sidebar-links { display: none; }

.sidebar-links { list-style: none; padding: 0 8px 4px; }
.sidebar-links li a {
  display: block; padding: 5px 12px;
  font-size: 0.82rem; color: var(--text2);
  text-decoration: none; border-radius: 6px;
  transition: background 0.12s, color 0.12s, padding-left 0.12s;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.sidebar-links li a:hover { background: var(--bg4); color: var(--text); padding-left: 16px; }
.sidebar-links li a.active {
  background: rgba(124,106,247,0.18);
  color: var(--accent);
  font-weight: 600;
  border-left: 2px solid var(--accent);
}

/* ── Main ── */
.main {
  margin-left: var(--sidebar-w);
  flex: 1; min-width: 0;
  padding: 40px 48px;
  animation: fadeUp 0.4s ease both;
}
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Content ── */
.content h1 { font-size: 2rem; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 8px; color: var(--text); line-height: 1.2; }
.content h2 {
  font-size: 1.3rem; font-weight: 700; color: var(--text);
  margin: 36px 0 12px; padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
}
.content h3 { font-size: 1.05rem; font-weight: 600; color: var(--accent2); margin: 24px 0 8px; }
.content h4 { font-size: 0.95rem; font-weight: 600; color: var(--accent); margin: 16px 0 6px; }
.content p { margin: 12px 0; color: var(--text); }
.content a { color: var(--accent2); text-decoration: none; border-bottom: 1px solid rgba(86,200,216,0.3); transition: border-color 0.15s, color 0.15s; }
.content a:hover { color: var(--accent); border-color: var(--accent); }
.content ul, .content ol { margin: 10px 0 10px 24px; }
.content li { margin: 4px 0; }
.content li::marker { color: var(--accent); }
.content strong { color: var(--text); font-weight: 700; }
.content em { color: var(--accent2); }
.content blockquote {
  border-left: 3px solid var(--accent);
  padding: 10px 18px; margin: 16px 0;
  background: rgba(124,106,247,0.07);
  border-radius: 0 var(--radius) var(--radius) 0;
  color: var(--text2);
}
.content hr { border: none; border-top: 1px solid var(--border); margin: 28px 0; }

/* ── Code ── */
.content code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.82em;
  background: var(--code-bg);
  color: var(--accent2);
  padding: 2px 7px; border-radius: 4px;
  border: 1px solid var(--border);
}
.content pre {
  background: var(--code-bg) !important;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 18px 20px;
  overflow-x: auto;
  margin: 16px 0;
  position: relative;
}
.content pre code { background: none; border: none; padding: 0; color: #e2e8f0; font-size: 0.85rem; }

/* Syntax highlighting (Monokai-inspired dark) */
.highlight .hll { background-color: #272822; }
.highlight .c  { color: #75715e; font-style: italic }
.highlight .k  { color: #66d9e8; font-weight: bold }
.highlight .n  { color: #f8f8f2 }
.highlight .o  { color: #f92672 }
.highlight .p  { color: #f8f8f2 }
.highlight .cm { color: #75715e; font-style: italic }
.highlight .cp { color: #75715e; font-weight: bold }
.highlight .cs { color: #75715e; font-style: italic; font-weight: bold }
.highlight .gd { color: #f92672 }
.highlight .ge { font-style: italic }
.highlight .gr { color: #f92672 }
.highlight .gh { color: #75715e; font-weight: bold }
.highlight .gi { color: #a6e22e }
.highlight .go { color: #75715e }
.highlight .gp { color: #75715e; font-weight: bold }
.highlight .gs { font-weight: bold }
.highlight .gu { color: #75715e; text-decoration: underline }
.highlight .gt { color: #f92672 }
.highlight .kc { color: #66d9e8; font-weight: bold }
.highlight .kd { color: #66d9e8; font-weight: bold }
.highlight .kn { color: #f92672; font-weight: bold }
.highlight .kp { color: #66d9e8 }
.highlight .kr { color: #66d9e8; font-weight: bold }
.highlight .kt { color: #66d9e8 }
.highlight .ld { color: #e6db74 }
.highlight .m  { color: #ae81ff }
.highlight .s  { color: #e6db74 }
.highlight .na { color: #a6e22e }
.highlight .nb { color: #f8f8f2 }
.highlight .nc { color: #a6e22e; font-weight: bold }
.highlight .no { color: #66d9e8 }
.highlight .nd { color: #a6e22e }
.highlight .ni { color: #f8f8f2; font-weight: bold }
.highlight .ne { color: #a6e22e; font-weight: bold }
.highlight .nf { color: #a6e22e }
.highlight .nl { color: #f8f8f2; font-weight: bold }
.highlight .nn { color: #f8f8f2 }
.highlight .nx { color: #a6e22e }
.highlight .py { color: #f8f8f2 }
.highlight .nt { color: #f92672 }
.highlight .nv { color: #f8f8f2 }
.highlight .ow { color: #f92672; font-weight: bold }
.highlight .w  { color: #f8f8f2 }
.highlight .mf { color: #ae81ff }
.highlight .mh { color: #ae81ff }
.highlight .mi { color: #ae81ff }
.highlight .mo { color: #ae81ff }
.highlight .sb { color: #e6db74 }
.highlight .sc { color: #e6db74 }
.highlight .sd { color: #e6db74; font-style: italic }
.highlight .s2 { color: #e6db74 }
.highlight .se { color: #ae81ff; font-weight: bold }
.highlight .sh { color: #e6db74 }
.highlight .si { color: #e6db74; font-weight: bold }
.highlight .sx { color: #e6db74 }
.highlight .sr { color: #e6db74 }
.highlight .ss { color: #ae81ff }
.highlight .s1 { color: #e6db74 }
.highlight .bp { color: #f8f8f2 }
.highlight .vc { color: #f8f8f2 }
.highlight .vg { color: #f8f8f2 }
.highlight .vi { color: #f8f8f2 }
.highlight .il { color: #ae81ff }

/* ── Tables ── */
.content table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 0.875rem; }
.content th {
  background: var(--bg3);
  padding: 10px 14px; text-align: left;
  font-weight: 700; font-size: 0.78rem; text-transform: uppercase;
  letter-spacing: 0.5px; color: var(--accent2);
  border-bottom: 2px solid var(--border2);
}
.content td {
  padding: 10px 14px; border-bottom: 1px solid var(--border);
  color: var(--text2);
  transition: background 0.12s;
}
.content tr:hover td { background: var(--bg3); }
.content tr:last-child td { border-bottom: none; }

/* ── Page header ── */
.page-header { margin-bottom: 32px; }
.page-breadcrumb {
  font-size: 0.75rem; color: var(--text3);
  margin-bottom: 8px; display: flex; align-items: center; gap: 6px;
}
.page-breadcrumb a { color: var(--text3); text-decoration: none; border: none; transition: color 0.15s; }
.page-breadcrumb a:hover { color: var(--accent2); }
.page-title { font-size: 2rem; font-weight: 800; letter-spacing: -0.5px; line-height: 1.2; }
.page-meta {
  margin-top: 10px; font-size: 0.78rem; color: var(--text3);
  display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
}
.page-section-tag {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 3px 10px; border-radius: 20px;
  font-size: 0.72rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.5px;
  border: 1px solid;
}
.page-divider { border: none; border-top: 1px solid var(--border); margin: 24px 0 32px; }

/* ── Home page ── */
.home-hero {
  text-align: center; padding: 60px 20px 40px;
  background: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(124,106,247,0.12) 0%, transparent 70%);
}
.home-hero h1 {
  font-size: 2.8rem; font-weight: 900;
  letter-spacing: -1px;
  background: linear-gradient(135deg, #fff 0%, var(--accent) 50%, var(--accent2) 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 14px;
}
.home-hero p { font-size: 1.05rem; color: var(--text2); max-width: 520px; margin: 0 auto 32px; }
.home-stats {
  display: flex; justify-content: center; gap: 32px;
  flex-wrap: wrap; margin-bottom: 48px;
}
.stat-card {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 18px 28px; text-align: center;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.stat-card:hover {
  transform: translateY(-3px);
  border-color: var(--border2);
  box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
.stat-num { font-size: 2rem; font-weight: 900; color: var(--accent); }
.stat-label { font-size: 0.75rem; color: var(--text3); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }

.home-sections { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; }
.section-card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px;
  text-decoration: none; color: var(--text);
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s, background 0.2s;
  display: flex; flex-direction: column; gap: 8px;
  position: relative; overflow: hidden;
}
.section-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: var(--card-color, var(--accent));
  transform: scaleX(0); transform-origin: left;
  transition: transform 0.25s ease;
}
.section-card:hover {
  transform: translateY(-4px);
  border-color: var(--border2);
  box-shadow: 0 12px 40px rgba(0,0,0,0.4);
  background: var(--bg3);
}
.section-card:hover::before { transform: scaleX(1); }
.card-icon { font-size: 1.8rem; margin-bottom: 4px; }
.card-title { font-weight: 700; font-size: 0.95rem; }
.card-count { font-size: 0.75rem; color: var(--text3); }
.card-pages { margin-top: 6px; }
.card-pages a {
  display: inline-block;
  font-size: 0.72rem; color: var(--text3);
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 4px; padding: 2px 7px; margin: 2px 2px 2px 0;
  text-decoration: none; transition: background 0.12s, color 0.12s;
}
.card-pages a:hover { background: var(--bg4); color: var(--text); }

/* ── Animations ── */
.section-card, .stat-card { animation: cardPop 0.4s ease both; }
@keyframes cardPop {
  from { opacity: 0; transform: scale(0.97) translateY(10px); }
  to   { opacity: 1; transform: scale(1) translateY(0); }
}
.section-card:nth-child(1)  { animation-delay: 0.03s; }
.section-card:nth-child(2)  { animation-delay: 0.06s; }
.section-card:nth-child(3)  { animation-delay: 0.09s; }
.section-card:nth-child(4)  { animation-delay: 0.12s; }
.section-card:nth-child(5)  { animation-delay: 0.15s; }
.section-card:nth-child(6)  { animation-delay: 0.18s; }
.section-card:nth-child(7)  { animation-delay: 0.21s; }
.section-card:nth-child(8)  { animation-delay: 0.24s; }
.section-card:nth-child(9)  { animation-delay: 0.27s; }
.section-card:nth-child(10) { animation-delay: 0.30s; }
.section-card:nth-child(11) { animation-delay: 0.33s; }
.section-card:nth-child(12) { animation-delay: 0.36s; }
.section-card:nth-child(13) { animation-delay: 0.39s; }

/* ── Mobile ── */
@media (max-width: 860px) {
  #hamburger { display: block; }
  .sidebar { transform: translateX(-100%); }
  .sidebar.open { transform: translateX(0); }
  .main { margin-left: 0; padding: 24px 20px; }
  .sidebar-overlay {
    display: none; position: fixed; inset: 0;
    background: rgba(0,0,0,0.6); z-index: 99;
  }
  .sidebar-overlay.show { display: block; }
  .home-hero h1 { font-size: 1.8rem; }
  .home-stats { gap: 16px; }
}
@media (max-width: 560px) {
  .main { padding: 20px 16px; }
  .content pre { padding: 12px 14px; }
  .content table { font-size: 0.78rem; }
  .content th, .content td { padding: 8px 10px; }
}

/* ── Copy button on code blocks ── */
.pre-wrap { position: relative; }
.copy-btn {
  position: absolute; top: 10px; right: 10px;
  background: var(--bg4); border: 1px solid var(--border2);
  color: var(--text2); font-size: 0.72rem; padding: 3px 10px;
  border-radius: 5px; cursor: pointer;
  transition: background 0.15s, color 0.15s;
  font-family: 'JetBrains Mono', monospace;
}
.copy-btn:hover { background: var(--accent); color: #fff; border-color: var(--accent); }
.copy-btn.copied { background: #22c55e; color: #fff; border-color: #22c55e; }

/* ── Back to top ── */
#back-top {
  position: fixed; bottom: 28px; right: 28px;
  background: var(--accent); color: #fff;
  border: none; border-radius: 50%;
  width: 40px; height: 40px;
  font-size: 1.1rem; cursor: pointer;
  display: none; align-items: center; justify-content: center;
  box-shadow: 0 4px 16px rgba(124,106,247,0.4);
  transition: transform 0.2s, box-shadow 0.2s;
  z-index: 150;
}
#back-top.show { display: flex; }
#back-top:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(124,106,247,0.6); }

/* ── Progress bar ── */
#read-progress {
  position: fixed; top: var(--topbar-h); left: 0; height: 2px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  z-index: 199; transition: width 0.1s;
  width: 0%;
}
"""

# ── JavaScript ────────────────────────────────────────────────────────────────
GLOBAL_JS = """
// ── Search ──────────────────────────────────────────────────────────────────
const IDX = window.__SEARCH_INDEX__ || [];
const $si = document.getElementById('search-input');
const $sr = document.getElementById('search-results');

function highlight(text, q) {
  if (!q) return text;
  const rx = new RegExp('(' + q.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&') + ')', 'gi');
  return text.replace(rx, '<span class="sr-highlight">$1</span>');
}

function doSearch(q) {
  if (!q || q.length < 2) { $sr.style.display='none'; return; }
  const ql = q.toLowerCase();
  const hits = IDX.filter(p =>
    p.title.toLowerCase().includes(ql) ||
    p.section.toLowerCase().includes(ql) ||
    p.body.toLowerCase().includes(ql)
  ).slice(0, 8);
  if (!hits.length) {
    $sr.innerHTML = '<div class="search-empty">No results for "' + q + '"</div>';
  } else {
    $sr.innerHTML = hits.map(p => {
      const idx = p.body.toLowerCase().indexOf(ql);
      const snip = idx >= 0
        ? '...' + p.body.substring(Math.max(0,idx-40), idx+80) + '...'
        : p.body.substring(0,100) + '...';
      return `<div class="search-result" onclick="location.href='${p.url}'">
        <div class="sr-title">${highlight(p.title, q)}</div>
        <div class="sr-section">${p.section}</div>
        <div class="sr-snippet">${highlight(snip, q)}</div>
      </div>`;
    }).join('');
  }
  $sr.style.display = 'block';
}

if ($si) {
  let timer;
  $si.addEventListener('input', e => { clearTimeout(timer); timer = setTimeout(() => doSearch(e.target.value.trim()), 160); });
  $si.addEventListener('focus', () => { if ($si.value.trim().length >= 2) $sr.style.display='block'; });
  document.addEventListener('click', e => { if (!e.target.closest('.search-wrap')) $sr.style.display='none'; });
  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault(); $si.focus(); $si.select();
    }
    if (e.key === 'Escape') { $sr.style.display='none'; $si.blur(); }
  });
}

// ── Sidebar toggle ───────────────────────────────────────────────────────────
const $ham = document.getElementById('hamburger');
const $sb  = document.querySelector('.sidebar');
const $ov  = document.querySelector('.sidebar-overlay');
if ($ham) {
  $ham.addEventListener('click', () => {
    $sb.classList.toggle('open');
    $ov && $ov.classList.toggle('show');
  });
  $ov && $ov.addEventListener('click', () => {
    $sb.classList.remove('open');
    $ov.classList.remove('show');
  });
}

// ── Sidebar collapse sections ────────────────────────────────────────────────
document.querySelectorAll('.sidebar-section-header').forEach(hdr => {
  hdr.addEventListener('click', () => hdr.parentElement.classList.toggle('collapsed'));
});

// ── Copy code buttons ────────────────────────────────────────────────────────
document.querySelectorAll('pre').forEach(pre => {
  const wrap = document.createElement('div');
  wrap.className = 'pre-wrap';
  pre.parentNode.insertBefore(wrap, pre);
  wrap.appendChild(pre);
  const btn = document.createElement('button');
  btn.className = 'copy-btn'; btn.textContent = 'copy';
  btn.addEventListener('click', () => {
    navigator.clipboard.writeText(pre.innerText).then(() => {
      btn.textContent = 'copied!'; btn.classList.add('copied');
      setTimeout(() => { btn.textContent='copy'; btn.classList.remove('copied'); }, 2000);
    });
  });
  wrap.appendChild(btn);
});

// ── Read progress bar ────────────────────────────────────────────────────────
const $prog = document.getElementById('read-progress');
const $btop = document.getElementById('back-top');
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
  if ($prog) $prog.style.width = pct + '%';
  if ($btop) $btop.classList.toggle('show', h.scrollTop > 400);
}, { passive: true });
if ($btop) $btop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

// ── Active sidebar link ───────────────────────────────────────────────────────
const cur = location.pathname;
document.querySelectorAll('.sidebar-links a').forEach(a => {
  if (a.getAttribute('href') === cur || a.getAttribute('href') === cur + 'index.html') {
    a.classList.add('active');
    a.closest('.sidebar-section')?.classList.remove('collapsed');
  }
});
"""

# ── HTML template ─────────────────────────────────────────────────────────────
def build_page(title, section_key, content_html, search_index, sidebar_html, breadcrumb="", depth=0):
    prefix = "../" * depth
    sec = SECTION_META.get(section_key, {})
    sec_label = sec.get("label", section_key)
    sec_icon  = sec.get("icon", "📄")
    sec_color = sec.get("color", "#7c6af7")

    tag_html = f'''<span class="page-section-tag" style="color:{sec_color};border-color:{sec_color}30;background:{sec_color}12">
      {sec_icon} {sec_label}
    </span>''' if section_key else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Brain Dump</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{GLOBAL_CSS}</style>
</head>
<body>

<div id="read-progress"></div>

<!-- Topbar -->
<header class="topbar">
  <button id="hamburger" aria-label="Menu">☰</button>
  <a href="{prefix}index.html" class="logo">🧠 Brain<span>Dump</span></a>
  <div class="search-wrap">
    <span class="search-icon">🔍</span>
    <input id="search-input" type="search" placeholder="Search notes…" autocomplete="off" spellcheck="false">
    <span class="kbd-hint">⌘K</span>
    <div id="search-results"></div>
  </div>
</header>

<!-- Sidebar overlay -->
<div class="sidebar-overlay"></div>

<!-- Sidebar -->
<aside class="sidebar">
{sidebar_html}
</aside>

<!-- Main -->
<main class="main">
  <article class="content">
    <div class="page-header">
      {f'<div class="page-breadcrumb"><a href="{prefix}index.html">Home</a> <span>›</span> <span>{sec_label}</span></div>' if section_key else ''}
      <h1 class="page-title">{title}</h1>
      <div class="page-meta">{tag_html}</div>
    </div>
    <hr class="page-divider">
    {content_html}
  </article>
</main>

<button id="back-top" aria-label="Back to top">↑</button>

<script>window.__SEARCH_INDEX__ = {json.dumps(search_index, ensure_ascii=False)};</script>
<script>{GLOBAL_JS}</script>
</body>
</html>"""

# ── Sidebar builder ───────────────────────────────────────────────────────────
def build_sidebar(pages_by_section, prefix=""):
    html = ""
    for sec_key, meta in SECTION_META.items():
        pages = pages_by_section.get(sec_key, [])
        if not pages:
            continue
        color = meta["color"]
        links = "\n".join(
            f'<li><a href="{prefix}{sec_key}/{p["slug"]}.html">{p["title"]}</a></li>'
            for p in pages
        )
        html += f"""<div class="sidebar-section">
  <div class="sidebar-section-header" style="color:{color}">
    <span class="sec-icon">{meta["icon"]}</span>
    <span>{meta["label"]}</span>
    <span class="chevron">▼</span>
  </div>
  <ul class="sidebar-links">{links}</ul>
</div>\n"""
    return html

# ── Main build ────────────────────────────────────────────────────────────────
def build():
    shutil.rmtree(SITE, ignore_errors=True)
    os.makedirs(SITE, exist_ok=True)

    # Collect all pages
    pages_by_section = {}
    all_pages = []

    for sec_key in SECTION_META:
        sec_dir = Path(DOCS) / sec_key
        if not sec_dir.exists():
            continue
        pages = []
        for md_file in sorted(sec_dir.glob("*.md")):
            text = md_file.read_text(errors='ignore')
            title = extract_title(text)
            slug  = md_file.stem
            body  = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
            body  = re.sub(r'#+ ', '', body)
            body  = re.sub(r'\s+', ' ', body).strip()[:600]
            pages.append({"title": title, "slug": slug, "text": text, "body": body})
            all_pages.append({
                "title": title, "section": SECTION_META[sec_key]["label"],
                "url": f"/{sec_key}/{slug}.html", "body": body
            })
        pages_by_section[sec_key] = pages

    search_index = all_pages

    # Build section pages
    for sec_key, pages in pages_by_section.items():
        sec_dir = Path(SITE) / sec_key
        sec_dir.mkdir(exist_ok=True)
        sidebar = build_sidebar(pages_by_section, prefix="../")
        for p in pages:
            html_body = md_to_html(p["text"])
            page = build_page(p["title"], sec_key, html_body, search_index, sidebar, depth=1)
            (sec_dir / f'{p["slug"]}.html').write_text(page)
            print(f"  ✓ {sec_key}/{p['slug']}.html")

    # Build home page
    sidebar_home = build_sidebar(pages_by_section)
    total_notes = sum(len(v) for v in pages_by_section.values())
    total_sections = len(pages_by_section)

    cards_html = ""
    for i, (sec_key, pages) in enumerate(
        sorted(pages_by_section.items(), key=lambda x: -len(x[1]))
    ):
        meta  = SECTION_META[sec_key]
        color = meta["color"]
        page_links = " ".join(
            f'<a href="{sec_key}/{p["slug"]}.html">{p["title"][:28]}</a>'
            for p in pages[:5]
        )
        more = f'<a href="{sec_key}/{pages[5]["slug"]}.html">+{len(pages)-5} more</a>' if len(pages) > 5 else ""
        cards_html += f"""<a class="section-card" href="{sec_key}/{pages[0]['slug']}.html"
  style="--card-color:{color}">
  <div class="card-icon">{meta["icon"]}</div>
  <div class="card-title">{meta["label"]}</div>
  <div class="card-count">{len(pages)} notes</div>
  <div class="card-pages">{page_links}{more}</div>
</a>\n"""

    home_content = f"""
<div class="home-hero">
  <h1>Personal Brain Dump</h1>
  <p>A searchable knowledge base of engineering notes, patterns, and references — all in one place.</p>
  <div class="home-stats">
    <div class="stat-card"><div class="stat-num">{total_notes}</div><div class="stat-label">Notes</div></div>
    <div class="stat-card"><div class="stat-num">{total_sections}</div><div class="stat-label">Sections</div></div>
    <div class="stat-card"><div class="stat-num">1</div><div class="stat-label">Source</div></div>
  </div>
</div>
<div class="home-sections">{cards_html}</div>"""

    home_page = build_page("Home", "", home_content, search_index, sidebar_home)
    (Path(SITE) / "index.html").write_text(home_page)
    print(f"\n✓ index.html")
    print(f"✓ Built {total_notes} pages across {total_sections} sections")
    print(f"✓ Site ready at: {SITE}")

if __name__ == "__main__":
    build()
