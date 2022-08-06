def kmp(word: str) -> list:
    

def findWord(s: str, word: str):
    cnt, indexs = 0, []   
    i = 0

    while i < len(s):
        j = 0
        while i+j < len(s) and j < len(word) and s[i+j] == word[j]:
            j += 1
        if j == len(word):
            cnt += 1
            indexs.append(i+1)
        i += 1

    return cnt, indexs
    

s = input()
word = input()

cnt, indexs = findWord(s, word)
print(cnt)
print(*[x for x in indexs])