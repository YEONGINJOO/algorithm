from random import shuffle
lst = [i for i in range(1, 10001)]
shuffle(lst)
while True:
    A = lst.pop()
    print(f'? A {A}', flush=True)
    k = int(input())
    if k == 1:
        break
lst = [i for i in range(1, 10001)]
shuffle(lst)
while True:
    B = lst.pop()
    print(f'? B {B}', flush=True)
    k = int(input())
    if k == 1:
        break
print(f'! {A+B}', flush = True)