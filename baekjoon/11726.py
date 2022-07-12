import sys
input = sys.stdin.readline

cnt = [0, 1, 2, 3]

def tiles(n):
    if n < len(cnt):
        return cnt[n]
        
    cnt.append((tiles(n-1) + tiles(n-2)) % 10007)
    return cnt[n]


n = int(input())
print(tiles(n))