def min_soldiers(N, S):
    # DP 배열 초기화
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # 0자리까지는 0명
    
    # 문자열 S를 점검하여 DP 업데이트
    for i in range(1, N + 1):
        for length in range(1, 4):  # 1자리에서 3자리
            j = i - length
            if j < 0:
                continue  # 음수 인덱스는 무시
            
            # 부분 문자열 S[j:i]
            part = S[j:i]
            if part[0] == '0' or len(part) > 3:  # 선행 0이 있거나 3자리 초과
                continue
            
            # 정수로 변환
            number = int(part)
            if 1 <= number <= 641:  # 유효한 범위 체크
                dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[N]

# 입력 예시
N = int(input().strip())
S = input().strip()
result = min_soldiers(N, S)
print(result)
