from dataclasses import dataclass

from .location import Location


@dataclass
class Pawn:
    name: str
    location: Location

    def move(self, direction):
        new_location = self.location[direction]
        if new_location:
            self.location = new_location
        else:
            print(f"{self.name!r}: Cannot move in direction {direction!r}.")
