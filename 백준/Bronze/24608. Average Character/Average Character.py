S = input()
sm = 0
for i in S:
    sm += ord(i)
sm = sm // len(S)
print(chr(sm))