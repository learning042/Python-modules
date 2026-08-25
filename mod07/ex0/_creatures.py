from .creatures import Creature
from typing import Any


class Flameling(Creature):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__("Flameling", "Fire", **kwargs)

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__("Pyrodon", "Fire/Flying", **kwargs)

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__("Aquabub", "Water", **kwargs)

    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__("Torragon", "Water", **kwargs)

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"
