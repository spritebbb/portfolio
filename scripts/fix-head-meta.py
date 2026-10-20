import pathlib

# 五个入口 HTML 的 <head> 还留着第一版深绿配色（#0f1f10 / #c6f19d / color-scheme: dark），
# 改 tokens.css 时漏了这一处，页面本身是暖白，浏览器 UI 和 favicon 却是深绿。
PAGES = [
    "index.html",
    "tuzhan-assistant/index.html",
    "tuzhan-bot/index.html",
    "dsh-skill-usage/index.html",
    "cstudy/index.html",
]

OLD_THEME = '<meta name="theme-color" content="#0f1f10" />'
NEW_THEME = '<meta name="theme-color" content="#f0eeeb" />'
OLD_SCHEME = '<meta name="color-scheme" content="dark" />'
NEW_SCHEME = '<meta name="color-scheme" content="light" />'
OLD_ICON = "%230f1f10'/%3E%3Crect x='14' y='14' width='36' height='36' fill='%23c6f19d'"
NEW_ICON = "%23f0eeeb'/%3E%3Crect x='14' y='14' width='36' height='36' fill='%23c8102e'"

for p in PAGES:
    f = pathlib.Path(p)
    if not f.exists():
        print("MISS", p)
        continue
    t = f.read_text(encoding="utf-8")
    before = t
    t = t.replace(OLD_THEME, NEW_THEME)
    t = t.replace(OLD_SCHEME, NEW_SCHEME)
    t = t.replace(OLD_ICON, NEW_ICON)
    if t != before:
        f.write_text(t, encoding="utf-8", newline="")
        print("OK  ", p)
    else:
        print("SKIP", p, "(no match)")
