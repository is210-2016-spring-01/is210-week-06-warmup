#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05"""


def flip_keys(*to_flip):
    """1.  A list named ``to_flip``. This list is assumed to have nested,
        immutable sequences inside it, eg: ``[(1, 2, 3), 'hello']``"""
    counter = 0
    for flip in to_flip:
        flip1 = flip[1][::-1]
        #flip = list(flip[1]).reverse()
        flip2 = flip[0][::-1]
        #flip = flip[0][::-1].extend(flip[1:3])
        #flip = flip1.reverse()
        counter +=1
        return flip2, flip1
