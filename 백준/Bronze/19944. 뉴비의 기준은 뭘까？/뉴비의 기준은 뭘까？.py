N, M = map(int, input().split())
if M == 1 or M == 2:
    print('NEWBIE!')
elif N >= M and M != 1 and M != 2:
    print('OLDBIE!')
else:
    print('TLE!')