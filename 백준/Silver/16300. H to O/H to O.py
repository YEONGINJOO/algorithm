import sys
input = sys.stdin.readline
a, b = map(str, input().split())
boon = input().strip()
vowel = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mo = {}
i = 0
while i < len(a):
    if a[i] in vowel:
        if a[i] in mo:
            mo[a[i]] += 1
        else:
            mo[a[i]] = 1
        i += 1
    else:
        num = ''
        for j in range(i, len(a)):
            if a[j] in vowel:
                mo[a[i - 1]] += int(num) - 1
                i = j
                break
            elif j == len(a)-1:
                num += a[j]
                mo[a[i - 1]] += int(num) - 1
                i = j + 1
                break
            else:
                num += a[j]
for j in mo:
    mo[j] *= int(b)
ja = {}
k = 0
while k < len(boon):
    if boon[k] in vowel:
        if boon[k] in ja:
            ja[boon[k]] += 1
        else:
            ja[boon[k]] = 1
        k += 1
    else:
        num = ''
        for j in range(k, len(boon)):
            if boon[j] in vowel:
                ja[boon[k - 1]] += int(num) - 1
                k = j
                break
            elif j == len(boon)-1:
                num += boon[j]
                ja[boon[k - 1]] += int(num) - 1
                k = j + 1
                break
            else:
                num += boon[j]
mn = 987654321
for l in ja:
    if l not in mo:
        mn = 0
        break
    else:
        cnt = mo[l] // ja[l]
        if cnt < mn:
            mn = cnt
print(mn)