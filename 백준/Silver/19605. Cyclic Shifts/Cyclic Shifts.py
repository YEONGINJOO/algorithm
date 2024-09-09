import sys
input = sys.stdin.readline
T = input().strip()
S = input().strip()
ans = 'no'
for i in range(len(S)):
    if S in T:
        ans = 'yes'
        break
    S = S[1:] + S[0]
print(ans)