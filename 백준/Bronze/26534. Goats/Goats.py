import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

w_cnt = 0
t_cnt = 0
for i in a:
    for j in b:
        if i == j:
            continue
        t_cnt += 1
        if i > j:
            w_cnt += 1
prob = w_cnt/t_cnt
print(f'{prob:.5f}')