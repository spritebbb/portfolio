import pathlib

p = pathlib.Path('src/components/ProjectGrid.vue')
t = p.read_text(encoding='utf-8')

old = '''            <div class="card-shot" data-ui>
              <span class="card-shot-name">{{ p.name }}</span>
              <span class="card-shot-note">界面截图待补</span>
            </div>'''

new = '''            <div class="card-shot" data-ui>
              <img
                v-if="p.poster"
                class="card-shot-img"
                :src="p.poster"
                :alt="`${p.name} 的界面截图`"
                loading="eager"
                decoding="async"
              />
              <template v-else>
                <span class="card-shot-name">{{ p.name }}</span>
                <span class="card-shot-note">界面截图待补</span>
              </template>
            </div>'''

if 'card-shot-img' not in t:
    assert old in t, 'card-shot block not found'
    t = t.replace(old, new)

    anchor = '.card-shot-name {'
    css = '''.card-shot-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 62%;
  display: block;
}

.card-shot-name {'''
    t = t.replace(anchor, css, 1)

p.write_text(t, encoding='utf-8', newline='')
print('grid:', 'card-shot-img' in t)
