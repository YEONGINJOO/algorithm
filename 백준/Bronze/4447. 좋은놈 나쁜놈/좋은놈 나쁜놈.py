import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    adict = {'g': 0, 'b': 0}
    a = input().strip()
    b = a.lower()
    for i in range(len(b)):
        if b[i] in adict:
            adict[b[i]] += 1
    if adict['g'] > adict['b']:
        print(f'{a} is GOOD')
    elif adict['g'] < adict['b']:
        print(f'{a} is A BADDY')
    else:
        print(f'{a} is NEUTRAL')