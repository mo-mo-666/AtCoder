#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     05/08/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np

l = list(input())
l = np.array(l)


state = 'AC'

if l[0] != 'A':
    state = 'WA'
else:
    l[0] = 'a'
    l2 = l[2:-1].copy()
    Cplace = np.where(l2=='C')[0]

    if len(Cplace) == 1:
        l2[Cplace[0]] = 'c'
        l[2:-1] = l2
        arr = ''.join(l)
        if not arr.islower():
            state = 'WA'

    else:
        state = 'WA'

print(state)

