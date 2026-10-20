# -*- coding: utf-8 -*-
"""Make the shots figcaption per-project instead of hardcoded for Cstudy."""
import pathlib
import sys

# --- 1) ProjectView.vue: use project.shotsCaption ---
pv = pathlib.Path("src/ProjectView.vue")
t = pv.read_text(encoding="utf-8")
old = "        上面是它现在的界面，从左边起：知识图谱、考纲覆盖、笔记。\n"
new = "        {{ project.shotsCaption }}\n"
if "{{ project.shotsCaption }}" in t:
    print("ProjectView already dynamic")
else:
    if old not in t:
        sys.exit("caption line not found")
    t = t.replace(old, new, 1)
    pv.write_text(t, encoding="utf-8", newline="")
    print("ProjectView caption -> dynamic")

# --- 2) projects.ts: add shotsCaption field + values ---
pt = pathlib.Path("src/data/projects.ts")
s = pt.read_text(encoding="utf-8")

if "shotsCaption?" not in s:
    anchor = "  shots?: string[]\n"
    if anchor not in s:
        sys.exit("shots? field not found")
    s = s.replace(anchor, anchor + "  shotsCaption?: string\n", 1)
    print("field added")

pairs = [
    (
        "    shots: [cstudyGraph, cstudySyllabus, cstudyNotes],\n",
        "    shots: [cstudyGraph, cstudySyllabus, cstudyNotes],\n"
        "    shotsCaption: '上面是它现在的界面，从左边起：知识图谱、考纲覆盖、笔记。',\n",
    ),
    (
        "    shots: [tuzhanMain, tuzhanSettings, tuzhanGrowth],\n",
        "    shots: [tuzhanMain, tuzhanSettings, tuzhanGrowth],\n"
        "    shotsCaption: '上面是它现在的界面，从左边起：主聊天页、设置里的数据保护与模型配置、成长总览。',\n",
    ),
]
for old_line, new_line in pairs:
    if "shotsCaption:" in s and new_line.split("shotsCaption:")[1][:9] in s:
        print("skip (exists):", old_line.strip())
        continue
    if old_line not in s:
        sys.exit("shots line not found: " + old_line.strip())
    s = s.replace(old_line, new_line, 1)
    print("caption set for", old_line.strip())

pt.write_text(s, encoding="utf-8", newline="")
print("projects.ts written")
