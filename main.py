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
        self.names = {}

    # insert color in trie
    def insert_color(self, color: str) -> None:
        node = self.root
        for char in color:
            node = node.children[char]
        node.word = True

    def insert_name(self, name: str) -> None:
        self.names[name] = 0
        
    # check if the team is in the trie
    def search(self, team: str) -> bool:
        # check if the color is in the trie
        node = self.root
        for index, char in enumerate(team):
            if char not in node.children:
                return False
            node = node.children[char]
            # check if the name is in the dictionary
            if node.word and team[index+1:] in self.names:
                    return True
        
            
C, N = map(int, input().split())
trie = Trie()
for _ in range(C):
    trie.insert_color(input().rstrip())
for _ in range(N):
    trie.insert_name(input().rstrip())
    
for _ in range(int(input())):
    if trie.search(input().rstrip()):
        print("Yes")
    else:
        print("No")