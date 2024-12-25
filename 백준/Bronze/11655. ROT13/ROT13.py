alst = [chr(i) for i in range(97, 123)]
llst = [chr(i) for i in range(65, 91)]
alp_dict = {chr(i):i+13 for i in range(97, 123)}
lap = {chr(i):i+13 for i in range(65, 91)}
for i in range(26):
    if alp_dict[alst[i]] > 122:
        alp_dict[alst[i]] = chr(alp_dict[alst[i]]-26)
    else:
        alp_dict[alst[i]] = chr(alp_dict[alst[i]])
    if lap[llst[i]] > 90:
        lap[llst[i]] = chr(lap[llst[i]]-26)
    else:
        lap[llst[i]] = chr(lap[llst[i]])
a = input()
ans = ''
for i in range(len(a)):
    if a[i] in lap:
        ans += lap[a[i]]
    elif a[i] in alp_dict:
        ans += alp_dict[a[i]]
    else:
        ans += a[i]
print(ans)