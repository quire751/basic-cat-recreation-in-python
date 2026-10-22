import sys
from pathlib import Path

if len(sys.argv) <= 1:
    print("ERROR: REQUIRES ONE ARGUMENT.")
    sys.exit(1)
else:
    file = sys.argv[1]
path = Path(file)

## Okay finally fixed this!!
if path.is_dir():
    print("Cannot Access Directories. Please try on a **real** file.")
    sys.exit(1)

## Prints the given file's text.
try:
    with open(file, "r") as f:
        _ = sys.stdout.write(f.read())  
except FileNotFoundError:
    print("That File doesn't exist! Please try on a file that actually exists.")
    sys.exit(1)
except PermissionError:
    print("You don't have permission to print the contents of this 'file'")
    sys.exit(1)

