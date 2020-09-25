from pathlib import Path
from time import ctime

path = Path("app.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(ctime(path.stat().st_ctime))
# print(path.read_text())
