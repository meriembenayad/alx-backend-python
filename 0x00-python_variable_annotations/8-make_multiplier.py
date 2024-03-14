#!/usr/bin/env python3
""" 8. Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Method that returns a function that multiplies a float by multiplier
    """

    def multiply(num: float) -> float:
        """ multiplies a float by multiplier """
        return num * multiplier

    return multiply
