# 9935
s = input()
bomb = input()
isbomb = []
i, result = 0, ''

for word in s:
    if word == bomb[0]:
        i = 1
        isbomb.append((word, i))
    elif word == bomb[i]:
        i += 1
        isbomb.append((word, i))
        if i == len(bomb):
            for _ in range(i):
                isbomb.pop()
            i = 0 if isbomb == [] else isbomb[-1][1]
    elif word != bomb[i] and word in bomb:
        result += ''.join([w[0] for w in isbomb])
        isbomb = []
    else:
        result += word

print(result if result else "FRULA")