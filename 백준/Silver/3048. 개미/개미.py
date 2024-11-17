def simulate_ants(N1, N2, group1, group2, T):
    # 초기 상태: 두 그룹의 개미를 합친 리스트
    ants = list(group1)[::-1] + list(group2)
    
    for _ in range(T):
        # 점프를 위한 새로운 상태 리스트
        new_ants = ants[:]
        
        # 점프할 수 있는 개미를 확인
        for i in range(len(ants)):
            if ants[i] in group1:  # 첫 번째 그룹의 개미
                if i < len(ants) - 1 and ants[i + 1] in group2:
                    new_ants[i], new_ants[i + 1] = ants[i + 1], ants[i]
            else:  # 두 번째 그룹의 개미
                if i > 0 and ants[i - 1] in group1:
                    new_ants[i], new_ants[i - 1] = ants[i - 1], ants[i]
        
        ants = new_ants
    
    return ''.join(ants)

N1, N2 = map(int, input().split())
group1 = input().strip()
group2 = input().strip()
T = int(input().strip())

result = simulate_ants(N1, N2, group1, group2, T)
print(result)