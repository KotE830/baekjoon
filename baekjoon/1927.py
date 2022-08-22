import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    elif heap:
        print(heapq.heappop(heap))
    else:
        print(0)