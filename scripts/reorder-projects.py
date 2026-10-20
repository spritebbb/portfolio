# -*- coding: utf-8 -*-
"""Reorder projects: heaviest and most active first, retired ones last."""
import pathlib
import re
import sys

p = pathlib.Path("src/data/projects.ts")
t = p.read_text(encoding="utf-8")

start = t.index("export const projects: Project[] = [")
end = t.index("\n]", start)
head = t[:start]
body = t[start:end]
tail = t[end:]

# split into objects, each begins with "  {\n" and ends before the next "  {\n"
parts = re.split(r"(?m)^(?=  \{\n)", body)
prefix = parts[0]  # "export const projects: Project[] = [\n"
objects = parts[1:]
print("found", len(objects), "objects")

slugs = []
for o in objects:
    m = re.search(r"slug: '([^']+)'", o)
    slugs.append(m.group(1) if m else "?")
print("order before:", slugs)

target = ["tuzhan-assistant", "jd-pipeline", "cstudy", "dsh-skill-usage", "tuzhan-bot"]
if sorted(slugs) != sorted(target):
    sys.exit(f"slug set mismatch: {slugs}")

by_slug = {s: o for s, o in zip(slugs, objects)}
ordered = [by_slug[s] for s in target]
print("order after :", target)

new_body = prefix + "".join(ordered)
new_body = new_body.rstrip()
if not new_body.endswith(","):
    new_body = new_body + ","

t2 = head + new_body + tail
p.write_text(t2, encoding="utf-8", newline="")
print("written")
