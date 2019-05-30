#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     08/09/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from math import gcd

n, x = map(int, input().split())
l = list(map(int, input().split()))
ans = abs(l[0]-x)

for m in l:
    ans = gcd(ans, abs(m-x))

print(ans)

