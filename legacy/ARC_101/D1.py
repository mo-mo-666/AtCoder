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

import statistics as st

n = int(input())
a = list(map(int, input().split()))
big = {}
for i in range(n):
    if a[i] in big.keys():
        big[a[i]] += 1
    else:
        big[a[i]] = 1

s = sorted(big.keys())

for i in range(1, n):
    for j in range(1, i):
        big[st.median_high(a[i-j:i])] += 1

count = 0
m = sum(big.values())
for i in s:
    if count < m // + 1 :
        count += big[i]
        ans = i
    else:
        break

print(ans)


