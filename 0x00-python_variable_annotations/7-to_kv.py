#!/usr/bin/env python3
""" 7. Complex types - string and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Method that returns a tuple
        - first element of the tuple is the string k
        - second element is the square of int/float v -> float
    """
    return (k, v ** 2)
