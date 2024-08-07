import sys
input = sys.stdin.readline

ansdict = {}
while True:
    a = input().strip()
    if a == '0':
        break
    if a not in ansdict:
        ansdict[a] = 1
    else:
        ansdict[a] += 1
cnt = 0
for i in ansdict:
    cnt += ansdict[i]
    print(f'{i}: {ansdict[i]}')
print(f'Grand Total: {cnt}')