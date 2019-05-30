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

ans = sum(pn) // 2
de = [x >= 2 for x in pn]
while sum(de) >= 1:
    if 1 in pn:
        i = de.index(1)
            for j in range(n):
                if i in ok[j]:
                    p, q = ok[j]
                    if pn[p] == 1 or pn[q] == 1:
                        pn[p] = pn[q] = 0
                        ans -= 1
                        break
                    else:

        ans += 1
    else:
        ans += sum(x >= 2 for x in pn) // 2
        break

        de = [x >= 2 for x in pn]

ans += sum(x >= 1 for x in pn) // 2

print(ans)




