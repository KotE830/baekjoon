from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def print_graph(n: int, graph: dict, r: int):
    def dfs(r, path = {}) -> dict:
        path[r] = 1
        for w in graph[r]:
            if w not in path:
                path = dfs(w, path)
        return path
        

    path = {v: i+1 for i, v in enumerate(dfs(r))}
    for i in range(1, n+1):
        print(0 if i not in path else path[i])
        
    
n, m, r = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for w in graph:
    graph[w].sort()

print_graph(n, graph, r)