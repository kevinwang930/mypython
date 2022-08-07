from pathlib import Path

path = Path(__file__)
if path.exists() and path.is_file():
    print(type(path))

testPath = Path('test.py').resolve()
print(testPath)
