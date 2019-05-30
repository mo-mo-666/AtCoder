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

coord = []

for i in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))

div = (coord[0][0] + coord[0][1]) % 2

ans = 0

for i in range(1, n):
    x, y = coord[i]
    if (x + y) % 2 != div:
        ans = -1
        break


if ans == -1:
    print(-1)

else:
    if div == 0:
        m = 20

        print(m)
        print(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
        for j in range(n):
            w = 'x'
            x, y = coord[j]
            if x >= 1:
                for i in range(x):
                        w += 'R'
            elif x <= -1:
                for i in range(-x):
                        w += 'L'

            if y >= 1:
                for i in range(y):
                        w += 'U'
            elif y <= -1:
                for i in range(-y):
                        w += 'D'

            r = m - abs(x) - abs(y)
            if r >= 1:
                for i in range(r//2):
                    w += 'LR'

            print(w[1:])

    else:
        m = 19
        print(m)
        print(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

        for j in range(n):
            w = 'x'
            x, y = coord[j]
            if x >= 1:
                for i in range(x):
                        w += 'R'
            elif x <= -1:
                for i in range(-x):
                        w += 'L'

            if y >= 1:
                for i in range(y):
                        w += 'U'
            elif y <= -1:
                for i in range(-y):
                        w += 'D'

            r = m - abs(x) - abs(y)
            if r >= 1:
                for i in range(r//2):
                    w += 'LR'

            print(w[1:])



