n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
s = []
negative = 0
for i, j in zip(a, b):
    s.append(i - j)
    if i - j < 0:
        negative += i - j
        ans += 1

s.sort(reverse=True)

if ans != 0:
    if sum(s) < 0:
        ans = -1
    else:
        for i , p in enumerate(s):
            negative += p
            if negative >= 0:
                ans += i + 1
                break
    

print(ans)


