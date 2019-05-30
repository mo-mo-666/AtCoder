#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mo-mo-
#
# Created:     01/07/2018
# Copyright:   (c) mo-mo- 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from statistics import *

n = int(input())
a = list(map(int, input().split()))

ss = sum(a)
s = ss / 4

b1 = 0
j1 = 0

while b1 < s:
    b1 += a[j1]
    j1 += 1

b3 = 0
j3 = n - 1

while b3 < s:
    b3 += a[j3]
    j3 -= 1

b2 = 0
j2 = j1 + 1

while b2 < 2*s-b1:
    b2 += a[j2]
    j2 += 1


sum1_1 = b1
sum1_2 = b2
sum1_3 = ss - b1 - b2 - b3
sum1_4 = b3

sumlist1 = sorted([sum1_1, sum1_2, sum1_3, sum1_4])
range1 = sumlist1[3] - sumlist1[0]

sum2_1 = sum1_1 - a[j1-1]
sum2_2 = sum1_2 + a[j1-1]
sumlist2 = sorted([sum2_1, sum2_2, sum1_3, sum1_4])
range2 = sumlist2[3] - sumlist2[0]

sum3_3 = sum1_3 + a[j3+1]
sum3_4 = sum1_4 - a[j3+1]
sumlist3 = sorted([sum1_1, sum1_2, sum3_3, sum3_4])
range3 = sumlist3[3] - sumlist3[0]

sumlist4 = sorted([sum2_1, sum2_2, sum3_3, sum3_4])
range4 = sumlist4[3] - sumlist4[0]

sum5_2 = sum1_2 - a[j2-1]
sum5_3 = sum1_3 + a[j2-1]
sumlist5 = sorted([sum1_1, sum5_2, sum5_3, sum1_4])
range5 = sumlist5[3] - sumlist5[0]

sum6_1 = sum1_1 - a[j1-1]
sum6_2 = sum5_2 + a[j1-1]
sumlist6 = sorted([sum6_1, sum6_2, sum5_3, sum1_4])
range6 = sumlist6[3] - sumlist6[0]

sum7_3 = sum5_3 + a[j3+1]
sum7_4 = sum1_4 - a[j3+1]
sumlist7 = sorted([sum1_1, sum5_2, sum7_3, sum7_4])
range7 = sumlist7[3] - sumlist7[0]

sumlist8 = sorted([sum6_1, sum6_2, sum7_3, sum7_4])
range8 = sumlist8[3] - sumlist8[0]

print(min([range1,range2, range3, range4, range5, range6, range7,range8]))









