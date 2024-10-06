import sys
input = sys.stdin.readline
while True:
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        break
    ans1 = 30 * c + 40 * d
    ans2 = 35 * c + 30 * d
    ans3 = 40 * c + 20 * d
    print(min(ans1, ans2, ans3))