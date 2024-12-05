import os
from pathlib import Path

c_extensions = (".c", ".h")

def format_directory(path : Path):
    for file in path.rglob('*'):
        if file.is_file() and file.suffix in c_extensions:
            os.system("clang-format -i -style=file " + str(file))

if __name__ == "__main__":
    dirs = ["src"]
    for dir in dirs:
        path = Path(dir)
        format_directory(path)
