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
    else:
        result += ''.join([w[0] for w in isbomb]) + word
        isbomb = []
        i = 0
        
    if i == len(bomb):
        for _ in range(i):
            isbomb.pop()
        i = isbomb[-1][1] if isbomb else 0

result += ''.join([w[0] for w in isbomb])
print(result if result else "FRULA")