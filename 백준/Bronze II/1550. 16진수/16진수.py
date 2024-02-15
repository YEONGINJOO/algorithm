a = input()
ans = 0
for i in range(len(a)):
    if a[i] == 'A':
        ans += 10 * (16 ** (len(a)-1-i))
    elif a[i] == 'B':
        ans += 11 * (16 ** (len(a)-1-i))
    elif a[i] == 'C':
        ans += 12 * (16 ** (len(a)-1-i))
    elif a[i] == 'D':
        ans += 13 * (16 ** (len(a)-1-i))
    elif a[i] == 'E':
        ans += 14 * (16 ** (len(a)-1-i))
    elif a[i] == 'F':
        ans += 15 * (16 ** (len(a)-1-i))
    else:
        ans += int(a[i]) * (16 ** (len(a)-1-i))
print(ans)