M = 10**6
P = 15 * M // 10

def fib(n: int) -> int:
    fibs = [0, 1]
    if n < 2:
        return fibs[n]
            
    for i in range(2, n+1):
        fibs.append((fibs[i-1] + fibs[i-2]) % M)
    
    return fibs[-1]


print(fib(int(input()) % P))