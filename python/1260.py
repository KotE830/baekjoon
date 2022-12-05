import collections
import sys
input = sys.stdin.readline

def dfs_bfs(graph: dict, v: int):
    def dfs(v, dfs_path = {}) -> dict:
        dfs_path[v] = 1
        for w in graph[v]:
            if w not in dfs_path:
                dfs_path[v] = dfs(w, dfs_path)
        return dfs_path

    
    def bfs(v, bfs_path = {}) -> dict:
        bfs_path[v] = 1
        queue = collections.deque([v])

        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if w not in bfs_path:
                    queue.append(w)
                    bfs_path[w] = 1
        return bfs_path
        

    dfs_path = dfs(v)
    bfs_path = bfs(v)

    print(*dfs_path)
    print(*bfs_path)
    

n, m, v = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for w in graph:
    graph[w].sort()

dfs_bfs(graph, v)