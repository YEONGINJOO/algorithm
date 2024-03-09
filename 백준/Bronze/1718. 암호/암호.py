ap_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

n = input()
s = input()
if len(n) > len(s):
    while len(n) > len(s):
        for i in range(len(s)):
            s += s[i]
ans = ''
for i in range(len(n)):
    if n[i] == ' ':
        ans += ' '
    else:
        if ap_dict[n[i]] - ap_dict[s[i]] < 0:
            ans += chr(ap_dict[n[i]] - ap_dict[s[i]] + ap_dict['z'] + 96)
        elif ap_dict[n[i]] - ap_dict[s[i]] == 0:
            ans += chr(ap_dict['z'] + 96)
        else:
            ans += chr(ap_dict[n[i]] - ap_dict[s[i]] + 96)
print(ans)