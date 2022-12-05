from collections import deque

def hide_and_seek(n: int, k: int) -> int:
    def bfs() -> int:
        queue = deque([[n, 0]])
        gone = {}        

        while queue:
            x, s = queue.popleft()
            if x == k:
                return s

            if x not in gone and x >= 0:
                gone[x] = 1
                queue.append([x-1, s+1])
                if x < k:
                    queue.append([x+1, s+1])
                    queue.appendleft([x*2, s])


    return bfs()
    

n, k = map(int, input().split())
print(hide_and_seek(n, k))