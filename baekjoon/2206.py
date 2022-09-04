from collections import deque
import sys
input = sys.stdin.readline

def shortest_path(N: int, M: int, graph: list) -> int:
    queue = deque([(0, 0, 0)])
    visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        crush, x, y = queue.popleft()

        if x == M-1 and y == N-1:
            return visited[crush][y][x]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[crush][ny][nx] != 0:
                continue   

            if graph[ny][nx] == '0':
                visited[crush][ny][nx] = visited[crush][y][x] + 1
                queue.append((crush, nx, ny))
            elif crush == 0:
                visited[1][ny][nx] = visited[crush][y][x] + 1
                queue.append((1, nx, ny))
                
    return -1


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
print(shortest_path(N, M, graph))