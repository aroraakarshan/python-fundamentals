"""Build all 14 companion notebooks from the parts files."""
from pathlib import Path
from nbkit import write_notebook

from build_notebooks_p1 import NB_01, NB_02, NB_03
from build_notebooks_p2 import NB_04, NB_05, NB_06
from build_notebooks_p3 import NB_07, NB_08, NB_09, NB_10, NB_11
from build_notebooks_p4 import NB_12, NB_13, NB_14

ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    (NB_01, "Chapter_01_Why_Python_for_VLSI.ipynb"),
    (NB_02, "Chapter_02_Python_Environment_Setup.ipynb"),
    (NB_03, "Chapter_03_Understanding_Basics.ipynb"),
    (NB_05, "Chapter_04_First_Python_Script.ipynb"),
    (NB_06, "Chapter_06_Integer_Mastery_for_VLSI.ipynb"),
    (NB_07, "Chapter_08_String_Mastery_for_VLSI.ipynb"),
    (NB_08, "Chapter_10_List_Mastery_for_VLSI.ipynb"),
    (NB_09, "Chapter_11_Dictionary_Mastery_for_VLSI.ipynb"),
    (NB_10, "Chapter_12_Tuple_Mastery_for_VLSI.ipynb"),
    (NB_11, "Chapter_13_Set_Mastery_for_VLSI.ipynb"),
    (NB_04, "Chapter_14_Control_Structures_Conditionals_and_Loops.ipynb"),
    (NB_12, "Chapter_15_Functions_and_Modules_for_VLSI.ipynb"),
    (NB_13, "Chapter_16_File_IO_Operations_for_VLSI.ipynb"),
    (NB_14, "Chapter_17_Advanced_File_Processing_for_VLSI.ipynb"),
]

if __name__ == "__main__":
    for cells, name in TARGETS:
        write_notebook(ROOT / name, cells)
    print(f"\nBuilt {len(TARGETS)} notebooks.")
