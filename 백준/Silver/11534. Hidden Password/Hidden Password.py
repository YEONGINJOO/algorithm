from collections import deque

p, s = input().split()
p = deque(p)
flag = 1
for c in s:
    if len(p) == 0:
        break
    if c != p[0] and c in p:
        flag = 0
        break
    if c == p[0]:
        p.popleft()

if len(p) != 0:
    flag = 0

if flag:
    print('PASS')
else:
    print('FAIL')