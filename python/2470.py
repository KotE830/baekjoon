# equal to 2467

def twoSum(n: int, arr: list) -> tuple:
    left, right = 0, n-1
    answer = (arr[0], arr[n-1])
    distance = abs(arr[0] + arr[n-1])
    
    while left < right:
        if distance > abs(arr[left] + arr[right]):
            distance = abs(arr[left] + arr[right])
            answer = (arr[left], arr[right])
            
        if arr[left] + arr[right] > 0:
            right -= 1
        elif arr[left] + arr[right] < 0:
            left += 1
        else:
            return (arr[left], arr[right])

    return answer


n = int(input())
arr = list(map(int, input().split()))

print(*twoSum(n, sorted(arr)))