from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self._name = name
        self._ctype = creature_type
        super().__init__()

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._ctype} type Creature"
