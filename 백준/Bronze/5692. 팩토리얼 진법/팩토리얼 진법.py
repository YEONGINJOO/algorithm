import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    a = n // 10000
    b = (n - a * 10000) // 1000
    c = (n - a * 10000 - b * 1000) // 100
    d = (n - a * 10000 - b * 1000 - c * 100) // 10
    e = (n - a * 10000 - b * 1000 - c * 100 - d * 10)

    ans = 120 * a + 24 * b + 6 * c + 2 * d + e
    print(ans)