# 10026
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def count_areas(N: int, grid: list) -> int:
    def dfs(x: int, y: int, mark: str):
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        
        grid[y][x] = mark
        for i in range(4):
            nx, ny, = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and grid[ny][nx] == 1:
                dfs(nx, ny)
        

    count_r, count_g = 0
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1:
                dfs(x, y, 'R', 'G')
                count_r += 1
                dfs(x, y, 'G', 'B')
                count_g += 1
    return (count_r, count_g)
    


N = int(input())
grid = [list(map(int, input().split())) for _ in range(h)]
print(*count_areas(N, grid))