import sys
input = sys.stdin.readline

n = int(input())
ace = list(map(int, input().split()))
newyork = list(map(int, input().split()))
ace_cnt = 0
newyork_cnt = 0
# ace = -1 new = 1
flag = 0
mx = 0
for i in range(n):
    if ace[i] == 1 and newyork[i] == 2:
        if flag == -1:
            ace_cnt = 0
        newyork_cnt += 1
        flag = 1
    elif ace[i] == 1 and newyork[i] == 3:
        if flag == 1:
            newyork_cnt = 0
        ace_cnt += 1
        flag = -1
    elif ace[i] == 2 and newyork[i] == 1:
        if flag == 1:
            newyork_cnt = 0
        ace_cnt += 1
        flag = -1
    elif ace[i] == 2 and newyork[i] == 3:
        if flag == -1:
            ace_cnt = 0
        newyork_cnt += 1
        flag = 1
    elif ace[i] == 3 and newyork[i] == 1:
        if flag == -1:
            ace_cnt = 0
        newyork_cnt += 1
        flag = 1
    elif ace[i] == 3 and newyork[i] == 2:
        if flag == 1:
            newyork_cnt = 0
        ace_cnt += 1
        flag = -1
    elif ace[i] == newyork[i] and flag == -1:
        ace_cnt = 0
        newyork_cnt += 1
        flag = 1
    elif ace[i] == newyork[i] and flag == 1:
        newyork_cnt = 0
        ace_cnt += 1
        flag = -1
    if mx < max(newyork_cnt, ace_cnt):
        mx = max(newyork_cnt, ace_cnt)
print(mx)