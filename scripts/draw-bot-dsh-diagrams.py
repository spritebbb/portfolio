# -*- coding: utf-8 -*-
"""Draw architecture diagrams for the QQ bot and the DSH plugin."""
import pathlib
import math
from PIL import Image, ImageDraw, ImageFont

OUT = pathlib.Path("src/assets/media")
W = 1400

BG = (240, 238, 235)
INK = (27, 23, 19)
MUTED = (84, 73, 63)
RED = (200, 16, 46)
BOX = (248, 248, 246)

SONG = "C:/Windows/Fonts/simsun.ttc"
HEI = "C:/Windows/Fonts/msyh.ttc"


def F(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def canvas(h):
    im = Image.new("RGB", (W, h), BG)
    return im, ImageDraw.Draw(im)


def ct(d, xy, text, f, fill):
    x0, y0, x1, y1 = xy
    b = d.textbbox((0, 0), text, font=f)
    d.text((x0 + (x1 - x0 - (b[2] - b[0])) / 2, y0 + (y1 - y0 - (b[3] - b[1])) / 2 - 4), text, font=f, fill=fill)


def box(d, xy, label, sub=None, fs=28, sfs=18):
    d.rectangle(xy, fill=BOX, outline=INK, width=2)
    x0, y0, x1, y1 = xy
    if not sub:
        ct(d, xy, label, F(SONG, fs), INK)
        return
    f1, f2 = F(SONG, fs), F(HEI, sfs)
    b1 = d.textbbox((0, 0), label, font=f1)
    b2 = d.textbbox((0, 0), sub, font=f2)
    total = (b1[3] - b1[1]) + 10 + (b2[3] - b2[1])
    top = y0 + (y1 - y0 - total) / 2
    d.text((x0 + (x1 - x0 - (b1[2] - b1[0])) / 2, top), label, font=f1, fill=INK)
    d.text((x0 + (x1 - x0 - (b2[2] - b2[0])) / 2, top + (b1[3] - b1[1]) + 10), sub, font=f2, fill=MUTED)


def arrow(d, p0, p1, color=RED, w=3):
    d.line([p0, p1], fill=color, width=w)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (-0.42, 0.42):
        d.line([p1, (p1[0] - 13 * math.cos(ang + s), p1[1] - 13 * math.sin(ang + s))], fill=color, width=w)


def title(d, text, y=46):
    d.text((60, y), text, font=F(SONG, 37), fill=INK)


def note(d, text, y):
    d.text((60, y), text, font=F(HEI, 21), fill=MUTED)


# ---------- bot 1: message flow ----------
def bot_flow():
    im, d = canvas(600)
    title(d, "一条消息进来，先问清它是哪一类")
    box(d, (60, 200, 320, 320), "群里一条消息", fs=26)
    box(d, (400, 200, 660, 320), "意图路由", "四路分流", fs=28)
    arrow(d, (320, 260), (396, 260))
    routes = [("闲聊", "走人格对话"), ("回忆", "才触发 RAG 检索"), ("情感", "读好感度与心情"),
              ("搜索", "调工具再回答")]
    # trunk out of the router, then one branch per route
    d.line([(660, 260), (700, 260)], fill=RED, width=3)
    ys = [380 + i * 52 for i in range(4)]
    d.line([(700, ys[0] + 12), (700, ys[-1] + 12)], fill=RED, width=3)
    d.line([(700, 260), (700, ys[0] + 12)], fill=RED, width=3)
    for (a, b), y in zip(routes, ys):
        d.line([(700, y + 12), (760, y + 12)], fill=RED, width=3)
        arrow(d, (700, y + 12), (766, y + 12))
        d.text((790, y - 2), a, font=F(SONG, 23), fill=INK)
        d.text((880, y + 2), b, font=F(HEI, 19), fill=MUTED)
    note(d, "四路分开走，是为了别把无关的历史一股脑塞进 prompt：塞得越多，答得越差。", 560)
    im.save(OUT / "bot-diagram-flow.jpg", quality=88)
    print("flow")


# ---------- bot 2: five-tuple ----------
def bot_tuple():
    im, d = canvas(660)
    title(d, "一句话，拆成五个字段")
    box(d, (60, 180, 700, 300), "「我上周说不喜欢香菜，改主意了」", fs=24)
    fields = ["主体 · 她", "关系 · 讨厌", "客体 · 香菜", "时间 · 2026-06-14", "来源 · 群聊第 3 轮"]
    for i, f in enumerate(fields):
        y = 350 + i * 40
        d.text((60, y), f, font=F(SONG, 24), fill=INK)
    d.rectangle((760, 300, 1340, 520), fill=BOX, outline=INK, width=2)
    lines = ["检索时按字段查：", "  · 按主体：她怎么看这件事", "  · 按时间：最近的说法覆盖旧的",
             "  · 按来源：这句话是谁在哪儿说的", "", "改主意能被表达出来，", "因为「旧值」和「新值」都在字段里。"]
    for i, l in enumerate(lines):
        d.text((800, 330 + i * 26), l, font=F(HEI, 20), fill=INK if i < 4 else MUTED)
    note(d, "整句丢进向量库，两句几乎重合；拆成字段之后，谁在什么时候改的口供是能分开的。", 610)
    im.save(OUT / "bot-diagram-tuple.jpg", quality=88)
    print("tuple")


# ---------- bot 3: modules grouped ----------
def bot_modules():
    im, d = canvas(680)
    title(d, "三十个模块，五个组")
    groups = [
        ("记忆", "memory · vector_store · triple_memory · topic_memory"),
        ("说话", "intent · tool_loop · style · terms · memes · speak"),
        ("情绪", "affection · mood · rhythm"),
        ("时间", "schedule · holidays · proactive"),
        ("运行", "offline_alert · cards · profile · features"),
    ]
    for i, (g, mods) in enumerate(groups):
        y = 160 + i * 84
        box(d, (60, y, 300, y + 62), g, fs=24)
        d.text((340, y + 14), mods, font=F(HEI, 18), fill=MUTED)
    note(d, "每个模块只管一件事，跨模块通过事件和读取接口拿数据，不直接改别人的表。", 630)
    im.save(OUT / "bot-diagram-modules.jpg", quality=88)
    print("modules")


# ---------- dsh 1: data flow ----------
def dsh_flow():
    im, d = canvas(560)
    title(d, "一条记录，从日志流到面板")
    steps = [("会话日志", "skill 调用 · /name"), ("投影", "纯函数 fold"), ("host", "折进 list rows"),
             ("client", "侧边栏渲染")]
    gap = 30
    bw = (W - 120 - gap * 3) // 4
    y0, y1 = 210, 360
    for i, (a, b) in enumerate(steps):
        x0 = 60 + i * (bw + gap)
        box(d, (x0, y0, x0 + bw, y1), a, b, fs=27, sfs=17)
        if i < 3:
            arrow(d, (x0 + bw + 4, (y0 + y1) // 2), (x0 + bw + gap - 4, (y0 + y1) // 2))
    note(d, "中间没有新表：投影是纯函数，同一份日志重放多少次，结果都一样。", 450)
    im.save(OUT / "dsh-diagram-flow.jpg", quality=88)
    print("dsh flow")


# ---------- dsh 2: projection shape ----------
def dsh_shape():
    im, d = canvas(560)
    title(d, "投影长这样：两个值，一份历史")
    d.rectangle((60, 160, 1340, 470), fill=BOX, outline=INK, width=2)
    lines = [
        "skillUsage = {",
        "  active  : 这个会话现在挂着的技能",
        "  history : [{ name, at, by: 'tool' | 'user' }, …]",
        "}",
        "",
        "host  把这份值折进 list rows，不落库",
        "client 用 useSessions 读它，画在 sidebar.footer.action",
    ]
    for i, l in enumerate(lines):
        color = INK if i < 4 else MUTED
        d.text((96, 190 + i * 40), l, font=F(HEI, 21), fill=color)
    note(d, "「不另存一份」是这套东西的全部要点：两份真相早晚对不上。", 500)
    im.save(OUT / "dsh-diagram-shape.jpg", quality=88)
    print("dsh shape")


# ---------- dsh 3: two halves ----------
def dsh_sides():
    im, d = canvas(560)
    title(d, "两端各做一半，中间不共享内存")
    d.rectangle((60, 170, 660, 400), fill=BOX, outline=INK, width=2)
    d.text((92, 196), "host 半边", font=F(SONG, 26), fill=INK)
    for i, l in enumerate(["注册 skillUsage 投影", "观察 skill 工具调用", "把值折进 list rows"]):
        d.text((92, 250 + i * 34), "· " + l, font=F(HEI, 20), fill=MUTED)
    d.rectangle((740, 170, 1340, 400), fill=BOX, outline=INK, width=2)
    d.text((772, 196), "client 半边", font=F(SONG, 26), fill=INK)
    for i, l in enumerate(["读 useSessions 座位", "画技能中心面板", "构造 /name 让 host 注入正文"]):
        d.text((772, 250 + i * 34), "· " + l, font=F(HEI, 20), fill=MUTED)
    arrow(d, (660, 285), (736, 285))
    note(d, "两边通过 projection 这一个通道交换数据，没有额外的表、没有额外的进程。", 460)
    im.save(OUT / "dsh-diagram-sides.jpg", quality=88)
    print("dsh sides")


bot_flow()
bot_tuple()
bot_modules()
dsh_flow()
dsh_shape()
dsh_sides()
