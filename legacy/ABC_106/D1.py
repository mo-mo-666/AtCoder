#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     18/08/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np

n, m, q = map(int, input().split())

mat = np.zeros((n, n), dtype=np.uint32)

for i in range(m):
    l, r = map(int, input().split())
    mat[l-1, r-1] += 1
for i in range(q):
    p, q = map(int, input().split())
    mat2 = mat[p-1:q, p-1:q]
    print(np.sum(mat2))



