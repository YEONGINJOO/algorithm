import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d, e = map(int, input().split())

A = a * d * (d - 1)
B = 2 * a * d * e
C = a * e**2 + b * e + c - d * c - e

# 판별식 계산
discriminant = B**2 - 4 * A * C

if A == 0:
    if B == 0:
        if C == 0:
            print("Nice")  # 모든 x에서 만난다.
        else:
            print("Head on")  # 만나지 않는다.
    else:
        print("Remember my character")  # 1개의 해
else:
    if discriminant > 0:
        print("Go ahead")  # 2개의 해
    elif discriminant == 0:
        print("Remember my character")  # 1개의 해
    else:
        print("Head on")  # 해가 없다.