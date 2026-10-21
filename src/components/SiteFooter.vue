<template>
  <footer class="foot">
    <div class="foot-top">
      <div class="foot-col">
        <p class="foot-key">项目</p>
        <ul>
          <li v-for="p in projects" :key="p.slug">
            <a :href="`./${p.slug}/`">{{ p.name }}</a>
          </li>
        </ul>
      </div>

      <div class="foot-col">
        <p class="foot-key">常用</p>
        <ul>
          <li>Python · FastAPI</li>
          <li>Vue 3 · TypeScript</li>
          <li>SQLite · 向量检索</li>
          <li>MCP · NoneBot2</li>
        </ul>
      </div>

      <div class="foot-col">
        <p class="foot-key">找得到我</p>
        <ul>
          <li><a href="mailto:huangzesheng02@gmail.com">huangzesheng02@gmail.com</a></li>
          <li><a href="tel:+8619172459404">191-7245-9404</a></li>
          <li>
            <a href="https://github.com/spritebbb" target="_blank" rel="noopener noreferrer"
              >github.com/spritebbb</a
            >
          </li>
        </ul>
      </div>

      <div class="foot-col">
        <p class="foot-key">说明</p>
        <ul>
          <li>页面图片均为项目自身的界面截图与架构图，未使用外部素材。</li>
          <li>五个项目的代码都在 GitHub 上公开，可从各详情页的「看源码」进入。</li>
        </ul>
      </div>
    </div>

    <div class="foot-bottom">
      <svg
        class="foot-mark foot-mark-latin"
        viewBox="0 0 1328 210"
        preserveAspectRatio="xMinYMax meet"
        aria-hidden="true"
      >
        <text
          x="0"
          y="170"
          textLength="1328"
          lengthAdjust="spacing"
          font-size="186"
          font-weight="500"
          letter-spacing="-0.03em"
        >
          HUANG ZESHENG
        </text>
      </svg>
      <svg
        class="foot-mark foot-mark-cjk"
        viewBox="0 0 1328 260"
        preserveAspectRatio="xMinYMax meet"
        aria-hidden="true"
      >
        <text x="0" y="220" textLength="1328" lengthAdjust="spacing" font-size="250" font-family="Newsreader, Noto Serif SC, serif">黄泽圣</text>
      </svg>
      <p class="foot-legal">
        <span>© 2026 黄泽圣</span>
        <span>用 Vue 3 和 Vite 手写，没有用模板</span>
      </p>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { projects } from '../data/projects'
</script>

<style scoped>
.foot {
  /* the only dark block in the page: it closes things and makes the warm ground read warmer */
  --ink-on-paper: var(--on-deep);
  --muted: var(--on-deep-muted);
  background: var(--deep);
  color: var(--on-deep);
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto 1fr auto;
  padding: clamp(2rem, 4vh, 3rem) var(--margin) clamp(1.25rem, 3vh, 2rem);
}

.foot-top {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1.5rem 2rem;
}

.foot-col {
  font-size: 1rem;
  line-height: 1.65;
}

.foot-key {
  color: var(--ink-on-paper);
  font-weight: 600;
  margin-bottom: 0.4rem;
  max-width: none;
}

.foot-col ul {
  list-style: none;
  padding: 0;
  margin: 0;
  color: var(--on-deep-muted);
}

.foot-col li + li {
  margin-top: 0.15rem;
}

.foot-col a {
  color: var(--on-deep-muted);
  transition: color var(--t-hover) var(--ease-out);
}

.foot-col a:hover {
  color: var(--ink-on-paper);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.28em;
}

.foot-bottom {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 0.75rem;
  padding-top: 2rem;
}

.foot-mark {
  width: 100%;
  height: auto;
  fill: var(--ink-on-paper);
  overflow: visible;
}

.foot-mark-cjk {
  display: none;
}

.foot-legal {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 0.5rem 1.5rem;
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--on-deep-muted);
  max-width: none;
}

@media (max-width: 900px) {
  .foot-top {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    row-gap: 2rem;
  }

  .foot-mark-latin {
    display: none;
  }

  .foot-mark-cjk {
    display: block;
  }

  .foot-bottom {
    padding-top: 20svh;
  }
}
</style>
