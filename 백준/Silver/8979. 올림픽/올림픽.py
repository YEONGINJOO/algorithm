n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
lst = sorted(lst, key=lambda x: (x[1], x[2], x[3]), reverse=True)
idx = [lst[i][0] for i in range(n)].index(k)
for i in range(n):
    if lst[idx][1:] == lst[i][1:]:
        print(i+1)
        break