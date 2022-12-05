import heapq
import sys
input=sys.stdin.readline

n, heap = int(input()), []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    elif heap:
        print(heapq.heappop(heap)[1])
    else:
        print(0)