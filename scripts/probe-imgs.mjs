// Diagnostic: are the <img> elements actually decoded when the inspector samples?
import { createServer } from 'node:http';
import { readFileSync, existsSync, statSync } from 'node:fs';
import { join, extname, resolve, normalize } from 'node:path';
import { pathToFileURL } from 'node:url';

const { Browser } = await import(
  pathToFileURL('C:/Users/sprite/.dsh/skills/design-taste-frontend/scripts/lib/cdp.mjs').href
);

const root = resolve(process.cwd(), 'dist');
const types = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css',
  '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2', '.json': 'application/json',
};
const server = createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p.endsWith('/')) p += 'index.html';
  const file = normalize(join(root, p));
  if (!file.startsWith(root) || !existsSync(file) || statSync(file).isDirectory()) {
    res.writeHead(404).end('nope');
    return;
  }
  res.writeHead(200, { 'content-type': types[extname(file)] || 'application/octet-stream' });
  res.end(readFileSync(file));
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}/`;

const snap = (label) => (el) => ({ label, el });

const browser = await Browser.launch({ width: 1440, height: 900 });
try {
  const page = await browser.newPage({ width: 1440, height: 900 });
  await page.goto(base + 'index.html', { settleMs: 1400 });

  const read = () =>
    page.eval(() => {
      const vh = window.innerHeight;
      return [...document.images].map((i) => {
        const r = i.getBoundingClientRect();
        return {
          file: (i.currentSrc || i.src).split('/').pop().slice(0, 34),
          complete: i.complete,
          nat: i.naturalWidth,
          boxW: Math.round(r.width),
          boxH: Math.round(r.height),
          top: Math.round(r.top + window.scrollY),
          inViewport: r.top < vh && r.bottom > 0,
          clipped: getComputedStyle(i.parentElement).clipPath,
        };
      });
    });

  console.log('--- after load, no scroll (1400ms) ---');
  console.log(JSON.stringify(await read(), null, 1));

  await new Promise((r) => setTimeout(r, 3000));
  console.log('--- 3s later, still no scroll ---');
  console.log(JSON.stringify(await read(), null, 1));

  await page.wheel(6000, { step: 400, pauseMs: 60 });
  await new Promise((r) => setTimeout(r, 1200));
  console.log('--- after scrolling to bottom ---');
  console.log(JSON.stringify(await read(), null, 1));

  await page.close();
} finally {
  await browser.close();
  server.close();
}
