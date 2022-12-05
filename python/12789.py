n = int(input())
people = list(map(int, input().split()))
waiting, i = [], 1

for p in people:
    if not waiting or p < waiting[-1]:
        waiting.append(p)
    elif p == i:
        i += 1
    else:
        waiting.append(-1)
        break
    while waiting and waiting[-1] == i:
        waiting.pop()
        i += 1

print("Sad" if waiting else "Nice")
