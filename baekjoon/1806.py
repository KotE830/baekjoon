def subsequence(n: int, s: int, arr: list) -> int:
    if sum(arr) < s:
        return 0
        
    left = right = 0
    distance = n
    sums = arr[0]

    while left < n:
        if sums >= s and distance > right - left + 1:
            distance = right - left + 1

        if left == right or sums < s:
            right += 1
            if right == n:
                break
            sums += arr[right]
        else:
            sums -= arr[left]
            left += 1

    return distance


n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(subsequence(n, s, arr))