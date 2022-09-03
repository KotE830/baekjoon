from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def shortest_path(N: int, graph: defaultdict, v1: int, v2: int) -> int:
    def path(start: int, end: int) -> int:
        dist = {}
        queue = [(0, start)]

        while queue:
            weight, node = heapq.heappop(queue)

            if node == end:
                return weight
            
            if node not in dist:
                dist[node] = weight
                for v, w in graph[node]:
                    heapq.heappush(queue, (weight+w, v))

        return INF

    
    path1 = path(1, v1) + path(v1, v2) + path(v2, N)
    path2 = path(1, v2) + path(v2, v1) + path(v1, N)
    
    result = min(path1, path2)
    return result if result < INF else -1


N, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, input().split())

print(shortest_path(N, graph, v1, v2))