from alchemy.elements import create_air


def main() -> None:
    print(
            "=== Alembic 3 ===\n"
            "Accessing alchemy/elements.py using "
            "'from ... import ...' structure\n"
            f"Testing create_air: {create_air()}"
    )


if __name__ == "__main__":
    main()
