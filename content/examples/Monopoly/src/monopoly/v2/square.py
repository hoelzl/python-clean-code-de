from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player


@dataclass
class Square(ABC):
    name: str
    index: int

    @abstractmethod
    def landed_on(self, player: "Player"):
        ...


def make_square(name: str, index: int, cls: Type[Square]):
    return cls(name=name, index=index)  # noqa


@dataclass
class GoSquare(Square):
    def landed_on(self, player: "Player"):
        pass


@dataclass
class RegularSquare(Square):
    def landed_on(self, player: "Player"):
        pass


@dataclass
class IncomeTaxSquare(Square):
    def landed_on(self, player: "Player"):
        pass


@dataclass
class GoToJailSquare(Square):
    def landed_on(self, player: "Player"):
        pass


@dataclass
class DrawCardSquare(Square):
    def landed_on(self, player: "Player"):
        pass
