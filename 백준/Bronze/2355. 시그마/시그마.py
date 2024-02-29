a, b = map(int, input().split())
if b > a:
    print((b**2+b+a-a**2)//2)
else:
    print((a ** 2 + a + b - b ** 2) // 2)