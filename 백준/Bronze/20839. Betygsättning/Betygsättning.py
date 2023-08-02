x, y, z = map(int, input().split())
x1, y1, z1 = map(int, input().split())

if x == x1 and y == y1 and z == z1:
    print('A')
elif y == y1 and z == z1 and x/2 <= x1 < x:
    print('B')
elif y == y1 and z == z1:
    print('C')
elif z == z1 and y/2 <= y1 < y:
    print('D')
else:
    print('E')