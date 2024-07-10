import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()
if c != 'Fizz' and c != 'Buzz' and c != 'FizzBuzz':
    if (int(c) + 1) % 3 == 0 and (int(c) + 1) % 5 == 0:
        print('FizzBuzz')
    elif (int(c) + 1) % 3 == 0 and (int(c) + 1) % 5 != 0:
        print('Fizz')
    elif (int(c) + 1) % 3 != 0 and (int(c) + 1) % 5 == 0:
        print('Buzz')
    else:
        print(int(c)+1)
elif c == 'Fizz':
    if b == 'Buzz':
        print(int(a) + 3)
    else:
        if (int(b) + 2) % 5 == 0:
            print('Buzz')
        else:
            print(int(b)+2)
elif c == 'Buzz':
    if b == 'Fizz':
        print(int(a) + 3)
    else:
        if (int(b) + 2) % 3 == 0:
            print('Fizz')
        else:
            print(int(b)+2)
else:
    print(int(b)+2)