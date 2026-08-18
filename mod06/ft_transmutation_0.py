import alchemy.transmutation.recipes


def main() -> None:
    print(
            "=== Transmutation 0 ===\n"
            "Using file alchemy/transmutation/recipes.py directly\n"
            f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()
