n = int(input())
binn = bin(n)[2:][::-1]
ans = 0
for i in range(len(binn)):
    ans += 3 ** i * int(binn[i])
print(ans)