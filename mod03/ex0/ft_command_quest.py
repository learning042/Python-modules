import sys


def print_args(argc: int, argv: list[str] = sys.argv) -> None:
    if not argv[1:]:
        return
    print(f"Arguments received: {argc - 1}")
    count = 1
    for arg in argv[1:]:
        print(f"Argument {count}: {arg}")
        count += 1


def main() -> None:
    print("=== Command Quest ===")
    argc = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    if argc == 1:
        print("No arguments provided!")
    print_args(argc)
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
