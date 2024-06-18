import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
mx = 0
for i in range(1, n-1):
    sm = 0
    if lst[i-1] > lst[i+1]:
        sm += lst[i] + lst[i+1]
    else:
        sm += lst[i] + lst[i-1]
    if sm > mx:
        mx = sm
print(max(mx, lst[0], lst[-1]))