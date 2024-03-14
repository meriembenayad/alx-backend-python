#!/usr/bin/env python3
""" 9. Let's duck type an iterable object """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Method that returns values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
