n = int(input())
a = bin(n)
a = a[2:][::-1]
print(int(a, 2))