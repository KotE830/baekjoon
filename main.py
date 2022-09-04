# 9663 N-Queen

def n_queen(n: int) -> int:
    chessboard = [[0 for _ in range(n)] for _ in range(n)]
    
    def dfs(new_y: int) -> int:
        if new_y == n:
            return 1

        count = 0
        for new_x in range(n):
            if chessboard[new_y][new_x]:
                continue

            k1, k2 = new_y - new_x, new_y + new_x
            for y in range(new_y + 1, n):
                chessboard[y][new_x] = 0
                if y-k1 >= 0 and y-k1 < n:
                    chessboard[y][y-k1] = 0
                if k2-y >= 0 and k2-y < n:
                    chessboard[y][k2-y] = 0

            count += dfs(new_y + 1)
            
        return count
        

    return dfs(0)
    

n = int(input())
print(n_queen(n))