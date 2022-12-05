def n_queen(n: int) -> int:
    queen_xpos = [True for _ in range(n)]
    diagonal = [True for _ in range(n*2+1)]
    reverse_dia = [True for _ in range(n*2+1)]
    
    def dfs(y: int) -> int:
        if y == n:
            return 1

        count = 0            
        for x in range(n):        
            if queen_xpos[x] and diagonal[y+x] and reverse_dia[y-x+n]:
                queen_xpos[x] = diagonal[y+x] = reverse_dia[y-x+n] = False
                count += dfs(y+1)
                queen_xpos[x] = diagonal[y+x] = reverse_dia[y-x+n] = True
                
        return count


    return dfs(0)


n = int(input())
print(n_queen(n))