<template>
  <section id="work" class="work section">
    <div class="wrap">
      <nav class="work-para" aria-label="项目列表">
        <span class="work-open">五个项目：</span
        ><template v-for="(p, i) in projects" :key="p.slug"
          ><a class="work-name" :href="`./${p.slug}/`" data-reveal>{{ p.name }}<span
              v-if="i < projects.length - 1"
              class="work-sep"
              >，</span
              ><span v-else class="work-end">。</span
            ></a
          ></template>
      </nav>

      <p class="small work-meta">
        五个仓库都在 GitHub · 388 项自动化测试 · 五道真机验收门
      </p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { projects } from '../data/projects'
</script>

<style scoped>
.work {
  padding-top: var(--section);
  padding-bottom: var(--section);
}

.work-para {
  font-size: clamp(2.25rem, 6.4vw, 5.4rem);
  line-height: 1.1;
  letter-spacing: -0.006em;
  font-weight: 700;
  color: var(--muted);
  max-width: none;
  text-wrap: pretty;
}

.work-open {
  color: var(--ink);
}

.work-name {
  font-family: var(--font-display);
  display: inline-block;
  white-space: nowrap;
  color: var(--muted);
  transition: color var(--t-hover) var(--ease-out);
}

.work-name:hover {
  color: var(--ink);
  text-decoration: underline;
  text-decoration-thickness: 0.06em;
  text-underline-offset: 0.12em;
}

.work-sep,
.work-end {
  color: var(--muted);
}

.work-meta {
  margin-top: clamp(1.5rem, 4vh, 2.75rem);
  font-size: 1rem;
  color: var(--muted);
}

@media (max-width: 900px) {
  .work-para {
    font-size: clamp(1.75rem, 9vw, 3rem);
    line-height: 1.24;
    letter-spacing: -0.018em;
  }

  .work-name {
    display: inline;
    white-space: normal;
    color: var(--ink);
  }
}
</style>
