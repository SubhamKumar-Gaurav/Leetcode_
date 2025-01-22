class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows=len(isWater)
        cols=len(isWater[0]) 
        height=[[float("inf")]*cols for i in range(rows)] 

        for i in range(len(isWater)) : 
            for j in range(len(isWater[0])) : 
                if isWater[i][j]==1 :  
                    height[i][j]=0 
                else : 
                    if i>0 : 
                        height[i][j]=min(height[i][j], height[i-1][j]+1)
                    if j>0 : 
                        height[i][j]=min(height[i][j], height[i][j-1]+1) 
        
        for i in range(rows-1,-1,-1) : 
            for j in range(cols-1,-1,-1) : 
                if i<rows-1 : 
                    height[i][j]=min(height[i][j], height[i+1][j]+1) 
                if j<cols-1 : 
                    height[i][j]=min(height[i][j], height[i][j+1]+1) 
        return height 