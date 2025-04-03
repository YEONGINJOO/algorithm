import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
j_cnt = 0
h_cnt = 0
for i in lst:
    if i % 2 == 0:
        j_cnt += 1
    else:
        h_cnt += 1
if j_cnt > h_cnt:
    print('Happy')
else:
    print('Sad')