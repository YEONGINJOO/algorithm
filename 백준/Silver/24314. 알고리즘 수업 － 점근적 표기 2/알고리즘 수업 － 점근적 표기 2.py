import sys
input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
flag = 0
for i in range(n0, n0 + 10):
    fn = a1 * i + a0
    gn = c * i
    if gn > fn:
        flag = 0
        break
    else:
        flag = 1
if flag == 0:
    print(0)
else:
    print(1)