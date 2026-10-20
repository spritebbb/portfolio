<template>
  <div class="pv">
    <header class="pv-top">
      <a class="pv-back" href="../">← 全部项目</a>
      <a
        class="pv-gh"
        :href="project.repo"
        target="_blank"
        rel="noopener noreferrer"
        >仓库 ↗</a
      >
    </header>

    <main class="wrap">
      <h1 class="pv-title lines">
        <span class="line"><span>{{ project.name }}</span></span>
      </h1>

      <p class="pv-en" data-reveal>{{ project.en }}</p>
      <p class="pv-tag" data-reveal>{{ project.tagline }}</p>

      <dl class="pv-facts" data-reveal>
        <div>
          <dt>时间</dt>
          <dd class="nums">{{ project.period }}</dd>
        </div>
        <div>
          <dt>技术栈</dt>
          <dd>{{ project.stack.join(' · ') }}</dd>
        </div>
      </dl>

      <p class="pv-actions" data-reveal>
        <a class="button" :href="project.repo" target="_blank" rel="noopener noreferrer">
          看源码 ↗
        </a>
        <span class="pv-actions-note">仓库公开，提交历史和测试都在里面</span>
      </p>

      <figure v-if="project.video" class="pv-reel" data-reveal>
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

      <figure v-if="project.shots" class="pv-shots" data-reveal>
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
          {{ project.shotsCaption }}
        </figcaption>
      </figure>

      <div class="pv-shot" :class="{ 'pv-shot--slim': project.shots }" data-ui data-reveal>
        <div class="pv-metrics">
          <div v-for="m in project.metrics" :key="m.label" class="pv-metric">
            <span class="pv-metric-v nums">{{ m.value }}</span>
            <span class="pv-metric-l">{{ m.label }}</span>
          </div>
        </div>
        <div v-if="!project.shots" class="pv-shot-foot">
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
              {{ `这个位置将来放 ${project.name} 的真实截图。现在先把它的真实数字放在上面，不拿别人的图充样子。` }}
            </p>
          </template>
          <p v-if="project.repoNote" class="pv-shot-v">{{ project.repoNote }}</p>
        </div>
      </div>

      <section v-if="decision" class="pv-dec" data-reveal>
        <h2 class="pv-h pv-dec-q">{{ decision.question }}</h2>

        <ul class="pv-dec-opts">
          <li v-for="o in decision.options" :key="o">{{ o }}</li>
        </ul>

        <p class="pv-p pv-dec-call">{{ decision.call }}</p>

        <dl class="pv-dec-figs">
          <div v-for="f in decision.figures" :key="f.l">
            <dt class="pv-dec-f">{{ f.v }}</dt>
            <dd class="pv-dec-l">{{ f.l }}</dd>
          </div>
        </dl>
      </section>

      <article class="pv-body">
        <section v-for="(b, i) in project.body" :key="b.heading" class="pv-block">
          <h2 class="pv-h" data-reveal>{{ b.heading }}</h2>
          <p v-for="(para, j) in b.paras" :key="j" class="pv-p" data-reveal>{{ para }}</p>
          <ul v-if="b.points" class="pv-list" data-reveal>
            <li v-for="(pt, k) in b.points" :key="k">{{ pt }}</li>
          </ul>
        </section>

        <section class="pv-pit">
          <h2 class="pv-h pv-h-sm">最深的一个坑</h2>
          <p class="pv-p pv-pit-p">{{ project.pitfall }}</p>
        </section>
      </article>
    </main>

    <figure class="pv-band">
      <img
        :src="picFront"
        width="1600"
        height="1200"
        alt="一张手写的索引卡，上面记着日期、编号和随手画的图"
        loading="eager"
        decoding="async"
      />
      <img
        :src="picBox"
        width="1600"
        height="901"
        alt="一个打开的纸盒，里面是手写的考古索引卡，卡片顶端有字母分类标签"
        loading="eager"
        decoding="async"
      />
      <img
        :src="picDrawers"
        width="1600"
        height="1200"
        alt="图书馆里成排的木质卡片目录柜，抽屉前有金属把手"
        loading="eager"
        decoding="async"
      />
      <figcaption>
        这些不是 {{ project.name }} 的截图，是「把一件事存成一条可查的记录」的历史做法：一张卡记一条，按字段建索引。
        截图的位置还空着，等真图放进来。
      </figcaption>
    </figure>

    <nav class="pv-next">
      <a class="pv-next-a" :href="`../${next.slug}/`">
        <span class="pv-next-k">下一个</span>
        <span class="pv-next-t">{{ next.name }}</span>
      </a>
    </nav>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import type { Project } from './data/projects'
import { decisions } from './data/decisions'
import { initReveal } from './lib/reveal'
import picFront from './assets/photos/the-first-card-written-west-of-cambridge.jpg'
import picBox from './assets/photos/emilie-haspels-index-card-file-wp-20170131.jpg'
import picDrawers from './assets/photos/manchester-central-library-march-2010-4467481691.jpg'

const props = defineProps<{ project: Project; next: Project }>()
const decision = computed(() => decisions[props.project.slug])

onMounted(() => {
  initReveal()
  document.title = `${props.project.name} · 黄泽圣`
})
</script>

<style scoped>
.pv-actions {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.pv-actions-note {
  font-size: var(--step-small);
  color: var(--muted);
}

.pv-band {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--gutter);
  padding: var(--section) var(--margin) 0;
}

.pv-band img {
  width: 100%;
  filter: grayscale(1) sepia(0.3) contrast(1.06) brightness(1.03);
}

.pv-band figcaption {
  grid-column: 1 / -1;
  margin-top: 0.9rem;
  font-size: var(--step-small);
  line-height: 1.6;
  color: var(--muted);
  max-width: 62ch;
}

@media (max-width: 900px) {
  .pv-band {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

.pv {
  padding-bottom: 0;
}

.pv-top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 1.75rem var(--margin) 0;
  font-size: var(--step-small);
}

.pv-back,
.pv-gh {
  color: var(--muted);
  transition: color var(--t-hover) var(--ease-out);
}

.pv-back:hover,
.pv-gh:hover {
  color: var(--ink);
}

.pv-title {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 7vw, 6rem);
  line-height: 1.02;
  letter-spacing: -0.006em;
  font-weight: 700;
  margin-top: clamp(2.5rem, 8vh, 5.5rem);
}

.pv-en {
  margin-top: 0.75rem;
  color: var(--muted);
  font-size: 1rem;
  letter-spacing: 0.01em;
}

.pv-tag {
  margin-top: clamp(1rem, 2.5vh, 1.75rem);
  font-size: var(--step-lead);
  line-height: 1.5;
  color: var(--ink);
  max-width: 30ch;
}

.pv-facts {
  margin-top: clamp(2rem, 5vh, 3rem);
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 3rem;
  font-size: 1rem;
}

.pv-facts > div {
  display: flex;
  gap: 0.6rem;
  align-items: baseline;
}

.pv-facts dt {
  color: var(--muted);
}

.pv-facts dd {
  margin: 0;
  color: var(--ink);
}

.pv-metrics {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: clamp(1rem, 2.5vw, 2rem);
}

.pv-metric {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.pv-metric-v {
  font-family: var(--font-display);
  font-size: clamp(2rem, 4vw, 3.25rem);
  line-height: 1;
  font-weight: 700;
  letter-spacing: -0.006em;
}

.pv-metric-l {
  font-size: 1rem;
  color: var(--muted);
}

.pv-reel {
  margin: clamp(2.5rem, 6vh, 4rem) 0 0;
}

.pv-reel-v {
  width: 100%;
  max-width: 900px;
  max-height: min(64vh, 560px);
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

.pv-panel {
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
  color: #f07486;
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

.pv-shots {
  margin: clamp(2.5rem, 6vh, 4rem) 0 0;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: clamp(0.8rem, 1.8vw, 1.4rem);
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

.pv-shot--slim {
  min-height: 0;
  justify-content: flex-start;
}

.pv-shot {
  margin-top: clamp(2.5rem, 6vh, 4rem);
  min-height: clamp(22rem, 40vh, 28rem);
  --muted: var(--on-deep-muted);
  background: var(--deep);
  color: var(--on-deep);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 2rem;
  padding: clamp(1.5rem, 3vw, 2.5rem);
}

.pv-shot-v {
  margin-top: 1.15rem;
  font-size: var(--step-small);
  line-height: 1.6;
  color: var(--on-deep);
  max-width: 58ch;
}

.pv-shot-foot {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.pv-shot-t {
  font-family: var(--font-display);
  font-size: var(--step-lead);
  line-height: 1.3;
  font-weight: 700;
  max-width: none;
}

.pv-shot-d {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 48ch;
}

.pv-dec {
  margin-top: var(--section);
  padding-left: clamp(1.1rem, 2.4vw, 2rem);
  border-left: 3px solid var(--accent);
}

.pv-dec-q {
  max-width: 20ch;
  text-wrap: balance;
}

.pv-dec-opts {
  margin-top: 1.9rem;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.55rem;
  max-width: 62ch;
  color: var(--muted);
  font-size: var(--step-body);
}

.pv-dec-opts li {
  padding-left: 1.35em;
  text-indent: -1.35em;
}

.pv-dec-opts li::before {
  content: "";
  display: inline-block;
  width: 6px;
  height: 6px;
  background: var(--accent);
  margin-right: 0.75em;
  vertical-align: middle;
  transform: translateY(-2px);
}

.pv-dec-call {
  margin-top: 1.6rem;
  max-width: 62ch;
}

.pv-dec-figs {
  margin: 2.25rem 0 0;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--gutter);
}

.pv-dec-figs > div {
  background: var(--surface);
  padding: 1.15rem 1.35rem;
}

.pv-dec-f {
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 2.6vw, 2.25rem);
  line-height: 1;
  font-weight: 700;
  color: var(--ink);
}

.pv-dec-l {
  margin: 0.5rem 0 0;
  font-size: var(--step-small);
  color: var(--muted);
  line-height: 1.45;
}

@media (max-width: 760px) {
  .pv-dec-figs {
    grid-template-columns: 1fr;
  }
}

.pv-body {
  margin-top: clamp(3.5rem, 9vh, 6rem);
}

.pv-block + .pv-block {
  margin-top: clamp(3rem, 8vh, 5.5rem);
}

.pv-h {
  font-family: var(--font-display);
  font-size: clamp(1.625rem, 3.2vw, 2.75rem);
  line-height: 1.15;
  letter-spacing: -0.006em;
  font-weight: 700;
  max-width: 24ch;
}

.pv-h-sm {
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 2.2vw, 1.75rem);
}

.pv-p {
  margin-top: 1.25rem;
  color: var(--muted);
  max-width: 58ch;
}

.pv-list {
  margin-top: 1.5rem;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  max-width: 58ch;
}

.pv-list li {
  padding-left: 1.5rem;
  position: relative;
  color: var(--ink);
}

.pv-list li::before {
  content: "·";
  position: absolute;
  left: 0.35rem;
  color: var(--accent);
  font-weight: 700;
}

.pv-pit {
  margin-top: clamp(3rem, 8vh, 5.5rem);
  background: var(--surface);
  padding: clamp(1.5rem, 4vw, 3rem);
}

.pv-pit-p {
  color: var(--ink);
  max-width: 52ch;
}

.pv-next {
  margin-top: clamp(4rem, 10vh, 7rem);
  background: var(--accent);
  color: var(--accent-ink);
}

.pv-next-a {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: clamp(2rem, 5vh, 3.25rem) var(--margin);
  transition: background-color var(--t-hover) var(--ease-out);
}

.pv-next-a:hover {
  background: var(--accent-soft);
}

.pv-next-k {
  font-size: 1rem;
  color: var(--on-deep-muted);
}

.pv-next-t {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 4.6vw, 3.5rem);
  line-height: 1.05;
  letter-spacing: -0.006em;
  font-weight: 700;
}

@media (max-width: 900px) {
  .pv-metrics {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.25rem 1rem;
  }

  .pv-shot {
    aspect-ratio: 4 / 3;
  }
}
</style>
