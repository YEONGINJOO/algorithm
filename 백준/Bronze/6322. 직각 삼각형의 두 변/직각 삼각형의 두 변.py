import sys
input = sys.stdin.readline

i = 1
while True:
    ans = ''
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a == -1:
        if b >= c:
            ans = 'Impossible.'
        else:
            a = (c ** 2 - b ** 2) ** (1/2)
            ans = f'a = {a:.3f}'
    if b == -1:
        if a >= c:
            ans = 'Impossible.'
        else:
            b = (c ** 2 - a ** 2) ** (1 / 2)
            ans = f'b = {b:.3f}'
    if c == -1:
        c = (a ** 2 + b ** 2) ** (1/2)
        ans = f'c = {c:.3f}'
    print(f'Triangle #{i}')
    print(ans)
    print()
    i += 1