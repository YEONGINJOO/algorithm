import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = input().strip()
lst = [input().strip() for _ in range(m)]
for i in range(m):
    ans = 'false'
    s = len(a)
    s_idx = 0
    for j in range(len(lst[i])):
        if s_idx < s and lst[i][j] == a[s_idx]:
            s_idx += 1
        if s_idx == s:
            break
    if s_idx == s:
        ans = 'true'
    print(ans)
