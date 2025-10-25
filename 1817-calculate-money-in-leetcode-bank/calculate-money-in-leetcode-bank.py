class Solution:
    def totalMoney(self, n: int) -> int: 
        total_weeks=n//7 
        remainder=n%7 
        res=0 
        i=0
        while i<total_weeks : 
            res+=28+(7*i) 
            i+=1 
        res+=(remainder*(remainder+1))//2 + (remainder*i)
        return res 