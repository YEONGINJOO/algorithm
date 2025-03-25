import sys
input = sys.stdin.readline
N, L = map(int, input().split())
knots = sorted(int(input()) for _ in range(N))  # 정렬된 매듭 리스트
knots_set = set(knots)  # 빠른 조회를 위한 집합
fold_positions = set()

# 가능한 모든 접는 위치 탐색 (매듭과 매듭 사이도 가능)
for i in range(N):
    for j in range(i + 1, N):  # i와 j 두 매듭의 중앙을 접는 위치로 고려
        fold = (knots[i] + knots[j]) / 2  # 중앙 위치
        if fold in fold_positions or fold <= 0 or fold >= L:  # 끝점에서는 접을 수 없음
            continue
        
        # 접었을 때 대칭 확인
        valid = True
        for knot in knots:
            mirrored = 2 * fold - knot  # 대칭되는 위치
            if mirrored in knots_set:  # 매듭이 정확히 대칭되면 OK
                continue
            if 0 <= mirrored <= L:  # 대칭 위치가 유효한 범위 내에 있으면
                valid = False
                break
        
        if valid:
            fold_positions.add(fold)  # 유효한 접는 위치 저장

print(len(fold_positions))
