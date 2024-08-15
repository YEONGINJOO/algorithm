import sys
input = sys.stdin.readline

n, m = map(int, input().split())
narr = list(map(int, input().split()))
marr = list(map(int, input().split()))

if m > n:
    for i in range(m-n):
        narr.append(0)
mx = 0
for i in range(m):
    if marr[i] - narr[i] > mx:
        mx = marr[i] - narr[i]
print(mx)