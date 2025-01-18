import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a, b = map(str, input().strip().split())
alp = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 4,
    'F': 3,
    'G': 1,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 2,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 1,
    'X': 2,
    'Y': 2,
    'Z': 1,
}
moonja = ''
if len(a) < len(b):
    for i in range(len(a)):
        moonja += a[i]
        moonja += b[i]
    moonja += b[len(a):]
else:
    for i in range(len(b)):
        moonja += a[i]
        moonja += b[i]
    moonja += a[len(b):]
lst = []
for i in moonja:
    lst.append(alp[i])
while len(lst) > 2:
    temp = []
    for i in range(len(lst)-1):
        if lst[i] + lst[i+1] < 10:
            temp.append(lst[i] + lst[i+1])
        else:
            temp.append((lst[i] + lst[i + 1]) % 10)
    lst = temp
for i in range(2):
    if i == 0 and lst[i] == 0:
        continue
    else:
        print(lst[i], end='')
print('%', end='')