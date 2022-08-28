import sys
input = sys.stdin.readline

def lands(n: int, houses: list) -> list:
    def dfs(i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= n or j >= n or houses[i][j] == '0':
            return 0

        count = 1
        houses[i][j] = '0'
        
        count += dfs(i+1, j)
        count += dfs(i-1, j)
        count += dfs(i, j+1)
        count += dfs(i, j-1)

        return count


    result = [0]

    for i in range(n):
        for j in range(n):
            if houses[i][j] == '1':
                result.append(dfs(i, j))
                result[0] += 1

    return [result[0]] + sorted(result[1:])


n = int(input())
houses = [list(input().rstrip()) for _ in range(n)]
for x in lands(n, houses):
    print(x)