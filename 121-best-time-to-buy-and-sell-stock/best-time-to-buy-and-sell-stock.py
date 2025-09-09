class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        prefixMin=[0]*n 
        prefixMin[0]=prices[0] 
        for i in range(1, n) : 
            prefixMin[i]=min(prices[i], prefixMin[i-1]) 
        
        suffixMax=[0]*n 
        suffixMax[-1]=prices[-1] 
        for i in range(n-2, -1, -1) : 
            suffixMax[i]=max(prices[i], suffixMax[i+1]) 
        
        ans=0 
        for i in range(n-1) : 
            if suffixMax[i+1]>prefixMin[i] : 
                curr=suffixMax[i+1]-prefixMin[i] 
                ans=max(ans, curr)
        return ans