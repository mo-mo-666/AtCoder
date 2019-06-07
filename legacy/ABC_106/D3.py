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
mat = np.flipud(mat)
matmul = np.cumsum(mat, axis=0)
matmul = np.flipd[matmul]
matmul2 = np.cumsum(matmul, axis=1)

for i in range(q):
    p, q = map(int, input().split())
    ans = matmul2[p-1, q-1]
    print(ans)