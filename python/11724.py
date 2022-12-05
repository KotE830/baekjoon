import collections
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def connected_components(N: int, graph: collections.defaultdict) -> int:
    visited = set()
    def dfs(node: int):
        visited.add(node)
        for v in graph[node]:
            if v not in visited:
                dfs(v)


    count = 0
    for node in range(1, N+1):
        if node not in visited:
            dfs(node)
            count += 1

    return count
    
    
N, M = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(connected_components(N, graph))