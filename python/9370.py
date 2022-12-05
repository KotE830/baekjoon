from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def destinations(n: int, graph: defaultdict, g: int, h: int, ends: list) -> list:
    def path(start: int) -> list:
        dist = [INF] * (n+1)
        queue = [(0, start)]

        while queue:
            weight, node = heapq.heappop(queue)
            if dist[node] == INF:
                dist[node] = weight
                for v, w in graph[node]:
                    heapq.heappush(queue, (weight+w, v))

        return dist

    
    result = []
    path_s, path_g, path_h = path(s), path(g), path(h)
    for end in ends:
        p = path_s[end]
        p1 = path_s[g] + path_g[h] + path_h[end]
        p2 = path_s[h] + path_h[g] + path_g[end]
        if p == min(p1, p2) and p < INF:
            result.append(end)
    
    return sorted(result)


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    graph = defaultdict(list)
    ends = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    for _ in range(t):
        ends.append(int(input()))

    print(*destinations(n, graph, g, h, ends))