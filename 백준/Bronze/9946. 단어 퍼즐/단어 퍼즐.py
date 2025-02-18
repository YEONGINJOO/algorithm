import sys
input = sys.stdin.readline
i = 1
while True:
    a = input().strip()
    b = input().strip()
    if a == 'END' and b == 'END':
        break
    if sorted(a) == sorted(b):
        print(f'Case {i}: same')
    else:
        print(f'Case {i}: different')
    i += 1