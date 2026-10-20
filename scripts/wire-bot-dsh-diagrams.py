# -*- coding: utf-8 -*-
"""Let panels and diagram shots coexist; wire diagrams for the bot and the plugin."""
import pathlib
import sys

# ---------- 1. template: keep the panel even when shots exist ----------
pv = pathlib.Path("src/ProjectView.vue")
t = pv.read_text(encoding="utf-8")
old = '<div v-if="!project.shots" class="pv-shot-foot">'
new = '<div v-if="!project.shots || project.panel" class="pv-shot-foot">'
if new in t:
    print("template already patched")
elif old in t:
    t = t.replace(old, new, 1)
    pv.write_text(t, encoding="utf-8", newline="")
    print("template patched")
else:
    sys.exit("shot-foot condition not found")

# ---------- 2. data ----------
p = pathlib.Path("src/data/projects.ts")
t = p.read_text(encoding="utf-8")

if "botDiagramFlow" in t:
    print("bot diagrams already wired")
else:
    anchor = "import demoPoster from '../assets/media/jd-pipeline-poster.jpg'"
    t = t.replace(
        anchor,
        anchor
        + "\nimport botDiagramFlow from '../assets/media/bot-diagram-flow.jpg'"
        + "\nimport botDiagramTuple from '../assets/media/bot-diagram-tuple.jpg'"
        + "\nimport botDiagramModules from '../assets/media/bot-diagram-modules.jpg'"
        + "\nimport dshDiagramFlow from '../assets/media/dsh-diagram-flow.jpg'"
        + "\nimport dshDiagramShape from '../assets/media/dsh-diagram-shape.jpg'"
        + "\nimport dshDiagramSides from '../assets/media/dsh-diagram-sides.jpg'",
        1,
    )
    print("imports added")

    bot_anchor = "    panel: {\n      title: '三十个模块，一个管一件事',"
    bot_add = """    shots: [botDiagramFlow, botDiagramTuple, botDiagramModules],
    shotsCaption:
      '上面三张是它自己的图纸，不是界面截图：一条消息怎么被分流、一句话怎么拆成五个字段、三十个模块怎么分组。',
    panel: {
      title: '三十个模块，一个管一件事',"""
    if bot_anchor not in t:
        sys.exit("bot panel anchor not found")
    t = t.replace(bot_anchor, bot_add, 1)
    print("bot shots wired")

    dsh_anchor = "    panel: {\n      title: '一条记录，从日志流到面板',"
    dsh_add = """    shots: [dshDiagramFlow, dshDiagramShape, dshDiagramSides],
    shotsCaption:
      '上面三张是它自己的图纸，不是界面截图：数据怎么流、投影长什么样、两端各做什么。',
    panel: {
      title: '一条记录，从日志流到面板',"""
    if dsh_anchor not in t:
        sys.exit("dsh panel anchor not found")
    t = t.replace(dsh_anchor, dsh_add, 1)
    print("dsh shots wired")

    p.write_text(t, encoding="utf-8", newline="")
    print("projects.ts written")
