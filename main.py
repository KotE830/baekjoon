import collections, heapq, sys
input = sys.stdin.readline

def solve_problems(N: int, count: list, graph: collections.defaultdict):
    heap, result = [], []

    for i in range(1, N+1):
        if count[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        u = heapq.heappop(heap)
        for v in graph[u]:
            count[v] -= 1
            if count[v] == 0:
                heapq.heappush(heap, v)
        result.append(u)

    print(*result)


N, M = map(int, input().split())
count = [0 for _ in range(N+1)]
graph = collections.defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    count[B] += 1
    
solve_problems(N, count, graph)