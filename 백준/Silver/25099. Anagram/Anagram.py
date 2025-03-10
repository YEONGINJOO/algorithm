import sys
input = sys.stdin.readline

n = int(input())
words = []
seen_anagrams = set()

for _ in range(n):
    word = input().strip()
    sorted_word = ''.join(sorted(word))
    
    if sorted_word not in seen_anagrams:
        seen_anagrams.add(sorted_word)
        words.append(word)

for word in words:
    print(word)