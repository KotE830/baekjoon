import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def count_areas(N: int, grid: list) -> tuple:
    def dfs(x: int, y: int, color: str, mark: str):
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        
        grid[y][x] = mark
        for i in range(4):
            nx, ny, = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and grid[ny][nx] == color:
                dfs(nx, ny, color, mark)
        

    count = 0
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 'R' or grid[y][x] == 'G':
                dfs(x, y, grid[y][x], 'C')
                count += 1
            elif grid[y][x] == 'B':
                dfs(x, y, 'B', 'b')
                count += 1

    cow = 0
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 'C':
                dfs(x, y, 'C', '0')
                cow += 1
            elif grid[y][x] == 'b':
                dfs(x, y, 'b', '0')
                cow += 1
                
    return (count, cow)


N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]
print(*count_areas(N, grid))