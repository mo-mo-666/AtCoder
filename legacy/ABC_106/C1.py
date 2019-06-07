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

s = list(input())
k = int(input())

big = False

for i in range(len(s)):
    if s[i] != '1':
        big = i
        break

if not big:
    ans = s[0]
elif k <= big:
    ans = 1
else:
    ans = s[big]

print(ans)