class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0 : 
            return [1] 
        if rowIndex==1 : 
            return [1,1] 
        prev=[[1], [1,1]] 
        for i in range(2, rowIndex+2) : 
            temp=[None]*i
            temp[0]=1 
            temp[-1]=1  
            for j in range(1, len(temp)-1) : 
                temp[j]=prev[j-1]+prev[j] 
            prev=temp 
        return prev 