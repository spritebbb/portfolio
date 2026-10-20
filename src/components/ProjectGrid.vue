<template>
  <section id="projects" class="grid-sec section">
    <div class="wrap">
      <h2 class="head grid-title" data-reveal>
        <span>五个项目，</span>
        <span class="grid-indent">各自能跑</span>
      </h2>

      <ul class="cards">
        <li v-for="p in projects" :key="p.slug" class="card" data-reveal>
          <a class="card-link" :href="`./${p.slug}/`">
            <div class="card-shot" data-ui>
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
            </div>
            <div class="card-body">
              <p class="card-name">{{ p.name }}</p>
              <p class="card-tag">{{ p.tagline }}</p>
              <ul class="card-nums">
                <li v-for="m in p.metrics.slice(0, 3)" :key="m.label">
                  <span class="card-num">{{ m.value }}</span>
                  <span class="card-num-l">{{ m.label }}</span>
                </li>
              </ul>
              <span class="card-go">看详情 ↗</span>
            </div>
          </a>
        </li>
      </ul>
    </div>
  </section>
</template>

<script setup lang="ts">
import { projects } from '../data/projects'
</script>

<style scoped>
.grid-sec {
  padding-block: var(--section);
}

.grid-title {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: var(--step-head);
  line-height: 1.15;
  margin: 0 0 clamp(2rem, 5vh, 3.5rem);
}

.grid-indent {
  display: block;
  padding-left: 2ch;
  color: var(--muted);
}

.cards {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: clamp(1.25rem, 2.6vw, 2.25rem);
}

.card {
  background: var(--paper);
}

.card-link {
  display: block;
  padding: clamp(1rem, 1.8vw, 1.5rem);
}

.card-shot {
  aspect-ratio: 16 / 9;
  background: var(--surface);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  padding: clamp(1rem, 2vw, 1.6rem);
  color: var(--ink);
}

.card-shot-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 62%;
  display: block;
}

.card-shot-name {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: clamp(1.35rem, 2.2vw, 2rem);
  line-height: 1.2;
}

.card-shot-note {
  font-size: var(--step-small);
  color: var(--muted);
}

.card-body {
  padding-top: clamp(0.9rem, 1.6vw, 1.25rem);
}

.card-name {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.125rem;
  margin: 0;
}

.card-tag {
  margin: 0.5rem 0 0;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 34ch;
}

.card-nums {
  list-style: none;
  padding: 0;
  margin: 1rem 0 0;
  display: flex;
  gap: clamp(1rem, 2.4vw, 2rem);
  flex-wrap: wrap;
}

.card-num {
  display: block;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.5rem;
  line-height: 1.1;
  color: var(--accent);
}

.card-num-l {
  display: block;
  font-size: var(--step-small);
  color: var(--muted);
}

.card-go {
  display: inline-block;
  margin-top: 1.1rem;
  font-size: var(--step-small);
  color: var(--ink);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.3em;
}

.card-link:hover .card-go {
  color: var(--accent);
}

@media (max-width: 860px) {
  .cards {
    grid-template-columns: 1fr;
  }

  .grid-indent {
    padding-left: 1ch;
  }
}
</style>
