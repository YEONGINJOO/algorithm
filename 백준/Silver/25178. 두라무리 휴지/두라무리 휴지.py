import sys
input = sys.stdin.readline

n = int(input())
a = input().strip()
b = input().strip()
v = 'aeiou'
flag = 0
asort = sorted(a)
bsort = sorted(b)
lst = []
if asort == bsort:
    flag = 1
else:
    flag = 0
lst.append(flag)
if a[0] == b[0] and a[-1] == b[-1]:
    flag = 1
else:
    flag = 0
lst.append(flag)
tempa = ''
tempb = ''
for i in range(n):
    if a[i] not in v:
        tempa += a[i]
    if b[i] not in v:
        tempb += b[i]
if tempa == tempb:
    flag = 1
else:
    flag = 0
lst.append(flag)
if 0 in lst:
    print('NO')
else:
    print('YES')