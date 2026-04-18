#!/usr/bin/env python3
"""Build all 14 companion notebooks, faithful to python_for_vlsi book chapters."""
from __future__ import annotations
from pathlib import Path
from nbkit import md, code, exercise, title_block, recap, next_up, write_notebook

ROOT = Path(__file__).resolve().parent.parent


# ---------- Chapter 1 -------------------------------------------------------
NB_01 = title_block(1, "Why Python for VLSI?", "lesson-01", [
    "Why Python is replacing Tcl and Perl in modern EDA flows",
    "How the same file-reading task looks in Python, Tcl, and Perl",
    "Which Python libraries matter for VLSI engineers",
    "Why industry adoption and community matter for career growth",
]) + [
    md("## The same task, three languages\n\n"
       "The book opens with the classic example: open a report file and print every line. "
       "Watch how much noise Python strips away compared to Tcl and Perl."),
    md("**Tcl** (reference only):\n\n"
       "```tcl\n"
       'set file [open "report.txt" r]\n'
       "while {[gets $file line] != -1} {\n"
       "    puts $line\n"
       "}\n"
       "close $file\n"
       "```\n\n"
       "**Perl** (reference only):\n\n"
       "```perl\n"
       'open(my $fh, \'<\', "report.txt") or die "Cannot open file: $!";\n'
       "while (my $line = <$fh>) {\n"
       "    chomp $line;\n"
       '    print "$line\\n";\n'
       "}\n"
       "close($fh);\n"
       "```\n\n"
       "**Python** — and this one actually runs:"),
    code("from pathlib import Path\n\n"
         "# Create a tiny sample report so the cell is self-contained.\n"
         "Path('report.txt').write_text(\n"
         "    'Startpoint: U1/clk\\n'\n"
         "    'Endpoint: U2/data\\n'\n"
         "    'Slack: -0.045 setup\\n'\n"
         ")\n\n"
         "with open('report.txt') as file:\n"
         "    for line in file:\n"
         "        print(line.strip())"),
    md("Three lines of real work. No `set`, no `$`, no manual `close`. "
       "The `with` block closes the file for you when the loop ends."),

    md("## Why this matters beyond readability\n\n"
       "The book calls out four things Python gives you that the older languages don't:\n\n"
       "1. **A massive standard library** — `os`, `subprocess`, `re`, `pathlib`, `json` ship with every install.\n"
       "2. **A huge ecosystem of free packages** — `pandas`, `numpy`, `matplotlib`, `click`, `jinja2`, `streamlit`.\n"
       "3. **First-class support in modern EDA tools** — Synopsys, Cadence, and ANSYS expose Python APIs.\n"
       "4. **AI assistants produce better Python than Tcl or Perl.** In practice, you move faster."),
    code("# Automating a shell command is one line in Python.\n"
         "import subprocess, sys\n"
         "result = subprocess.run([sys.executable, '--version'], capture_output=True, text=True)\n"
         "print('stdout:', result.stdout.strip() or result.stderr.strip())\n"
         "print('return code:', result.returncode)"),
    md("The book uses `os.system(\"calibre -drc my_design.gds\")` as the illustration — "
       "`subprocess.run` is the modern, safer replacement and captures output for you."),

    md("## Why learning Python now pays off\n\n"
       "The *Future* section of the chapter boils down to three points:\n\n"
       "- **Industry adoption** — vendors are migrating flows from Tcl to Python.\n"
       "- **Career growth** — roles that combine design knowledge with Python automation are in demand.\n"
       "- **Open-source and community** — docs, tutorials, and help are one search away."),
] + exercise(
    "## Exercise 1\n\n"
    "Create `lib_files.txt` with three lines — `design.v`, `design.lib`, `design.sdc` — "
    "then read it back and print only lines ending in `.lib`.",
    "from pathlib import Path\n"
    "Path('lib_files.txt').write_text('design.v\\ndesign.lib\\ndesign.sdc\\n')\n"
    "with open('lib_files.txt') as f:\n"
    "    for line in f:\n"
    "        line = line.strip()\n"
    "        if line.endswith('.lib'):\n"
    "            print(line)",
) + exercise(
    "## Exercise 2\n\n"
    "Use `subprocess.run` to call `uname -a` and print just the first word of the output.",
    "import subprocess, shlex\n"
    "result = subprocess.run(shlex.split('uname -a'), capture_output=True, text=True)\n"
    "print(result.stdout.split()[0] if result.stdout else '(no output)')",
) + [
    recap([
        "Python reads a file in three lines; Tcl and Perl need five or more.",
        "`with open(...) as f:` closes the file for you — no manual `close()`.",
        "The standard library already covers most automation you need on day one.",
        "EDA vendors are shipping Python APIs; that trend is not reversing.",
    ]),
    next_up(2, "Installing Python for VLSI Engineers"),
]


# ---------- Chapter 2 -------------------------------------------------------
NB_02 = title_block(2, "Installing Python for VLSI Engineers", "lesson-02", [
    "How to check whether Python and pip are already installed",
    "Why Python 3.11+ is the recommendation for VLSI work",
    "Popular editors: Jupyter, VS Code, PyCharm — and when to pick which",
    "Installing a package with `pip` safely on a shared workstation",
]) + [
    md("## Is Python already here?\n\n"
       "On most Linux machines — including every VLSI workstation the book targets — Python 3 is pre-installed."),
    code("import sys\n"
         "print('Executable:', sys.executable)\n"
         "print('Version:   ', sys.version.split()[0])"),
    md("The book recommends **Python 3.11.4 or newer** for VLSI work. "
       "This notebook requires **3.9+** as a minimum. If you see anything older, ask IT for "
       "the latest Python package path — don't upgrade the system install yourself."),

    md("## `pip` — Python's package manager"),
    code("import subprocess, sys\n"
         "print(subprocess.run([sys.executable, '-m', 'pip', '--version'],\n"
         "                     capture_output=True, text=True).stdout.strip())"),
    md("If this prints a version, you're ready. If it says `No module named pip`, run "
       "`python -m ensurepip --upgrade` once."),

    md("## Picking an editor\n\n"
       "| Editor | Best for | Install |\n"
       "|---|---|---|\n"
       "| **Jupyter Notebook** | Exploring, plotting (you're in one now) | `pip install notebook` |\n"
       "| **VS Code** | Day-to-day scripting, remote editing | Download from code.visualstudio.com |\n"
       "| **PyCharm** | Larger projects, refactoring | Community edition from jetbrains.com |"),

    md("## Installing a package — the safe pattern"),
    code("# Shape of a real install (commented so this cell doesn't actually install anything):\n"
         "# subprocess.run([sys.executable, '-m', 'pip', 'install', '--user', 'requests'])\n"
         "print('Safe pattern: python -m pip install --user <package>')"),
    md("Rules from the book:\n\n"
       "- **Never** `sudo pip install` on a shared VLSI server.\n"
       "- Prefer `--user` or a virtual environment.\n"
       "- Record exact versions with `pip freeze > requirements.txt` for production scripts."),
] + exercise(
    "## Exercise 1\n\n"
    "Print your Python's `sys.prefix` (install root) and the first entry of `sys.path`.",
    "import sys\n"
    "print('prefix:', sys.prefix)\n"
    "print('first sys.path:', sys.path[0])",
) + exercise(
    "## Exercise 2\n\n"
    "Import three stdlib modules you expect to use for VLSI automation. Print something to prove each works.",
    "import os, re, pathlib\n"
    "print('os.name:', os.name)\n"
    "print('re works:', bool(re.match(r'\\d+', '42')))\n"
    "print('cwd:', pathlib.Path.cwd())",
) + [
    recap([
        "Python 3 is almost always pre-installed on modern Linux — check first.",
        "Prefer `pip install --user` on shared systems.",
        "Jupyter, VS Code, and PyCharm cover the common editor choices.",
        "Record package versions for reproducible flows.",
    ]),
    next_up(3, "Understanding the Basics Before Writing Python Code"),
]


# ---------- Chapter 3 -------------------------------------------------------
NB_03 = title_block(3, "Understanding the Basics Before Writing Python Code", "lesson-03", [
    "What variables, data types, and comments actually are",
    "What a script, function, module, and package each mean",
    "How each concept compares with Tcl and Perl",
    "Why Python's syntax is easier to read than `$var` or `set var value`",
]) + [
    md("## What is a variable?\n\n"
       "A variable is a labeled box in memory. Python uses `=` — no `set` or `$`."),
    code("voltage = 1.2\n"
         "cell_name = 'INV_X1'\n"
         "num_pins = 24\n"
         "is_clock = True\n"
         "print(voltage, cell_name, num_pins, is_clock)"),

    md("## Data types\n\n"
       "Python figures out the type automatically. The four everyday ones:\n\n"
       "- `int` — whole numbers: `24`, `-5`\n"
       "- `float` — decimals: `1.2`, `-0.045`\n"
       "- `str` — text: `\"U1\"`\n"
       "- `bool` — `True` or `False`"),
    code("for v in (voltage, cell_name, num_pins, is_clock):\n"
         "    print(v, '→', type(v).__name__)"),

    md("## Comments — notes for humans\n\n"
       "Everything after `#` is ignored. Explain *why*, not *what*."),
    code("# Calculate power as voltage * current\n"
         "current = 0.5\n"
         "power = voltage * current\n"
         "print(f'power = {power} W')"),

    md("## What is a script?\n\n"
       "A script is just a file ending in `.py` that runs top to bottom. The cells in this notebook "
       "are conceptually the same — they execute in order. Chapters 4–18 in the book can all be "
       "practised in a single `.py` file."),

    md("## What is a function?\n\n"
       "A reusable block of code. `def` names it; `return` hands back the result."),
    code("def calculate_power(v, i):\n"
         "    return v * i\n\n"
         "print('Power:', calculate_power(1.1, 0.3))"),

    md("## What is a module?\n\n"
       "A file full of functions and variables. `import` brings it in. Python ships with many."),
    code("import math\n"
         "print(math.sqrt(16))\n"
         "print(math.pi)"),

    md("## What is a package?\n\n"
       "A group of related modules installed as a unit (`pip install ...`). `import` brings it in, same as a module."),
    code("import json\n"
         "cell_info = {'name': 'INV_X1', 'area': 1.2, 'power': 0.05}\n"
         "print(json.dumps(cell_info, indent=2))"),
] + exercise(
    "## Exercise 1\n\n"
    "Create four variables — one of each core type (`int`, `float`, `str`, `bool`) — with VLSI-flavoured names. "
    "Print each value and its type name.",
    "layer = 3\n"
    "pitch_um = 0.14\n"
    "net_name = 'clk'\n"
    "is_gated = False\n"
    "for v in (layer, pitch_um, net_name, is_gated):\n"
    "    print(v, type(v).__name__)",
) + exercise(
    "## Exercise 2\n\n"
    "Write `area(width, length)` returning `width * length`; test with two different calls.",
    "def area(width, length):\n"
    "    return width * length\n\n"
    "print(area(2, 5))\n"
    "print(area(0.14, 10))",
) + [
    recap([
        "A variable names a spot in memory; Python assigns with `=`.",
        "The four everyday types are `int`, `float`, `str`, `bool`.",
        "Comments start with `#`; use them to explain *why*.",
        "A script is a `.py` file; a function is a reusable block; `import` pulls in modules and packages.",
    ]),
    next_up(4, "Writing Your First Python Script"),
]
