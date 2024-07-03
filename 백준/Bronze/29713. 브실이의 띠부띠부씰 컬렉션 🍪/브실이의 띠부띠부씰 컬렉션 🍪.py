import sys
input = sys.stdin.readline
b = 'BRONZESILVER'
n = int(input())
a = input().strip()
chip = {b[i]: 0 for i in range(len(b))}
for i in range(n):
    if a[i] in b:
        chip[a[i]] += 1
chip['R'] = chip['R'] // 2
chip['E'] = chip['E'] // 2
print(min(chip.values()))