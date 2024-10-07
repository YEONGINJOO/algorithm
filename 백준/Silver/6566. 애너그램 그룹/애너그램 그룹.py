import sys
input = sys.stdin.readline
ans_lst = []
ans_dict = {}
while True:
    try:
        a = input().strip()
        if a == '':
            break
        b = "".join(sorted(a))
        if b in ans_dict:
            ans_dict[b].append(a)
        else:
            ans_dict[b] = [a]
    except EOFError:
        break
lst = []
for i in ans_dict:
    lst.append(ans_dict[i])
lst.sort(key=lambda x: (-len(x), x[0]))
for i in range(5):
    print(f'Group of size {len(lst[i])}:', end=' ')
    print(*sorted(list(set(lst[i]))), sep=" ", end=" .\n")