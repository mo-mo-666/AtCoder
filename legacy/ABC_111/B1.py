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

n = int(input())

l = [111 * i for i in range(1, 10)]

for num in l:
    if n > num:
        continue
    else:
        ans = num
        break
print(ans)