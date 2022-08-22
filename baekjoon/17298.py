import sys
input = sys.stdin.readline

def nge(arr: list) -> list:
    answer, stack = [], []
    for n in arr[::-1]:
        while stack and stack[-1] <= n:
            stack.pop()
        
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
        stack.append(n)
        
    return answer[::-1]
    

n = int(input())
arr = list(map(int, input().split()))

print(*nge(arr))