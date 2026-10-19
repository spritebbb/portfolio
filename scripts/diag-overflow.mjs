// Diagnostic: find elements that stick out past the viewport.
// Zero dependencies; reuses the taste-skill CDP client + a tiny static server.
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
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml',
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

const browser = await Browser.launch({ width: 1440, height: 900 });
try {
  for (const [w, h] of [[1440, 900], [768, 1024], [390, 844]]) {
    const page = await browser.newPage({ width: w, height: h });
    await page.goto(base + 'index.html', { settleMs: 1800 });
    // force every lazy image to load before measuring
    await page.eval(() => {
      document.querySelectorAll('img[loading]').forEach((i) => { i.loading = 'eager'; });
      window.scrollTo(0, document.body.scrollHeight);
      return true;
    });
    await new Promise((r) => setTimeout(r, 1200));
    const report = await page.eval(() => {
      const vw = document.documentElement.clientWidth;
      const out = [];
      for (const el of document.querySelectorAll('body *')) {
        const r = el.getBoundingClientRect();
        if (r.width === 0 && r.height === 0) continue;
        const over = Math.max(r.right - vw, -r.left);
        if (over > 1) {
          out.push({
            tag: el.tagName.toLowerCase(),
            cls: String(el.className?.baseVal ?? el.className ?? '').slice(0, 70),
            left: Math.round(r.left), right: Math.round(r.right),
            w: Math.round(r.width), h: Math.round(r.height), over: Math.round(over),
            parent: String(el.parentElement?.className?.baseVal ?? el.parentElement?.className ?? '').slice(0, 50),
          });
        }
      }
      out.sort((a, b) => b.over - a.over);
      return {
        vw,
        docScrollWidth: document.documentElement.scrollWidth,
        bodyScrollWidth: document.body.scrollWidth,
        imgs: [...document.querySelectorAll('img')].map((i) => ({
          w: i.naturalWidth, cw: Math.round(i.getBoundingClientRect().width),
        })),
        offenders: out.slice(0, 14),
      };
    });
    console.log(`\n===== ${w}x${h} =====`);
    console.log(JSON.stringify(report, null, 2));
    await page.close();
  }
} finally {
  await browser.close();
  server.close();
}
