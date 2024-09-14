import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
while n != 0:
    lst_n = list(str(n))
    temp = ''
    if '1' in lst_n:
        for i in range(len(lst_n)):
            if lst_n[i] == '1':
                cnt += 1
            else:
                temp += lst_n[i]
        if temp == '':
            temp = '0'
        n = int(temp)
    else:
        n -= 1
        cnt += 1
print(cnt)