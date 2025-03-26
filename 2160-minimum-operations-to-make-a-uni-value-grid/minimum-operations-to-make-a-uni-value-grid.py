
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:  
        for row in grid : 
            for n in row : 
                if n%x != grid[0][0]%x : 
                    return -1 

        arr=[] 
        for i in range(len(grid)) : 
            for j in range(len(grid[i])) : 
                arr.append(grid[i][j]) 
        arr.sort() 
        prefix=0 
        total=sum(arr)
        res=float("inf") 

        for i in range(len(arr)) : 
            cost_left=arr[i]*i - prefix 
            cost_right=total-prefix-(arr[i]*(len(arr)-i))    
            ops=(cost_left+cost_right)//x 
            res=min(res, ops) 
            prefix+=arr[i]
        return res 