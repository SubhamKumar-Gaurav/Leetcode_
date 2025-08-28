from collections import defaultdict 

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]: 
        n=len(grid)
        d=defaultdict(list) 
        for i in range(n) : 
            for j in range(n) : 
                d[i-j].append(grid[i][j]) 
        
        for i in d : 
            if i>=0 : 
                d[i].sort(reverse=True) 
            else : 
                d[i].sort() 
        
        for i in range(n) : 
            for j in range(n) : 
                grid[i][j]=d[i-j].pop(0)
        return grid