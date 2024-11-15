import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lamp = [0] * (M+1)
switch = [[]]
lamp[0] = 1
for i in range(N):
    order = list(map(int, input().split()))
    switch.append(order[1:])
    for j in order[1:]:
        lamp[j] += 1
if 0 in lamp:
    print(0)
else:
    for i in switch[1:]:
        for j in i:
            if lamp[j] - 1 == 0:
                break
        else:
            print(1)
            break
    else:
        print(0)