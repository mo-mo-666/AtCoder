from operator import itemgetter

n, m = map(int, input().split())

city_num = [0 for _ in range(n)]
l = []
for i in range(m):
    p, y = map(int, input().split())
    l.append([i, p, y])

l.sort(key=itemgetter(2))

for i in range(m):
    j, p, y = l[i]
    city_num[p-1] += 1
    idz = str(str(p).zfill(6))
    idk = str(str(city_num[p-1]).zfill(6))
    l[i].append(idz+idk)

l.sort(key=itemgetter(0))
for i in range(m):
    print(l[i][-1])



