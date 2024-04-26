n = int(input())
st_n = str(n)
cnt = 0
if len(st_n) > 1:
    for i in range(len(st_n)-1):
        cnt += 9 * (10 ** i) * (i+1)
        n = n - 9 * (10 ** (i))
    cnt += n * len(st_n)
else:
    cnt = n
print(cnt)