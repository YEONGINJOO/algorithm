import sys
input = sys.stdin.readline
i = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    ans = 0
    ans += l * (v // p)
    cha = v - p * (v // p)
    if cha > l:
        ans += l
    else:
        ans += cha
    print(f'Case {i}: {ans}')
    i += 1