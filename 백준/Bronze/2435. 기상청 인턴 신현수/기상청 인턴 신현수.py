import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = list(map(int, input().split()))
mx = -987654321
for i in range(n-k+1):
    sm = sum(lst[i:i+k])
    if sm > mx:
        mx = sm
print(mx)