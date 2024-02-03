n = int(input())
m = int(input())
n_lst = []
m_lst = []
for _ in range(n):
    a = input()
    n_lst.append(a)
for _ in range(m):
    b = input()
    m_lst.append(b)
for i in range(n):
    for j in range(m):
        print(n_lst[i]+' as '+m_lst[j])