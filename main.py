from collections import deque
import heapq
import sys
input = sys.stdin.readline

def shortest_path(N: int, M: int, graph: list) -> int:
    queue = deque([(1, 0, 0, 0)])
    visited = [[[0, 0] * M] * N]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        count, broke, x, y = queue.popleft()

        if x == M-1 and y == N-1:
            return count

        count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

                visit을 새로운 2차원배열을 생성한다음에 초기값을 큰값으로 초기화. 그다음 visit값은 0(벽안부시고 도달한경우), 1(벽부시고 도달한경우), 큰값(도달 한적없는경우)로 나누어집니다.
                
            if graph[ny][nx] == '0':
                queue.append((count, broke, nx, ny))
            elif broke == 0:
                queue.append((count, 1, nx, ny))
        for g in graph:
            print(*g)
        print(x, y)
    
    return -1


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
print(shortest_path(N, M, graph))