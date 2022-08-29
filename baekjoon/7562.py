from collections import deque
import sys
input = sys.stdin.readline

def move_knight(l: int, start_x: int, start_y: int,\
                target_x: int, target_y: int) -> int:
    def bfs() -> int:
        queue = deque([[start_x, start_y, 0]])
        gone = {}        

        while queue:
            x, y, m = queue.popleft()
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
    

t = int(input())
for _ in range(t):
    l = int(input())
    start_x, start_y = map(int, input().split())
    x, y = map(int, input().split())
    print(move_knight(l, start_x, start_y, x, y))