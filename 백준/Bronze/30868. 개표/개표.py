t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    a = n // 5
    b = n % 5
    for i in range(a):
        lst.append('++++ ')
    for i in range(b):
        lst.append('|')
    for j in lst:
        print(j, end='')
    print()