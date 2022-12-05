from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def shortest_time(start: int, end: int, graph: defaultdict):
    gone = set()
    queue = [(0, start)]

    while queue:
        time, node = heapq.heappop(queue)
        if node == end:
            return time

        if node not in gone:
            gone.add(node)
            for v, w in graph[node]:
                heapq.heappush(queue, (time+w, v))


N, M, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

results = []
for n in range(1, N+1):
    results.append(shortest_time(n, X, graph) + shortest_time(X, n, graph))
print(max(results))