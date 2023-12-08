T = int(input())
for _ in range(T):
    n = int(input())
    a = bin(n)
    binary = a[2:]
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            print(i, end=' ')