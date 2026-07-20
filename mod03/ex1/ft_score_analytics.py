import sys


def main() -> None:
    print(" === Player Score Analytics ===")
    argc = len(sys.argv)
    if argc == 1:
        print(" No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return
    scores = []
    for score_str in sys.argv[1:]:
        try:
            score = int(score_str)
            scores += [score]
        except Exception:
            print(f" Invalid parameter: '{score}'")
    scores_len = len(scores)
    if scores_len == 0:
        print(" No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return
    total_score = sum(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score
    print(f" Scores processed: {scores}")
    print(f" Total players: {scores_len}")
    print(f" Total score: {total_score}")
    print(f" Average score: {total_score / scores_len:.1f}")
    print(f" High score: {high_score}")
    print(f" Low score: {low_score}")
    print(f" Score range: {score_range}")


if __name__ == "__main__":
    main()
