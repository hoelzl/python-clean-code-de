import random
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable


class Dice(ABC):
    """Roll with a combination of multiple dice."""

    def roll(self, seed=None):
        if seed is not None:
            random.seed(seed)
        return self._roll()

    @abstractmethod
    def _roll(self) -> int:
        ...

    @property
    @abstractmethod
    def min_value(self) -> int:
        ...

    @property
    @abstractmethod
    def max_value(self) -> int:
        ...


@dataclass
class ConstantDice(Dice):
    value: int

    def _roll(self) -> int:
        """Return the constant value of the dice.

        >>> d = ConstantDice(3)
        >>> d._roll()
        3
        """
        return self.value

    @property
    def min_value(self) -> int:
        """Return the constant value of the dice.

        >>> d = ConstantDice(5)
        >>> d._roll()
        5
        """
        return self.value

    @property
    def max_value(self) -> int:
        """Return the constant value of the dice.

        >>> d = ConstantDice(3)
        >>> d._roll()
        3
        """
        return self.value


@dataclass
class FairDice(Dice):
    num_dice: int
    num_sides: int

    def __post_init__(self):
        assert self.num_dice >= 1
        assert self.num_sides >= 2

    def _roll(self) -> int:
        """Roll the dice and return the result.

        >>> FairDice(2, 6).roll(42)
        7
        """
        result = 0
        for _ in range(self.num_dice):
            result += random.randint(1, self.num_sides)
        return result

    @property
    def min_value(self) -> int:
        """Return the lowest possible value.

        >>> FairDice(2, 6).min_value
        2
        """
        return self.num_dice

    @property
    def max_value(self) -> int:
        """Return the highest possible value.

        >>> FairDice(2, 6).max_value
        12
        """
        return self.num_sides * self.num_dice


@dataclass
class SumDice(Dice):
    dice: list[Dice]

    def _roll(self) -> int:
        """Roll all dice and return the sum.

        >>> d = SumDice([ConstantDice(2), FairDice(2, 6)])
        >>> d.roll(42)  # noqa
        9
        """
        return sum(d._roll() for d in self.dice)

    @property
    def min_value(self) -> int:
        """Return the lowest possible value..

        >>> d = SumDice([ConstantDice(2), FairDice(2, 6)])
        >>> d.min_value  # noqa
        4
        """
        return sum(d.min_value for d in self.dice)

    @property
    def max_value(self) -> int:
        """Return the highest possible value..

        >>> d = SumDice([ConstantDice(2), FairDice(2, 6)])
        >>> d.max_value  # noqa
        14
        """
        return sum(d.max_value for d in self.dice)


class SimpleDie(Dice):
    def __init__(self, num_sides):
        assert num_sides >= 2
        self.num_sides = num_sides

    def __eq__(self, other):
        if isinstance(other, SimpleDie):
            return self.num_sides == other.num_sides
        else:
            return False

    def _roll(self) -> int:
        return random.randint(1, self.num_sides)

    @property
    def min_value(self) -> int:
        return 1

    @property
    def max_value(self) -> int:
        return self.num_sides


@dataclass
class MultipleRollDice(Dice):
    rolls: int
    dice: Dice

    def __post_init__(self):
        assert self.rolls >= 1
        assert self.dice

    def _roll(self) -> int:
        result = 0
        for _ in range(self.rolls):
            result += self.dice._roll()
        return result

    @property
    def min_value(self) -> int:
        return self.rolls * self.dice.min_value

    @property
    def max_value(self) -> int:
        return self.rolls * self.dice.max_value


DICE_REGEX = re.compile(r"^\s*(\d*)\s*([Dd]?)\s*(\d+)\s*$")


def create_single_die(configuration: str) -> Dice:
    """
    Parse a single die configuration string into a die.

    :param configuration: A string in the form '2d6'
    :return: A Dice spec
    """
    match = DICE_REGEX.match(configuration)
    if match.group(2):
        num_dice = int(match.group(1) or "1")
        num_sides = int(match.group(3))
        return FairDice(num_dice, num_sides)
    else:
        value = int(match.group(3))
        return ConstantDice(value)


def create_dice(configuration: str) -> Dice:
    """
    Create dice from a configuration string.

    :param configuration: A string in the form '2d6 + 4'
    :return: A dice corresponding to the configuration string.
    """
    single_configs = configuration.split("+")
    dice = [create_single_die(config) for config in single_configs]
    if len(dice) == 1:
        return dice[0]
    else:
        return SumDice(dice)


def to_json(dice: Dice | Iterable[Dice]):
    if isinstance(dice, Dice):
        match type(dice):
            case ConstantDice(value):
                return {"type": "ConstantDice", "value": value}
            case FairDice(num_dice, num_sides):
                return {
                    "type": "FairDice",
                    "num_dice": num_dice,
                    "num_sides": num_sides,
                }
            case SumDice(dice):
                return {"type": "SumDice", "dice": to_json(dice)}
            case SimpleDie(num_sides):
                return {"type": "SimpleDie", "num_sides": num_sides}
            case MultipleRollDice(rolls, dice):
                return {
                    "type": "MultipleRollDice",
                    "rolls": rolls,
                    "dice": to_json(dice),
                }
            case _:
                raise ValueError(f"{dice} is not a known dice type.")
    else:
        return [to_json(die) for die in dice]
