import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    dress = {}
    for _ in range(n):
        value, key = input().split()
        if key in dress:
            dress[key] = dress[key] + 1
        else:
            dress[key] = 1
    result = 1
    for i in dress.values():
        result = result * (i+1)
    print(result - 1)