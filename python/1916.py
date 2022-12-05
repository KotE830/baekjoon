from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def shortest_price(start: int, end: int, graph: defaultdict):
    gone = set()
    queue = [(0, start)]

    while queue:
        price, node = heapq.heappop(queue)
        if node == end:
            return price

        if node not in gone:
            gone.add(node)
            for v, w in graph[node]:
                heapq.heappush(queue, (price+w, v))


N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
A, B = map(int, input().split())

print(shortest_price(A, B, graph))