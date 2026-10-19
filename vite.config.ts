import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'node:path'

const root = import.meta.dirname

export default defineConfig({
  // Relative base so the same dist works on GitHub Pages project sites,
  // Cloudflare Pages, or opened straight from disk.
  base: './',
  plugins: [vue()],
  build: {
    // GitHub Pages 'deploy from branch' only serves '/' or '/docs',
    // so the build lands in docs/ and ships with the source.
    outDir: 'docs',
    emptyOutDir: true,
    target: 'es2022',
    assetsInlineLimit: 0,
    rollupOptions: {
      input: {
        home: resolve(root, 'index.html'),
        'tuzhan-assistant': resolve(root, 'tuzhan-assistant/index.html'),
        'tuzhan-bot': resolve(root, 'tuzhan-bot/index.html'),
        'dsh-skill-usage': resolve(root, 'dsh-skill-usage/index.html'),
        cstudy: resolve(root, 'cstudy/index.html'),
      },
    },
  },
})
