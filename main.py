from collections import defaultdict
import sys
input = sys.stdin.readline

# find the greatest weight
def max_weight(N, islands, start, end, max_C) -> int:
    # check if start and end are connected with w
    def connected(weight: int) -> bool:
        visited = [False for _ in range(N+1)]
        stack = [start]
        visited[start] = True
        
        while stack:
            x = stack.pop()
            for v, w in islands[x]:
                if not visited[v] and weight <= w:
                    if v == end:
                        return True
                        
                    visited[v] = True
                    stack.append(v)

        return False
        

    left, right = 1, max_C
    while left <= right:
        mid = left + (right - left) // 2
        if connected(mid):
            left = mid + 1
        else:
            right = mid - 1

    return left-1
    

N, M = map(int, input().split())
max_C = 0

islands = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    islands[A].append((B, C))
    islands[B].append((A, C))
    max_C = max(max_C, C)

start, end = map(int, input().split())

print(max_weight(N, islands, start, end, max_C))