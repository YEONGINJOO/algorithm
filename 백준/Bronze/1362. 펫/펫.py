i = 1
while True:
    o, w = map(int, input().split())
    ans = ''
    if o == 0 and w == 0:
        break
    dead = 0
    while True:
        a, b = map(str, input().split())
        if a == '#' and b == '0':
            break
        if a == 'E':
            w -= int(b)
            if w <= 0:
                dead = 1
        elif a == 'F':
            w += int(b)
    if w <= 0 or dead == 1:
        ans = 'RIP'
    elif w > o * 0.5 and w < 2 * o:
        ans = ':-)'
    else:
        ans = ':-('
    print(f'{i} {ans}')
    i += 1