import sys
input = sys.stdin.readline
arr = [input().strip().split() for _ in range(9)]
manda = []
temp = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                temp.append(arr[k + 3 * i][l + 3 * j])
        manda.append(temp)
        temp = []
a = manda[4]
manda.remove(a)
for i in range(8):
    sub = manda[i][4]
    manda[i].remove(sub)
    manda[i].sort()
    manda[i].insert(0, sub)
manda.sort()
x = 1
for i in manda:
    for j in range(9):
        if j == 0:
            print(f'#{x}. {i[j]}')
        else:
            print(f'#{x}-{j}. {i[j]}')
    x += 1