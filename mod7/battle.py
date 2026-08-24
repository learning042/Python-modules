from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(
            factory1: CreatureFactory,
            factory2: CreatureFactory,
            evolution1: str = "base",
            evolution2: str = "base"
           ) -> None:
    print("Testing battle")
    for ev in (evolution1, evolution2):
        if ev not in ("base", "evolved"):
            raise ValueError(
                    "The creature must be 'base' or 'evolved' "
                    f", got '{ev}'"
                   )
    creature1 = getattr(factory1, "create_" + evolution1)()
    creature2 = getattr(factory2, "create_" + evolution2)()
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    factory1 = FlameFactory()
    factory2 = AquaFactory()
    test_factory(factory1)
    test_factory(factory2)
    battle(factory1, factory2)


if __name__ == "__main__":
    main()
