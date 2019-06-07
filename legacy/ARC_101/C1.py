#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     25/08/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n, k = map(int, input().split())
x = list(map(int, input().split()) )
b = None

for i in range(n):
    if x[i] == 0:
        b = i
        start = True
        break
    elif x[i] > 0:
        b = i
        start = False
        break


if not b:
    m = abs(x[-k])

else:
    if start:
        del x[b]
        k -= 1
        n -= 1

    if k == 0:
        m = 0
    elif k == 1:
        if b-1 >= 0:
            m = min(x[b], abs(x[b-1]))
        else:
            m = x[b]

    else:
        if b >= k:
            m1 = abs(x[b-k])
        else:
            m1 = None

        if b+k-1 <= n-1:
            m2 = abs(x[b+k-1])
        else:
            m2 = None

        m = 2*10**8
        for i in range(1, k):
            if b-i >= 0 and b-i+k-1 < n:
                m = min(2*abs(x[b-i])+abs(x[b-i+k-1]),abs(x[b-i])+2*abs(x[b-i+k-1]), m)

        if m1:
            m = min(m, m1)
        if m2:
            m = min(m, m2)

print(m)









