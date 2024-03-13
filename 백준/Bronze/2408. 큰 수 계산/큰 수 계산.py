n = int(input())
ans = ''
for _ in range(2*n-1):
    a = input()
    if a == '/':
        a = '//'
    ans += a
print(eval(ans))