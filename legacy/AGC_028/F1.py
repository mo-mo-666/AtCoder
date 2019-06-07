#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     13/10/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n = int(input())

puzzle = []

for i in range(n):
    ro = input().split()
    puzzle.append(ro)

ans = 0


for i in range(n):
    for j in range(n):
        if (i == 0 and j == 0) or puzzle[i][j]=='#':
            continue

        ok = puzzle.copy()
        if i + 1 <= n - 1:
            ok[i+1] = [False for _ in range(n)]
            if j != n - 1:
                ok[i][j+1] == True
        for x in range(i, -1, -1):
            for y in range(j, -1, -1):
                if i + 1 <= n - 1:
                    if not ok[i+1][j]:
                        if j != n - 1:
                            if not ok[i][j+1]:
                                ok[i][j] == False
                        else:
                            ok[i][j] == False
                else:
                    if j != n - 1:
                            if not ok[i][j+1]:
                                ok[i][j] == False
                    else:
                        ok[i][j] == False







for i in range(n-1, -1, -1):
    if un[i] == '#':
        for j in range(i, -1, -1):
            un[j] = False
        break

ok[-1] = un


for i in range(n-1, -1, -1):
    if ok[i][-1] == '#':
        for j in range(i, -1, -1):
            un[j] = False
        break






for i in range(n):


