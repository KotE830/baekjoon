from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.leaf = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert feeds
    def insert(self, feeds: str) -> bool:
        node = self.root
        for feed in feeds:
            node = node.children[feed]
        node.leaf = True

    # print trie
    def print_trie(self, node, floor = 0) -> None:
        # dfs
        for feed in sorted(node.children):
            print("--" * floor + feed)
            self.print_trie(node.children[feed], floor + 1)


N = int(input())
trie = Trie()
for _ in range(N):
    trie.insert(input().split()[1:])
trie.print_trie(trie.root)