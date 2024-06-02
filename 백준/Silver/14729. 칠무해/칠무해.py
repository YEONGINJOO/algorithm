import sys
input = sys.stdin.readline

n = int(input())
lst = [float(sys.stdin.readline().strip()) for _ in range(n)]
lst.sort()
for i in range(7):
    print(f'{lst[i]:.3f}')