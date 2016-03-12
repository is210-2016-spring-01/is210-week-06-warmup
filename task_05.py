#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05"""


def flip_keys(*to_flip):
    """1.  A list named ``to_flip``. This list is assumed to have nested,
        immutable sequences inside it, eg: ``[(1, 2, 3), 'hello']``"""
    counter = 0
    for flip in to_flip:
        flip1 = flip[1][::-1]
        flip2 = flip[0][::-1]
        counter += 1
        flip = list()
        flip.append(flip2)
        flip.append(flip1)
        return flip, flip2, flip1, counter == len(to_flip)
