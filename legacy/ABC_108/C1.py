#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     01/09/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n, k = map(int, input().split())

f = n // k
ans = f**3

if k % 2 == 0:
    g = (n - k//2) // k + 1
    ans += g**3

print(ans)

