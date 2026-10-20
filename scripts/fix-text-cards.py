# -*- coding: utf-8 -*-
"""Fix duplicated project name inside text-only cards and enlarge the numbers."""
import pathlib
import sys

p = pathlib.Path("src/components/ProjectGrid.vue")
t = p.read_text(encoding="utf-8")

# 1) add modifier class on the shot container
old_open = '<div class="card-shot" data-ui>'
new_open = '<div class="card-shot" :class="{ \'card-shot--nums\': p.textOnly }" data-ui>'
if "card-shot--nums" in t:
    print("modifier already present")
else:
    if old_open not in t:
        sys.exit("card-shot open tag not found")
    t = t.replace(old_open, new_open, 1)
    print("modifier added")

# 2) drop the duplicated name in the textOnly branch
old_branch = """              <template v-else-if="p.textOnly">
                <span class="card-shot-name">{{ p.name }}</span>
                <span class="card-shot-nums">"""
new_branch = """              <template v-else-if="p.textOnly">
                <span class="card-shot-nums">"""
if old_branch not in t:
    if new_branch in t:
        print("textOnly branch already fixed")
    else:
        sys.exit("textOnly branch not found")
else:
    t = t.replace(old_branch, new_branch, 1)
    print("duplicate name removed")

# 3) taller numbers, centred block
old_css = """.card-shot-nums {
  display: flex;
  gap: 1.4rem;
  font-size: var(--step-small);
  color: var(--muted);
}

.card-shot-nums b {
  display: block;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.6rem;
  line-height: 1.1;
  color: var(--accent);
}"""
new_css = """.card-shot--nums {
  align-items: center;
  justify-content: center;
}

.card-shot-nums {
  display: flex;
  gap: clamp(1.1rem, 3vw, 2.6rem);
  width: 100%;
  justify-content: center;
  font-size: var(--step-small);
  line-height: 1.35;
  color: var(--muted);
  text-align: center;
}

.card-shot-nums > span {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.card-shot-nums b {
  display: block;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: clamp(1.9rem, 3.8vw, 2.9rem);
  line-height: 1;
  color: var(--accent);
}"""
if "card-shot--nums {" in t:
    print("css already patched")
else:
    if old_css not in t:
        sys.exit("nums css block not found")
    t = t.replace(old_css, new_css, 1)
    print("css patched")

p.write_text(t, encoding="utf-8", newline="")
print("written")
