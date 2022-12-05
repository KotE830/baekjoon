from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def snakes_and_ladders(graph: defaultdict) -> int:
    gone = set()
    queue = [(0, 1)]

    while queue:
        count, square = heapq.heappop(queue)
        
        count += 1
        for i in range(1, 7):
            next = square + i
            if next in graph:
                next = graph[next]
                
            if next == 100:
                return count
                
            if next not in gone:
                gone.add(next)
                heapq.heappush(queue, (count, next))


N, M = map(int, input().split())
graph = defaultdict(int)
for _ in range(N+M):
    x, y = map(int, input().split())
    graph[x] = y

print(snakes_and_ladders(graph))