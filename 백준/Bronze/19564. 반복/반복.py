import sys
input = sys.stdin.readline

def min_repeats_to_form_string(s):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp_index = {char: idx for idx, char in enumerate(alp)}

    current_max_index = -1
    repeat_count = 1

    for char in s:
        char_index = alp_index[char]
        if char_index <= current_max_index:
            repeat_count += 1
            current_max_index = char_index
        else:
            current_max_index = char_index

    return repeat_count

s = input().strip()
print(min_repeats_to_form_string(s))