x, y = map(str, input().split())
re_x = x[::-1]
re_y = y[::-1]
ans = int(str(int(re_x) + int(re_y))[::-1])
print(ans)