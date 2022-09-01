import heapq

def bfs(n):
    queue = [[0, n, [n]]]
    while queue:
        count, x, nums = heapq.heappop(queue)
        if x == 1:
            return count, nums
        if x % 3 == 0:
            heapq.heappush(queue, [count+1, x//3, nums+[x//3]])
        if x % 2 == 0:
            heapq.heappush(queue, [count+1, x//2, nums+[x//2]])
        heapq.heappush(queue, [count+1, x-1, nums+[x-1]])


n = int(input())
count, nums = bfs(n)
print(count)
print(*nums)