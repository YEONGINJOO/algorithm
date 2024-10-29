import sys
input = sys.stdin.readline
mn, mx = map(int, input().split())
lst = [1] * (mx-mn+1)
for i in range(2, 1000000):
    d = i * i
    x = (mn-1)//d+1
    y = mx//d
    for j in range(x, y+1):
        lst[j*d-mn] = 0
print(sum(lst))