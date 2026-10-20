# -*- coding: utf-8 -*-
"""Wire the three pipeline diagrams into the jd-pipeline page."""
import pathlib
import sys

p = pathlib.Path("src/data/projects.ts")
t = p.read_text(encoding="utf-8")

if "jdDiagramSteps" in t:
    print("already wired")
    sys.exit(0)

# imports
imp_anchor = "import demoPoster from '../assets/media/jd-pipeline-poster.jpg'"
if imp_anchor not in t:
    sys.exit("demoPoster import not found")
t = t.replace(
    imp_anchor,
    imp_anchor
    + "\nimport jdDiagramSteps from '../assets/media/jd-diagram-steps.jpg'"
    + "\nimport jdDiagramSpec from '../assets/media/jd-diagram-spec.jpg'"
    + "\nimport jdDiagramGates from '../assets/media/jd-diagram-gates.jpg'",
    1,
)
print("imports added")

# shots on the project
anchor = "    poster: demoPoster,"
if anchor not in t:
    sys.exit("poster anchor not found")
t = t.replace(
    anchor,
    anchor
    + """
    shots: [jdDiagramSteps, jdDiagramSpec, jdDiagramGates],
    shotsCaption:
      '上面三张不是界面截图，是这条产线自己的图纸：五步怎么串、一份规格长出什么、五道门各查什么。系统跑起来的样子在更上面的视频里。',""",
    1,
)
print("shots wired")

p.write_text(t, encoding="utf-8", newline="")
print("written")
