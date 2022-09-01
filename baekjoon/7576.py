from collections import deque
import sys
input = sys.stdin.readline

def ripe(n: int, m: int, tomatoes: list) -> int:
    queue = deque([])
    for x in range(n):
        for y in range(m):
            if tomatoes[x][y] == 1:
                queue.append([x, y])
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    day = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append([nx, ny])
            day = tomatoes[x][y]

    for x in range(n):
        for y in range(m):
            if tomatoes[x][y] == 0:
                return -1

    return day - 1


m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
print(ripe(n, m, tomatoes))