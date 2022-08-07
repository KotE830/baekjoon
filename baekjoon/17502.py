n = int(input())
s = list(input())

left, right = 0, n-1
while left <= right:
    if s[left] == '?' and s[right] != '?':
        s[left] = s[right]
    elif s[left] != '?' and s[right] == '?':
        s[right] = s[left]
    elif s[left] == '?' and s[right] == '?':
        s[left], s[right] = 'a', 'a'

    left += 1
    right -= 1

print(''.join(s))