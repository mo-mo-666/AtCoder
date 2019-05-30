n = int(input())
a = tuple(map(int, input().split()))

ans = 0
pwtwo = [2**i for i in range(1, 31)]
pn = [0 for _ in range(n)]
ok = []
for i in range(n):
    for j in range(i+1, n):
        if (a[i]+a[j]) in pwtwo:
            ok.append((i, j))
            pn[i] += 1
            pn[j] += 1
while 1 in pn:
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




