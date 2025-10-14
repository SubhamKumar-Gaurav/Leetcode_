class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        if obstacleGrid[0][0]==1 : 
            return 0 

        n=len(obstacleGrid) 
        m=len(obstacleGrid[0]) 
        arr=[[0 for j in range(m)] for i in range(n)] 
        arr[0][0]=1 
        for i in range(1,m) : 
            if obstacleGrid[0][i]!=1 : 
                arr[0][i]=arr[0][i-1] 
        for i in range(1, n) : 
            if obstacleGrid[i][0]!=1 : 
                arr[i][0]=arr[i-1][0]  
        
        for i in range(1, n) : 
            for j in range(1, m) : 
                if obstacleGrid[i][j]!=1 : 
                    arr[i][j]=arr[i-1][j]+arr[i][j-1] 
        
        return arr[n-1][m-1]