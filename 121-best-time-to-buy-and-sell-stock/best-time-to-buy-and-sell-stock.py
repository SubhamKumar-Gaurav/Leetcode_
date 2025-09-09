class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minval=float("inf") 
        maxval=0 
        for i in prices :  
            minval=min(minval, i) 
            maxval=max(maxval, i-minval) 
        return maxval