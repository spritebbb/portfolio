import pathlib

# 1) projects.ts
p = pathlib.Path('src/data/projects.ts')
t = p.read_text(encoding='utf-8')

if 'jd-pipeline-demo.mp4' not in t:
    t = ("import demoVideo from '../assets/media/jd-pipeline-demo.mp4'\n"
         "import demoPoster from '../assets/media/jd-pipeline-poster.jpg'\n\n") + t

if 'video?: string' not in t:
    t = t.replace(
        "  /** Optional line about the repo's current state (e.g. mid-rewrite). */",
        "  /** Optional demo video and its poster frame. */\n"
        "  video?: string\n"
        "  poster?: string\n"
        "  /** Optional line about the repo's current state (e.g. mid-rewrite). */",
    )

marker = "    tableNumber: '30 个脚本 · 五道验收门',"
if 'video: demoVideo' not in t:
    t = t.replace(marker, marker + "\n    video: demoVideo,\n    poster: demoPoster,")

p.write_text(t, encoding='utf-8', newline='')
print('projects.ts:', 'video: demoVideo' in t)

# 2) ProjectView.vue
p = pathlib.Path('src/ProjectView.vue')
t = p.read_text(encoding='utf-8')

old = '''      <div class="pv-shot" data-ui data-reveal>
        <div class="pv-metrics">'''

new = '''      <figure v-if="project.video" class="pv-reel" data-reveal>
        <video
          class="pv-reel-v"
          :src="project.video"
          :poster="project.poster"
          controls
          muted
          loop
          playsinline
          preload="metadata"
        ></video>
        <figcaption class="pv-reel-c">
          这段是产线生成的那套系统跑起来的实拍。
        </figcaption>
      </figure>

      <div class="pv-shot" data-ui data-reveal>
        <div class="pv-metrics">'''

if 'pv-reel' not in t:
    assert old in t, 'pv-shot block not found'
    t = t.replace(old, new)

    anchor = '.pv-shot {'
    css = '''.pv-reel {
  margin: clamp(2.5rem, 6vh, 4rem) 0 0;
}

.pv-reel-v {
  width: 100%;
  display: block;
  background: var(--deep);
}

.pv-reel-c {
  margin-top: 0.9rem;
  font-size: var(--step-small);
  line-height: 1.6;
  color: var(--muted);
  max-width: 62ch;
}

.pv-shot {'''
    t = t.replace(anchor, css, 1)

p.write_text(t, encoding='utf-8', newline='')
print('ProjectView.vue:', 'pv-reel' in t)
