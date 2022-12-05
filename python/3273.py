def twoSum(n: int, arr: list, x: int) -> int:
    left, right = 0, n-1
    count = 0
    
    while left < right:
        if arr[left] + arr[right] > x:
            right -= 1
        elif arr[left] + arr[right] < x:
            left += 1
        else:
            count += 1
            left += 1
            right -= 1

    return count


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

print(twoSum(n, sorted(arr), x))