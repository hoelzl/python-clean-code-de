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


class GameObject(ABC):
    @abstractmethod
    def __str__(self):
        ...

    @property
    def description(self):
        return str(self)
