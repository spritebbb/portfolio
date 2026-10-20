import pathlib

# 1) projects.ts — add textOnly flag and set it for the two non-key projects
p = pathlib.Path('src/data/projects.ts')
t = p.read_text(encoding='utf-8')

if 'textOnly?: boolean' not in t:
    t = t.replace(
        "  /** Optional demo video and its poster frame. */",
        "  /** No screenshot: the card shows a text panel instead. */\n"
        "  textOnly?: boolean\n"
        "  /** Optional demo video and its poster frame. */",
    )

for slug in ("tuzhan-bot", "dsh-skill-usage"):
    idx = t.find("slug: '%s'" % slug)
    assert idx > 0, slug
    seg = t[idx:idx + 2500]
    if 'textOnly: true' not in seg:
        seg2 = seg.replace("    stack: [", "    textOnly: true,\n    stack: [", 1)
        t = t[:idx] + seg2 + t[idx + 2500:]

p.write_text(t, encoding='utf-8', newline='')
print('projects.ts textOnly:', t.count('textOnly: true'))

# 2) ProjectGrid — three-way branch in the card shot
p = pathlib.Path('src/components/ProjectGrid.vue')
t = p.read_text(encoding='utf-8')

old = '''            <div class="card-shot" data-ui>
              <img
                v-if="p.poster"
                class="card-shot-img"
                :src="p.poster"
                :alt="`${p.name} 的界面截图`"
                loading="eager"
                decoding="async"
              />
              <template v-else>
                <span class="card-shot-name">{{ p.name }}</span>
                <span class="card-shot-note">界面截图待补</span>
              </template>
            </div>'''

new = '''            <div class="card-shot" data-ui>
              <img
                v-if="p.poster"
                class="card-shot-img"
                :src="p.poster"
                :alt="`${p.name} 的界面截图`"
                loading="eager"
                decoding="async"
              />
              <template v-else-if="p.textOnly">
                <span class="card-shot-name">{{ p.name }}</span>
                <span class="card-shot-nums">
                  <span v-for="m in p.metrics.slice(0, 3)" :key="m.label">
                    <b>{{ m.value }}</b>{{ m.label }}
                  </span>
                </span>
              </template>
              <template v-else>
                <span class="card-shot-name">{{ p.name }}</span>
                <span class="card-shot-note">界面截图待补</span>
              </template>
            </div>'''

if 'card-shot-nums' not in t:
    assert old in t, 'card-shot block not found'
    t = t.replace(old, new)
    t = t.replace('.card-shot-img {', '''.card-shot-nums {
  display: flex;
  gap: 1.4rem;
  font-size: var(--step-small);
  color: var(--muted);
}

.card-shot-nums b {
  display: block;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.6rem;
  line-height: 1.1;
  color: var(--accent);
}

.card-shot-img {''', 1)

p.write_text(t, encoding='utf-8', newline='')
print('grid textOnly:', 'card-shot-nums' in t)
