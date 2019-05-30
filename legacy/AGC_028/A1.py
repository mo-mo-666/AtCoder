#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     13/10/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from fractions import gcd

n, m = map(int, input().split())

s = input()
t = input()


l = (n * m) // gcd(n, m)

p = l // n
q = l // m
r = (p * q) // gcd(p, q)

ans = l

for i in range(l//r):
    if s[r//p*i] != t[r//q*i]:
        ans = -1
        break

print(ans)

