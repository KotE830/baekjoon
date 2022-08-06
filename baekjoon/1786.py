def kmp(word: str) -> list:
    pi = [-1]
    i, j = -1, 0

    while j < len(word):
        if i == -1 or word[i] == word[j]:
            i += 1
            j += 1
            pi.append(i)
        else:
            i = pi[i]

    return pi
        
    
def findWord(s: str, word: str):
    cnt, indexs = 0, []
    pi = kmp(word)
    i, j = 0, 0

    while i < len(s):
        if j == -1 or s[i] == word[j]:
            i += 1
            j += 1
        else:
            j = pi[j]

        if j == len(word):
            cnt += 1
            indexs.append(i - len(word) + 1)
            j = pi[j]
    
    return cnt, indexs
    

s = input()
word = input()

cnt, indexs = findWord(s, word)
print(cnt)
print(*[x for x in indexs])