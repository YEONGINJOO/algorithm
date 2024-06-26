import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break
    s, t = line.split()
    
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    if i == len(s):
        print("Yes")
    else:
        print("No")