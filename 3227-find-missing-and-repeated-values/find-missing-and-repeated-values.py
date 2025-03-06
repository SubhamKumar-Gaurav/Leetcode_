class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]: 
        d={} 
        n=len(grid)
        for i in range(1, n**2 +1) : 
            d[i]=0 
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                d[grid[i][j]]+=1 
        for i in d : 
            if d[i]==2 : 
                a=i 
            if d[i]==0 : 
                b=i 
        return [a,b]