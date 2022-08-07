def water(w: int, heights: list) -> int:
    left, right, h = 0, w-1, 0
    water = 0

    while left < right:
        if heights[left] <= h:
            water += h - heights[left]
            left += 1
        elif heights[right] <= h:
            water += h - heights[right]
            right -= 1
        else:
            h = min(heights[left], heights[right])

    return water


h, w = map(int, input().split())
heights = list(map(int, input().split()))
print(water(w, heights))