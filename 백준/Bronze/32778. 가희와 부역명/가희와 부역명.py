c = input().strip()
if '(' not in c:
    print(c)
    print('-')
else:
    a, b = c.strip().split('(')
    print(a)
    print(b[:-1])