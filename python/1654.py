import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))
    
start, end = 1, lans[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lans:
        cnt = cnt + (i//mid)
        
    if cnt >= n:
        start = mid+1
    else:
        end = mid-1

print(end)