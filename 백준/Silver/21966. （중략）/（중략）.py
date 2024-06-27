import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

if len(s) <= 25:
    print(s)
else:
    mid = s[11:-12]
    fst = s[:11]
    last = s[-11:]
    if '.' in mid:
        print(s[:9] + '......' + s[-10:])
    else:
        print(fst+'...'+last)