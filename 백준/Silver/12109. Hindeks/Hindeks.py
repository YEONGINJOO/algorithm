import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
h = 0
for i in range(1, N+1):
    if lst[N-i] >= i:
        h = i
    else:
        break
print(h)