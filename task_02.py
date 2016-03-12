#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Six Lists And Tuples."""

import data

BALLETS = data.BALLETS
del BALLETS[11]

BALLETS[2] = 'Swan Lake'
BALLETS.append('Herman Schmerman')
BALLETS.extend(['Don Quixote', 'Sylvia'])
