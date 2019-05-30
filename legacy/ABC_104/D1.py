#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     05/08/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

l = list(input())
n = len(l)
ABC_n = 0
BC_n = 0
C_n = 0
ha_n = 0


def count_inc(car):
    global ABC_n, BC_n, C_n, ha_n
    if car == 'A':
        ABC_n += BC_n
        ABC_n = ABC_n % (10**9 + 7)
    elif car == 'B':
        BC_n += C_n
        BC_n = BC_n % (10**9 + 7)
    elif car == 'C':
        C_n += 3**ha_n
        C_n = C_n % (10**9 + 7)
    else:
        ABC_n = 3*ABC_n +  BC_n
        ABC_n = ABC_n % (10**9 + 7)
        BC_n = 3*BC_n + C_n
        BC_n = BC_n % (10**9 + 7)
        C_n = 3*C_n  + 3**ha_n
        C_n = C_n % (10**9 + 7)
        ha_n += 1

for i in range(n-1, -1, -1):
    count_inc(l[i])
    #print(ABC_n)
    #print(BC_n)
    #print(C_n)

print(ABC_n)


