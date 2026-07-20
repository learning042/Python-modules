import random


def gen_player_achievements() -> set[str]:
    achievements = ["Crafting Genius", "World Savior", "Master Explorer",
                    "Collector supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Speed Runner", "Survivor",
                    "Treasure Hunter", "First Steps", "Sharp Mind",
                    "Unstoppable", "Hidden Path Finger"]
    num_ach = random.randrange(14)
    player_ach: set[str] = set()
    i = 0
    while i < num_ach:
        player_ach = player_ach.union({random.choice(achievements)})
        i += 1
    return player_ach


class Player:
    def __init__(self, name: str) -> None:
        self.name = name.capitalize()
        self.achievements = gen_player_achievements()


def main() -> None:
    print(" === Achievement Tracker System ===")
    alice = Player("alice")
    bob = Player("bob")
    charlie = Player("charlie")
    dylan = Player("dylan")
    players = [alice, bob, charlie, dylan]
    achievements = {"Crafting Genius", "World Savior", "Master Explorer",
                    "Collector supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Speed Runner", "Survivor",
                    "Treasure Hunter", "First Steps", "Sharp Mind",
                    "Unstoppable", "Hidden Path Finder"}
    for player in players:
        print(f" Player {player.name}: {player.achievements}")
    print()
    dist_ach: set[str] = set()
    for player in players:
        dist_ach = dist_ach.union(player.achievements)
    print(f" All distinct achievements: {dist_ach}")
    print()
    common_ach = alice.achievements
    for player in players:
        common_ach = common_ach.intersection(player.achievements)
    print(f" Common achievements: {common_ach}")
    print()
    for player1 in players:
        ach1 = player1.achievements
        for player2 in players:
            if player1 == player2:
                continue
            ach2 = player2.achievements
            ach1 = ach1.difference(ach2)
        print(f" Only {player1.name} has: {ach1}")
    print()
    for player in players:
        print(f" {player.name} is missing: "
              f"{achievements.difference(player.achievements)}")


if __name__ == "__main__":
    main()
