import sys


def cat() -> None:
    argc = len(sys.argv)
    if argc != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print(" === Cyber Archives Recovery ===")
    print(f" Accessing file '{sys.argv[1]}'")
    file = None
    try:
        file = open(sys.argv[1])
        content = file.read()
        print(" ---")
        print()
        print(" " + content.replace("\n", "\n "))
        print(" ---")
    except (FileNotFoundError, PermissionError) as oe:
        print(f" Error opening file '{sys.argv[1]}': {oe}")
    except Exception as e:
        print(f" Error: {e}")
    finally:
        if file is not None:
            file.close()
            print(f" File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    cat()
