import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
d = 1
a = []
for i in range(n):
    d += lst[i] + (i + 1)
    a.append(d)
    d = 1
print(max(a))