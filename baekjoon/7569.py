from collections import deque
import sys
input = sys.stdin.readline

def ripe(n: int, m: int, h: int, tomatoes: list) -> int:
    queue = deque([])
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomatoes[z][y][x] == 1:
                    queue.append([x, y, z])
    
    dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
    day = 1
    
    while queue:
        x, y, z = queue.popleft()
        
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            
            if tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
                queue.append([nx, ny, nz])
            day = tomatoes[z][y][x]

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomatoes[z][y][x] == 0:
                    return -1

    return day - 1


m, n, h = map(int, input().split())
tomatoes = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]
print(ripe(n, m, h, tomatoes))