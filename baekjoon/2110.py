import sys
input = sys.stdin.readline

# return the longest possible distance
def max_distance(houses: list, C: int) -> int:
    # check the distances between houses and houses can be greater than dis
    def check_distance(dis: int) -> bool:
        now_x, count = houses[0], 1
        for x in houses:
            if x - now_x >= dis:
                count += 1
                now_x = x
            if count == C:
                return True

        return False

        
    left, right = 0, houses[-1] - houses[0]
    while left <= right:
        mid = left + (right - left) // 2
        if check_distance(mid):
            left = mid + 1
        else:
            right = mid - 1

    return left-1


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

print(max_distance(sorted(houses), C))