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

n = int(input())

if n < 105:
    ans = 0
elif n < 135:
    ans = 1
elif n < 189:
    ans = 2
else:
    ans = 3

print(ans)