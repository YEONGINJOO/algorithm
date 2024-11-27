import sys
input = sys.stdin.readline

def recursion(s, l, r, cnt):
    if l >= r:
        cnt += 1
        return [1, cnt]
    elif s[l] != s[r]:
        cnt += 1
        return [0, cnt]
    else:
        cnt += 1
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

T = int(input())
for _ in range(T):
    S = input().strip()
    print(*isPalindrome(S))