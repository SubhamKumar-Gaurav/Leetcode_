class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        l=1 
        r=max(piles)
        res=0  
        while l<=r : 
            m=(l+r)//2 
            temp=0 
            for i in piles : 
                temp+=math.ceil(i/m) 
            if temp<=h : 
                res=m 
                r=m-1 
            else : 
                l=m+1 
        return res 