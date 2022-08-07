def trap(height: list) -> int:
    left, right, h = 0, len(height)-1, 0
    v = 0

    while left < right:
        if height[left] <= h:
            v += h - height[left]
            left += 1
        elif height[right] <= h:
            v += h - height[right]
            right -= 1
        else:
            h = min(height[left], height[right])
        print(left, right, h)

    return v


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))