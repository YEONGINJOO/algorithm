import sys
input = sys.stdin.readline

a, b = map(int, input().split())
lst = []
for i in range(1, 100):
    if len(lst) == 1001:
        break
    for j in range(i):
        lst.append(i)
        if len(lst) == 1001:
            break
print(sum(lst[a-1:b]))