import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        ans = 'yes'
    else:
        ans = 'no'
    print(f'Scenario #{i}:')
    print(ans)
    print()