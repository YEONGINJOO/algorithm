d, m = map(int, input().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
sm = d
for i in range(m):
    sm += month[i]
if sm % 7 == 1:
    ans = "Thursday"
elif sm % 7 == 2:
    ans = "Friday"
elif sm % 7 == 3:
    ans = "Saturday"
elif sm % 7 == 4:
    ans = "Sunday"
elif sm % 7 == 5:
    ans = "Monday"
elif sm % 7 == 6:
    ans = "Tuesday"
elif sm % 7 == 0:
    ans = "Wednesday"
print(ans)