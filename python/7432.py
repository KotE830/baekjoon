from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert directorys in path
    def insert(self, path: str) -> None:
        node = self.root
        for directory in path.split("\\"):
            node = node.children[directory]

    # print directorys
    def print_trie(self, node, space = 0) -> None:
        for child in sorted(node.children):
            print(' ' * space + child)
            self.print_trie(node.children[child], space + 1)
        

N = int(input())
trie = Trie()
for _ in range(N):
    trie.insert(input().rstrip())
trie.print_trie(trie.root)