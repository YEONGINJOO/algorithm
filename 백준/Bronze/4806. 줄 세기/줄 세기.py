sum_a = 0
while True:
    try:
        a = input()
        sum_a += 1
    except EOFError:
        break
print(sum_a)