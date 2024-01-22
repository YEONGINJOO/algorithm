def facto(a):
    if a == 1:
        return 1
    return a * facto(a-1)

while True:
    n = input()
    if n == '0':
        break
    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * facto(len(n)-i)
    print(ans)