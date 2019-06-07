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

N, M, X, Y = map(int, input().split())

x_l = list(map(int, input().split()))
y_l = list(map(int, input().split()))

xm = max(x_l)
ym = min(y_l)

ans = 'No War'

if xm >= ym:
    ans = 'War'

elif xm >= Y:
    ans = 'War'

elif X >= ym:
    ans = 'War'

elif X >= Y:
    ans = 'War'

print(ans)


