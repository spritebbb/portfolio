# -*- coding: utf-8 -*-
"""Add real data panels for the two text-only projects."""
import pathlib
import re
import sys

p = pathlib.Path("src/data/projects.ts")
t = p.read_text(encoding="utf-8")

# 1) interface field
if "panel?: {" in t:
    print("interface already has panel")
else:
    anchor = "  textOnly?: boolean"
    if anchor not in t:
        sys.exit("textOnly field not found")
    t = t.replace(
        anchor,
        """  textOnly?: boolean
  panel?: { title: string; rows: { k: string; v: string }[] }""",
        1,
    )
    print("interface patched")

# 2) tuzhan-bot panel
bot_anchor = "    repoNote:\n      '这个项目已经停更"
bot_panel = """    panel: {
      title: '三十个模块，一个管一件事',
      rows: [
        { k: 'memory', v: '短期对话与人格状态' },
        { k: 'vector_store', v: '本地向量检索，语义召回' },
        { k: 'triple_memory', v: '五元组结构化事实，主体·关系·客体·时间·来源' },
        { k: 'intent', v: '闲聊 / 回忆 / 情感 / 搜索四路分流' },
        { k: 'tool_loop', v: '两轮工具调用迭代，自主决定何时检索' },
        { k: 'affection', v: '好感度四阶段与羁绊' },
        { k: 'mood', v: '心情系统，独立衰减' },
        { k: 'proactive', v: '主动消息与开口时机判断' },
        { k: 'offline_alert', v: '掉线检测、重连与心跳' },
        { k: 'cards', v: '状态卡片渲染成图发回群里' },
      ],
    },
    repoNote:
      '这个项目已经停更"""
if "triple_memory" in t:
    print("bot panel already present")
else:
    if bot_anchor not in t:
        sys.exit("tuzhan-bot repoNote anchor not found")
    t = t.replace(bot_anchor, bot_panel, 1)
    print("bot panel added")

# 3) dsh panel
dsh_anchor = "    repoNote:\n      '这个插件停在 v0.2.0"
dsh_panel = """    panel: {
      title: '一条记录，从日志流到面板',
      rows: [
        { k: '① 输入', v: 'session log 里的 skill 调用，以及用户 /name 的显式调用' },
        { k: '② 折叠', v: 'skillUsage 投影，纯函数，重放多少次结果都一样' },
        { k: '③ 传输', v: 'host 把投影值折进 list rows，不新开表、不落库' },
        { k: '④ 渲染', v: 'client 用 useSessions 读，画在 sidebar.footer.action' },
        { k: '⑤ 启用', v: '勾选技能后构造一条 /name 提示，让 host 注入全文' },
      ],
    },
    repoNote:
      '这个插件停在 v0.2.0"""
if "skillUsage 投影" in t:
    print("dsh panel already present")
else:
    if dsh_anchor not in t:
        sys.exit("dsh repoNote anchor not found")
    t = t.replace(dsh_anchor, dsh_panel, 1)
    print("dsh panel added")

p.write_text(t, encoding="utf-8", newline="")
print("projects.ts written")
