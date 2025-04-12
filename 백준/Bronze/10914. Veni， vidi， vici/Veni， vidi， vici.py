n = int(input())
words = input().split()

result = []

for word in words:
    decrypted_word = ''
    for i in range(0, len(word) - 1, 2):
        y = ord(word[i]) - ord('a')
        z = ord(word[i+1]) - ord('a')
        x = (y + z - n) % 26
        decrypted_word += chr(x + ord('a'))
    result.append(decrypted_word)

print(*result)