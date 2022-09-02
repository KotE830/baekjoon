from collections import defaultdict
import heapq

def shortest_path(V: int, E: int, K: int, graph: defaultdict) -> defaultdict:
    routes = defaultdict(int)
    queue = [(0, K)]

    while queue:
        weight, node = heapq.heappop(queue)
            
        routes[node] = weight

        for v, w in graph[node]:
            alt = weight + w
            if alt < routes[v]:
                heapq.heappush(queue, (weight+w, v))

    return routes
    

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

routes = shortest_path(V, E, K, graph)
for i in range(1, V+1):
    print(routes[i] if i in routes else 'INF')