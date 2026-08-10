def secure_archive(filename: str,
                   action: str = "r",
                   content: str = ""
                   ) -> tuple[bool, str]:
    if action in ("r", "read", 0):
        mode = "r"
    elif action in ("w", "write", 1):
        mode = "w"
    else:
        return (False, "Invalid action: Try 'r' or 'w' (read or write)")
    try:
        with open(filename, mode) as file:
            if mode == "r":
                return (True, file.read())
            else:
                file.write(content)
                return (True, "Content successfully written to file")
    except Exception as e:
        return (False, f"{e}")


def main() -> None:
    print(" === Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file")
    print(secure_archive("/not/existing/file", "r"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd'", "r"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("file", "r"))
    print()
    print("Using 'secure_archive' to write previous content to a new file")
    print(secure_archive(
                         "new_file", "w",
                         "[FRAGMENT 001] Digital preservation"
                         "protocols established 2087\n[FRAGMENT 002] Knowledge"
                         "must survive the entropy wars\n[FRAGMENT 003] Every"
                         "byte saved is a victory against oblivion\n"
                         )
          )


if __name__ == "__main__":
    main()
