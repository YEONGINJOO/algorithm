N = int(input())
print(N * (N-1) // 2)
num = 1
for _ in range(N):
    print(num, end=' ')
    num *= 2
print()
print(N-1)
num = 1
for _ in range(N):
    print(num, end=' ')
    num += 1