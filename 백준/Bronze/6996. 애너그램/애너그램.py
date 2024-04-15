t = int(input())
for _ in range(t):
    a, b = map(str, input().split())
    a_lst = list(a)
    a_lst.sort()
    b_lst= list(b)
    b_lst.sort()
    if a_lst == b_lst:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')