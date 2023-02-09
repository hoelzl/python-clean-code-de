from dataclasses import dataclass

from .base_classes import GameObject


@dataclass()
class TreasureChest(GameObject):
    gold: int = 50

    def __str__(self):
        return "a treasure chest"

    @property
    def description(self):
        return f"a treasure chest containing {self.gold} gold pieces"


@dataclass()
class Torch(GameObject):
    def __str__(self):
        return "a torch"
