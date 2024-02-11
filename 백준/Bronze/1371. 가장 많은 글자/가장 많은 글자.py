ap_dict = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
}
st = ''
for _ in range(50):
    try:
        a = input()
        st += a
    except EOFError:
        break
# print(st)
for i in st:
    if i in ap_dict:
        ap_dict[i] += 1
ans = ''
mx = 0
for j in ap_dict:
    if ap_dict[j] > mx:
        mx = ap_dict[j]
        ans = j
    elif ap_dict[j] == mx:
        mx = ap_dict[j]
        ans += j
print(ans)