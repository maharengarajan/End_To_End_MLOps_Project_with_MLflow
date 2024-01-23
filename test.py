import os
from pathlib import Path

print(Path("X/Y/z.txt"))

print(Path("X\Y\z.txt"))

print(os.path.split("a/b/c.txt"))