import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    names = ["Alice", "bob", "Charlie", "dylan", "Emma",
             "Gregory", "john", "kevin", "Liam"]
    capitalized = [name.capitalize() for name in names]
    only_capital = [name for name in names if name == name.capitalize()]
    scores = {name: random.randrange(1000) for name in capitalized}
    average = round(sum(scores.values()) / len(scores), 2)
    high_scores = {name: score
                   for name, score in scores.items()
                   if score > average
                   }
    print(
            f"Initial list of players: {names}\n"
            f"New list with all names capitalized: {capitalized}\n"
            f"New list of capitalzied names only: {only_capital}\n\n"
            f"Score dict: {scores}\n"
            f"Score average is {average}\n"
            f"High scores: {high_scores}"
    )


if __name__ == "__main__":
    main()
