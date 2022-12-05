from collections import deque
import sys
input = sys.stdin.readline

def treasure(X: int, Y: int, grid: list):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    
    def bfs(x, y) -> int:
        queue = deque([(0, x, y)])
        visited = [[False] * X for _ in range(Y)]
        visited[y][x] = True

        while queue:
            t, x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < X and 0 <= ny < Y and grid[ny][nx] == 'L' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((t+1, nx, ny))

        return t
        
    
    max_shortest = 0
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 'L':
                max_shortest = max(max_shortest, bfs(x, y))

    return max_shortest


Y, X = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(Y)]
print(treasure(X, Y, grid))