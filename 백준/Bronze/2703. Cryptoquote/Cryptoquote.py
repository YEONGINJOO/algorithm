t = int(input())
for _ in range(t):
    a = input()
    b = input()
    a_dic = {}
    for i in range(len(b)):
        a_dic[chr(i+65)] = b[i]
    ans = ''
    for j in a:
        if j == ' ':
            ans += ' '
        else:
            ans += a_dic[j]
    print(ans)