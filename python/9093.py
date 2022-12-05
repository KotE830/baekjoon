t = int(input())
for _ in range(t):
    words = input().split()
    print(*[word[::-1] for word in words])