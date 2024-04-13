n = int(input())
grade = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}
sm = 0
sm_1 = 0
for _ in range(n):
    a, b, c = map(str, input().split())
    sm += int(b) * grade[c]
    sm_1 += int(b)
average = sm / sm_1
print("{:.2f}".format(round(average + 10**-10, 2)))