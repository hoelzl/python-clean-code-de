from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player


class Action(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @abstractmethod
    def execute(self, instigator: "Player") -> None:
        ...
