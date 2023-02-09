import random
from dataclasses import dataclass
from random import randint


@dataclass
class Die:
    def roll(self):
        """Roll the die and return the result.

        >>> random.seed(19)
        >>> d = Die()
        >>> d.roll()
        6
        >>> d.roll()
        1
        """
        return randint(1, 6)
