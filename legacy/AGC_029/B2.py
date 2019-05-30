n = int(input())
a = tuple(map(int, input().split()))

ans = 0
pwtwo = [2**i for i in range(1, 31)]
pn = {}
ok = []
for i in range(n):
    for j in range(i+1, n):
        if (a[i]+a[j]) in pwtwo:
            ok.append((i, j))
            if i in pn:
                pn[i] += 1
            else:
                pn[i] = 1
            if j in pn:
                pn[j] += 1
            else:
                pn[j] = 1
            
while 1 in pn.values():
    i = pn.index(1)
    for j in range(n):
        if i in ok[j]:
            p, q = ok[j]
            pn[p] = 0
            pn[q] = 0
            break
    ans += 1

ans += sum(x >= 2 for x in pn) // 2

print(ans)




