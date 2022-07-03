import sys
input = sys.stdin.readline
    
def granica(nums):
    result = []

    g = abs(nums[0] - nums[1])
    for i in range(1, len(nums)-1):
        g = gcd(g, abs(nums[i+1] - nums[i]))
    
    for i in range(2, int(g**0.5)+1):
        if g % i == 0:
            result.append(i)
            result.append(g//i)
    result.append(g)
    
    return result

    
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

        
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

result = list(set(granica(nums)))
result.sort()
print(*result)


'''
k1 = m * a1 + n
k2 = m * a2 + n
k3 = m * a3 + n
k4 = m * a4 + n

k2 - k1 = m * (a2 - a1)
k3 - k2 = m * (a3 - a2)
k4 - k3 = m * (a4 - a3)
'''