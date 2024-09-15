import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    n = int(input())
    arr = set()
    st = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    if n == 0:
        print(f'Case #{i+1}: INSOMNIA')
    else:
        j = 1
        while arr != {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
            a = n * j
            str_a = str(a)
            for k in range(len(str_a)):
                if int(str_a[k]) not in arr:
                    arr.add(int(str_a[k]))
            j += 1
        print(f'Case #{i+1}: {a}')