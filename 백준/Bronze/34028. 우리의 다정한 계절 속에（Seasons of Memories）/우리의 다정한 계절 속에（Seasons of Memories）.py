from datetime import date, timedelta

# 시작일과 입력일 설정
start_date = date(2015, 1, 16)
a, b, c = map(int, input().split())
end_date = date(a, b, c)

# 계절 정보 저장
season_dict = {
    12: 'winter', 1: 'winter', 2: 'winter',
    3: 'spring', 4: 'spring', 5: 'spring',
    6: 'summer', 7: 'summer', 8: 'summer',
    9: 'fall', 10: 'fall', 11: 'fall'
}

# 중복 방지를 위한 set
season_set = set()

# 하루씩 순회
current = start_date
while current <= end_date:
    y = current.year
    m = current.month
    season = season_dict[m]

    # 겨울은 1, 2월이면 작년 겨울로 처리
    if season == 'winter' and m in [1, 2]:
        season_set.add((y - 1, 'winter'))
    else:
        season_set.add((y, season))
    
    current += timedelta(days=1)

print(len(season_set))
