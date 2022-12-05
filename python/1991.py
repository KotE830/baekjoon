import collections
import sys
input = sys.stdin.readline

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def make_tree(tree_nodes: collections.defaultdict) -> TreeNode:
    def dfs(value) -> TreeNode:
        if value == '.':
            return None
        if value not in tree_nodes:
            return TreeNode(value)
            
        node = TreeNode(value)
        node.right = dfs(tree_nodes[value].pop())
        node.left = dfs(tree_nodes[value].pop())
        return node

    return dfs('A')


def traversals(tree_root: TreeNode):
    def preorder(node):
        if node:
            print(node.val, end='')
            preorder(node.left)
            preorder(node.right)
            
    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end='')
            inorder(node.right)
            
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            print(node.val, end='')

    preorder(tree_root)
    print()
    inorder(tree_root)
    print()
    postorder(tree_root)
    print()
    
    
N = int(input())
tree_nodes = collections.defaultdict(list)
for _ in range(N):
    root, left, right = input().split()
    tree_nodes[root].append(left)
    tree_nodes[root].append(right)

tree_root = make_tree(tree_nodes)
traversals(tree_root)