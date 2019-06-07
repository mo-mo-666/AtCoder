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


N, M = map(int, input().split())

count = 1
ab = []

for i in range(M):
    ab.append(list(map(int, input().split())))
ab.sort()

a, b = ab[0]

for i in range(1, M):
    a_new, b_new = ab[i]

    if b <= a_new:
        a, b = a_new, b_new
        count += 1

    elif  b_new <= b:
        a, b = a_new, b_new

    else:
        a = a_new

print(count)




