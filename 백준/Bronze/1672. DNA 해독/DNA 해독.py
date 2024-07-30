import sys
input = sys.stdin.readline

n = int(input())
a = list(input().strip())
while len(a) > 1:
    ma1 = a.pop()
    ma2 = a.pop()
    if ma1 == 'A' and ma2 == 'A':
        a.append('A')
    elif ma1 == 'A' and ma2 == 'G':
        a.append('C')
    elif ma1 == 'A' and ma2 == 'C':
        a.append('A')
    elif ma1 == 'A' and ma2 == 'T':
        a.append('G')
    elif ma1 == 'G' and ma2 == 'A':
        a.append('C')
    elif ma1 == 'G' and ma2 == 'G':
        a.append('G')
    elif ma1 == 'G' and ma2 == 'C':
        a.append('T')
    elif ma1 == 'G' and ma2 == 'T':
        a.append('A')
    elif ma1 == 'C' and ma2 == 'A':
        a.append('A')
    elif ma1 == 'C' and ma2 == 'G':
        a.append('T')
    elif ma1 == 'C' and ma2 == 'C':
        a.append('C')
    elif ma1 == 'C' and ma2 == 'T':
        a.append('G')
    elif ma1 == 'T' and ma2 == 'A':
        a.append('G')
    elif ma1 == 'T' and ma2 == 'G':
        a.append('A')
    elif ma1 == 'T' and ma2 == 'C':
        a.append('G')
    elif ma1 == 'T' and ma2 == 'T':
        a.append('T')
print(a[0])