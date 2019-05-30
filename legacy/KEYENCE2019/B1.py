s = input()
 
n = len(s)
nozoku = n - 7

ans = 'NO'

if nozoku == 0:
    if s == 'keyence':
        ans = 'YES'
else:
    
    for i in range(8):
        if s[:i] + s[i+nozoku:] == 'keyence':
            ans = 'YES'
            break
   
    
print(ans) 