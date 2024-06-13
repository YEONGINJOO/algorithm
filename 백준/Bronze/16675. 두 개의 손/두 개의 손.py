import sys
input = sys.stdin.readline

ml, mr, tl, tr = map(str, input().strip().split())
if ml == mr and tl == tr:
    if ml == tl:
        print('?')
    else:
        if ml == 'S':
            if tl == 'P':
                print('MS')
            else:
                print('TK')
        elif ml == 'R':
            if tl == 'S':
                print('MS')
            else:
                print('TK')
        elif ml == 'P':
            if tl == 'R':
                print('MS')
            else:
                print('TK')
elif ml == mr and tl != tr:
    if ml == 'R':
        if tl == 'P' or tr == 'P':
            print('TK')
        elif tl == 'R' and tr == 'S':
            print('?')
        elif tl == 'S' and tr == 'R':
            print('?')
    elif ml == 'S':
        if tl == 'R' or tr == 'R':
            print('TK')
        elif tl == 'P' and tr == 'S':
            print('?')
        elif tl == 'S' and tr == 'P':
            print('?')
    elif ml == 'P':
        if tl == 'S' or tr == 'S':
            print('TK')
        elif tl == 'P' and tr == 'R':
            print('?')
        elif tl == 'R' and tr == 'P':
            print('?')
elif ml != mr and tl == tr:
    if tl == 'R':
        if ml == 'P' or mr == 'P':
            print('MS')
        elif ml == 'R' and mr == 'S':
            print('?')
        elif ml == 'S' and mr == 'R':
            print('?')
    elif tl == 'S':
        if ml == 'R' or mr == 'R':
            print('MS')
        elif ml == 'P' and mr == 'S':
            print('?')
        elif ml == 'S' and mr == 'P':
            print('?')
    elif tl == 'P':
        if ml == 'S' or mr == 'S':
            print('MS')
        elif ml == 'P' and mr == 'R':
            print('?')
        elif ml == 'R' and mr == 'P':
            print('?')
else:
    print('?')