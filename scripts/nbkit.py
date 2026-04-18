"""Emit an .ipynb v4 file from a list of (kind, source) cell tuples."""
from __future__ import annotations
import json
from pathlib import Path


def md(text: str):
    return ("md", text)


def code(text: str):
    return ("code", text)


def exercise(prompt: str, solution: str):
    return [
        md(prompt),
        code("# Your code here\n"),
        md(f"<details><summary>Show solution</summary>\n\n```python\n{solution}\n```\n\n</details>"),
    ]


def setup_cell():
    return code(
        "import sys, platform\n"
        'print(f"Python {sys.version.split()[0]} on {platform.system()}")\n'
        'assert sys.version_info >= (3, 9), "This notebook needs Python 3.9 or newer."'
    )


def title_block(ch_num: int, title: str, lesson_slug: str, learn: list[str]):
    learn_md = "\n".join(f"- {b}" for b in learn)
    return [
        md(
            f"# Chapter {ch_num}: {title}\n\n"
            f"Companion notebook to **python-from-zero** · "
            f"`{lesson_slug}` · based on *Python for VLSI*, Chapter {ch_num}.\n\n"
            f"### You will learn\n\n{learn_md}"
        ),
        setup_cell(),
    ]


def recap(points: list[str]):
    bullets = "\n".join(f"- {p}" for p in points)
    return md(f"## Recap\n\n{bullets}")


def next_up(ch: int | None, title: str | None):
    if ch is None:
        return md(
            "## What's next\n\nYou've reached the end of the companion series. Return to "
            "the [python-from-zero](https://python-from-zero.pages.dev) site to keep going."
        )
    return md(
        f"## What's next\n\nContinue with **Chapter {ch}: {title}** in this repo, "
        f"and the matching lesson on [python-from-zero](https://python-from-zero.pages.dev)."
    )


def to_notebook(cells: list) -> dict:
    out = []
    for kind, src in cells:
        lines = src.splitlines(keepends=True)
        base = {"source": lines, "metadata": {}}
        if kind == "md":
            out.append({**base, "cell_type": "markdown"})
        elif kind == "code":
            out.append({**base, "cell_type": "code", "execution_count": None, "outputs": []})
        else:
            raise ValueError(kind)
    return {
        "cells": out,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "name": "python",
                "version": "3.11",
                "mimetype": "text/x-python",
                "file_extension": ".py",
                "pygments_lexer": "ipython3",
                "codemirror_mode": {"name": "ipython", "version": 3},
                "nbconvert_exporter": "python",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_notebook(path: Path, cells: list):
    nb = to_notebook(cells)
    path.write_text(json.dumps(nb, indent=1) + "\n")
    print(f"wrote {path.name}  ({len(cells)} cells)")
