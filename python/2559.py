import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sums = list(map(int, input().split()))

for i in range(1, len(sums)):
    sums[i] = sums[i-1] + sums[i]

temps = [sums[k-1]]
for i in range(k, len(sums)):
    temps.append(sums[i]-sums[i-k])

print(max(temps))