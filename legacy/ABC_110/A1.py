#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     23/09/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a = list(map(int, input().split()))

a.sort()

ans = a[2]*10 + a[1] + a[0]

print(ans)

