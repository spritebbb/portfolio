import pathlib

# 1) projects.ts — import the three Cstudy shots, add poster + shots
p = pathlib.Path('src/data/projects.ts')
t = p.read_text(encoding='utf-8')

if 'cstudy-graph.png' not in t:
    t = t.replace(
        "import demoPoster from '../assets/media/jd-pipeline-poster.jpg'",
        "import demoPoster from '../assets/media/jd-pipeline-poster.jpg'\n"
        "import cstudyGraph from '../assets/media/cstudy-graph.png'\n"
        "import cstudyNotes from '../assets/media/cstudy-notes.png'\n"
        "import cstudySyllabus from '../assets/media/cstudy-syllabus.png'",
    )

if 'shots?: string[]' not in t:
    t = t.replace(
        "  /** Optional demo video and its poster frame. */",
        "  /** Optional real screenshots (first one doubles as the card cover). */\n"
        "  shots?: string[]\n"
        "  /** Optional demo video and its poster frame. */",
    )

idx = t.find("slug: 'cstudy'")
assert idx > 0
seg = t[idx:idx + 2500]
if 'cstudyGraph' not in seg:
    seg2 = seg.replace(
        "    stack: [",
        "    poster: cstudyGraph,\n"
        "    shots: [cstudyGraph, cstudySyllabus, cstudyNotes],\n"
        "    stack: [",
        1,
    )
    t = t[:idx] + seg2 + t[idx + 2500:]

p.write_text(t, encoding='utf-8', newline='')
print('cstudy shots wired:', 'shots: [cstudyGraph' in t)

# 2) ProjectGrid — a shot list also supplies the card cover
p = pathlib.Path('src/components/ProjectGrid.vue')
t = p.read_text(encoding='utf-8')
if 'p.poster || (p.shots && p.shots[0])' not in t:
    t = t.replace(
        '                v-if="p.poster"\n                class="card-shot-img"\n                :src="p.poster"',
        '                v-if="p.poster || p.shots"\n                class="card-shot-img"\n                :src="p.poster || p.shots?.[0]"',
    )
p.write_text(t, encoding='utf-8', newline='')
print('grid cover:', 'p.shots?.[0]' in t)

# 3) ProjectView — render the shot list right after the video / before pv-shot
p = pathlib.Path('src/ProjectView.vue')
t = p.read_text(encoding='utf-8')
if 'pv-shots' not in t:
    anchor = '      <div class="pv-shot" data-ui data-reveal>'
    block = '''      <figure v-if="project.shots" class="pv-shots" data-reveal>
        <img
          v-for="(shot, i) in project.shots"
          :key="shot"
          class="pv-shots-i"
          :src="shot"
          :alt="`${project.name} 的界面截图 ${i + 1}`"
          loading="eager"
          decoding="async"
        />
        <figcaption class="pv-shots-c">
          上面是它现在的界面，从左边起：知识图谱、考纲覆盖、笔记。
        </figcaption>
      </figure>

''' + anchor
    assert anchor in t
    t = t.replace(anchor, block, 1)

    css_anchor = '.pv-shot {'
    css = '''.pv-shots {
  margin: clamp(2.5rem, 6vh, 4rem) 0 0;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: clamp(0.6rem, 1.4vw, 1.1rem);
}

.pv-shots-i {
  width: 100%;
  display: block;
  background: var(--deep);
}

.pv-shots-c {
  grid-column: 1 / -1;
  margin-top: 0.4rem;
  font-size: var(--step-small);
  line-height: 1.6;
  color: var(--muted);
  max-width: 62ch;
}

.pv-shot {'''
    t = t.replace(css_anchor, css, 1)

p.write_text(t, encoding='utf-8', newline='')
print('ProjectView shots:', 'pv-shots' in t)
