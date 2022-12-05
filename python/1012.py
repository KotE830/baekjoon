import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def earthworms(n: int, m: int, lands: list) -> int:
    def dfs(i: int, j: int):
        if i < 0 or j < 0 or i >= n or j >= m or not lands[i][j]:
            return

        lands[i][j] = 0
        
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)


    count = 0
    for i in range(n):
        for j in range(m):
            if lands[i][j]:
                dfs(i, j)
                count += 1
    return count


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    lands = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        lands[y][x] = 1
        
    print(earthworms(n, m, lands))