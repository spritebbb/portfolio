# -*- coding: utf-8 -*-
"""Remove the repeated archive-photo band from every project page."""
import pathlib
import re
import sys

p = pathlib.Path("src/ProjectView.vue")
t = p.read_text(encoding="utf-8")

start_marker = '    <figure class="pv-band">'
end_marker = "    </figure>\n\n    <nav class=\"pv-next\">"

if start_marker not in t:
    print("band already removed")
    sys.exit(0)

i = t.index(start_marker)
j = t.index(end_marker, i)
removed = t[i:j]
t = t[:i] + t[j + len("    </figure>\n\n"):]
print("template block removed:", len(removed), "chars")

# imports
for line in [
    "import picFront from './assets/photos/the-first-card-written-west-of-cambridge.jpg'\n",
    "import picBox from './assets/photos/emilie-haspels-index-card-file-wp-20170131.jpg'\n",
    "import picDrawers from './assets/photos/manchester-central-library-march-2010-4467481691.jpg'\n",
]:
    if line in t:
        t = t.replace(line, "", 1)
        print("removed import:", line.split("from ")[0].strip())

# styles: .pv-band { ... } blocks and their media query
t = re.sub(r"(?ms)^\.pv-band \{[^}]*\}\n\n?", "", t)
t = re.sub(r"(?ms)^\.pv-band img \{[^}]*\}\n\n?", "", t)
t = re.sub(r"(?ms)^\.pv-band figcaption \{[^}]*\}\n\n?", "", t)
t = re.sub(r"(?ms)^@media \(max-width: 900px\) \{\n  \.pv-band[^}]*\{[^}]*\}\n\}\n\n?", "", t)

# any leftover media block holding only .pv-band
t = re.sub(r"(?ms)^@media \(max-width: 900px\) \{\n  \.pv-band[^\n]*\n(?:[^\n]*\n)*?\}\n", "", t)

p.write_text(t, encoding="utf-8", newline="")
print("pv-band refs left:", t.count("pv-band"))
print("picFront refs left:", t.count("picFront"))
