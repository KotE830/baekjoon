import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def count_islands(w: int, h: int, grid: list) -> int:
    def dfs(x: int, y: int):
        dx, dy = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
        
        grid[y][x] = 0
        for i in range(8):
            nx, ny, = x + dx[i], y + dy[i]
            if nx >= 0 and nx < w and ny >= 0 and ny < h and grid[ny][nx] == 1:
                dfs(nx, ny)
        

    count = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 1:
                dfs(x, y)
                count += 1
    return count
    

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]

    print(count_islands(w, h, grid))