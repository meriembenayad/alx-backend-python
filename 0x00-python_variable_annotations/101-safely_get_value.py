#!/usr/bin/env python3
""" 11. More involved type annotations """
from typing import TypeVar, Mapping, Any, Union

# Declare type variable
T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """ Add type annotations to the function """
    if key in dct:
        return dct[key]
    else:
        return default
