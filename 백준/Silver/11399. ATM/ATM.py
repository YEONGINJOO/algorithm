import sys
input = sys.stdin.readline


n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0
for i in range(n):
    for j in range(i+1):
        cnt += lst[j]
print(cnt)