import sys
input = sys.stdin.readline

while True:
    a = int(input())
    if a == -1:
        break
    ba = bin(a)[2:]
    if len(ba) < 32:
        ba = '0' * (32-len(ba)) + ba
    ba = ba[::-1]
    ans = int(ba, 2)
    print(ans)