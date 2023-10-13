a = input()
cnt = 10
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        cnt += 5
    elif a[i] != a[i+1]:
        cnt += 10
print(cnt)