n = int(input())
S = input().strip()
for i in range(n):
    if S[i] == 'I':
        print('i', end='')
    else:
        print('L', end='')