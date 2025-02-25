import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x = input()
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))
    if max(N_lst) >= max(M_lst):
        print('S')
    else:
        print('B')