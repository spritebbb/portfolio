# -*- coding: utf-8 -*-
"""Make the proof table follow project order instead of hard-coded shape labels."""
import pathlib
import re
import sys

# ---------- 1. data: add tableShape per project ----------
dp = pathlib.Path("src/data/projects.ts")
dt = dp.read_text(encoding="utf-8")

shapes = {
    "tuzhan-assistant": "桌面",
    "jd-pipeline": "产线",
    "cstudy": "工具",
    "dsh-skill-usage": "插件",
    "tuzhan-bot": "群聊",
}

if "tableShape" in dt:
    print("tableShape already present")
else:
    # add to the interface right after tableResult
    if "tableResult: string" in dt and "tableShape" not in dt:
        dt = dt.replace("  tableResult: string\n", "  tableResult: string\n  tableShape: string\n", 1)

    # insert per project, keyed by slug line
    for slug, shape in shapes.items():
        marker = f"slug: '{slug}',"
        idx = dt.find(marker)
        if idx < 0:
            print("WARN slug not found:", slug)
            continue
        # find the tableResult line after this slug
        m = re.search(r"\n(\s+)tableResult:", dt[idx:])
        if not m:
            print("WARN tableResult not found for", slug)
            continue
        insert_at = idx + m.start() + 1
        dt = dt[:insert_at] + f"{m.group(1)}tableShape: '{shape}',\n" + dt[insert_at:]

    dp.write_text(dt, encoding="utf-8", newline="")
    print("projects.ts updated")

# ---------- 2. ProofTable: v-for over projects ----------
vp = pathlib.Path("src/components/ProofTable.vue")
vt = vp.read_text(encoding="utf-8")

old_rows = vt[vt.index("          <tr class=\"proof-row\">"):vt.index("        </tbody>")]
new_rows = """          <tr v-for="p in projects" :key="p.slug" class="proof-row">
            <td class="proof-shape">{{ p.tableShape }}</td>
            <td class="proof-name">{{ p.name }}</td>
            <td class="proof-what">{{ p.tableResult }}</td>
            <td class="proof-num nums">{{ p.tableNumber }}</td>
          </tr>
"""
vt = vt.replace(old_rows, new_rows, 1)

old_script = vt[vt.index("<script setup lang=\"ts\">"):vt.index("</script>") + len("</script>")]
new_script = """<script setup lang="ts">
import { projects } from '../data/projects'
</script>"""
vt = vt.replace(old_script, new_script, 1)

vp.write_text(vt, encoding="utf-8", newline="")
print("ProofTable.vue rewired to v-for")
