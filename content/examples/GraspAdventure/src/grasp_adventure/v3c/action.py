from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .location import Location

if TYPE_CHECKING:
    from .pawn import Pawn


class Action(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @abstractmethod
    def execute(self, instigator: "Pawn") -> None:
        ...


@dataclass
class MoveAction(Action):
    direction: str
    target: Location

    @property
    def description(self) -> str:
        return f"move {self.direction} to {self.target.name}"

    def execute(self, instigator: "Pawn") -> None:
        instigator.location = self.target


@dataclass
class WaitAction(Action):
    @property
    def description(self) -> str:
        return "wait one turn"

    def execute(self, instigator: "Pawn") -> None:
        # Do nothing...
        pass
