#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     23/09/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

s = list(input())
t = list(input())

s_d = {}
t_d = {}

ans = 'Yes'

for i in range(len(s)):
    a = s[i]
    b = t[i]
    if a in s_d.keys() and b in t_d.keys():
        if s_d[a] != t_d[b]:
            ans = 'No'
            break

    elif a in s_d.keys() and b not in t_d.keys():
        ans = 'No'
        break

    elif a not in s_d.keys() and b in t_d.keys():
        ans = 'No'
        break

    else:
        s_d[a] = i
        t_d[b] = i

print(ans)

