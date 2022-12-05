import collections
import sys
input = sys.stdin.readline

def print_graph(n: int, graph: dict, r: int):
    def bfs(r: int) -> dict:
        path = {r: 1}
        queue = collections.deque([r])
        
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if w not in path:
                    path[w] = 1
                    queue.append(w)
        return path


    path = {v: i+1 for i, v in enumerate(bfs(r))}
    for i in range(1, n+1):
        print(0 if i not in path else path[i])


n, m, r = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for w in graph:
    graph[w].sort(reverse=True)

print_graph(n, graph, r)