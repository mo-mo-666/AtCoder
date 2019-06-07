n, d = map(int, input().split())
a = list(map(int, input().split()))

s = 0
a1 = a[0]
a2 = a[-1]
cost1 = [0, 0]
cost1_2 = [0, 0]
cost2 = [n-1, 0]
cost2_2 = [n-1, 0]

for i, v in enumerate(a):
    s += v
    c1 = d * i - v + a1
    
    if c1 <= cost1[1]:
        cost1_2 = cost1.copy()
        cost1 = [i, c1]

ans = s * 2 - a1 - a2 + d * (n-1)

for i , v in enumerate(reversed(a)):
    c2 = d * i - v + a2
    
    if c2 <= cost2[1]:
        cost2_2 = cost2.copy()
        cost2 = [n-1-i, c2]

if cost1[0] == cost2[0]:
    ad = min(cost1_2[1] + cost2[1], cost1[1] + cost2_2[1])
else:
    ad = cost1[1] + cost2[1]

ans = ans + ad

print(ans)



 




