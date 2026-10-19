<template>
  <header class="hero">
    <div class="hero-top">
      <a class="hero-mark" href="./">黄泽圣</a>
      <a
        class="hero-gh"
        href="https://github.com/spritebbb"
        target="_blank"
        rel="noopener noreferrer">GitHub</a
      >
    </div>

    <div class="hero-body">
      <h1 class="display hero-title lines">
        <span class="line"><span>给 AI 一副记性</span></span>
        <span class="line"><span>让它记得住人</span></span>
      </h1>

      <p class="hero-sub" data-reveal>
        四个项目，同一件事：<br class="m-only" />让 AI 记得住一个人，<br />并且记得对。
      </p>

      <div class="hero-actions" data-reveal>
        <a class="button" href="#work">
          看这四个项目
          <span class="arrow" aria-hidden="true">↗</span>
        </a>
        <a
          class="link-plain hero-alt"
          href="https://github.com/spritebbb"
          target="_blank"
          rel="noopener noreferrer">四个仓库都在 GitHub</a
        >
      </div>
    </div>

    <div class="hero-foot">
      <span>2027 届 · 襄阳职业技术大学 · 人工智能技术应用</span>
      <span>找 AI 应用开发 / Python 后端</span>
    </div>
  </header>
</template>

<style scoped>
.hero {
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto 1fr auto;
  padding: 1.75rem var(--margin) 0;
}

.m-only {
  display: none;
}

@media (max-width: 560px) {
  .m-only {
    display: initial;
  }
}

.hero-foot {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem 2rem;
  flex-wrap: wrap;
  margin: 0 calc(var(--margin) * -1);
  padding: 1.05rem var(--margin);
  background: var(--accent);
  color: var(--accent-ink);
  font-size: var(--step-small);
  letter-spacing: 0.01em;
}

.hero-top {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  font-size: var(--step-small);
}

.hero-mark {
  font-weight: 600;
  letter-spacing: 0.01em;
}

.hero-gh {
  color: var(--muted);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.32em;
  text-decoration-color: currentcolor;
  transition: color var(--t-hover) var(--ease-out);
}

.hero-gh:hover {
  color: var(--ink);
}

.hero-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0;
  padding-bottom: 6vh;
  text-align: center;
}

.hero-title {
  margin: 0;
  width: fit-content;
  margin-inline: auto;
  margin-top: -4vh;
}

.hero-sub {
  margin-top: clamp(1.5rem, 4vh, 3.5rem);
  font-size: var(--step-body);
  line-height: 1.7;
  color: var(--muted);
  max-width: 34ch;
}

.hero-actions {
  margin-top: clamp(1.75rem, 4.5vh, 3rem);
  display: flex;
  align-items: center;
  gap: clamp(1rem, 2.5vw, 2rem);
  flex-wrap: wrap;
  justify-content: center;
}

.hero-alt {
  font-size: var(--step-small);
}

@media (max-width: 900px) {
  .hero-body {
    padding-bottom: 8vh;
  }

  .hero-title {
    margin-top: 0;
  }

  .hero-sub {
    max-width: 26ch;
  }

  .hero-actions {
    flex-direction: column;
    gap: 1.25rem;
  }
}
</style>
