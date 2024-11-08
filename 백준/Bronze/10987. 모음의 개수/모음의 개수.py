a = input()
cnt = 0
lst = ['a', 'e', 'i', 'o', 'u']
for i in a:
    if i in lst:
        cnt += 1
print(cnt)