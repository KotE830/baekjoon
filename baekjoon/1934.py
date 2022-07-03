import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a < b: a, b = b, a
    print(a * b // gcd(a, b))