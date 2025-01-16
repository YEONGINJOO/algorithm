import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i in range(n):
        for j in range(m-1):
            if arr[j][i] == 1:
                b_cnt = 0
                for k in range(j+1, m):
                    if arr[k][i] == 1:
                        b_cnt += 1
                cnt += m - 1 - j - b_cnt
    print(cnt)