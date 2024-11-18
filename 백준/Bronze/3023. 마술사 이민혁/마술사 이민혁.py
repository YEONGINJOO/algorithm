import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(r):
    lst = list(input().strip())
    a = lst + lst[::-1]
    b = a.copy()
    arr1.append(a)
    arr2.append(b)
A, B = map(int, input().split())
b = arr1 + arr2[::-1]
if b[A-1][B-1] == '#':
    b[A - 1][B - 1] = '.'
else:
    b[A - 1][B - 1] = '#'
for i in b:
    print(''.join(i))