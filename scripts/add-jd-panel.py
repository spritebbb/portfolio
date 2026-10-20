# -*- coding: utf-8 -*-
"""Give the pipeline page a real data panel instead of the 'screenshot pending' note."""
import pathlib
import sys

p = pathlib.Path("src/data/projects.ts")
t = p.read_text(encoding="utf-8")

anchor = "    poster: demoPoster,"
if "① 换参数" in t:
    print("panel already present")
    sys.exit(0)
if anchor not in t:
    sys.exit("jd-pipeline poster anchor not found")

panel = """    poster: demoPoster,
    panel: {
      title: '一条流水线，五步把系统交出去',
      rows: [
        { k: '① 换参数', v: 'new-project.mjs 换四个参数，产出一套能直接跑的后台系统' },
        { k: '② 加模块', v: 'new-module.mjs 按 JSON 规格生成 8 个 Java 文件、建表脚本、前端 api 与页面，重复执行结果一致' },
        { k: '③ 体检', v: 'schema-check.mjs 只读检查库表，遇到 DROP 直接拒绝执行' },
        { k: '④ 验收', v: '五道门全在真实浏览器里跑：整页截图、WCAG 对比度、表格溢出、个人中心 18 项、头像上传 12 项' },
        { k: '⑤ 交付', v: 'pack-deploy.mjs 一条命令产出 Windows 与 Linux 包，自带 JRE，客户机不用装 Java' },
      ],
    },"""

t = t.replace(anchor, panel, 1)
p.write_text(t, encoding="utf-8", newline="")
print("jd-pipeline panel added")
