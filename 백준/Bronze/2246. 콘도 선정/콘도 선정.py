import sys
input = sys.stdin.readline
n = int(input())
lst = []
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])
lst.sort()
mn = 10001
for i in lst:
    temp = i[1]
    if temp < mn:
        mn = temp
        cnt += 1
print(cnt)