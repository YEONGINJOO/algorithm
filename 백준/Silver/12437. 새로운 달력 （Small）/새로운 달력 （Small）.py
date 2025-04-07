import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    ans = 0
    m, md, wd = map(int, input().split())
    arr = []
    idx = 0
    for a in range(m):
        temp = []
        for k in range(1, md+1):
            if idx:
                for e in range(idx):
                    temp.append(0)
                idx = 0
            temp.append(k)
            if len(temp) == wd:
                arr.append(temp)
                temp = []
            elif k == md:
                b = len(temp)
                if b != wd:
                    for j in range(wd-b):
                        temp.append(0)
                    arr.append(temp)
                    idx = b
                elif b == 0:
                    continue
    ans = len(arr)
    print(f'Case #{i+1}: {ans}')