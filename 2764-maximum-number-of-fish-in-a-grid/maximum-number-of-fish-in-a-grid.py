class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r,c) : 
            if r<0 or c<0 or r==rows or c==cols or grid[r][c]==0 or (r,c) in visit : 
                return 0 
            visit.add((r,c)) 
            res=grid[r][c] 
            neighbours=[[r+1,c], [r-1,c], [r,c+1], [r,c-1]] 
            for nr, nc in neighbours : 
                res+=dfs(nr,nc) 
            return res 

        rows=len(grid) 
        cols=len(grid[0])
        visit=set() 
        res=0 
        for r in range(rows) : 
            for c in range(cols) : 
                res=max(res,dfs(r,c))
        return res 