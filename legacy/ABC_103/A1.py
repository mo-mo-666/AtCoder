#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     21/07/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a, b, c = map(int, input().split())


M = max(a, b, c)
m = min(a, b, c)
print(M - m)