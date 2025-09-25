class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int: 
        n=len(triangle) 
        if n==1 : 
            return triangle[0][0] 
        
        tri=triangle.copy() 
        
        for i in range(n-2, -1, -1) : 
            for j in range(len(tri[i])) : 
                tri[i][j]+=min(tri[i+1][j], tri[i+1][j+1]) 
        
        return tri[0][0] 