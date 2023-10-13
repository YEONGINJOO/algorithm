import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    mx = 0
    for i in range(N):
        A, B = map(str, input().split())
        if int(B) > mx:
            mx = int(B)
            ans = A
        else:
            continue
    print(ans)