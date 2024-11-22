import sys
input = sys.stdin.readline

n = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(n):
    lst = list(map(int, input().split()))
    ans = ''
    for i in range(len(lst)):
        try:
            if chr(lst[i]) in alpha:
                ans += chr(lst[i]).lower()
            else:
                ans += '-'
        except ValueError:
            ans += '-'
    print(ans[1:]+ans[0]+'ay')