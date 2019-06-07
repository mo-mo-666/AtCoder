#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     29/09/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

l = list(input())

for i in range(len(l)):
    if l[i] == '1':
        l[i] = '9'
    else:
        l[i] = '1'

ans = l[0] + l[1] + l[2]
print(ans)

