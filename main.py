import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def move_piece(R: int, C: int, grid: list) -> int:
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    def dfs(x: int, y: int, count: int) -> int:
        visited[ord(grid[y][x]) - 65] = True
        new_count = 0
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < C and ny < R and not visited[ord(grid[ny][nx]) - 65]:
                new_count = max(new_count, dfs(nx, ny, count+1))
                visited[ord(grid[ny][nx]) - 65] = False

        return max(count, new_count)
        

    visited = [False for _ in range(26)]
    return dfs(0, 0, 1)
            

R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]
print(move_piece(R, C, grid))