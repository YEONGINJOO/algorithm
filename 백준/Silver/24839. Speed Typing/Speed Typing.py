import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    original = input().strip()
    ota = input().strip()
    flag = False
    k = 0
    for j in range(len(original)):
        flag = False
        while k < len(ota):
            if ota[k] == original[j]:
                flag = True
                k += 1
                break
            k += 1
        if flag != True:
            break
    if flag:
        ans = len(ota) - len(original)
    else:
        ans = 'IMPOSSIBLE'
    print(f'Case #{i}: {ans}')
