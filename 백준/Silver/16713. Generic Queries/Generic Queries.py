import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
lst = list(map(int, input().split()))

arr = [0] * (N+1)
for i in range(1, N+1):
    arr[i] = arr[i-1]^lst[i-1]
ans = 0
for _ in range(Q):
    s, e = map(int, input().split())
    query = arr[e]^arr[s-1]
    ans ^= query
print(ans)
