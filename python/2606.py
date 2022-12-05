from collections import defaultdict
import sys
input = sys.stdin.readline

def worm_virus(graph: dict, v: int) -> dict:
    def dfs(start_v, path = {}) -> dict:
        stack = [start_v]
        
        while stack:
            v = stack.pop()
            if v not in path:
                path[v] = 1
                for w in graph[v]:
                    stack.append(w)
        return path
        

    return dfs(v)

n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

path = worm_virus(graph, 1)
print(len(path.keys())-1)