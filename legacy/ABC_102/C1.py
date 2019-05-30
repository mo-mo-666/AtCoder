from statistics import *


n = int(input())
list = input().split()

for i in range(n):
    list[i] = int(list[i]) - (i + 1)

b = int(median(list))

for i in range(n):
    list[i] = abs(list[i] - b)

print(sum(list))

