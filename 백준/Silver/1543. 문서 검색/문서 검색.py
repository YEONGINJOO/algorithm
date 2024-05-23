a = input()
b = input()
i = 0
cnt = 0
while i < len(a):
    if a[i:i+len(b)] == b:
        cnt += 1
        i += len(b)
    else:
        i += 1
print(cnt)