import sys
input = sys.stdin.readline
N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
a = sum(lst)
print(f'{a/N:.6f}')
if N % 2 != 0:
    print(f'{lst[N//2]:.6f}')
else:
    mean = (lst[N//2] + lst[N//2-1]) / 2
    print(f'{mean:.6f}')