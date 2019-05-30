import numpy as np

n = int(input())
a, b = map(int, input().split())
p = np.array(list(map(int, input().split())))

AA = np.sum(p <= a)
BB = np.sum(p <= b) - AA
CC = n - AA - BB

print(min(AA, BB, CC)) 