ap_dict = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1
}
while True:
    a = input()
    if a == '#':
        break
    num = 0
    for i in range(len(a)):
        num += ap_dict[a[i]] * (8 ** (len(a)-i-1))
    print(num)