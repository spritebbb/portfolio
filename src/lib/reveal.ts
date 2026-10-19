/**
 * Reveal-on-scroll. One observer for every animated block.
 * Respects prefers-reduced-motion by simply marking everything in.
 */

const SELECTOR = '[data-reveal], .lines, .shutter'

const reduced =
  typeof window !== 'undefined' &&
  window.matchMedia('(prefers-reduced-motion: reduce)').matches

export function initReveal(): void {
  const nodes = Array.from(document.querySelectorAll<HTMLElement>(SELECTOR))
  if (nodes.length === 0) return

  if (reduced) {
    nodes.forEach((n) => n.classList.add('is-in'))
    return
  }

  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue
        entry.target.classList.add('is-in')
        io.unobserve(entry.target)
      }
    },
    { rootMargin: '0px 0px 8% 0px', threshold: 0.01 },
  )

  nodes.forEach((n) => io.observe(n))
}
