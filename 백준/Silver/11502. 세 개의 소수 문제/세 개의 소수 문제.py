import sys
input = sys.stdin.readline

n = 1000
a = [False,False] + [True]*(n-1)
primes = []
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

t = int(input())
for _ in range(t):
    k = int(input())
    bp = False
    ans = []
    for i in primes:
        for j in primes:
            for l in primes:
                if i + j + l == k:
                    ans.append(str(i))
                    ans.append(str(j))
                    ans.append(str(l))
                    bp = True
                    break
            if bp:
                break
        if bp:
            break
    if ans != []:
        print(*ans)
    else:
        print(0)