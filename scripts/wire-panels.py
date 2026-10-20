# -*- coding: utf-8 -*-
"""Replace the 'no screenshot' explanation with a real data panel for text-only projects."""
import pathlib
import sys

# ---------- 1. ProjectView.vue template ----------
pv = pathlib.Path("src/ProjectView.vue")
t = pv.read_text(encoding="utf-8")

old = """        <div v-if="!project.shots" class="pv-shot-foot">
          <p class="pv-shot-t">
            {{ project.textOnly ? '这个项目没有截图' : '界面截图待补' }}
          </p>
          <p class="pv-shot-d">
            {{
              project.textOnly
                ? '它不是重点展示的项目，所以不单独配图。上面这几个数字是它全部的量化结果，剩下的都在下面的文字里。'
                : `这个位置将来放 ${project.name} 的真实截图。现在先把它的真实数字放在上面，不拿别人的图充样子。`
            }}
          </p>
          <p v-if="project.repoNote" class="pv-shot-v">{{ project.repoNote }}</p>
        </div>"""

new = """        <div v-if="!project.shots" class="pv-shot-foot">
          <template v-if="project.panel">
            <p class="pv-shot-t">{{ project.panel.title }}</p>
            <dl class="pv-panel">
              <div v-for="r in project.panel.rows" :key="r.k" class="pv-panel-row">
                <dt class="pv-panel-k">{{ r.k }}</dt>
                <dd class="pv-panel-v">{{ r.v }}</dd>
              </div>
            </dl>
          </template>
          <template v-else>
            <p class="pv-shot-t">界面截图待补</p>
            <p class="pv-shot-d">
              `这个位置将来放 ${project.name} 的真实截图。现在先把它的真实数字放在上面，不拿别人的图充样子。`
            </p>
          </template>
          <p v-if="project.repoNote" class="pv-shot-v">{{ project.repoNote }}</p>
        </div>"""

if "pv-panel-row" in t:
    print("template already patched")
else:
    if old not in t:
        sys.exit("shot-foot block not found")
    t = t.replace(old, new, 1)
    # fix the stray backtick template literal that must become a binding
    t = t.replace(
        "            <p class=\"pv-shot-d\">\n              `这个位置将来放 ${project.name} 的真实截图。现在先把它的真实数字放在上面，不拿别人的图充样子。`\n            </p>",
        "            <p class=\"pv-shot-d\">\n              {{ `这个位置将来放 ${project.name} 的真实截图。现在先把它的真实数字放在上面，不拿别人的图充样子。` }}\n            </p>",
        1,
    )
    print("template patched")

# ---------- 2. styles ----------
css_anchor = ".pv-shots {"
panel_css = """.pv-panel {
  display: grid;
  gap: 0;
  margin: 1.35rem 0 0;
  max-width: 72ch;
}

.pv-panel-row {
  display: grid;
  grid-template-columns: minmax(6.5rem, 12rem) 1fr;
  gap: clamp(0.85rem, 2vw, 1.6rem);
  align-items: baseline;
  padding: 0.62rem 0.85rem;
}

.pv-panel-row:nth-child(odd) {
  background: rgba(255, 255, 255, 0.055);
}

.pv-panel-k {
  margin: 0;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--accent);
  letter-spacing: 0.01em;
}

.pv-panel-v {
  margin: 0;
  font-size: var(--step-small);
  line-height: 1.5;
  color: var(--on-deep-muted);
}

@media (max-width: 620px) {
  .pv-panel-row {
    grid-template-columns: 1fr;
    gap: 0.2rem;
  }
}

.pv-shots {"""

if ".pv-panel {" in t:
    print("css already patched")
else:
    if css_anchor not in t:
        sys.exit("css anchor not found")
    t = t.replace(css_anchor, panel_css, 1)
    print("css patched")

pv.write_text(t, encoding="utf-8", newline="")
print("ProjectView.vue written")
