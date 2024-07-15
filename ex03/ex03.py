import sys
from pathlib import Path
from colorama import Fore, Style

def print_directory_structure(directory, prefix='',):
    try:
        entries = list(directory.iterdir())
    except Exception as e:
        print(f":For {directory} there's an error {e}")
        return

    for entry in entries:
        if entry.is_dir():
            print(Fore.BLUE + prefix + f"[DIR] {entry.name}" + Style.RESET_ALL)
            print_directory_structure(entry, prefix + '--')
        else:
            print(Fore.GREEN + prefix + f"[FILE] {entry.name}" + Style.RESET_ALL)

if len(sys.argv) != 2:
    print("Please specify a folder")
    sys.exit(1)

directory_path = Path(sys.argv[1])
if not directory_path.exists() or not directory_path.is_dir():
    print(f"{directory_path} is not a valid directory")
    sys.exit(1)

print(f"Directory structure of {directory_path}:")
print(Fore.BLUE + f"[DIR] {directory_path.name}" + Style.RESET_ALL)
print_directory_structure(directory_path, "--")