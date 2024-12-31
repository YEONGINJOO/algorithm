n = int(input())
a_cnt = [0] * 4
b_cnt = [0] * 4
c_cnt = [0] * 4

for _ in range(n):
    a, b, c = map(int, input().split())
    a_cnt[0] += a
    a_cnt[a] += 1
    b_cnt[0] += b
    b_cnt[b] += 1
    c_cnt[0] += c
    c_cnt[c] += 1

# 최고 점수를 찾기
max_score = max(a_cnt[0], b_cnt[0], c_cnt[0])

# 최고 점수를 가진 후보들 찾기
candidates = []
if a_cnt[0] == max_score:
    candidates.append((1, a_cnt[3], a_cnt[2]))  # 후보 1의 정보
if b_cnt[0] == max_score:
    candidates.append((2, b_cnt[3], b_cnt[2]))  # 후보 2의 정보
if c_cnt[0] == max_score:
    candidates.append((3, c_cnt[3], c_cnt[2]))  # 후보 3의 정보

# 유일한 최고 점수인지 확인
if len(candidates) == 1:
    print(candidates[0][0], max_score)  # 유일한 후보 출력
else:
    # 동점자 중 3점 개수 비교
    candidates.sort(key=lambda x: (-x[1], -x[2]))  # 3점 → 2점 순으로 내림차순 정렬
    if candidates[0][1] != candidates[1][1]:  # 3점 개수로 결정 가능
        print(candidates[0][0], max_score)
    elif candidates[0][2] != candidates[1][2]:  # 2점 개수로 결정 가능
        print(candidates[0][0], max_score)
    else:
        print(0, max_score)  # 모든 조건이 동일한 경우
