R, B = map(int, input().split())
L = W = 0
a = R+B
for i in range(1, a):
    if a % i == 0:
        W = i
        L = a // W
        if L >= W:
            if L+W == R/2 + 2:
                break
print(L, W)