s = input()
words = []
for i in range(len(s)):
    words.append(s[i:])

result = sorted(words)
print("\n".join(result))