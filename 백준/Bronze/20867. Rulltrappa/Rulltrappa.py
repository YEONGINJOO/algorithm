# 63 %
M, S, G = map(int, input().split())
A, B = map(float, input().split())
L, R = map(int, input().split())
#if M/S + L/A < M/G + R/B:
#    print('friskus')
#else:
#    print('latmask')

if M/G + L/A < M/S + R/B:
    print('friskus')
else:
    print('latmask')