s = int(input())
ma, f, mb = map(int, input().split())
if s <= 240:
    print('high speed rail')
elif s > ma + f + mb:
    print('flight')
else:
    print('high speed rail')