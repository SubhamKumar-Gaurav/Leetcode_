class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int: 
        count=len(prices) 
        temp=0 
        for i in range(1,len(prices)) : 
            if prices[i-1]-prices[i] == 1 : 
                temp+=1 
                count+=temp 
            else : 
                temp=0 
        return count 