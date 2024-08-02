t = int(input())
for j in range(t):
    n = int(input())
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) > n:
        print(f'{n} is an abundant number.')
    elif sum(arr) < n:
        print(f'{n} is a deficient number.')
    else:
        print(f'{n} is a perfect number.')
    if j != t-1:
        print()