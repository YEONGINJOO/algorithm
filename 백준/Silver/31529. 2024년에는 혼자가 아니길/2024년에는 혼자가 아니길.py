X, Y = map(int, input().split())
if X > Y:
    print(-1)
elif Y >= 3 * X:
    print(-1)
else:
    W = (2 * X - Y) / 4
    print(int(2024*W))