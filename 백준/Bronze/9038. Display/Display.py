import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    a = input().strip()
    a_lst = a.split()
    temp = ''
    cnt = 0
    for i in range(len(a_lst)):
        if len(temp) + len(a_lst[i]) > n:
            cnt += 1
            if len(a_lst[i]) < n:
                temp = a_lst[i] + ' '
            else:
                temp = a_lst[i]
        else:
            if len(a_lst[i]) + len(temp) == n:
                temp += a_lst[i]
            else:
                temp += a_lst[i] + ' '
    if temp:
        cnt += 1
    print(cnt)