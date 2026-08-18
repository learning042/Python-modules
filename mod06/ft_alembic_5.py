from alchemy import create_air


def main() -> None:
    print(
            "=== Alembic 5 ===\n"
            "Accessing the alchemy module using 'from alchemy import ...'\n"
            f"Testing create_air: {create_air()}"
    )


if __name__ == "__main__":
    main()
