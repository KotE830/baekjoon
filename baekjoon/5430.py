from collections import deque
import sys
input=sys.stdin.readline

def AC(p: str, queue: deque) -> str:
    re = 0
    for com in p:
        if com == 'R':
            re = 1 -re
        elif com == 'D':
            if not queue:
                return 'error'
            elif re == 0:
                queue.popleft()
            else:
                queue.pop()

    arr = []
    while queue:
        arr.append(queue.pop() if re else queue.popleft())
    return '[' + ','.join(arr) + ']'

t = int(input())
for _ in range(t):
    p, n = input(), int(input())
    arr = input()[1:-2].split(',')

    try:
        while True:
            arr.remove('')
    except ValueError:
        pass
        
    print(AC(p, deque(arr)))