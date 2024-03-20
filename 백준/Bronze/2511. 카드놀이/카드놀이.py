import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_cnt = 0
b_cnt = 0
a_win = 0
for i in range(10):
    if a[i] > b[i]:
        a_cnt += 3
        a_win = 1
    elif a[i] < b[i]:
        b_cnt += 3
        a_win = 0
    else:
        a_cnt += 1
        b_cnt += 1

if a_cnt > b_cnt:
    ans = 'A'
elif b_cnt < a_cnt:
    ans = 'B'
else:
    if a_win == 1:
        ans = 'A'
    else:
        ans = 'B'
if a == b:
    ans = 'D'
print(a_cnt, b_cnt)
print(ans)