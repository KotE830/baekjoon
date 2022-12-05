import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def safe_areas(N: int, grid: list) -> int:
    def dfs(x: int, y: int):
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        
        visited[y][x] = 1
        for i in range(4):
            nx, ny, = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and grid[ny][nx] > level and not visited[ny][nx]:
                dfs(nx, ny)

    
    min_level = 100
    for area in grid:
        min_level = min(min_level, min(area))

    max_areas = 1
    for level in range(min_level, 100):
        count = 0
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if grid[y][x] > level and not visited[y][x]:
                    dfs(x, y)
                    count += 1

        if count == 0:
            break
        max_areas = max(max_areas, count)
                
    return max_areas


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
print(safe_areas(N, grid))