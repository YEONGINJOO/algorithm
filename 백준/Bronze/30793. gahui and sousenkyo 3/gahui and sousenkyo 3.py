p, r = map(int, input().split())
if p/r >= 0.6:
    print('very strong')
elif 0.6 > p/r >= 0.4:
    print('strong')
elif 0.4 > p/r >= 0.2:
    print('normal')
else:
    print('weak')