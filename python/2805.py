import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, 2000000000

while start <= end:
    mid = start + (end - start) // 2
    sum = 0

    for i in trees:
        if i > mid:
            sum += (i - mid)
    
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)