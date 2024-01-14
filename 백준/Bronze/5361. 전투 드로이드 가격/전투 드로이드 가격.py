n = int(input())
for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    blaster = 350.34
    sigak = 230.90
    chunggak = 190.55
    arms = 125.30
    legs = 180.90
    cost = a * blaster + b *sigak + c*chunggak + d*arms + e*legs
    print(f'${cost:.2f}')