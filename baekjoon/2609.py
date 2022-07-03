import sys
input = sys.stdin.readline

def prime(n):
    nums = [False, False] + [True] * (n-1)
    primes = []

    for i in range(n+1):
        if nums[i]:
            primes.append(i)
            for j in range(i, n+1, i):
                nums[j] = False

    return primes


a, b = map(int, input().split())
if b > a: a, b = b, a
primes = prime(a//2)
a_nums, b_nums = {i:0 for i in primes}, {i:0 for i in primes}

for i in primes:
    while a % i == 0 and a > 0:
        a_nums[i] = a_nums[i] + 1
        a = a // i
    while b % i == 0 and b > 0:
        b_nums[i] = b_nums[i] + 1
        b = b // i
        
gcd, lcm = 1, 1
for i in primes:
    gcd = gcd * (i ** (min(a_nums[i], b_nums[i])))
    lcm = lcm * i ** (max(a_nums[i], b_nums[i]))

print(gcd)
print(lcm)