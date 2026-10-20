# -*- coding: utf-8 -*-
"""Wire the Tuzhan Assistant screenshots into projects.ts."""
import pathlib
import sys

p = pathlib.Path("src/data/projects.ts")
t = p.read_text(encoding="utf-8")

# 1) imports
imp_anchor = "import cstudySyllabus from '../assets/media/cstudy-syllabus.png'\n"
new_imports = (
    imp_anchor
    + "import tuzhanMain from '../assets/media/tuzhan-assistant-main.jpg'\n"
    + "import tuzhanSettings from '../assets/media/tuzhan-assistant-settings.jpg'\n"
    + "import tuzhanGrowth from '../assets/media/tuzhan-assistant-growth.jpg'\n"
)
if "tuzhan-assistant-main.jpg" not in t:
    if imp_anchor not in t:
        sys.exit("import anchor not found")
    t = t.replace(imp_anchor, new_imports, 1)
    print("imports added")
else:
    print("imports already present")

# 2) attach poster/shots to the tuzhan-assistant block
anchor = """    slug: 'tuzhan-assistant',
    name: '菟菚桌面助手',
    en: 'TZtuzhanAssistant',
    tagline: '一个装在桌面上、会记事也会忘事的 AI 伙伴。',"""
if "poster: tuzhanMain" in t:
    print("already wired")
else:
    if anchor not in t:
        sys.exit("tuzhan-assistant anchor not found")
    t = t.replace(anchor, anchor, 1)

    # insert after the metrics array of this project: find repo: line then insert shots before 'stack:'
    start = t.index(anchor)
    # locate the 'stack:' of this block
    stack_idx = t.index("    stack: [", start)
    insert = (
        "    poster: tuzhanMain,\n"
        "    shots: [tuzhanMain, tuzhanSettings, tuzhanGrowth],\n"
    )
    t = t[:stack_idx] + insert + t[stack_idx:]
    print("shots wired into tuzhan-assistant")

p.write_text(t, encoding="utf-8", newline="")
print("written")
