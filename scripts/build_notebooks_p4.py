"""Part 4: Chapters 12, 13, 14 — Functions, File I/O, Advanced File Processing."""
from nbkit import md, code, exercise, title_block, recap, next_up


# ---------- Chapter 12 (Functions — book ch15) ------------------------------
NB_12 = title_block(15, "Functions in Python for VLSI Automation", "lesson-15", [
    "Why functions matter: DRY, readability, testability",
    "Defining functions with parameters and `return`",
    "Default values, positional vs keyword arguments",
    "`*args` and `**kwargs` for flexible APIs",
]) + [
    md("## Why functions?\n\n"
       "Functions let you name a block of work once and call it many times. Less duplication, "
       "fewer bugs, easier to test."),
    code("def greet():\n"
         "    print('Hello, VLSI engineer!')\n\n"
         "greet()"),

    md("## Parameters and `return`"),
    code("def check_slack(slack):\n"
         "    if slack < 0:\n"
         "        return 'Violation'\n"
         "    elif slack == 0:\n"
         "        return 'Critical'\n"
         "    else:\n"
         "        return 'Safe'\n\n"
         "print(check_slack(-0.05))\n"
         "print(check_slack(0.0))\n"
         "print(check_slack(0.12))"),

    md("## Default arguments"),
    code("def log_violation(net, severity='low'):\n"
         "    print(f'{net} has a {severity} violation')\n\n"
         "log_violation('clk')\n"
         "log_violation('rst', 'high')"),

    md("## Positional vs keyword arguments\n\n"
       "Positional arguments match by order. Keyword arguments match by name — clearer for "
       "calls with many parameters."),
    code("def report_violation(cell, severity):\n"
         "    print(f'{cell}: {severity}')\n\n"
         "report_violation('U1', 'high')\n"
         "report_violation(severity='medium', cell='U2')\n"
         "report_violation('U3', severity='low')"),

    md("## Keyword-only arguments with `*`\n\n"
       "Anything after `*` must be passed by name — useful to prevent ambiguous calls."),
    code("def config(*, mode, threshold):\n"
         "    print(mode, threshold)\n\n"
         "config(mode='setup', threshold=0.15)\n"
         "try:\n"
         "    config('setup', 0.15)\n"
         "except TypeError as e:\n"
         "    print('expected error:', e)"),

    md("## `*args` — variable positional arguments"),
    code("def report_cells(*cells):\n"
         "    for cell in cells:\n"
         "        print('Checking', cell)\n\n"
         "report_cells('U1', 'U2', 'U3')"),

    md("## `**kwargs` — variable keyword arguments"),
    code("def configure_tool(**settings):\n"
         "    for key, value in settings.items():\n"
         "        print(f'{key} set to {value}')\n\n"
         "configure_tool(clock='clk', threshold=0.2, mode='hold')"),

    md("## VLSI in practice — classify a list of slacks"),
    code("def classify(slack, setup_margin=0.0):\n"
         "    if slack < setup_margin:\n"
         "        return 'VIOLATION'\n"
         "    if slack < setup_margin + 0.05:\n"
         "        return 'MARGINAL'\n"
         "    return 'OK'\n\n"
         "paths = [('P1', -0.04), ('P2', 0.02), ('P3', 0.12), ('P4', 0.0)]\n"
         "for name, s in paths:\n"
         "    print(f'{name}: slack={s:+.3f}  -> {classify(s)}')"),
] + exercise(
    "## Exercise 1\n\n"
    "Write `area(w, h)` returning `w*h`. Call with positional and keyword args.",
    "def area(w, h):\n"
    "    return w * h\n"
    "print(area(2, 5))\n"
    "print(area(h=5, w=2))",
) + exercise(
    "## Exercise 2\n\n"
    "Write `summarize(*slacks)` that prints count, min, and max.",
    "def summarize(*slacks):\n"
    "    print('count:', len(slacks))\n"
    "    print('min:  ', min(slacks))\n"
    "    print('max:  ', max(slacks))\n"
    "summarize(0.1, -0.02, 0.05, -0.08)",
) + exercise(
    "## Exercise 3\n\n"
    "Write `set_options(**opts)` that stores options in a dict and prints sorted keys.",
    "def set_options(**opts):\n"
    "    for k in sorted(opts):\n"
    "        print(f'{k} = {opts[k]}')\n"
    "set_options(mode='setup', clk='clk_a', threshold=0.1)",
) + [
    recap([
        "`def name(params):` introduces a function; `return` sends a value back.",
        "Default values make parameters optional.",
        "Positional args match by order; keyword args match by name.",
        "`*args` bundles extra positional, `**kwargs` bundles extra keyword arguments.",
    ]),
    next_up(13, "File Handling in Python for VLSI Engineers"),
]


# ---------- Chapter 13 (File I/O — book ch16) -------------------------------
NB_13 = title_block(16, "File Handling in Python for VLSI Engineers", "lesson-16", [
    "Opening files safely with `with open(...)`",
    "Reading all, line-by-line, and into a list",
    "Writing, appending, file modes",
    "Using `pathlib` for clean path handling; reading `.gz` files",
]) + [
    md("## Open a file — always use `with`\n\n"
       "`with` guarantees the file closes, even on error."),
    code("from pathlib import Path\n"
         "Path('file.txt').write_text('hello VLSI engineer\\n')\n\n"
         "with open('file.txt', 'r') as f:\n"
         "    content = f.read()\n"
         "print(content)"),

    md("## File modes\n\n"
       "`'r'` read, `'w'` write (overwrite), `'a'` append, `'x'` create-new, "
       "`'b'` binary, `'t'` text (default)."),

    md("## Line-by-line — the memory-friendly pattern"),
    code("from pathlib import Path\n"
         "Path('sta.log').write_text(\n"
         "    'INFO starting run\\n'\n"
         "    'slack -0.03 setup VIOLATION\\n'\n"
         "    'slack 0.12 hold met\\n'\n"
         "    'INFO done\\n'\n"
         ")\n"
         "with open('sta.log') as f:\n"
         "    for line in f:\n"
         "        print(line.rstrip())"),

    md("## Read all lines into a list"),
    code("with open('sta.log') as f:\n"
         "    lines = f.readlines()\n"
         "print(len(lines), 'lines')\n"
         "print(lines[:2])"),

    md("## VLSI use case — filter a report"),
    code("with open('sta.log') as f:\n"
         "    for line in f:\n"
         "        if 'VIOLATION' in line:\n"
         "            print('Hold/Setup:', line.strip())"),

    md("## Writing files"),
    code("with open('summary.txt', 'w') as f:\n"
         "    f.write('Slack Violations: 3\\n')\n\n"
         "with open('summary.txt', 'a') as f:\n"
         "    f.write('New check complete.\\n')\n\n"
         "print(Path('summary.txt').read_text())"),

    md("## VLSI use case — write a list of nets"),
    code("nets = ['clk', 'reset', 'vdd']\n"
         "with open('critical_nets.txt', 'w') as f:\n"
         "    for net in nets:\n"
         "        f.write(net + '\\n')\n\n"
         "print(Path('critical_nets.txt').read_text())"),

    md("## Compressed files with `gzip`\n\n"
       "STA dumps are often `.gz`. Use `'rt'` for text mode."),
    code("import gzip\n"
         "from pathlib import Path\n"
         "with gzip.open('sta.rpt.gz', 'wt') as f:\n"
         "    f.write('slack -0.04 VIOLATION\\n')\n"
         "    f.write('slack 0.02 OK\\n')\n\n"
         "with gzip.open('sta.rpt.gz', 'rt') as f:\n"
         "    for line in f:\n"
         "        if 'VIOLATION' in line:\n"
         "            print(line.strip())"),

    md("## `pathlib` — the modern path API\n\n"
       "Object-oriented, chainable, cross-platform."),
    code("from pathlib import Path\n"
         "p = Path('critical_nets.txt')\n"
         "print('exists:', p.exists())\n"
         "print('is file:', p.is_file())\n"
         "print('size:', p.stat().st_size, 'bytes')\n"
         "print('name:', p.name, 'suffix:', p.suffix)\n\n"
         "logs = Path('logs_demo')\n"
         "logs.mkdir(exist_ok=True)\n"
         "(logs / 'a.rpt').write_text('one\\n')\n"
         "(logs / 'b.rpt').write_text('two\\n')\n"
         "for f in sorted(logs.glob('*.rpt')):\n"
         "    print('found:', f.name)"),

    md("## VLSI use case — check for required input files"),
    code("from pathlib import Path\n"
         "Path('netlist.v').write_text('// stub\\n')\n"
         "Path('cells.lib').write_text('// stub\\n')\n"
         "required = ['netlist.v', 'constraints.sdc', 'cells.lib']\n"
         "missing = [f for f in required if not Path(f).exists()]\n"
         "print('missing:', missing)"),
] + exercise(
    "## Exercise 1\n\n"
    "Write 3 net names (`clk`, `reset`, `data`) to `nets.out`, one per line, then read it back.",
    "from pathlib import Path\n"
    "with open('nets.out', 'w') as f:\n"
    "    for n in ['clk', 'reset', 'data']:\n"
    "        f.write(n + '\\n')\n"
    "print(Path('nets.out').read_text())",
) + exercise(
    "## Exercise 2\n\n"
    "Open `sta.log` and count lines containing `'slack'`.",
    "with open('sta.log') as f:\n"
    "    n = sum(1 for line in f if 'slack' in line)\n"
    "print('slack lines:', n)",
) + exercise(
    "## Exercise 3\n\n"
    "Create a directory `reports/`, write two `.rpt` files, and list them with `pathlib.glob`.",
    "from pathlib import Path\n"
    "d = Path('reports')\n"
    "d.mkdir(exist_ok=True)\n"
    "(d / 'setup.rpt').write_text('ok\\n')\n"
    "(d / 'hold.rpt').write_text('ok\\n')\n"
    "for f in sorted(d.glob('*.rpt')):\n"
    "    print(f.name)",
) + [
    recap([
        "Always open files with `with` — close is automatic.",
        "`'r'/'w'/'a'` are the everyday modes; add `'t'/'b'` for text/binary.",
        "Iterate line-by-line for large files; `readlines()` loads everything.",
        "`pathlib` is the clean, object-oriented way to work with paths.",
        "Use `gzip.open(..., 'rt')` for `.gz` text files.",
    ]),
    next_up(14, "Parsing Structured Data with Python"),
]


# ---------- Chapter 14 (Advanced File Processing — book ch17) ---------------
NB_14 = title_block(17, "Parsing Structured Data with Python", "lesson-17", [
    "Reading lines, stripping whitespace, splitting on delimiters",
    "Filtering and extracting values with string methods",
    "Parsing with `re.search` for patterns that aren't simple splits",
    "Bringing it together: pull every slack from an STA report and rank the worst",
]) + [
    md("## Setup — write a small STA report we can parse"),
    code("from pathlib import Path\n"
         "Path('sta.rpt').write_text(\n"
         "    'Startpoint: U1/clk\\n'\n"
         "    'Endpoint: U2/data\\n'\n"
         "    'Path Group: clk\\n'\n"
         "    'slack -0.045 setup violation\\n'\n"
         "    'slack 0.120 hold met\\n'\n"
         "    'slack -0.089 setup violation\\n'\n"
         ")"),

    md("## Read and split lines into tokens"),
    code("with open('sta.rpt') as f:\n"
         "    for line in f:\n"
         "        tokens = line.split()\n"
         "        print(tokens)"),

    md("## Extract slack values"),
    code("with open('sta.rpt') as f:\n"
         "    for line in f:\n"
         "        if line.startswith('slack'):\n"
         "            tokens = line.split()\n"
         "            slack = float(tokens[1])\n"
         "            print('Slack value:', slack)"),

    md("## Delimited files — CSV"),
    code("from pathlib import Path\n"
         "Path('nets.csv').write_text(\n"
         "    'clk,0.2,high_fanout\\n'\n"
         "    'reset,0.1,low_fanout\\n'\n"
         "    'data,0.25,high_fanout\\n'\n"
         ")\n\n"
         "with open('nets.csv') as f:\n"
         "    for line in f:\n"
         "        tokens = line.strip().split(',')\n"
         "        net_name = tokens[0]\n"
         "        fanout = float(tokens[1])\n"
         "        print(net_name, fanout)"),

    md("## Filter lines"),
    code("with open('sta.rpt') as f:\n"
         "    for line in f:\n"
         "        if line.startswith('slack') and 'violation' in line:\n"
         "            print('Violation:', line.strip())"),

    md("## Store, sort, and report the worst"),
    code("violations = []\n"
         "with open('sta.rpt') as f:\n"
         "    for line in f:\n"
         "        if line.startswith('slack'):\n"
         "            tokens = line.split()\n"
         "            try:\n"
         "                slack = float(tokens[1])\n"
         "                violations.append(slack)\n"
         "            except ValueError:\n"
         "                continue\n"
         "violations.sort()\n"
         "print('worst slack:', violations[0])"),

    md("## Regular expressions for patterns that aren't simple splits"),
    code("from pathlib import Path\n"
         "Path('sta_regex.rpt').write_text(\n"
         "    'slack: -0.045 (VIOLATION)\\n'\n"
         "    'slack: 0.110 (OK)\\n'\n"
         ")\n"
         "import re\n"
         "with open('sta_regex.rpt') as f:\n"
         "    for line in f:\n"
         "        match = re.search(r'slack:\\s*(-?\\d+\\.\\d+)', line)\n"
         "        if match:\n"
         "            print('Slack:', float(match.group(1)))"),

    md("## VLSI use case — extract net names"),
    code("from pathlib import Path\n"
         "Path('nets_report.txt').write_text('Net: clk\\nNet: reset\\nNet: data\\n')\n\n"
         "nets = []\n"
         "with open('nets_report.txt') as f:\n"
         "    for line in f:\n"
         "        if 'Net:' in line:\n"
         "            tokens = line.split()\n"
         "            idx = tokens.index('Net:')\n"
         "            nets.append(tokens[idx + 1])\n"
         "print(nets)"),

    md("## Pitfalls to watch for\n\n"
       "- Forgetting `.strip()` — trailing `\\n` ends up in tokens.\n"
       "- `IndexError` when a line has fewer tokens than expected — guard with `len(tokens)`.\n"
       "- Comparing strings to numbers — remember to cast with `float(...)`."),
    code("line = 'slack -0.03 violation\\n'\n"
         "tokens = line.split()\n"
         "if len(tokens) >= 2:\n"
         "    slack = float(tokens[1])\n"
         "    print('slack numeric:', slack, 'is negative?', slack < 0)"),
] + exercise(
    "## Exercise 1\n\n"
    "From `sta.rpt`, print only `violation` lines using `startswith('slack')` and `in`.",
    "with open('sta.rpt') as f:\n"
    "    for line in f:\n"
    "        if line.startswith('slack') and 'violation' in line:\n"
    "            print(line.strip())",
) + exercise(
    "## Exercise 2\n\n"
    "Parse `nets.csv` into a list of (name, fanout) tuples and print those with fanout ≥ 0.2.",
    "rows = []\n"
    "with open('nets.csv') as f:\n"
    "    for line in f:\n"
    "        name, fanout, _ = line.strip().split(',')\n"
    "        rows.append((name, float(fanout)))\n"
    "for name, fan in rows:\n"
    "    if fan >= 0.2:\n"
    "        print(name, fan)",
) + exercise(
    "## Exercise 3\n\n"
    "Using `re`, extract every float from `sta_regex.rpt` and print them sorted ascending.",
    "import re\n"
    "vals = []\n"
    "with open('sta_regex.rpt') as f:\n"
    "    for line in f:\n"
    "        m = re.search(r'(-?\\d+\\.\\d+)', line)\n"
    "        if m:\n"
    "            vals.append(float(m.group(1)))\n"
    "vals.sort()\n"
    "print(vals)",
) + [
    recap([
        "Read lines, strip whitespace, split on the right delimiter.",
        "Filter with `startswith`, `in`, or a combination.",
        "Cast tokens to `float`/`int` before comparing as numbers.",
        "Reach for `re.search` when the pattern isn't a clean split.",
    ]),
    next_up(None, None),
]
