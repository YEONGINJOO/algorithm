import sys
input = sys.stdin.readline
N, T = map(int, input().split())
x = y = 0
flag = 1
lst = []
cnt = 0
last = T
for i in range(N):
    a = input().strip().split()
    lst.append([int(a[0]) - cnt, a[1]])
    cnt = int(a[0])
    last = T - cnt

for i in range(N):
    if flag == 1:
        x += lst[i][0]
        if lst[i][1] == 'right':
            flag = -2
        else:
            flag = 2
    elif flag == 2:
        y += lst[i][0]
        if lst[i][1] == 'right':
            flag = 1
        else:
            flag = -1
    elif flag == -1:
        x -= lst[i][0]
        if lst[i][1] == 'right':
            flag = 2
        else:
            flag = -2
    elif flag == -2:
        y -= lst[i][0]
        if lst[i][1] == 'right':
            flag = -1
        else:
            flag = 1

if flag == 1:
    x += last
elif flag == 2:
    y += last
elif flag == -1:
    x -= last
elif flag == -2:
    y -= last
print(x, y)