from collections import Counter

s = input().upper()
counts = Counter(s)

if len(counts) == 1 or counts.most_common(1)[0][1] > counts.most_common(2)[1][1]:
    print(counts.most_common(1)[0][0])
else:
    print('?')