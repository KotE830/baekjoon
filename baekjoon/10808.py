from collections import defaultdict

s = input()
counts = defaultdict(int)
result = ['0'] * 26

for alp in s:
    counts[alp] += 1

for key, value in counts.items():
    result[ord(key)-97] = str(value)

print(" ".join(result))