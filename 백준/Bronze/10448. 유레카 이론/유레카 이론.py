import sys
input = sys.stdin.readline

lst = []
for i in range(1, 36):
    a = (i * (i+1)) // 2
    lst.append(a)

t = int(input())
for _ in range(t):
    b = int(input())
    ans = 0
    for i in range(35):
        for j in range(35):
            for k in range(35):
                if lst[i] + lst[j] + lst[k] == b:
                    ans = 1
                    break
    print(ans)