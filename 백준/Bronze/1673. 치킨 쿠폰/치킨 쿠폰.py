import sys
input = sys.stdin.readline
while True:
    try:
        n, k = map(int, input().split())
        cnt = n
        stamp = 0
        while n + stamp >= k:
            order = (n + stamp) // k
            stamp = (n + stamp) % k
            n = order
            cnt += order
        print(cnt)
    except:
        break