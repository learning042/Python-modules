import sys


def print_args(argv: list[str], argc: int) -> None:
    if argc == 1:
        print("No arguments provided!")
        return
    print(f"Arguments received: {argc - 1}")
    count = 1
    for arg in argv[1:]:
        print(f"Argument {count}: {arg}")
        count += 1
    print(f" Total arguments: {argc}")


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print_args(sys.argv, len(sys.argv))


if __name__ == "__main__":
    main()
