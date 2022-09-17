import heapq, sys
input = sys.stdin.readline

N = int(input())
max_heap = []
min_heap = []

for _ in range(N):
    n = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -n)
    else:
        heapq.heappush(min_heap, n)

    if not min_heap:
        print(-max_heap[0])
        continue
    elif -max_heap[0] > min_heap[0]:
        i, j = heapq.heappop(max_heap), heapq.heappop(min_heap)
        heapq.heappush(max_heap, -j)
        heapq.heappush(min_heap, -i)

    print(-max_heap[0])