from pathlib import Path

p1 = Path('abc.txt')
print(type(p1))

if not p1.exists():
    with open(p1,'w') as file:
        print(file.write('Content 3'))

print(p1.name)
print(p1.stem)
print(p1.suffix)