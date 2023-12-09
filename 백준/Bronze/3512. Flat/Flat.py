n, c = map(int, input().split())
all_width = 0
bed_width = 0
cost = 0
for i in range(n):
    a, b = map(str, input().split())
    all_width += int(a)
    if b == 'bedroom':
        bed_width += int(a)
    if b == 'balcony':
        cost += int(a)/2 * c
    else:
        cost += int(a) * c
print(all_width)
print(bed_width)
print(cost)