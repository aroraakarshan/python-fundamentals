"""Part 2: Chapters 4, 5, 6 — Control flow, First script, Integers."""
from nbkit import md, code, exercise, title_block, recap, next_up


# ---------- Chapter 4 (Control flow — book ch14) ----------------------------
NB_04 = title_block(14, "Control Flow in Python for VLSI Automation", "lesson-09", [
    "`if` / `elif` / `else` for decisions based on design metrics",
    "Comparison and logical operators, with common pitfalls",
    "`for` loops over lists and `range()` for count-based iteration",
    "`while`, `break`, `continue`, `pass`, and the `match` statement",
]) + [
    md("## Conditionals: `if`, `elif`, `else`\n\n"
       "The book's canonical example is classifying a timing slack."),
    code("slack = -0.05\n"
         "if slack < 0:\n"
         "    print('Timing violation')\n"
         "elif slack == 0:\n"
         "    print('Critical path')\n"
         "else:\n"
         "    print('Path is safe')"),
    md("Common beginner mistakes the book calls out:\n\n"
       "- Forgetting the `:` at the end of `if`.\n"
       "- Mixing tabs and spaces — Python uses indentation to group code.\n"
       "- Writing `=` (assignment) when you meant `==` (comparison)."),

    md("## Comparison operators\n\n"
       "`==`, `!=`, `>`, `<`, `>=`, `<=` — each returns a `bool`."),
    code("violation_count = 5\n"
         "print('Under limit:', violation_count <= 10)\n"
         "wire_length = 120\n"
         "print('Short wire:', wire_length < 100)"),

    md("## Logical operators: `and`, `or`, `not`\n\n"
       "`and` has higher precedence than `or`. Use parentheses when you aren't sure."),
    code("a, b, c = 1, 3, 10\n"
         "print((a > 0 and b < 5) or c == 10)\n"
         "print(not (a > 0))"),

    md("## `for` loops"),
    code("cells = ['U1', 'U2', 'U3']\n"
         "for cell in cells:\n"
         "    print('Checking cell:', cell)"),
    md("**Warning from the book:** don't modify a list while iterating over it. "
       "Iterate over a copy (`cells[:]`) or build a new list."),

    md("## `range()` — stop value is exclusive"),
    code("for i in range(3):\n"
         "    print(i)\n"
         "print('---')\n"
         "for i in range(2, 8, 2):\n"
         "    print('layer M', i)"),

    md("## `while` loops\n\n"
       "Run while the condition stays true. Make sure the condition will eventually become false!"),
    code("count = 0\n"
         "while count < 5:\n"
         "    print(count)\n"
         "    count += 1"),

    md("## `break`, `continue`, `pass`"),
    code("nets = ['clk', 'vdd', 'data', 'VDD', 'reset']\n"
         "for net in nets:\n"
         "    if net.lower() == 'vdd':\n"
         "        print('stop at power net'); break\n"
         "    if net.startswith('clk'):\n"
         "        continue\n"
         "    print('processing', net)"),

    md("## `match` (Python 3.10+)\n\n"
       "Cleaner than a stack of `elif`s when dispatching on a single value."),
    code("def describe(layer):\n"
         "    match layer:\n"
         "        case 'M1': return 'Metal1 — local routing'\n"
         "        case 'M2': return 'Metal2 — short interconnect'\n"
         "        case 'M3': return 'Metal3 — intermediate'\n"
         "        case _:    return 'Unknown layer'\n\n"
         "for layer in ('M1', 'M2', 'M7'):\n"
         "    print(layer, '→', describe(layer))"),

    md("## VLSI in practice — flag setup violations"),
    code("report = [\n"
         "    ('setup', -0.045),\n"
         "    ('hold',   0.120),\n"
         "    ('setup', -0.089),\n"
         "    ('setup',  0.010),\n"
         "    ('hold',  -0.005),\n"
         "]\n"
         "setup_v, hold_v = 0, 0\n"
         "for check, slack in report:\n"
         "    if slack >= 0:\n"
         "        continue\n"
         "    if check == 'setup':\n"
         "        setup_v += 1\n"
         "    else:\n"
         "        hold_v += 1\n"
         "print(f'setup violations: {setup_v}')\n"
         "print(f'hold  violations: {hold_v}')"),
] + exercise(
    "## Exercise 1\n\n"
    "Given `slacks = [0.12, -0.03, 0.05, -0.21, 0.00]`, print `\"violation\"` or `\"ok\"` for each.",
    "slacks = [0.12, -0.03, 0.05, -0.21, 0.00]\n"
    "for s in slacks:\n"
    "    print('violation' if s < 0 else 'ok', s)",
) + exercise(
    "## Exercise 2\n\n"
    "Use `range()` to iterate layers M1..M6 and print whether each is even- or odd-numbered.",
    "for layer in range(1, 7):\n"
    "    label = 'even' if layer % 2 == 0 else 'odd'\n"
    "    print(f'M{layer}: {label}')",
) + exercise(
    "## Exercise 3\n\n"
    "Write a `while` loop that starts at 1 and doubles until > 1000. Print each step.",
    "x = 1\n"
    "while x <= 1000:\n"
    "    print(x)\n"
    "    x *= 2",
) + [
    recap([
        "`if`/`elif`/`else` — one branch runs, in order.",
        "Indent with 4 spaces; mixing tabs and spaces is a common bug.",
        "`for` walks items; `range()` gives you integer sequences.",
        "`break` exits; `continue` skips; `match` dispatches on a single value.",
    ]),
    next_up(5, "Writing Your First Python Script"),
]


# ---------- Chapter 5 (First script — book ch4) -----------------------------
NB_05 = title_block(4, "Writing Your First Python Script", "lesson-04", [
    "The shape of a complete Python script: inputs, computation, output",
    "Compute power from voltage and current",
    "Compare the same script in Python, Tcl, and Perl",
    "Common beginner mistakes",
]) + [
    md("## The book's first script\n\n"
       "The classic three lines: define voltage and current, multiply, print. "
       "As a file you'd save this as `power_calc.py` and run `python3 power_calc.py`."),
    code("# This script calculates power from voltage and current\n\n"
         "# Define input values\n"
         "voltage = 1.2   # in volts\n"
         "current = 0.5   # in amperes\n\n"
         "# Calculate power\n"
         "power = voltage * current\n\n"
         "# Print the result\n"
         "print('Voltage:', voltage, 'V')\n"
         "print('Current:', current, 'A')\n"
         "print('Power:', power, 'W')"),

    md("## Reading it line by line\n\n"
       "- Lines starting with `#` are comments.\n"
       "- `voltage` and `current` are **variables** holding floats.\n"
       "- `power = voltage * current` is the calculation.\n"
       "- `print()` sends output to the terminal."),

    md("## The same script in Tcl and Perl\n\n"
       "Reference only — don't run. Feel how much ceremony each extra character costs.\n\n"
       "**Tcl:**\n```tcl\n"
       "set voltage 1.2\n"
       "set current 0.5\n"
       "set power [expr {$voltage * $current}]\n"
       'puts "Power: $power W"\n```\n\n'
       "**Perl:**\n```perl\n"
       "$voltage = 1.2;\n"
       "$current = 0.5;\n"
       "$power = $voltage * $current;\n"
       'print "Power: $power W\\n";\n```\n\n'
       "Python wins on clarity: no `expr`, no `$`, no trailing semicolons."),

    md("## Common mistakes to avoid\n\n"
       "- **Forgetting `.py` in the filename.** `python3` won't find your script.\n"
       "- **Wrong Python on PATH.** Run `python3 --version` to check.\n"
       "- **Indentation inside blocks.** Python uses whitespace to define structure."),
    code("# Formatted output with an f-string — more on these in Chapter 7\n"
         "voltage, current = 1.2, 0.5\n"
         "power = voltage * current\n"
         "print(f'V={voltage} V, I={current} A → P={power:.3f} W')"),

    md("## VLSI in practice — a tiny rail power table"),
    code("budget_W = 0.75\n"
         "rails = [\n"
         "    ('VDD_CORE', 0.8, 0.5),\n"
         "    ('VDD_IO',   1.8, 0.3),\n"
         "    ('VDD_SRAM', 0.9, 1.2),\n"
         "]\n"
         "print(f\"{'rail':10s} {'V':>4s} {'I':>4s} {'P(W)':>6s}  status\")\n"
         "for rail, v, i in rails:\n"
         "    p = v * i\n"
         "    status = 'over_budget' if p > budget_W else 'ok'\n"
         "    print(f'{rail:10s} {v:4.2f} {i:4.2f} {p:6.3f}  {status}')"),
] + exercise(
    "## Exercise 1\n\n"
    "Set `width=0.14`, `length=10`, compute area, print with 2 decimals.",
    "width = 0.14\n"
    "length = 10\n"
    "area = width * length\n"
    "print(f'area = {area:.2f}')",
) + exercise(
    "## Exercise 2\n\n"
    "Given slacks `-0.03`, `0.12`, `-0.08`, compute and print the average.",
    "slacks = [-0.03, 0.12, -0.08]\n"
    "avg = sum(slacks) / len(slacks)\n"
    "print(f'average slack = {avg:.4f}')",
) + [
    recap([
        "A script is a `.py` file run top-to-bottom.",
        "Variables hold values; `print()` shows them; comments explain *why*.",
        "Python needs no semicolons or sigils — the same logic fits in fewer keystrokes.",
        "Indentation matters — spaces define blocks.",
    ]),
    next_up(6, "Exploring Integer Operations for VLSI Use Cases"),
]


# ---------- Chapter 6 (Integers — book ch6) ---------------------------------
NB_06 = title_block(6, "Exploring Integer Operations for VLSI Use Cases", "lesson-06", [
    "Arithmetic: add, subtract, multiply, `/` vs `//`, and `%`",
    "Comparison operators for bounds and thresholds",
    "Useful built-ins: `range()`, `abs()`, `min()`, `max()`, `int()`",
    "Bitwise operations — masks, flags, bus widths",
]) + [
    md("## Arithmetic — addition, subtraction, multiplication\n\n"
       "Python doesn't need `expr` (Tcl) or `$` (Perl) to do math."),
    code("num_pins = 120\n"
         "extra_pins = 8\n"
         "total_pins = num_pins + extra_pins\n"
         "print(total_pins)\n"
         "metal_pitch_um = 0.2\n"
         "track_count = 5\n"
         "print(metal_pitch_um * track_count)"),

    md("## `/` vs `//`, and `%`\n\n"
       "`/` always returns a `float`. `//` truncates to an integer. `%` is the remainder."),
    code("total_length = 100\n"
         "grid_spacing = 7\n"
         "print('true  /:', total_length / grid_spacing)\n"
         "print('floor //:', total_length // grid_spacing)\n"
         "print('mod   %:', total_length % grid_spacing)\n"
         "for layer in range(1, 7):\n"
         "    parity = 'even' if layer % 2 == 0 else 'odd'\n"
         "    print(f'M{layer}: {parity}')"),

    md("## Comparison operators"),
    code("pin_count = 128\n"
         "if pin_count > 100:\n"
         "    print('High pin count')\n"
         "print(pin_count >= 128)\n"
         "print(pin_count != 0)"),

    md("## Useful built-ins"),
    code("for layer in range(1, 7):\n"
         "    print('Processing layer', layer)\n"
         "print('---')\n"
         "slack1, slack2 = 0.12, -0.05\n"
         "print('|skew| =', abs(slack1 - slack2))\n"
         "pins = [120, 100, 140, 96]\n"
         "print('min:', min(pins), 'max:', max(pins))"),

    md("## Converting strings to integers"),
    code("pin_text = '128'\n"
         "pin_count = int(pin_text)\n"
         "print(pin_count, type(pin_count).__name__)\n"
         "print(int('0xFF', 16), int('0b1010', 2))"),

    md("## Bitwise operations — masks and flags\n\n"
       "Used for layer masks, status flags, bus-enable bits."),
    code("mask = 0b1010\n"
         "flag = 0b0010\n"
         "print('flag set:', bool(mask & flag))\n"
         "print('bit 2 set:', bool(mask & 0b0100))\n"
         "print('union:', bin(mask | 0b0001))\n"
         "for n in range(1, 9):\n"
         "    print(f'{n}-bit bus → {2**n} states')"),
] + exercise(
    "## Exercise 1\n\n"
    "How many distinct words can a 32-bit address bus select? Print using `**`.",
    "print(2**32)",
) + exercise(
    "## Exercise 2\n\n"
    "Given `violations = [3, 7, 2, 9, 11]`, print max, min, and average (as an int).",
    "violations = [3, 7, 2, 9, 11]\n"
    "print('max:', max(violations))\n"
    "print('min:', min(violations))\n"
    "print('avg:', sum(violations) // len(violations))",
) + exercise(
    "## Exercise 3\n\n"
    "Print the bank number (`addr % 4`) for each address `0, 5, 10, 17, 23, 40`.",
    "for addr in (0, 5, 10, 17, 23, 40):\n"
    "    print(f'addr={addr} → bank={addr % 4}')",
) + [
    recap([
        "`/` always returns float; `//` truncates; `%` gives the remainder.",
        "`range(start, stop, step)` — stop is exclusive.",
        "`int()` parses strings; pass `base=` for hex or binary literals.",
        "Bitwise `&`, `|`, `^` work on integers — the go-to for masks and flags.",
    ]),
    next_up(7, "Working with Strings for VLSI Use Cases"),
]
