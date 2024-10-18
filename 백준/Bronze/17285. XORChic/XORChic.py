T = input()
key = ord(T[0]) ^ ord('C')
ans = ''
for i in T:
    ans += chr(ord(i) ^ key)
print(ans)