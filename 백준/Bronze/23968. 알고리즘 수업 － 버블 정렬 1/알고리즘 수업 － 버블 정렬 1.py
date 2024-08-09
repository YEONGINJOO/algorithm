import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
ans = []
for i in range(n, 1, -1):
    for j in range(0, i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            cnt += 1
        if cnt == k:
            ans.append(lst[j])
            ans.append(lst[j+1])
            break
    if ans:
        break
if ans:
    print(*ans)
else:
    print(-1)