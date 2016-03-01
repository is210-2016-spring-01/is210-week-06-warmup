#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a module"""


def flip_keys(to_flip):
    """Returns the reverse order of a tuple

    Args:
        to_flip (mixed): Immutable string or integersi in a nested list

    Returns:
        mixed: the list is reversed

    Example:

        >>> flip_keys([(4, 5, 6), 'def', (6, 7, 8)])
        [(6, 5, 4), 'fed', (8, 7, 6)]
    """
    num = 0
    for lis in to_flip:
        lis[::-1]
        num += 1
        return to_flip
