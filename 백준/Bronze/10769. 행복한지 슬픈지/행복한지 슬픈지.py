import sys
input = sys.stdin.readline
a = input().strip()
happy_cnt = a.count(':-)')
sad_cnt = a.count(':-(')
if '-' not in a:
    print('none')
elif happy_cnt > sad_cnt:
    print('happy')
elif happy_cnt < sad_cnt:
    print('sad')
else:
    print('unsure')