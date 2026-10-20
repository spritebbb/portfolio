<template>
  <section class="about section">
    <div class="wrap">
      <p class="about-copy" data-reveal>
        <span class="about-ink">我是黄泽圣</span>，湖北襄阳人，襄阳职业技术大学人工智能技术应用，2027
        年毕业。简历上写的是 Python 后端和 AI 应用开发，实际上做过的东西比简历上的宽一些：<span
          class="hl hl-a">五个项目</span
        >，没有一个是我能熟练之后再做的，都是边查边写。两个是同一个「菟菚」的两种形态，一个装在桌面上，一个待在
        QQ 群里；它们共用一套想法——记忆要有<span class="hl hl-b">来源</span>、有<span
          class="hl hl-b">置信度</span
        >、能被人<span class="hl hl-c">纠正</span>，也会随时间<span class="hl hl-c">变淡</span>。第三个是给
        DSH 写的小插件，把每次技能调用折成一份可读的记录。第四个把 B 站上的 C 语言课变成会出题的私教。第五个最不像我做的：
        一条 Java 加 Vue 的企业后台产线，换四个参数就能产出一套能交付给客户的后台系统。
        <span class="about-ink">我不太相信「AI 有记忆」这种说法</span>。我信的是：一句话是谁说的、什么时候说的、有多确定、错了能不能改。这些项目就是在把这件事一条条落到<span
          class="hl hl-a">数据库</span
        >里。
        <a class="about-last" href="#contact"
          ><span class="hl hl-a">如果你也在做类似的东西，下面能找到我。</span></a
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
