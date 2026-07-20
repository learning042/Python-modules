import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "swim", "climb", "release"]
    while True:
        random_player = random.choice(players)
        random_action = random.choice(actions)
        yield (random_player, random_action)


def consume_event(events: list) -> typing.Generator[tuple[str, str],
                                                    None,
                                                    None]:
    while events:
        index = random.randrange(len(events))
        item = events[index]
        events[:] = events[:index] + events[index + 1:]
        yield item


def main() -> None:
    print(" === Game Data Stream Processor ===")
    g = gen_event()
    for i in range(1000):
        player, action = next(g)
        print(f" Event {i}: Player {player} did action {action}")
    events = []
    for i in range(10):
        events += [next(g)]
    print(f" Built list of 10 events: {events}")
    for element in consume_event(events):
        print(f" Got event from list: {element}")
        print(f" Remains in list: {events}")


if __name__ == "__main__":
    main()
