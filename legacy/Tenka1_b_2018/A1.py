a = input()
n = len(a)

if n == 2:
    ans = a
else:
    ans = a[::-1]

print(ans)
