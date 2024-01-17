lst = []
while True:
    a = input()
    lst.append(a)
    if a == '=':
        break
ans = int(lst[0])
for i in range(len(lst)):
    if lst[i] == '+':
        ans += int(lst[i+1])
    elif lst[i] == '-':
        ans -= int(lst[i+1])
    elif lst[i] == '*':
        ans *= int(lst[i+1])
    elif lst[i] == '/':
        ans //= int(lst[i+1])
print(ans)