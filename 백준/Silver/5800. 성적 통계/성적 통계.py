import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    n, *a = map(int, input().split())
    a.sort()
    mx = 0
    for j in range(n-1):
        temp = a[j+1] - a[j]
        if temp > mx:
            mx = temp
    print(f'Class {i}')
    print(f'Max {max(a)}, Min {min(a)}, Largest gap {mx}')