a = input().strip()
a = a.upper()
alp_dict = {chr(i): '' for i in range(65, 91)}
for i in alp_dict:
    a_cnt = a.count(i)
    star = '*' * a_cnt
    print(f'{i} | {star}')