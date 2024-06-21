import sys
input = sys.stdin.readline

def is_acceptable(password):
    vowels = "aeiou"
    has_vowel = any(char in vowels for char in password)
    if not has_vowel:
        return False

    for i in range(len(password)):
        if i >= 2:
            if (password[i] in vowels and password[i-1] in vowels and password[i-2] in vowels) or \
               (password[i] not in vowels and password[i-1] not in vowels and password[i-2] not in vowels):
                return False
        if i >= 1:
            if password[i] == password[i-1] and password[i] not in "eo":
                return False

    return True

while True:
    st = input().strip()
    if st == "end":
        break
    if is_acceptable(st):
        print(f"<{st}> is acceptable.")
    else:
        print(f"<{st}> is not acceptable.")