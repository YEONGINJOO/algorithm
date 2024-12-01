from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    a = list(map(int, input().split()))
    if a == [0]:
        break
    b = a[1:]
    c = list(combinations(b, 6))
    for i in c:
        print(*i)
    print()