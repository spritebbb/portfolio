# -*- coding: utf-8 -*-
"""Redraw the pipeline diagrams with cleaner geometry."""
import pathlib
import math
from PIL import Image, ImageDraw, ImageFont

OUT = pathlib.Path("src/assets/media")
W, H = 1400, 700

BG = (240, 238, 235)
INK = (27, 23, 19)
MUTED = (84, 73, 63)
RED = (200, 16, 46)
BOX = (248, 248, 246)

SONG = "C:/Windows/Fonts/simsun.ttc"
HEI = "C:/Windows/Fonts/msyh.ttc"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def canvas(h=H):
    im = Image.new("RGB", (W, h), BG)
    return im, ImageDraw.Draw(im)


def center_text(d, xy, text, f, fill):
    x0, y0, x1, y1 = xy
    b = d.textbbox((0, 0), text, font=f)
    d.text((x0 + (x1 - x0 - (b[2] - b[0])) / 2, y0 + (y1 - y0 - (b[3] - b[1])) / 2 - 4), text, font=f, fill=fill)


def box(d, xy, label, sub=None, fs=30, sfs=20):
    d.rectangle(xy, fill=BOX, outline=INK, width=2)
    x0, y0, x1, y1 = xy
    if not sub:
        center_text(d, xy, label, font(SONG, fs), INK)
        return
    f1 = font(SONG, fs)
    f2 = font(HEI, sfs)
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


def title(d, text, y=48):
    d.text((60, y), text, font=font(SONG, 38), fill=INK)


def note(d, text, y):
    d.text((60, y), text, font=font(HEI, 21), fill=MUTED)


# ---------- 1. five steps ----------
def steps():
    im, d = canvas(560)
    title(d, "一条流水线，五步把系统交出去")
    labels = [("换参数", "new-project.mjs"), ("加模块", "new-module.mjs"), ("体检", "schema-check.mjs"),
              ("验收", "五道门"), ("交付", "pack-deploy.mjs")]
    gap = 32
    bw = (W - 120 - gap * 4) // 5
    y0, y1 = 210, 380
    for i, (lb, sb) in enumerate(labels):
        x0 = 60 + i * (bw + gap)
        box(d, (x0, y0, x0 + bw, y1), lb, sb, fs=31, sfs=17)
        if i < 4:
            arrow(d, (x0 + bw + 5, (y0 + y1) // 2), (x0 + bw + gap - 5, (y0 + y1) // 2))
    note(d, "每一步都能单独跑，也能串起来跑；重复执行结果一致。", 470)
    im.save(OUT / "jd-diagram-steps.jpg", quality=88)
    print("steps")


# ---------- 2. one spec ----------
def spec():
    im, d = canvas(620)
    title(d, "一份 JSON 规格，长出前后端一整条链路")
    box(d, (560, 150, 840, 262), "module.json", "字段 · 类型 · 校验 · 权限", fs=28, sfs=18)
    # two trunks from the spec
    d.line([(700, 262), (700, 300)], fill=RED, width=3)
    d.line([(250, 300), (1150, 300)], fill=RED, width=3)
    d.line([(250, 300), (250, 330)], fill=RED, width=3)
    d.line([(1150, 300), (1150, 330)], fill=RED, width=3)
    arrow(d, (250, 300), (250, 336))
    arrow(d, (1150, 300), (1150, 336))
    box(d, (70, 340, 470, 470), "后端 8 个文件", "Entity · Mapper · Service · Controller · 建表脚本", fs=27, sfs=17)
    box(d, (930, 340, 1330, 470), "前端 4 份产物", "api.ts · 列表页 · 表单页 · 路由与菜单", fs=27, sfs=17)
    note(d, "生成器是幂等的：改了规格再跑一次，标记块里的内容会重写，其余不动。", 530)
    im.save(OUT / "jd-diagram-spec.jpg", quality=88)
    print("spec")


# ---------- 3. five gates ----------
def gates():
    im, d = canvas(640)
    title(d, "五道验收门，全在真实浏览器里跑")
    rows = [("整页截图", "每屏都存一张，人工能看图"),
            ("WCAG 对比度", "正文至少 4.5 : 1"),
            ("表格溢出", "宽表不许撑破容器"),
            ("个人中心 18 项", "真实点击，不 mock"),
            ("头像上传 12 项", "选文件到裁切全走一遍")]
    for i, (a, b) in enumerate(rows):
        y = 170 + i * 82
        box(d, (60, y, 470, y + 62), a, fs=25)
        d.text((510, y + 18), b, font=font(HEI, 21), fill=MUTED)
        d.text((1250, y + 14), "通过", font=font(SONG, 24), fill=RED)
    note(d, "界面贴不贴主题算不好用，机器判不了；这五道门只管能不能用、有没有坏。", 560)
    im.save(OUT / "jd-diagram-gates.jpg", quality=88)
    print("gates")


steps()
spec()
gates()
