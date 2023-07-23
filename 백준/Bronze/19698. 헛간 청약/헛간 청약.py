N, W, H, L = map(int, input().split())
w = W // L
h = H // L

cnt = w*h
if N < cnt:
    ans = N
else:
    ans = cnt
print(ans)