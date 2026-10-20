import pathlib

p = pathlib.Path('src/ProjectView.vue')
t = p.read_text(encoding='utf-8')

old = '''        <div class="pv-shot-foot">
          <p class="pv-shot-t">界面截图待补</p>
          <p class="pv-shot-d">
            这个位置将来放 {{ project.name }} 的真实截图。现在先把它的真实数字放在上面，不拿别人的图充样子。
          </p>'''

new = '''        <div class="pv-shot-foot">
          <p class="pv-shot-t">
            {{ project.textOnly ? '这个项目没有截图' : '界面截图待补' }}
          </p>
          <p class="pv-shot-d">
            {{
              project.textOnly
                ? '它不是重点展示的项目，所以不单独配图。上面这几个数字是它全部的量化结果，剩下的都在下面的文字里。'
                : `这个位置将来放 ${project.name} 的真实截图。现在先把它的真实数字放在上面，不拿别人的图充样子。`
            }}
          </p>'''

if '它不是重点展示的项目' not in t:
    assert old in t, 'pv-shot-foot block not found'
    t = t.replace(old, new)

p.write_text(t, encoding='utf-8', newline='')
print('pv-shot-foot:', '它不是重点展示的项目' in t)
