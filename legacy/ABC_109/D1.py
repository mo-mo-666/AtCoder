#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     08/09/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


n = 0


h, w = map(int, input().split())

ex_kali = []
ex = []
for i in range(h):
    a = list(map(int, input().split()))
    for j in range(w):
        if a[j] % 2 != 0:

            ex_kali.append((i+1, j+1))
            if len(ex_kali) == 2:

                one, two = ex_kali
                x1, y1 = one
                x2, y2 = two
                n += abs(x1-x2) + abs(y1-y2)
                ex.append((x1, y1, x2, y2))
                ex_kali = []


print(n)
if n != 0:
    for xy in ex:
        x1, y1, x2, y2 = xy
        if not x1 == x2:
            for i in range(x2-x1):
                print(x1+i, y1, x1+i+1, y1)


        if y1 < y2 :
            for i in range(y2-y1):
                print(x2, y1+i, x2, y1+i+1)
        elif y1 > y2:
            for i in range(y1-y2):
                print(x2, y1-i, x2, y1-i-1)

