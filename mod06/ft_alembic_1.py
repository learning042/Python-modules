from elements import create_water


def main() -> None:
    print(
            "=== Alembic 1 ===\n"
            "Using: 'from ... import ...' structure "
            "to access elements.py\n"
            f"Testing create_water: {create_water()}"
    )


if __name__ == "__main__":
    main()
