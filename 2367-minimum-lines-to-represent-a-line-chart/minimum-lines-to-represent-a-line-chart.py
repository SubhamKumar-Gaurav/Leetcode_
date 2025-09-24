class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int: 
        n=len(stockPrices) 
        if n==1 : 
            return 0 
        ans=1 
        stockPrices.sort(key=lambda x: x[0])
        prev_dy = (stockPrices[1][1]-stockPrices[0][1])
        prev_dx = (stockPrices[1][0]-stockPrices[0][0])

        for i in range(1, n-1) : 
            curr_dy = (stockPrices[i+1][1]-stockPrices[i][1]) 
            curr_dx = (stockPrices[i+1][0]-stockPrices[i][0])
            if curr_dy*prev_dx != curr_dx*prev_dy : 
                ans+=1 
                prev_dx=curr_dx 
                prev_dy=curr_dy 
                
        return ans