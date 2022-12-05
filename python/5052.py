from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.number = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: str) -> bool:
        node = self.root
        for n in num:
            node = node.children[n]
            # check if num exists as a phone number
            if node.number:
                return False
        node.number = True
        # check if num is a prefix
        return not node.children
        

t = int(input())
for _ in range(t):
    n = int(input())
    trie, consistency = Trie(), True

    for _ in range(n):
        number = input().rstrip()
        if consistency:
            consistency = trie.insert(number)

    print("YES" if consistency else "NO")