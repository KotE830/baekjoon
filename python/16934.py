from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.word = 0
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert the word and print nickname
    def insert(self, word: str) -> None:
        node = self.root
        nickname = ''
        for index, char in enumerate(word):
            node = node.children[char]
            if not nickname and not node.children and node.word == 0:
                nickname = word[:index+1]
            
        node.word += 1

        if not nickname:
            nickname = word
        if node.word > 1:
            nickname += str(node.word)
        print(nickname)
        

N = int(input())
trie = Trie()
for _ in range(N):
    trie.insert(input().rstrip())