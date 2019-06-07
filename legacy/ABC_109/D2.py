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

ex = []
for i in range(h):
    a = list(map(int, input().split()))
    ex_line = []
    for j in range(w):
        if a[j] % 2 != 0:

            ex_line.append((i+1, j+1))


    ex.append(ex_line)
    ex_line = []

p_list = []
noko = []
for ex_line in ex:
    for i in range(0, len(ex_line), 2):
        x1, y1 = ex_line[i]
        x1, y2 = ex_line[i+1]
        n += y2 - y1
        p_list.append(x1, x2, y1, y2)
    if len(ex_line) % 2 != 0:
        noko.append(ex_line[-1])

for i in range(0, len(noko), 2):
    x1, y1 = noko[i]
    x2, y2 = noko[i+1]
    n += abs(x1-x2) + abs(y1-y2)
    if y1 > y2:
        noko.append(x1, y1, x2, y2)
    else:
        noko.append(x2, y2, x1, y1)

p = p_list + noko


print(n)
if n != 0:
    for xy in p:
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

