import math

n = int(input())

flag = False

if n == 1:
    print('Yes')
    print(2)
    print(1, 1)
    print(1, 1)
    

elif n == 2:
    print('Yes')
    print(2)
    print(2, 1, 2)
    print(2, 1, 2)
    

else:
    for i in range(int(math.sqrt(2*n)+1)):
        if i * (i + 1) == 2 * n:
            k = i
            flag = True
            break
    if flag:
        print('Yes')
        print(k + 1)
        lll = []
        mem = 1
        for j in range(k+1):
            s = []
            
            for l in range(k):
                if l >= j:
                    s.append(mem)
                    mem += 1
                else:
                    s.append(lll[l][j-1])

            lll.append(s)
            print(k, ' '.join(map(str, s)))


    else:
        print('No')

