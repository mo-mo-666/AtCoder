#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     07/07/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------



n, m, d = input().split()
n = int(n)
m = int(m)
d = int(d)

if d == 0:
    x = n
    if n == 1:
        result = m - 1
    else:
        result = x*(m-1)*n**(m-2)/n**m


else:
    x = 2*(n - d)

    result = x*(m-1)*n**(m-2)/n**m

print(result)