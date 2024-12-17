import sys
input = sys.stdin.readline
m, n = map(int, input().split())
numdict = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
}
arr = []
for i in range(m, n+1):
    a = str(i)
    temp = ''
    for j in a:
        temp += numdict[j]
    arr.append([i, temp])
arr.sort(key=lambda x:(x[1], x[0]))
for k in range(len(arr)):
    if k % 10 == 9:
        print(arr[k][0])
    else:
        print(arr[k][0], end= ' ')