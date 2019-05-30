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

vs = list(map(int, input().split()))

v_odd = {}
v_even = {}

for i in range(n):
    if i % 2 == 0:
        v = vs[i]
        if v in v_even:
            v_even[v] += 1
        else:
            v_even[v] = 1
    else:
        v = vs[i]
        if v in v_odd:
            v_odd[v] += 1
        else:
            v_odd[v] = 1

odd_sort = sorted(v_odd.items(), key=lambda x: -x[1])
even_sort = sorted(v_even.items(), key=lambda x: -x[1])

if odd_sort[0][0] == even_sort[0][0]:
    if len(odd_sort) >= 2:
        oddnext = odd_sort[1][1]
        if len(even_sort) >= 2:
            evennext = even_sort[1][1]
            ans = min(n-oddnext-even_sort[0][1], n-odd_sort[0][1]-evennext)
        else:
            ans = min(n-oddnext-even_sort[0][1], n-odd_sort[0][1])
    else:
        if len(even_sort) >= 2:
            evennext = even_sort[1][1]
            ans = min(n-odd_sort[0][1]-evennext, n-even_sort[0][1])
        else:
            ans = n // 2


else:
    ans = n - odd_sort[0][1] - even_sort[0][1]

print(ans)





