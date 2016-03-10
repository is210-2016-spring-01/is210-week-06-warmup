#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 4 docstring."""


def process_data(data):
    """Looping lists with a for loop.

    Args:
        data (int): To summed up and averaged.

    Retruns:
        integer: Argument added up.
        decimal: Argument averaged.

    Examples:

        >>> process_data([1, 2, 3])
        (6, 2.0)

       >>> process_data([2, 3, 4])
       (9, 3.0)
    """
    add = 0
    for num in data:
        add += num
        avg = add / float(len(data))
    return (add, avg)
