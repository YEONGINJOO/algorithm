import sys
input = sys.stdin.readline

mos_dict = {}
for _ in range(26):
    a, b = input().strip().split()
    mos_dict[a] = b
N = int(input())
word_lst = [input().strip() for _ in range(N)]
word_dict = {}
for i in range(N):
    temp = ''
    for j in word_lst[i]:
        temp += mos_dict[j]
    word_dict[temp] = word_lst[i]
while True:
    t = int(input())
    if t == 0:
        break
    arr = []
    flag = 1
    lst = [input().strip() for _ in range(t)]
    for i in range(t):
        if lst[i] not in word_dict:
            flag = 0
            arr = lst[i]
            break
        else:
            arr.append(word_dict[lst[i]])
    if flag == 1:
        print(*arr)
    else:
        print(f'{arr} not in dictionary.')