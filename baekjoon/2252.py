import collections, sys
input = sys.stdin.readline

def solve_problems(N: int, count: list, graph: collections.defaultdict) -> list:
    queue = collections.deque([])
    result = []
    for i in range(1, N+1):
        if count[i] == 0:
            queue.append(i)
            
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            count[v] -= 1
            if count[v] == 0:
                queue.append(v)
        result.append(u)
        
    return result


N, M = map(int, input().split())
count = [0 for _ in range(N+1)]
graph = collections.defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    count[B] += 1
    
print(*solve_problems(N, count, graph))