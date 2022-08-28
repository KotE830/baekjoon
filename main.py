from collections import deque

def hide_and_seek(n: int, k: int) -> list:
    def bfs() -> int:
        queue = deque([[n, 0, []]])
        gone = {}        

        while queue:
            x, s, ways = queue.popleft()
            if x < 0 or x > 100000 or x in gone:
                    continue

            ways.append(x)
                
            if x == k:
                return [s, ways]

            s += 1
            gone[x] = 1
            queue.append([x-1, s, ways[:]])
            if x < k:
                queue.append([x+1, s, ways[:]])
                queue.append([x*2, s, ways[:]])


    return bfs()
    

n, k = map(int, input().split())
s, ways = hide_and_seek(n, k)
print(s)
print(*ways)