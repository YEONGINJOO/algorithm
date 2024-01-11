N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    bin_a = bin(a)
    fin_a = bin_a[2:]
    cnt = 0
    for i in fin_a:
        if i == '1':
            cnt += 1
    if cnt % 2 == 0 and b == 0:
        print('Valid')
    elif cnt % 2 == 0 and b == 1:
        print('Corrupt')
    elif cnt % 2 != 0 and b == 1:
        print('Valid')
    else:
        print('Corrupt')