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

a = int(input())

if a < 1200:
    ans = 'ABC'
elif a < 2800:
    ans = 'ARC'
else:
    ans = 'AGC'

print(ans)