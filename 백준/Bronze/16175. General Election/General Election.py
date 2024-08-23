import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    lst = []
    for i in range(n):
        cnt = 0
        for j in range(m):
            cnt += arr[j][i]
        lst.append(cnt)
    print(lst.index(max(lst))+1)