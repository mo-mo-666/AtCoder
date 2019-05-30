#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     01/09/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def all_path(n):
    if n == 2:
        print(1, 2, 0)
    else:
        print(1, n, 2**(n-2)-1)
        for i in range(2, n-1):
            print(i, n, 2**(n-2)-2**(i-2)-1)
        print(n-1, n, 0)
        all_path(n-1)

l = int(input())

l_bi = list(bin(l-1))
l_bi = l_bi[2:]

length = len(l_bi) + 1
print(length+1)
all_path(length)

for i in range(length):
    if l_bi[i] == '1' and i == length-1:
        print(1, length+1, 2**(length-2)-1)

    elif l_bi[i] == '1':
        print(length-i ,length+1, 2**(length-1)-2**(length-i-2)-1)

