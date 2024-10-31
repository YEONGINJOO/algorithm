import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a_lst = input().strip().split()
    b_lst = input().strip().split()
    a_lst.sort()
    b_lst.sort()
    if a_lst == b_lst:
        print('NOT CHEATER')
    else:
        print('CHEATER')