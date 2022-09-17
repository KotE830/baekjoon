import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

count = 0
while len(heap) > 1:
    k = heapq.heappop(heap) + heapq.heappop(heap)
    count += k
    heapq.heappush(heap, k)

print(count)