import numpy as np


n, k = map(int, input().split())
a = tuple(map(int, input().split()))

s = [0]
x = 0
for i in range(n):
    x += a[i]
    s.append(x)
    


s_bin = []

for i in range(n):
    for j in range(i+1, n+1):
        cache  = s[j] - s[i]
        mozi = []
        for i in range(30):
            r = cache % 2
            mozi.append(r)
            cache = cache // 2
    

        s_bin.append(reversed(mozi))


s_bin = np.array(s_bin)
kakui = np.sum(s_bin, axis=0)  

ans = 0

for i in range(0, 30):
    if kakui[i] >= k:
        ans += 2**(29-i)
        s_bin = s_bin[s_bin[:, i] == 1]
        kakui = np.sum(s_bin, axis=0)
        
print(ans)

