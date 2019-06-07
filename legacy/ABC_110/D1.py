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

from math import factorial, sqrt

n, m = map(int, input().split())


ans = 1

if m != 1:
    factorization = {}
    while True:
        for i in range (2, int(sqrt(m))+1):
            if m % i == 0:
                if i in factorization:
                    factorization[i] += 1
                else:
                    factorization[i] = 1
                m = m // i
                break
        else:
            if m in factorization:
                    factorization[m] += 1
            else:
                factorization[m] = 1
            break


    for i in factorization.keys():
        k = factorization[i]

        num = 1
        for i in range(k):
            num *= (n+k-1-i)
        num //= factorial(k)
        ans *= num % (10**9+7)
        ans = ans % (10**9+7)



print(ans)



