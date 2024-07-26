def max_jump_students(N, heights):
    # 학생의 키를 오름차순으로 정렬
    heights.sort()
    
    # 중복된 키를 세어 최대 학생 수 구하기
    max_students = 0
    count = 0
    
    for i in range(N):
        # 현재 키와 같은 키가 몇 개인지 센다
        if i == 0 or heights[i] != heights[i - 1]:
            # 현재 키가 이전 키와 다르면
            max_students += min(count, 2)  # 이전 키에 대해 최대 2명까지
            count = 1  # 현재 키가 1명 있는 상태
        else:
            count += 1  # 같은 키가 더 늘어남
    
    # 마지막 키 처리
    max_students += min(count, 2)
    
    return max_students

# 입력 받기
N = int(input())
heights = list(map(int, input().split()))

# 결과 출력
print(max_jump_students(N, heights))