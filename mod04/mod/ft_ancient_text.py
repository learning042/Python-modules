import sys
import typing


def safe_open(filename: str, mode: str = "r") -> typing.IO[str] | None:
    try:
        file = open(filename, mode)
    except OSError as error:
        print(f" Error opening file '{filename}': {error}")
        return None
    return file
    

def cat(file: typing.IO[str]) -> None:
    try:
        buffer = file.read()
        print(" ---")
        print()
        print(" " + buffer.replace("\n", "\n "))
        print(" ---")
    except (OSError, UnicodeDecodeError) as error:
        print(f" Error reading file '{file.name}': {error}")
    finally:
        file.close()
        print(f" File '{file.name}' closed.")
    

def main() -> None:
    argc = len(sys.argv)
    if argc != 2:
        print(f" Usage: {sys.argv[0]} <file>")
        return
    print(" === Cyber Archives Recovery ===")
    print(f" Acessing file '{sys.argv[1]}'")
    file = safe_open(sys.argv[1])
    if file is None:
        return
    cat(file)
    

if __name__ == "__main__":
    main()