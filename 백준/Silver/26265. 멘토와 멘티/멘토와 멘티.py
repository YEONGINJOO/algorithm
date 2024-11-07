import sys
input = sys.stdin.readline
n = int(input())
d = {}
for _ in range(n):
    a, b = input().strip().split()
    if a not in d:
        d[a] = [b]
    else:
        d[a].append(b)
dl = sorted(d)
for i in dl:
    a = sorted(d[i], reverse=True)
    for j in a:
        print(i, j)