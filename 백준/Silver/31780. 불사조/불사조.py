def calculate_phoenix_power(x, m):
    total_power = x
    current_generation = [x]

    for _ in range(m):
        next_generation = []
        for power in current_generation:
            if power == 0:
                continue
            a = power // 2
            b = (power + 1) // 2
            next_generation.append(a)
            next_generation.append(b)
        
        total_power += sum(next_generation)
        current_generation = next_generation

    return total_power

x, m = map(int, input().split())
print(calculate_phoenix_power(x, m))