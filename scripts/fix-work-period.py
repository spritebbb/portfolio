# -*- coding: utf-8 -*-
"""Move the trailing full stop inside the last project link so it can never wrap alone."""
import pathlib
import re
import sys

p = pathlib.Path("src/components/WorkIndex.vue")
t = p.read_text(encoding="utf-8")

if 'v-else class="work-end"' in t:
    print("already patched")
    sys.exit(0)

# 1) remove the standalone full stop after </template
before = t
t = re.sub(r'\n\s*><span class="work-end">。\s*</span>', "", t, count=1)
if t == before:
    sys.exit("standalone work-end span not found")

# 2) attach a v-else full stop to the separator span
old = '''              class="work-sep"
              >，</span
            ></a'''
new = '''              class="work-sep"
              >，</span
              ><span v-else class="work-end">。</span
            ></a'''
if old not in t:
    sys.exit("separator span not found")
t = t.replace(old, new, 1)

p.write_text(t, encoding="utf-8", newline="")
print("patched")
print("--- resulting block ---")
block = t[t.index('<nav class="work-para"'):t.index('</nav>')]
print(block)
