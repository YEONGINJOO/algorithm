import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = [[i, 0] for i in range(5)]
comb = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
mx_cnt = 0
best_comb = (0, -1)
for c in comb:
    d1, d2 = c
    cnt = 0
    for student in arr:
        if student[d1] == 1 and student[d2] == 1:
            cnt += 1
    if cnt > mx_cnt:
        mx_cnt = cnt
        best_comb = c

result = [0] * 5
result[best_comb[0]] = 1
result[best_comb[1]] = 1
print(mx_cnt)
print(*result)