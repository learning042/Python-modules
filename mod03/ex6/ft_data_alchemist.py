import random


def main() -> None:
    print(" === Game Data Alchemist ===")
    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f" Initial list of players: {players}")
    all_capitalized = [player.capitalize() for player in players]
    print(f" New list with all names capitalized: {all_capitalized}")
    capitalized = [player for player in players
                   if player == player.capitalize()]
    print(f" New list of capitalized names only: {capitalized}")
    scores = {player: random.randrange(1000) for player in all_capitalized}
    print(f" Score dict: {scores}")
    average = round(sum(scores.values()) / len(scores), 2)
    print(f" Score average is {average}")
    high_scores = {player: scores[player] for player in scores
                   if scores[player] > average}
    print(f" High scores: {high_scores}")


if __name__ == "__main__":
    main()
