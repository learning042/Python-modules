import sys


def atoi_list(data: list[str]) -> list[int]:
    converted_data = []
    for element in data:
        try:
            converted_data.append(int(element))
        except ValueError:
            print(f"Invalid parameter: '{element}'")
    return converted_data


def print_analytics(scores: list[int], total_players: int) -> None:
    print(f"Scores processed: {scores}")
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = atoi_list(sys.argv[1:])
    total_players = len(scores)
    if not total_players:
        print("No scores provided. Usage: python3" +
              f"{sys.argv[0]}<score1> <score2> ...")
        return
    print_analytics(scores, total_players)


if __name__ == "__main__":
    main()
