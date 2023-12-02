N, W, H = map(int, input().split())
for i in range(N):
    a = int(input())
    if a < W or a < H:
        print('DA')
    elif a <= (W**2 + H**2)**(1/2):
        print('DA')
    else:
        print('NE')