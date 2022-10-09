from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert word
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # return the number of inputs
    def search(self, word: str) -> int:
        node = self.root
        count = 0
        
        for char in word:
            node = node.children[char]
            if node.word or len(node.children) > 1:
                count += 1
            
        return count


while True:
    try:
        N = int(input())
    except:
        break

    trie, words = Trie(), []
    for _ in range(N):
        word = input().rstrip()
        trie.insert(word)
        words.append(word)

    result = 0
    for word in words:
        result += trie.search(word)

    print(f'{result/N:.2f}')