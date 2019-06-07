n = int(input())
list = map(int, input().split())
list2 = sorted(list)
print(list2[n-1]-list2[0])

