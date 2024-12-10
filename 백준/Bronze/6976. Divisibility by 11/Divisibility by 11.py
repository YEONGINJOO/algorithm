import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = int(input())
    fst = a
    print(a)
    while True:
        if len(str(a)) <= 2:
            break
        st_a = str(a)
        fa = st_a[:-1]
        la = st_a[-1]
        a = int(fa) - int(la)
        print(a)
    if a % 11 == 0:
        print(f'The number {fst} is divisible by 11.')
    else:
        print(f'The number {fst} is not divisible by 11.')
    print()