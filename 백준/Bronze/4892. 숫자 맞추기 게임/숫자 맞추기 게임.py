i = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = n0 * 3
    if n1 % 2 == 0:
        ans = 'even'
        n4 = n0 // 2
        print(f'{i}. {ans} {n4}')
    else:
        ans = 'odd'
        n4 = (n0 -1)// 2
        print(f'{i}. {ans} {n4}')
    i += 1