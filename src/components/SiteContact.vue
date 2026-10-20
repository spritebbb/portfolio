<template>
  <section id="contact" class="contact">
    <div class="contact-list">
      <a class="crow crow-alt" href="mailto:huangzesheng02@gmail.com" data-reveal>
        <span class="crow-text">huangzesheng02@gmail.com</span>
      </a>
      <a class="crow" href="tel:+8619172459404" data-reveal>
        <span class="crow-text">191-7245-9404</span>
      </a>
      <a
        class="crow crow-alt"
        href="https://github.com/spritebbb"
        data-reveal
        target="_blank"
        rel="noopener noreferrer"
      >
        <span class="crow-text">github.com/spritebbb</span>
      </a>
      <div class="crow" data-reveal>
        <span class="crow-text">河南 · 信阳</span>
      </div>
    </div>

    <div class="greet">
      <p class="greet-text">在找 2027 届的实习</p>
      <a class="greet-btn" href="mailto:huangzesheng02@gmail.com" aria-label="写邮件给我">
        <span aria-hidden="true">↗</span>
      </a>
    </div>
  </section>
</template>

<style scoped>
.contact {
  padding-top: var(--section);
}

.contact-list {
  display: flex;
  flex-direction: column;
}

.crow {
  font-family: var(--font-display);
  display: flex;
  align-items: flex-end;
  min-height: clamp(5rem, 11vh, 9.5rem);
  padding: 1.2rem var(--margin) 1.35rem;
  font-size: clamp(2.75rem, 6vw, 5.5rem);
  line-height: 1;
  letter-spacing: -0.006em;
  font-weight: 400;
  color: var(--ink);
  transition: background-color var(--t-hover) var(--ease-out),
    color var(--t-hover) var(--ease-out);
  overflow: hidden;
}

.crow-alt {
  background: var(--surface);
}

a.crow:hover {
  background: var(--accent);
  color: var(--accent-ink);
}

.crow-text {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}

.greet {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  background: var(--accent);
  color: var(--accent-ink);
  padding: clamp(1.5rem, 4vh, 2.5rem) var(--margin);
}

.greet-text {
  font-size: clamp(1.5rem, 3.4vw, 2.75rem);
  line-height: 1.15;
  letter-spacing: -0.006em;
  font-weight: 500;
  max-width: none;
}

.greet-btn {
  flex: none;
  width: clamp(3rem, 5vw, 4.25rem);
  height: clamp(3rem, 5vw, 4.25rem);
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--accent-ink);
  color: var(--accent);
  font-size: clamp(1.35rem, 2.4vw, 1.9rem);
  line-height: 1;
  transition: transform var(--t-ui) var(--ease-out),
    background-color var(--t-hover) var(--ease-out);
}

.greet-btn:hover {
  transform: translate(0.15em, -0.15em);
}

@media (max-width: 900px) {
  .crow {
    min-height: 4.75rem;
    padding: 0.9rem var(--margin) 1rem;
    font-size: clamp(1.35rem, 7.8vw, 2.6rem);
    letter-spacing: -0.006em;
  }

  .greet {
    flex-direction: row;
    align-items: center;
  }
}
</style>
