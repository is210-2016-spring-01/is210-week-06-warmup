#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practicing tuple immutability."""

import data

DIRECTIONS = data.DIRECTIONS
DIRECTIONS = (DIRECTIONS[:len(DIRECTIONS)-1])+('West',)
