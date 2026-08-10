import sys


def cat() -> None | str:
    argc = len(sys.argv)
    if argc != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return None
    print(" === Cyber Archives Recovery & Preservation ===")
    print(f" Accessing file '{sys.argv[1]}'")
    file = None
    try:
        file = open(sys.argv[1])
        content = file.read()
        print(" ---")
        print()
        print(" " + content.replace("\n", "\n "))
        print(" ---")
        return content
    except (FileNotFoundError, PermissionError) as oe:
        sys.stderr.write(f" [STDERR] Error opening file '{sys.argv[1]}':"
                         f" {oe}\n")
    except Exception as e:
        sys.stderr.write(f" Error: {e}\n")
    finally:
        if file is not None:
            file.close()
            sys.stdout.write(f" File '{sys.argv[1]}' closed.\n")
    return None


def main() -> None:
    content = cat()
    if content is None:
        return
    new_content = content.replace("\n", "#\n")
    print()
    print(" Transform data:")
    print(" ---")
    print()
    print(" " + new_content.replace("\n", "\n "))
    print(" ---")
    sys.stdout.write(" Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()
    if new_filename == "":
        print(" Not saving data.")
    else:
        print(f" Saving data to '{new_filename}'")
        new_file = None
        try:
            new_file = open(new_filename, 'w')
            new_file.write(new_content)
            print(f" Data saved in file '{new_filename}'.")
        except OSError as oe:
            sys.stderr.write(f" [STDERR] Error opening file '{sys.argv[1]}':"
                             f"{oe}\n")
            sys.stderr.write(" Data not saved\n")
        except Exception as e:
            sys.stderr.write(f" Error: {e}\n")
            sys.stderr.write(" Nothing was saved\n")
        finally:
            if new_file is not None:
                new_file.close()


if __name__ == "__main__":
    main()
