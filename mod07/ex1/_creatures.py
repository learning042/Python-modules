from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability
from typing import Any


class Sproutling(Creature, HealCapability):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__("Sproutling", "Grass", **kwargs)

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self._name} heals itself for a small amount"
        return f"{self._name} heals {target._name} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__("Bloomelle", "Grass/Fairy", **kwargs)

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self._name} heals itself for a large amount"
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__("Shiftling", "Normal", **kwargs)

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__("Morphagon", "Normal/Dragon", **kwargs)

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form."
