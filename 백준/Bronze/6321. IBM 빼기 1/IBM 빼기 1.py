alpha_dict = {
    'A': 'B',
    'B': 'C',
    'C': 'D',
    'D': 'E',
    'E': 'F',
    'F': 'G',
    'G': 'H',
    'H': 'I',
    'I': 'J',
    'J': 'K',
    'K': 'L',
    'L': 'M',
    'M': 'N',
    'N': 'O',
    'O': 'P',
    'P': 'Q',
    'Q': 'R',
    'R': 'S',
    'S': 'T',
    'T': 'U',
    'U': 'V',
    'V': 'W',
    'W': 'X',
    'X': 'Y',
    'Y': 'Z',
    'Z': 'A'
}
n = int(input())
for j in range(n):
    a = input()
    ans = ''
    for i in range(len(a)):
        ans += alpha_dict[a[i]]
    print(f'String #{j+1}')
    print(ans)
    print()