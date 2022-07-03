import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0
i, j = 0, len(nums)-1

while i < j:
    if nums[i] + nums[j] == m:
        cnt = cnt + 1
        i = i + 1
        j = j - 1
    else:
        if nums[i] + nums[j] < m:
            i = i + 1
        else:
            j = j - 1

print(cnt)