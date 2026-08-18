import random


class Player:
    def __init__(self, name: str, all_achievements: list[str]) -> None:
        self._name = name
        self._achievements = gen_player_achievements(all_achievements)
        self._missing = set(all_achievements).difference(self._achievements)

    def print_achievements(self) -> None:
        print(f"Player {self._name}: {self._achievements}")

    def print_missing(self) -> None:
        print(f"{self._name} is missing: {self._missing}")

    def get_name(self) -> str:
        return self._name

    def get_achievements(self) -> set[str]:
        return self._achievements


def print_unique_achievements(players: list[Player]) -> None:
    for player in players:
        achs = player.get_achievements()
        unique = achs.difference(*(
                                 another.get_achievements()
                                 for another in players
                                 if another is not player
                                 ))
        print(f"Only {player.get_name()} has: {unique}")


def print_common_achievements(players: list[Player]) -> None:
    common = players[0].get_achievements().intersection(
            *(player.get_achievements() for player in players)
            )
    print(f"Common achievements: {common}")


def ft_range(number: int) -> list[int]:
    i = 0
    iterable = []
    while i < number:
        iterable.append(i)
        i += 1
    return iterable


def weighting(number: int) -> list[int]:
    weight = []
    i = 0
    while i < number:
        if i < 6:
            weight.append(0)
        elif i < 9:
            weight.append(100)
        else:
            weight.append(1)
        i += 1
    return weight


def gen_player_achievements(achievements: list[str]) -> set[str]:
    max_size = len(achievements)
    possible_sizes = ft_range(max_size)
    w = weighting(max_size)
    size = random.choices(possible_sizes, weights=w, k=1)[0]
    return set(random.sample(achievements, k=size))


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    achievements = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
    ]
    players = [
        Player("Alice", achievements),
        Player("Bob", achievements),
        Player("Charlie", achievements),
        Player("Dylan", achievements)
    ]
    for player in players:
        player.print_achievements()
        print()
    print(f"All distinct achievements: {set(achievements)}")
    print()
    print_common_achievements(players)
    print()
    print_unique_achievements(players)
    print()
    for player in players:
        player.print_missing()


if __name__ == "__main__":
    main()
