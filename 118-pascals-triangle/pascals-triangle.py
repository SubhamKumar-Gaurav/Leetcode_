class Solution:
    def generate(self, numRows: int) -> List[List[int]]: 
        if numRows==1 : 
            return [[1]] 
        if numRows==2 : 
            return [[1], [1,1]] 
        ans=[[1], [1,1]] 
        for i in range(3,numRows+1) : 
            prev=ans[-1]
            temp=[None]*i
            temp[0]=1 
            temp[-1]=1 
            for j in range(1, len(temp)-1) :
                temp[j]=prev[j-1]+prev[j] 
            ans.append(temp)
        return ans