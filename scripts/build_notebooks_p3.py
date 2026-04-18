"""Part 3: Chapters 7, 8, 9, 10, 11 — Strings, Lists, Dicts, Tuples, Sets."""
from nbkit import md, code, exercise, title_block, recap, next_up


# ---------- Chapter 7 (Strings — book ch8) ----------------------------------
NB_07 = title_block(8, "Working with Strings for VLSI Use Cases", "lesson-08", [
    "Declaring and concatenating strings the Python way",
    "`f-strings` for clean, formatted output",
    "The must-know operations: `len`, slicing, `split`, `replace`, `join`, `startswith`",
    "Using `re` to pull values out of report lines",
]) + [
    md("## Declaring strings\n\nSingle or double quotes both make a `str`."),
    code("cell_name = 'U1'\n"
         "file_path = '/designs/top/design.lib'\n"
         "print(cell_name, file_path)"),

    md("## Concatenation"),
    code("base_dir = '/home/user'\n"
         "full_path = base_dir + '/log.txt'\n"
         "print(full_path)\n"
         "print(f'{base_dir}/log.txt')"),

    md("## `f-strings` — the modern way to format output"),
    code("slack = -0.023\n"
         "cell = 'U1'\n"
         "instance = 'X12'\n"
         "width, length = 2, 5\n"
         "print(f'Timing Slack = {slack:.3f} ns')\n"
         "print(f'Instance: {cell}/{instance}')\n"
         "print(f'Area = {width * length} um^2')"),

    md("## Useful operations\n\nLength, slicing, splitting, replacing, joining."),
    code("cell = 'U1_A1'\n"
         "print('len:', len(cell))\n"
         "print('first two:', cell[:2])\n"
         "path = 'top/U1/A1'\n"
         "parts = path.split('/')\n"
         "print('parts:', parts)\n"
         "lib_file = 'design.v'\n"
         "print('renamed:', lib_file.replace('.v', '.lib'))\n"
         "print('joined:', '/'.join(parts))"),

    md("## Comparing and checking"),
    code("cell_name = 'U1_A1'\n"
         "if cell_name.startswith('U'):\n"
         "    print('top-level cell')\n"
         "log_line = 'ERROR: cell missing'\n"
         "if 'ERROR' in log_line:\n"
         "    print('found issue')"),

    md("## Regular expressions for report parsing"),
    code("import re\n"
         "line = 'Slack: -0.034 ns'\n"
         "match = re.search(r'Slack:\\s*(-?\\d+\\.\\d+)\\s*ns', line)\n"
         "if match:\n"
         "    slack = float(match.group(1))\n"
         "    print('slack =', slack)"),

    md("## VLSI in practice — summarise a short STA report"),
    code("from pathlib import Path\n"
         "Path('sta.rpt').write_text(\n"
         "    'Startpoint: U1/clk\\n'\n"
         "    'Endpoint: U2/data\\n'\n"
         "    'slack -0.045 setup violation\\n'\n"
         "    'slack 0.120 hold met\\n'\n"
         "    'slack -0.089 setup violation\\n'\n"
         ")\n"
         "violations = []\n"
         "with open('sta.rpt') as f:\n"
         "    for line in f:\n"
         "        if line.startswith('slack'):\n"
         "            tokens = line.split()\n"
         "            slack = float(tokens[1])\n"
         "            if slack < 0:\n"
         "                violations.append(slack)\n"
         "violations.sort()\n"
         "print('worst slack:', violations[0] if violations else 'none')\n"
         "print(f'{len(violations)} violation(s)')"),
] + exercise(
    "## Exercise 1\n\n"
    "Given `hier = 'top/U1/X12/inst_a'`, split by `/` and print just the last component.",
    "hier = 'top/U1/X12/inst_a'\n"
    "print(hier.split('/')[-1])",
) + exercise(
    "## Exercise 2\n\n"
    "Format `v = 0.9`, `i = 0.35` into `'P = 0.315 W'` with 3-decimal precision.",
    "v, i = 0.9, 0.35\n"
    "print(f'P = {v * i:.3f} W')",
) + exercise(
    "## Exercise 3\n\n"
    "From `lines = ['Slack: -0.01 ns', 'Note: OK', 'Slack: 0.05 ns']`, use `re` to extract each slack.",
    "import re\n"
    "lines = ['Slack: -0.01 ns', 'Note: OK', 'Slack: 0.05 ns']\n"
    "for ln in lines:\n"
    "    m = re.search(r'Slack:\\s*(-?\\d+\\.\\d+)', ln)\n"
    "    if m:\n"
    "        print(float(m.group(1)))",
) + [
    recap([
        "Strings are immutable sequences; operations return new strings.",
        "Prefer `f-strings` — the clearest formatting in modern Python.",
        "`split`, `join`, `replace`, `startswith` cover 80% of report parsing.",
        "Reach for `re.search` when the pattern isn't a simple delimiter.",
    ]),
    next_up(8, "Working with Lists for VLSI Data Handling"),
]


# ---------- Chapter 8 (Lists — book ch10) -----------------------------------
NB_08 = title_block(10, "Working with Lists for VLSI Data Handling", "lesson-10", [
    "What lists are, and how they differ from Tcl arrays and Perl `@arrays`",
    "Everyday operations: access, modify, append, extend, remove, pop, insert",
    "Looping, sorting, membership checks, comprehensions",
    "Gotchas: out-of-range indices, numeric-looking sort order, modifying while iterating",
]) + [
    md("## Creating lists"),
    code("cells = ['INV_X1', 'NAND2_X2', 'DFF_X1']\n"
         "slack_values = [0.1, -0.05, 0.0]\n"
         "print(cells, slack_values)"),

    md("## Access and modify"),
    code("cells = ['U1', 'U2', 'U3']\n"
         "print(cells[0], cells[-1])\n"
         "cells[1] = 'U2_MOD'\n"
         "print(cells)"),

    md("## Add and remove"),
    code("cells = ['U1', 'U2', 'U3']\n"
         "cells.append('U4')\n"
         "cells.extend(['U5', 'U6'])\n"
         "if 'U2' in cells:\n"
         "    cells.remove('U2')\n"
         "last = cells.pop()\n"
         "cells.insert(1, 'U_NEW')\n"
         "print(cells, 'popped:', last)"),

    md("## Looping, length, membership"),
    code("cells = ['U1', 'U2', 'U3']\n"
         "for c in cells:\n"
         "    print('checking', c)\n"
         "print('count:', len(cells))\n"
         "print('U1 in cells?', 'U1' in cells)"),

    md("## Sorting — beware of lexicographic order\n\n"
       "`U10` sorts before `U2` by default. Pass a `key` to sort by the numeric part."),
    code("cells = ['U10', 'U2', 'U1']\n"
         "cells.sort()\n"
         "print('lexical:', cells)\n"
         "cells.sort(key=lambda x: int(x[1:]))\n"
         "print('numeric:', cells)\n"
         "slacks = [0.2, -0.1, 0.05]\n"
         "slacks.sort()\n"
         "print('slacks:', slacks)"),

    md("## List comprehensions"),
    code("cells = ['INV_X1', 'DFF_X1', 'INV_X2', 'NAND2_X1']\n"
         "inv_cells = [c for c in cells if c.startswith('INV')]\n"
         "print(inv_cells)\n"
         "upper = [c.lower() for c in cells]\n"
         "print(upper)"),

    md("## VLSI in practice — bucket cells by family"),
    code("netlist = ['INV_X1', 'NAND2_X1', 'DFF_X2', 'INV_X2', 'NOR2_X1', 'DFF_X1']\n"
         "families = {}\n"
         "for cell in netlist:\n"
         "    prefix = cell.split('_')[0]\n"
         "    families.setdefault(prefix, []).append(cell)\n"
         "for family, members in families.items():\n"
         "    print(f'{family}: {members}')"),
] + exercise(
    "## Exercise 1\n\n"
    "Start with `['U1', 'U2', 'U3']`. Append `'U4'`, insert `'U0'` at front, remove `'U2'`, print result.",
    "cells = ['U1', 'U2', 'U3']\n"
    "cells.append('U4')\n"
    "cells.insert(0, 'U0')\n"
    "cells.remove('U2')\n"
    "print(cells)",
) + exercise(
    "## Exercise 2\n\n"
    "From `[0.12, -0.03, 0.05, -0.21, 0.00]`, keep only negative slacks in a new list.",
    "slacks = [0.12, -0.03, 0.05, -0.21, 0.00]\n"
    "print([s for s in slacks if s < 0])",
) + exercise(
    "## Exercise 3\n\n"
    "Sort `['U100', 'U7', 'U12', 'U1']` numerically by the integer after `U`.",
    "cells = ['U100', 'U7', 'U12', 'U1']\n"
    "cells.sort(key=lambda c: int(c[1:]))\n"
    "print(cells)",
) + [
    recap([
        "Lists are ordered, mutable, 0-indexed.",
        "`append` adds one; `extend` adds many.",
        "Default sort is lexicographic — pass `key=` for numeric-aware sorts.",
        "List comprehensions build new lists in one readable expression.",
    ]),
    next_up(9, "Using Dictionaries for Structured Data in VLSI"),
]


# ---------- Chapter 9 (Dicts — book ch11) -----------------------------------
NB_09 = title_block(11, "Using Dictionaries for Structured Data in VLSI", "lesson-11", [
    "Key-value pairs for mapping cell → area, net → pins, layer → width",
    "Safe access with `.get()` to avoid `KeyError`",
    "Adding, modifying, deleting entries",
    "Nested dictionaries for richer data like cell metadata",
]) + [
    md("## Creating a dictionary"),
    code("cell_area = {\n"
         "    'INV_X1': 1.2,\n"
         "    'NAND2_X1': 2.3,\n"
         "    'DFF_X1': 5.1,\n"
         "}\n"
         "print(cell_area)"),

    md("## Access, safely\n\n"
       "`d[key]` raises `KeyError` if missing. `d.get(key, default)` returns the default."),
    code("print(cell_area['INV_X1'])\n"
         "print(cell_area.get('XYZ', 0.0))"),

    md("## Add, modify, delete"),
    code("cell_area['BUF_X1'] = 0.9\n"
         "cell_area['INV_X1'] = 1.1\n"
         "del cell_area['NAND2_X1']\n"
         "removed = cell_area.pop('DFF_X1')\n"
         "print(cell_area, 'removed:', removed)"),

    md("## `.keys()`, `.values()`, `.items()`"),
    code("cell_power = {'INV_X1': 0.05, 'NAND2_X1': 0.08, 'BUF_X1': 0.04}\n"
         "print(list(cell_power.keys()))\n"
         "print(list(cell_power.values()))\n"
         "for cell, power in cell_power.items():\n"
         "    print(f'{cell} uses {power} mW')"),

    md("## `.update()` for merging"),
    code("cell_power.update({'DFF_X1': 0.12, 'BUF_X1': 0.045})\n"
         "print(cell_power)"),

    md("## Nested dictionaries"),
    code("cell_info = {\n"
         "    'INV_X1': {'area': 1.2, 'power': 0.05, 'pins': 2},\n"
         "    'DFF_X1': {'area': 5.1, 'power': 0.12, 'pins': 4},\n"
         "}\n"
         "print(cell_info['INV_X1']['area'])\n"
         "for cell, info in cell_info.items():\n"
         "    print(f\"{cell}: area={info['area']} pins={info['pins']}\")"),

    md("## VLSI in practice — count violations by type"),
    code("violations = ['setup', 'hold', 'setup', 'drc', 'setup', 'hold', 'antenna']\n"
         "counts = {}\n"
         "for v in violations:\n"
         "    counts[v] = counts.get(v, 0) + 1\n"
         "for name, n in sorted(counts.items()):\n"
         "    print(f'{name:8s} {n}')"),
] + exercise(
    "## Exercise 1\n\n"
    "Map `'M1', 'M2', 'M3'` to `0.14, 0.14, 0.20`. Print the width of M2 using `.get()`.",
    "widths = {'M1': 0.14, 'M2': 0.14, 'M3': 0.20}\n"
    "print(widths.get('M2'))",
) + exercise(
    "## Exercise 2\n\n"
    "Given `[('INV_X1', 0.05), ('DFF_X1', 0.12), ('INV_X1', 0.07)]`, build a dict mapping each cell to its max power.",
    "pairs = [('INV_X1', 0.05), ('DFF_X1', 0.12), ('INV_X1', 0.07)]\n"
    "maxp = {}\n"
    "for cell, p in pairs:\n"
    "    maxp[cell] = max(maxp.get(cell, 0.0), p)\n"
    "print(maxp)",
) + exercise(
    "## Exercise 3\n\n"
    "Using the `cell_info` dict above, print every cell whose area is greater than 2.",
    "cell_info = {\n"
    "    'INV_X1': {'area': 1.2, 'power': 0.05, 'pins': 2},\n"
    "    'DFF_X1': {'area': 5.1, 'power': 0.12, 'pins': 4},\n"
    "}\n"
    "for cell, info in cell_info.items():\n"
    "    if info['area'] > 2:\n"
    "        print(cell)",
) + [
    recap([
        "Dictionaries map unique keys to values; access is `O(1)`.",
        "`.get(key, default)` avoids `KeyError`.",
        "`.keys()`, `.values()`, `.items()` give iterable views.",
        "Nest dicts for structured records; merge with `.update()`.",
    ]),
    next_up(10, "Using Tuples for Fixed Data in VLSI"),
]


# ---------- Chapter 10 (Tuples — book ch12) ---------------------------------
NB_10 = title_block(12, "Using Tuples for Fixed Data in VLSI", "lesson-12", [
    "What a tuple is, and why immutability is useful",
    "Coordinates, bounding boxes, timing arcs — natural tuple use cases",
    "Unpacking, tuples as dict keys, lists of tuples",
    "The single-element tuple gotcha — remember the trailing comma",
]) + [
    md("## Creating tuples"),
    code("pin_location = (120, 340)\n"
         "cell_data = ('INV_X1', 1.2, 0.05)\n"
         "bbox = (10, 20, 110, 150)\n"
         "print(pin_location, cell_data, bbox)"),

    md("## Single-element tuple — trailing comma matters"),
    code("x = (42)\n"
         "y = (42,)\n"
         "print(type(x).__name__, type(y).__name__)"),

    md("## Access and unpack"),
    code("coord = (100, 200)\n"
         "print(coord[0], coord[1])\n"
         "name, area, power = ('NAND2_X1', 2.3, 0.08)\n"
         "print(name, area, power)"),

    md("## Immutability is a feature\n\n"
       "Tuples can be dictionary keys; lists cannot. Great for composite keys like timing arcs."),
    code("timing_arc = {\n"
         "    ('A', 'Z'): 0.12,\n"
         "    ('B', 'Z'): 0.15,\n"
         "    ('CLK', 'Q'): 0.20,\n"
         "}\n"
         "print(timing_arc[('CLK', 'Q')])\n"
         "for (src, dst), delay in timing_arc.items():\n"
         "    print(f'{src} → {dst}: {delay} ns')"),

    md("## Lists of tuples — records"),
    code("pins = [(100, 200), (150, 250), (180, 300)]\n"
         "for x, y in pins:\n"
         "    print(f'({x}, {y})')"),

    md("## What you can't do\n\nAttempting to change a tuple raises `TypeError` — which prevents silent bugs."),
    code("coord = (100, 200)\n"
         "try:\n"
         "    coord[0] = 120\n"
         "except TypeError as e:\n"
         "    print('expected error:', e)"),

    md("## VLSI in practice — compute total bbox area"),
    code("bboxes = [\n"
         "    (10, 20, 110, 150),\n"
         "    (200, 100, 260, 220),\n"
         "    (300, 300, 400, 400),\n"
         "]\n"
         "total = 0\n"
         "for x1, y1, x2, y2 in bboxes:\n"
         "    area = (x2 - x1) * (y2 - y1)\n"
         "    total += area\n"
         "    print(f'bbox ({x1},{y1})-({x2},{y2}) area={area}')\n"
         "print('total area:', total)"),
] + exercise(
    "## Exercise 1\n\n"
    "Create a single-element tuple containing `3.14` and confirm its type.",
    "t = (3.14,)\n"
    "print(t, type(t).__name__)",
) + exercise(
    "## Exercise 2\n\n"
    "Given `points = [(0, 0), (3, 4), (6, 8)]`, compute Euclidean distance from origin for each.",
    "points = [(0, 0), (3, 4), (6, 8)]\n"
    "for x, y in points:\n"
    "    d = (x*x + y*y) ** 0.5\n"
    "    print(f'({x},{y}) → {d:.2f}')",
) + exercise(
    "## Exercise 3\n\n"
    "Store arcs `('A','Z'): 0.10` and `('B','Z'): 0.14` in a dict and print the worst-case into Z.",
    "arcs = {('A','Z'): 0.10, ('B','Z'): 0.14}\n"
    "print('worst into Z:', max(arcs.values()))",
) + [
    recap([
        "Tuples are ordered, immutable — great for fixed records.",
        "A single-element tuple needs a trailing comma: `(42,)`.",
        "Tuples can be dictionary keys; lists cannot.",
        "Unpacking gives readable names: `x, y = coord`.",
    ]),
    next_up(11, "Using Sets for Unique Data in VLSI"),
]


# ---------- Chapter 11 (Sets — book ch13) -----------------------------------
NB_11 = title_block(13, "Using Sets for Unique Data in VLSI", "lesson-13", [
    "What a set is, and when uniqueness matters in VLSI",
    "Creating, adding, removing — and the `{}` vs `set()` gotcha",
    "Union, intersection, difference — mapped to design questions",
    "Why membership tests on large sets are much faster than on lists",
]) + [
    md("## Creating sets\n\nUse `{ ... }` with at least one element, or `set(...)`. An empty `{}` is a dict."),
    code("layers = {'M1', 'M2', 'M3'}\n"
         "print(layers)\n"
         "dup_list = ['M1', 'M2', 'M1', 'M2']\n"
         "print(set(dup_list))\n"
         "empty = set()\n"
         "also_empty = {}\n"
         "print(type(empty).__name__, type(also_empty).__name__)"),

    md("## Add, remove, membership"),
    code("layers = {'M1', 'M2', 'M3'}\n"
         "layers.add('M4')\n"
         "layers.discard('M5')\n"
         "layers.remove('M2')\n"
         "print('M1' in layers)\n"
         "print(layers)"),

    md("## Union, intersection, difference"),
    code("layout_layers = {'M1', 'M2', 'M3'}\n"
         "allowed_layers = {'M1', 'M2', 'M4'}\n"
         "print('union:       ', layout_layers | allowed_layers)\n"
         "print('intersection:', layout_layers & allowed_layers)\n"
         "print('diff (used-allowed):', layout_layers - allowed_layers)\n"
         "print('diff (allowed-used):', allowed_layers - layout_layers)"),

    md("## VLSI in practice — find unused and illegal layers"),
    code("spec_layers = {'M1', 'M2', 'M3', 'M4', 'VIA12', 'VIA23'}\n"
         "seen_layers = {'M1', 'M2', 'VIA12', 'POLY'}\n"
         "unused = spec_layers - seen_layers\n"
         "illegal = seen_layers - spec_layers\n"
         "print('unused in design:', unused)\n"
         "print('illegal layers:  ', illegal)"),

    md("## Why a set is fast\n\n"
       "Membership in a `set` is `O(1)` average; in a `list` it's `O(n)`. The difference is orders of magnitude."),
    code("import time\n"
         "big_list = list(range(100_000))\n"
         "big_set = set(big_list)\n"
         "target = 99_999\n"
         "t0 = time.perf_counter(); _ = target in big_list; t_list = time.perf_counter() - t0\n"
         "t0 = time.perf_counter(); _ = target in big_set;  t_set  = time.perf_counter() - t0\n"
         "print(f'list lookup: {t_list*1e6:.1f} us')\n"
         "print(f'set  lookup: {t_set*1e6:.3f} us')"),
] + exercise(
    "## Exercise 1\n\n"
    "Turn `['clk', 'reset', 'clk', 'data', 'reset']` into a set of unique net names.",
    "nets = ['clk', 'reset', 'clk', 'data', 'reset']\n"
    "print(set(nets))",
) + exercise(
    "## Exercise 2\n\n"
    "`used = {'INV_X1', 'DFF_X1'}` and `allowed = {'INV_X1', 'NAND2_X1'}`. Print cells used but not allowed.",
    "used = {'INV_X1', 'DFF_X1'}\n"
    "allowed = {'INV_X1', 'NAND2_X1'}\n"
    "print(used - allowed)",
) + exercise(
    "## Exercise 3\n\n"
    "Count unique violation types in `['setup', 'hold', 'setup', 'drc']`.",
    "v = ['setup', 'hold', 'setup', 'drc']\n"
    "print(len(set(v)))",
) + [
    recap([
        "A set is an unordered, duplicate-free collection.",
        "Empty set is `set()`; `{}` is an empty dict.",
        "Union `|`, intersection `&`, difference `-` map directly to design questions.",
        "Use sets for fast membership tests on large collections.",
    ]),
    next_up(12, "Functions in Python for VLSI Automation"),
]
