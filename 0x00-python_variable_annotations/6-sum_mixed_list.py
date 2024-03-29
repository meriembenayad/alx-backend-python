#!/usr/bin/env python3
""" 6. Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Method that returns sum of list of mixed int/float. """
    return sum(mxd_lst)
