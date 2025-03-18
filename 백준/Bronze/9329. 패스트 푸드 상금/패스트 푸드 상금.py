import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    prize = 0
    n_lst = [list(map(int, input().split())) for _ in range(n)]
    m_lst = list(map(int, input().split()))
    for i in range(n):
        k = n_lst[i][1:n_lst[i][0]+1]
        arr = []
        for j in range(len(k)):
            arr.append(m_lst[k[j]-1])
        prize += min(arr) * n_lst[i][-1]

    print(prize)