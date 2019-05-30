import numpy as np

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
h = np.array(h)

dift = abs((t - h * 0.006) - a)

ans = np.argmin(dift) + 1

print(ans)


