import sys
input = sys.stdin.readline

a = input().strip()
ans = ''
for i in a:
    if i == 'U' and ans == '':
        ans += i
    elif i == 'C':
        if ans == 'U':
            ans += i
        elif ans == 'UCP':
            ans += i
            break
    elif i == 'P' and ans == 'UC':
        ans += i
if 'UCPC' in ans:
    print('I love UCPC')
else:
    print('I hate UCPC')