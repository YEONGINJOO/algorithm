import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
mx = 0
high = 0
cnt = 0
for i in lst:
    if i > high:
        high = i
        cnt = 0
    else:
        cnt += 1
    if cnt > mx:
        mx = cnt
print(mx)