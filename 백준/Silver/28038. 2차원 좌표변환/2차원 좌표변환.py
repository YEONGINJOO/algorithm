import math

t = int(input())
for _ in range(t):
    n = int(input())
    a, b = map(float, input().split())
    if n == 1:  # 직교좌표계 (x, y)
        r = math.sqrt(a ** 2 + b ** 2)
        theta = math.atan2(b, a)
        if theta < 0:  # θ가 음수인 경우 2π를 더하여 양수로 변환
            theta += 2 * math.pi
        print(f'{r:.8f} {theta:.8f}')
    else:  # 극좌표계 (r, θ)
        r = a
        theta = b
        if r == 0:
            x = 0
            y = 0
        else:
            x = r * math.cos(theta)
            y = r * math.sin(theta)
        print(f'{x:.8f} {y:.8f}')