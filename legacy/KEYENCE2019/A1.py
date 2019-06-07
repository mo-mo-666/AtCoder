n = list(map(int, input().split()))

ans = 'NO'
if 1 in n and 9 in n and 7 in n and 4 in n:
    ans = 'YES'

print(ans)