from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.iterdir()

for path in file_paths:
    print(path)
