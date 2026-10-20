<template>
  <section class="about section">
    <div class="wrap">
      <p class="about-copy" data-reveal>
        <span class="about-ink">我是黄泽圣</span>，河南信阳人，襄阳职业技术大学人工智能技术应用，2027
        年毕业。简历上写的是 Python 后端和 AI 应用开发，实际做过的东西更宽：<span
          class="hl hl-a">五个项目</span
        >，两个 AI 伙伴、一个学习工具、一个编辑器插件、一条企业后台产线。<span class="hl hl-b">它们的共同点不是用了什么技术，是都从零搭起来、跑起来、测过。</span>
        桌面助手那套记忆是我自己设计的，因为现成方案在同一批问题上召回率差了快一半；后台产线是因为第二家公司又得从头搭一遍框架，我不想再搭第三遍。
        每个项目都留了<span class="hl hl-b">测试和文档</span>，也留了<span
          class="hl hl-c">坑</span
        >：有的停更了，有的正在重构，产线那个共用密钥的缺陷还写在 README 里没改。
        我不是一开始就知道怎么做对的人。我的办法是<span class="hl hl-a">先把东西跑起来</span>，再一个个把它<span
          class="hl hl-c">改成对的</span
        >。
        <a class="about-last" href="#contact"
          ><span class="hl hl-a">2027 年毕业，找 AI 应用开发或 Python 后端的实习。下面能找到我。</span></a
        >
      </p>
    </div>
  </section>
</template>

<style scoped>
.about {
  padding-block: clamp(5rem, 12vh, 9rem);
}

.about-copy {
  columns: 2;
  column-gap: 2.5rem;
  max-width: none;
  font-size: clamp(1.5rem, 2vw, 1.875rem);
  line-height: 1.55;
  letter-spacing: -0.012em;
  color: var(--muted);
  text-align: justify;
  text-justify: inter-ideograph;
  hyphens: auto;
}

.about-ink {
  color: var(--ink);
}

.hl {
  padding: 0.08em 0.16em;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  border-radius: 1px;
}

.hl-a {
  background: var(--accent);
  color: var(--accent-ink);
}

.hl-b {
  background: var(--paper);
  color: var(--ink-on-paper);
}

.hl-c {
  background: var(--clash);
  color: var(--paper);
}

.about-last {
  display: inline;
  color: inherit;
}

.about-last .hl {
  transition: background-color var(--t-hover) var(--ease-out);
}

.about-last:hover .hl {
  background: var(--accent-soft);
}

@media (max-width: 900px) {
  .about-copy {
    columns: 1;
    font-size: clamp(1.1875rem, 5vw, 1.5rem);
    line-height: 1.7;
    text-align: left;
    padding-inline: 0.25rem;
  }
}
</style>
