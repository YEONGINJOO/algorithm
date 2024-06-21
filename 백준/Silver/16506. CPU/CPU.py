import sys
input = sys.stdin.readline

opcode = {
    'ADD': '000000',
    'ADDC': '000010',
    'SUB': '000100',
    'SUBC': '000110',
    'MOV': '001000',
    'MOVC': '001010',
    'AND': '001100',
    'ANDC': '001110',
    'OR': '010000',
    'ORC': '010010',
    'NOT': '010100',
    'MULT': '011000',
    'MULTC': '011010',
    'LSFTL': '011100',
    'LSFTLC': '011110',
    'LSFTR': '100000',
    'LSFTRC': '100010',
    'ASFTR': '100100',
    'ASFTRC': '100110',
    'RL': '101000',
    'RLC': '101010',
    'RR': '101100',
    'RRC': '101110',
}

n = int(input())
for _ in range(n):
    lst = input().split()
    ans = ''
    ans += opcode[lst[0]]
    a = bin(int(lst[1]))[2:]
    if len(a) == 1:
        a = '00' + a
    elif len(a) == 2:
        a = '0' + a
    ans += a

    if lst[0] == 'MOV' or lst[0] == 'MOVC' or lst[0] == 'NOT':
        ans += '000'
    else:
        b = bin(int(lst[2]))[2:]
        if len(b) == 1:
            b = '00' + b
        elif len(b) == 2:
            b = '0' + b
        ans += b

    if lst[0][-1] == 'C':
        c = bin(int(lst[3]))[2:]
        if len(c) == 1:
            c = '000' + c
        elif len(c) == 2:
            c = '00' + c
        elif len(c) == 3:
            c = '0' + c
        ans += c
    else:
        d = bin(int(lst[3]))[2:]
        if len(d) == 1:
            d = '00' + d
        elif len(d) == 2:
            d = '0' + d
        ans += d + '0'
    print(ans)