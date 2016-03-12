#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Six Lists And Tuples."""

import copy
import data

DIRECTIONS = copy.copy(data.DIRECTIONS)
X = [DIRECTIONS[0], DIRECTIONS[1], DIRECTIONS[2],
     DIRECTIONS[3][len('Spaghetti '):-len('ern')]]
DIRECTIONS = X
