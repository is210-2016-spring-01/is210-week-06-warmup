#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutability differences between strings and tuples"""


def flip_keys(to_flip):
    """Reverses what's inside the list to be flipped

    Reverses what's in the list character by character.

    Args:
        A list (list): a list with contents.

    Returns:
        That list but reversed.

    Example:

        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']
    """
    counter = 0
    for item in to_flip:
        to_flip[counter] = item[::-1]
        counter += 1
    return to_flip
