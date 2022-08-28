from collections import deque

def hide_and_seek(n: int, k: int) -> list:
    def bfs() -> list:
        queue = deque([[n, 0]])
        gone = {}
        count, second = 0, 100001

        while queue:
            x, s = queue.popleft()
            if s > second or x < 0 or x > 100000 or \
                (x in gone and gone[x] != s):
                    continue
                
            if x == k:
                count += 1
                second = s

            if x not in gone:
                gone[x] = s
                
            s += 1
            if s < second:
                queue.append([x-1, s])
                if x < k:
                    queue.append([x+1, s])
                    queue.append([x*2, s])
        
        return [second, count]

    
    return bfs() if n < k else [n-k, 1]
    

n, k = map(int, input().split())
for x in hide_and_seek(n, k):
    print(x)