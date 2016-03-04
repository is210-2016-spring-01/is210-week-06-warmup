#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Six Lists And Tuples."""

import __builtin__


def process_data(data):
    """Does some maths and returns a tuple.

    Args:
        data (list): Argument to be calculated.

    Returns:
        tuple: the result of the argument calculation.

    Examples:

        >>> process_data([1, 2, 3])
        (6, 2.0)
        >>> process_data([16, 65, 99])
        (180, 60.0)
    """
    __builtin__.sum = 0
    count = 0
    for i, __builtin__.sum in enumerate(data):
        __builtin__.sum = __builtin__.sum + data[i]
        count = count + 1

    return (sum, float(sum)//count)
