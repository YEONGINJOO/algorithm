import sys
input = sys.stdin.readline
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = input().strip()
b = input().strip()
lst = []
temp = []
for i in range(len(b)):
    if b[i] in alpha:
        temp.append(b[i])
        if len(temp) == len(a):
            lst.append(temp)
            temp = []
if temp != []:
    lst.append(temp)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        c = alpha.index(lst[i][j]) + alpha.index(a[j])
        if c >= 26:
            c -= 26
        lst[i][j] = alpha[c]
for i in range(len(lst)):
    print(''.join(lst[i]), end='')