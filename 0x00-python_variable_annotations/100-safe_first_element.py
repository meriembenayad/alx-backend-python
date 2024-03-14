#!/usr/bin/env python3
""" 10. Duck typing - first element of a sequence """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ The types of the elements of the input are not know """
    if lst:
        return lst[0]
    else:
        return None
