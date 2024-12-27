n = int(input())
a = input().strip()
flag = 0
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        flag = 1
if flag == 1:
    print('No')
else:
    print('Yes')