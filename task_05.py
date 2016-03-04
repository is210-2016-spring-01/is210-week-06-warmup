#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 5 file."""


def flip_keys(to_flip):
    """To reverse items in a mixed list

    Args:
        to_flip(list): a list mixed with tuple and other values.

    Returns:
        list: to return values in the list, reversed.

    Examples:

        >>> flip_keys([(1, 2, 3), 'abc'])
    """
    counter = 0
    for value in to_flip:
        print value[::-1]
    counter += 1
    return to_flip
