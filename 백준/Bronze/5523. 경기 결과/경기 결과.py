n = int(input())
a_cnt = 0
b_cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a_cnt += 1
    elif a < b:
        b_cnt += 1
print(a_cnt, b_cnt)