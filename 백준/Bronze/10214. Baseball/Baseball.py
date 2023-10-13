import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    kr_cnt = 0
    ys_cnt = 0
    for i in range(9):
        Y, K = map(int, input().split())
        ys_cnt += Y
        kr_cnt += K
    if kr_cnt < ys_cnt:
        print('Yonsei')
    else:
        print('Korea')