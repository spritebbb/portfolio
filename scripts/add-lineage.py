# -*- coding: utf-8 -*-
"""Make the lineage explicit: the assistant grew out of the QQ bot."""
import pathlib
import sys

p = pathlib.Path("src/data/projects.ts")
t = p.read_text(encoding="utf-8")

if "先在 QQ 机器人上跑过一遍" in t:
    print("lineage already present")
    sys.exit(0)

old = """        heading: '记忆不是一段文本，是一条有出处的记录',
        paras: [
          '大多数「AI 记忆」的做法是把聊天记录摘要一下再塞回 prompt。问题是摘要会丢来源，丢了来源就没人能判断它该不该信。',"""

new = """        heading: '记忆不是一段文本，是一条有出处的记录',
        paras: [
          '这套东西不是一次写成的：记忆系统先在 QQ 机器人上跑过一遍，那边受够了风控和协议变动，搬进桌面端才不用再跟平台较劲。',
          '大多数「AI 记忆」的做法是把聊天记录摘要一下再塞回 prompt。问题是摘要会丢来源，丢了来源就没人能判断它该不该信。',"""

if old not in t:
    sys.exit("assistant first block anchor not found")
t = t.replace(old, new, 1)
print("assistant lineage sentence added")

# make the bot's repoNote point at a concrete project instead of "第一个项目"
old_note = "同样的记忆系统搬到桌面端就不用再受这些限制，所以重心转到了第一个项目。"
new_note = "同样的记忆系统搬到桌面端就不用再受这些限制，所以重心转到了菟菚桌面助手。"
if old_note in t:
    t = t.replace(old_note, new_note, 1)
    print("bot repoNote clarified")
else:
    print("bot repoNote text not matched, checking variant")
    old2 = "所以重心转到了第一个项目"
    if old2 in t:
        t = t.replace(old2, "所以重心转到了菟菚桌面助手", 1)
        print("bot repoNote clarified (variant)")

p.write_text(t, encoding="utf-8", newline="")
print("written")
