import sys
input = sys.stdin.readline

def sigRecept(n: int, towers: list) -> list:
    stack, sigs = [], [0] * n

    for i, tower in enumerate(towers):
        while stack and tower > stack[-1][1]:
            stack.pop()
        if stack:
            sigs[i] = stack[-1][0]
        stack.append([i+1, tower])

    return sigs
    
    
n = int(input())
towers = list(map(int, input().split()))

print(*sigRecept(n, towers))