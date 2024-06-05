import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n - 1, 0, -1):
    mx_idx = lst.index(max(lst[:i+1]))
    if i != mx_idx:
        lst[i], lst[mx_idx] = lst[mx_idx], lst[i]
        cnt += 1
        if cnt == k:
            print(*lst)
            exit()
print(-1)