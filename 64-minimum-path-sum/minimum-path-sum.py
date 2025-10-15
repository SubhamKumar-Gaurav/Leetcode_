class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        n=len(grid) 
        m=len(grid[0]) 
        arr=[[0 for j in range(m)] for i in range(n)] 
        arr[0][0]=grid[0][0] 
        for i in range(1, n) : 
            arr[i][0]=grid[i][0]+arr[i-1][0] 
        
        for i in range(1, m) : 
            arr[0][i]=grid[0][i]+arr[0][i-1] 
        
        for i in range(1, n) : 
            for j in range(1, m) : 
                arr[i][j]=grid[i][j]+min(arr[i-1][j], arr[i][j-1])
        
        return arr[n-1][m-1]