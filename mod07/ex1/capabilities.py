from abc import ABC, abstractmethod
from ex0.creatures import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed = False
        super().__init__()

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
