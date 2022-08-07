from collections import Counter

S = list(input())
s = [S[0]]

for i in range(1, len(S)):
    if S[i] != s[-1]:
        s.append(S[i])

if len(s) == 1:
    print(0)
else:
    counts = Counter(s)
    print(counts.most_common(2)[1][1])