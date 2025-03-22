import math
import sys
input = sys.stdin.readline

N, R = map(int, input().split())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])

mx = 0
anx, any = 0, 0
xy_set = set()

for x, y in arr:
    for dx in range(-R, R+1):
        dy = int(math.sqrt(R**2 - dx**2))
        xy_set.add((x+dx, y+dy))
        xy_set.add((x+dx, y-dy))

for cx, cy in xy_set:
    cnt = 0
    for x, y in arr:
        if (cx-x)**2 + (cy-y)**2 <= R**2:
            cnt += 1
    if cnt > mx:
        mx = cnt
        anx, any = cx, cy

print(anx, any)