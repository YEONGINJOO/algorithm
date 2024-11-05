a = input()
pi_c = a.count('pi')
ka_c = a.count('ka')
chu_c = a.count('chu')
if len(a) == (pi_c*2) + (ka_c*2) + (chu_c*3):
    print('YES')
else:
    print('NO')
