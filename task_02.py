#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1] = "Swan Lake"

BALLETS.append("Herman Schmerman")

MORE = ("Don Quixote", "Sylvia")

BALLETS.extend(MORE)
