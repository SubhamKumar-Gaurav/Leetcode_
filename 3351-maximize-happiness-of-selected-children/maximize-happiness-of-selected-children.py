from heapq import heappush, heappop
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        pq=[]  
        for i in happiness : 
            heappush(pq, -i) 
        
        res=0
        reduction=0  
        while k : 
            temp=heappop(pq)+reduction 
            if temp>=0 : 
                break 
            res+=(-temp) 
            k-=1 
            reduction+=1 
        return res 