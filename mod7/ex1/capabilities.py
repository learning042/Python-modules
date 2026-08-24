from abc import ABC, abstractmethod
from ex0.creatures import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature | None) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self, **kwargs) -> None:
        self._transformed = False
        super().__init__(**kwargs)

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
