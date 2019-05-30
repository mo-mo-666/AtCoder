import numpy as np

h, w, k = map(int, input().split())

if w == 1:
    print(1)
    
elif w == 2:
    a = (1, 1)
    b = (1, 1)
    nex = [a, b]
elif w == 3:
    a = (2, 1, 0)
    b = (1, 1, 1)
    c = (0, 1, 2)
    nex = [a, b, c]
elif w == 4:
    a = (3, 2, 0, 0)
    b = (2, 2, 1, 0)
    c = tuple(reversed(b))
    d = tuple(reversed(a))
    nex = [a, b, c, d]
elif w == 5:
    a = (5, 3, 0, 0, 0)
    b = (3, 3, 2, 0, 0)
    c = (0, 2, 4, 2, 0)
    d = tuple(reversed(b))
    e = tuple(reversed(a))
    nex = [a, b, c, d, e]
elif w == 6:
    a = (8, 5, 0, 0, 0, 0)
    b = (5, 5, 3, 0, 0, 0)
    c = (0, 3, 6, 4, 0, 0)
    d = tuple(reversed(c))
    e = tuple(reversed(b))
    f = tuple(reversed(a))
    nex = [a, b, c, d, e, f]
elif w == 7:
    a = (13, 8, 0, 0, 0, 0, 0)
    b = (8, 8, 5, 0, 0, 0, 0)
    c = (0, 5, 10, 4, 0, 0, 0)
    d = (0, 0, 4, 6, 4, 0, 0)
    e = tuple(reversed(c))
    f = tuple(reversed(b))
    g = tuple(reversed(a))
    nex = [a, b, c, d, e, f, g]
else:
    a = (21, 13, 0, 0, 0, 0, 0, 0)
    b = (13, 13, 8, 0, 0, 0, 0, 0)
    c = (0, 8, 16, 10, 0, 0, 0, 0)
    d = (0, 0, 10, 15, 9, 0, 0, 0)
    e = tuple(reversed(d))
    f = tuple(reversed(c))
    g = tuple(reversed(b))
    h1 = tuple(reversed(a))
    nex = [a, b, c, d, e, f, g, h1]

if w != 1:
    nex = np.array(nex)
    num = [0 for _ in range(w)]
    num[0] = 1
    num = np.array(num)
    cache = np.array([0 for _ in range(w)])

    for i in range(h):
        for j in range(w):
            cache[j] = np.dot(nex[j], num) % 1000000007
        num = cache

    print(num[k-1])