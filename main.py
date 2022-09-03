import sys
input = sys.stdin.readline

def twoSum(n: int, waters: list) -> tuple:
    left, right = 0, n-1
    result = (abs(waters[0] + waters[n-1]), waters[0], waters[n-1])

    while left != right:
        value = abs(waters[left] + waters[right])
        if value < abs(result[0]):
            result = (value, waters[left], waters[right])

        if value < 0:
            left += 1
        elif value > 0:
            right -= 1
        else:
            return (waters[left], waters[right])

    return (result[1:])

    
n = int(input())
waters = list(map(int, input().split()))
print(*twoSum(n, waters))