import collections
import sys
input = sys.stdin.readline

def leaf_nodes(nodes: list, remove_node: int) -> int:
    tree = collections.defaultdict(list)
    root = 0
    for i, node in enumerate(nodes):
        if node == -1:
            root = i
        if i != remove_node and node != remove_node:
            tree[node].append(i)
    
    if root == remove_node:
        return 0
        
    count, stack = 0, [root]
    while stack:
        node = stack.pop()
        if node not in tree:
            count += 1
        else:
            for child in tree[node]:
                stack.append(child)

    return count

    
N = int(input())
nodes = list(map(int, input().split()))
remove_node = int(input())
print(leaf_nodes(nodes, remove_node))