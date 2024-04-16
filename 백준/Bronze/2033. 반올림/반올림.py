n = list(input())
n = n[::-1]
for i in range(len(n)-1):
    if int(n[i]) >= 5:
        n[i+1] = str(int(n[i+1]) + 1)
        n[i] = '0'
    else:
        n[i] = '0'
ans = ''
n = n[::-1]
for i in range(len(n)):
    ans += n[i]
print(ans)