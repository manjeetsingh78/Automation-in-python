from pathlib import Path

files_dr = Path('files')

for filepath in files_dr.iterdir():
    with open(filepath,'r') as file:
        content = file.read()
        new_content = content[:-1]
    with open(filepath,'w') as file:
        file.write(new_content)