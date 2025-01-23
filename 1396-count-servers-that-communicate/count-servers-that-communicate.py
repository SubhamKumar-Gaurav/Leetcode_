class Solution:
    def countServers(self, grid: List[List[int]]) -> int: 
        def isolated (s,i,j) : 
            rows=len(s)
            cols=len(s[0]) 
            for row in range(rows) : 
                if row!=i and s[row][j]==1 : 
                    return False 
            for col in range(cols) : 
                if col!=j and s[i][col]==1 : 
                    return False 
            return True 

        total_server=0 
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j]==1 : 
                    total_server+=1 
       
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j]==1 :
                    if isolated(grid, i, j) : 
                        total_server-=1 
        return total_server