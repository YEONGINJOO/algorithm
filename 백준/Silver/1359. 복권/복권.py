from math import comb

def lottery_probability(N, M, K):
    total_cases = comb(N, M)
    success_cases = 0
    
    for i in range(K, M + 1):
        success_cases += comb(M, i) * comb(N - M, M - i)
    
    return success_cases / total_cases

N, M, K = map(int, input().split())

probability = lottery_probability(N, M, K)
print(f"{probability:.12f}")