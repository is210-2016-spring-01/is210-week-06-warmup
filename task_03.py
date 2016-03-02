#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Changing tuple of directions."""

import data

DIRECTIONS = data.DIRECTIONS

DIRECTIONS = list(DIRECTIONS[:len(DIRECTIONS) - 1])

DIRECTIONS.append('West')

DIRECTIONS = tuple(DIRECTIONS)
