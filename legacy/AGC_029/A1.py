s = input()
s = s[::-1]
ans = 0
b = 0
for i in range(len(s)):
    if s[i] == "B":
        ans += i
        ans -= b
        b += 1
print(ans)
