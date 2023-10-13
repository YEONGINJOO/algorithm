import sys
input = sys.stdin.readline
'''
@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자
'''
T = int(input())
for _ in range(T):
    lst = list(map(str, input().split()))
    ans = float(lst[0])
    for i in range(1, len(lst)):
        if lst[i] == '@':
            ans = ans * 3
        elif lst[i] == '#':
            ans = ans - 7
        elif lst[i] == '%':
            ans = ans + 5
    print(f'{ans:.2f}')