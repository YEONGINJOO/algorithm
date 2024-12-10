import sys
input = sys.stdin.readline

tc = 0
lc = 0
for _ in range(9):
    s = input().strip()
    if s == 'Tiger':
        tc += 1
    else:
        lc += 1
if tc > lc:
    print('Tiger')
else:
    print('Lion')