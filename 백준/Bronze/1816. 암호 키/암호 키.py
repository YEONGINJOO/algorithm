n = int(input())
ans = ''
for i in range(n):
    a = int(input())
    for i in range(2, 1000001):
        if a % i == 0:
            ans = 'NO'
            break
        else:
            ans = 'YES'
    print(ans)