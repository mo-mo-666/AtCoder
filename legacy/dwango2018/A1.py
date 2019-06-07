import numpy as np

n = int(input())
l = np.array(list(map(int, input().split())))

m = np.mean(l)
 
dif = abs(l - m)

mini = dif[0]
ans = 0

for i in range(n):
    if dif[i] < mini:
        mini = dif[i]
        ans = i
print(ans)


