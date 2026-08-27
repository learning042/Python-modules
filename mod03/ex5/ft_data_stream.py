import typing
import random


def gen_event(
              players: list[str],
              actions: list[str]
             ) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
                  events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        choice = random.randrange(len(events))
        yield events.pop(choice)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release"]
    g = gen_event(players, actions)
    for i in range(1000):
        player, action = next(g)
        print(f"Event {i}: Player {player} did action {action}")
    events = [next(g) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
