import pathlib

p = pathlib.Path('src/ProjectView.vue')
t = p.read_text(encoding='utf-8')

# 1) add a slim modifier when real shots exist
old_tag = '      <div class="pv-shot" data-ui data-reveal>'
new_tag = '      <div class="pv-shot" :class="{ \'pv-shot--slim\': project.shots }" data-ui data-reveal>'

if 'pv-shot--slim' not in t:
    assert old_tag in t, 'pv-shot tag not found'
    t = t.replace(old_tag, new_tag, 1)

    css_anchor = '.pv-shot {'
    css = '''.pv-shot--slim {
  min-height: 0;
  justify-content: flex-start;
}

.pv-shot {'''
    t = t.replace(css_anchor, css, 1)

p.write_text(t, encoding='utf-8', newline='')
print('slim:', 'pv-shot--slim' in t)
