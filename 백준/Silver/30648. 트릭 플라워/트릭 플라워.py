a, b = map(int, input().split())
r = int(input())
x = a
y = b
cnt = 0
arr = {}
for i in range(r+1):
    for j in range(r-i+1):
        if i == a and j == b:
            arr[(i, j)] = 1
        else:
            arr[(i, j)] = 0

while True:
    if (x+1) + (y+1) >= r:
        x = x // 2
        y = y // 2
    else:
        x = x + 1
        y = y + 1
    arr[(x, y)] += 1
    cnt += 1
    if arr[(x, y)] == 2:
        break
print(cnt)