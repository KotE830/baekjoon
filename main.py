from collections import deque
import sys
input = sys.stdin.readline

def ripe(m: int, n: int, tomatoes: list) -> int:
    def bfs() -> int:
        max_count = 0
        for i in range(n):
            for j in range(m):
                if not tomatoes[i][j]:
                    continue
                    
                queue = deque([[i, j, 0]])
                gone = {}

        while queue:
            x, y, count = queue.popleft()
            if (x, y) in gone or x < 0 or x >= l or y < 0 or y >= l:
                    continue
                
            if x == target_x and y == target_y:
                return m

            gone[(x, y)] = 1
            m += 1
            queue.append([x+1, y+2, m])
            queue.append([x+2, y+1, m])
            queue.append([x+2, y-1, m])
            queue.append([x+1, y-2, m])
            queue.append([x-1, y-2, m])
            queue.append([x-2, y-1, m])
            queue.append([x-2, y+1, m])
            queue.append([x-1, y+2, m])


    return bfs()
    

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
print(ripe(m, n, tomatoes))