<template>
  <section class="demo section">
    <div class="wrap grid">
      <div class="demo-head" data-reveal>
        <h2 class="head demo-title">
          <span>一条记忆</span>
          <span class="demo-indent">的一生</span>
        </h2>
        <p class="demo-sub">
          拖时间，看一条事实怎么变淡；点「又提到一次」，看它怎么重新变实。
        </p>
        <p class="demo-note">
          曲线是示意，不是把项目那套代码原样搬过来：真实参数单独管，这里只留「重要的事衰减得慢」。
        </p>
      </div>

      <div class="demo-card" data-ui data-reveal>
        <dl class="demo-meta">
          <div>
            <dt>主语</dt>
            <dd>她</dd>
          </div>
          <div>
            <dt>来源</dt>
            <dd>2026-06-14 · 群聊第 3 轮</dd>
          </div>
          <div>
            <dt>固定</dt>
            <dd>{{ pinned ? '是' : '否' }}</dd>
          </div>
        </dl>

        <p class="demo-fact">
          <span class="demo-s">她</span>
          <span class="demo-dot" aria-hidden="true">·</span>
          <span class="demo-r">讨厌</span>
          <span class="demo-dot" aria-hidden="true">·</span>
          <span class="demo-o">香菜</span>
        </p>

        <div class="demo-readout">
          <span class="demo-conf nums">{{ Math.round(confidence * 100) }}%</span>
          <span class="demo-state">{{ stateLabel }}</span>
        </div>

        <div class="demo-controls">
          <label class="demo-slider">
            <span class="demo-slider-label">
              距上次提到
              <span class="nums">{{ days }}</span> 天
            </span>
            <input
              v-model.number="days"
              class="demo-range"
              type="range"
              min="0"
              max="240"
              step="1"
              :aria-valuetext="`${days} 天`"
            />
          </label>

          <div class="demo-buttons">
            <button class="demo-btn" type="button" @click="mention">
              又提到一次
            </button>
            <button
              class="demo-btn demo-btn-ghost"
              type="button"
              :aria-pressed="pinned"
              @click="pinned = !pinned"
            >
              {{ pinned ? '取消固定保留' : '固定保留' }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

const days = ref(0)
const pinned = ref(false)
const reinforcements = ref(0)

const HALF_LIFE = 75

const confidence = computed(() => {
  if (pinned.value) return 0.98
  const base = 0.92 + reinforcements.value * 0.14
  return Math.min(1, Math.max(0.02, base * Math.exp(-days.value / HALF_LIFE)))
})

const stateLabel = computed(() => {
  if (pinned.value) return '已固定保留，不再衰减'
  const c = confidence.value
  if (c > 0.75) return '还记得清楚'
  if (c > 0.45) return '开始模糊'
  if (c > 0.2) return '只剩下一点影子'
  return '基本想不起来了'
})

const mention = () => {
  days.value = 0
  reinforcements.value += 1
}
</script>

<style scoped>
.demo-head {
  grid-column: 1 / 7;
}

.demo-title {
  display: flex;
  flex-direction: column;
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.02;
}

.demo-indent {
  padding-left: 1.6em;
}

.demo-sub {
  margin-top: 1.5rem;
  color: var(--muted);
  font-size: var(--step-body);
  max-width: 34ch;
}

.demo-note {
  margin-top: 1rem;
  color: var(--muted);
  font-size: var(--step-small);
  line-height: 1.55;
  max-width: 36ch;
}

.demo-card {
  grid-column: 7 / 13;
  align-self: end;
  background: var(--surface);
  padding: clamp(1.5rem, 3vw, 2.75rem);
  border-radius: var(--radius);
}

.demo-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem 2rem;
  margin: 0;
  font-size: 1rem;
  color: var(--muted);
}

.demo-meta > div {
  display: flex;
  gap: 0.5rem;
}

.demo-meta dt {
  color: var(--muted);
}

.demo-meta dd {
  margin: 0;
  color: var(--ink);
}

.demo-fact {
  font-family: var(--font-display);
  margin-top: 1.75rem;
  font-size: clamp(1.75rem, 3.2vw, 2.75rem);
  line-height: 1.15;
  letter-spacing: -0.006em;
  font-weight: 500;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.28em;
  max-width: none;
}

.demo-dot {
  color: var(--muted);
  font-weight: 400;
}

.demo-r {
  color: var(--accent);
}

.demo-readout {
  margin-top: 2rem;
  display: flex;
  align-items: baseline;
  gap: 1rem;
  flex-wrap: wrap;
}

.demo-conf {
  font-size: clamp(2.5rem, 4.6vw, 4rem);
  line-height: 1;
  font-weight: 500;
  letter-spacing: -0.006em;
}

.demo-state {
  color: var(--muted);
  font-size: 1rem;
}

.demo-controls {
  margin-top: 2.25rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.demo-slider {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.demo-slider-label {
  font-size: 1rem;
  color: var(--muted);
}

.demo-range {
  width: 100%;
  accent-color: var(--accent);
  height: 2rem;
  cursor: pointer;
}

.demo-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.demo-btn {
  min-height: 2.75rem;
  padding: 0.55rem 1.15rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: 1rem;
  font-weight: 600;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  transition: background-color var(--t-hover) var(--ease-out),
    transform var(--t-press) var(--ease-soft);
}

.demo-btn:hover {
  background: var(--accent-soft);
}

.demo-btn:active {
  transform: translateY(2px);
}

.demo-btn-ghost {
  background: transparent;
  color: var(--ink);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.32em;
  text-decoration-color: var(--muted);
}

.demo-btn-ghost:hover {
  background: var(--deep);
  text-decoration-color: var(--accent);
}

@media (max-width: 900px) {
  .demo-head,
  .demo-card {
    grid-column: 1 / 13;
  }

  .demo-card {
    margin-top: 2rem;
  }

  .demo-indent {
    padding-left: 0.8em;
  }
}
</style>
