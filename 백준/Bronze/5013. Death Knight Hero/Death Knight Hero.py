n = int(input())
cnt = 0
for _ in range(n):
    ki = input()
    win = 1
    for i in range(len(ki)-1):
        if ki[i] == 'C' and ki[i+1] == 'D':
            win = 0
    if win == 1:
        cnt += 1
print(cnt)