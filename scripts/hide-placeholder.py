import pathlib

p = pathlib.Path('src/ProjectView.vue')
t = p.read_text(encoding='utf-8')

old = '        <div class="pv-shot-foot">'
new = '        <div v-if="!project.shots" class="pv-shot-foot">'

if new not in t:
    assert old in t, 'pv-shot-foot not found'
    t = t.replace(old, new, 1)
    p.write_text(t, encoding='utf-8', newline='')
    print('patched')
else:
    print('already patched')
