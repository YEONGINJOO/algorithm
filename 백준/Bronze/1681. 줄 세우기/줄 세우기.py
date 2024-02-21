import sys
input = sys.stdin.readline
n, l = map(int, input().split())
cnt = 0
i = 1
ans = 0
while cnt < n:
    if str(l) in str(i):
        pass
    else:
        ans = i
        cnt += 1
    i +=1
print(ans)