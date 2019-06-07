import numpy as np

h, w = map(int, input().split())
l = [ list(input()) for _ in range(h)]
print(l)
l = np.array(l)
l = np.array(l == '#')
black = np.where(l)


def go(i, j, kouho):
    cache = []

    if i - 1 >= 0:
        if not l[i-1][j]:
            kouho.add((i-1, j))
            if i - 2 >= 0 and  l[i-2][j]:
                kouho.union(go(i-2, j, kouho))
            if j - 1 >= 0 and  l[i-1][j-1]:
                kouho.union(go(i-1, j-1, kouho))
                cache.add(i-1, j-1)
            if j + 1 <= w-1 and  l[i-1][j+1]:
                kouho.union(go(i-1, j+1, kouho))
                cache.add(i-1, j+1)
                  
    if i + 1 <= h-1:
        if not l[i+1][j]:
            kouho.add((i+1, j))
            if i + 2 <= h-1 and  l[i+2][j]:
                kouho.union(go(i-2, j, kouho))
            if j - 1 >= 0 and  l[i+1][j-1]:
                kouho.union(go(i+1, j-1, kouho))
                cache.add(i+1, j-1)
            if j + 1 <= w-1 and  l[i+1][j+1]:
                kouho.union(go(i+1, j+1, kouho))
                cache.add(i+1, j+1)

    if j - 1 >= 0:
        if not l[i][j-1]:
            kouho.add((i, j-1))
            if j - 2 >= 0 and  l[i][j-2]:
                kouho.union(go(i, j-2, kouho))
            if not (i-1, j-1) in cache and i - 1 >= 0 and  l[i-1][j-1]:
                kouho.union(go(i-1, j-1, kouho))
               
            if not (i+1, j-1) in cache and i + 1 <= h-1 and  l[i+1][j-1]:
                kouho.union(go(i+1, j-1, kouho))
               
    if j + 1 <= w-1:
        if not l[i][j+1]:
            kouho.add((i, j+1)) 
            if j + 2 <= w-1 and  l[i][j+2]:
                kouho.union(go(i, j+2, kouho))
            if not (i-1, j+1) in cache and i - 1 >= 0 and  l[i-1][j+1]:
                kouho.union(go(i-1, j+1, kouho))
                
            if not (i+1, j+1) in cache and i + 1 <= h-1 and  l[i+1][j+1]:
                kouho.union(go(i+1, j+1, kouho))

    return kouho

ans = 0
print(black)
for i, j in black:
    ans += len(go(i, j, set()))

print(ans)

