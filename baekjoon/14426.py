from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search_prefix(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


N, M = map(int, input().split())
trie, count = Trie(), 0

for _ in range(N):
    trie.insert(input())
for _ in range(M):
    if trie.search_prefix(input()):
        count += 1
        
print(count)