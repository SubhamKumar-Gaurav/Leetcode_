class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        total_zero=s.count("0") 
        curr_zero=0 
        res=0 
        for i in range(1,n) : 
            if s[i-1]=="0" : 
                curr_zero+=1 
                total_zero-=1 
            res=max(res,curr_zero+n-i-total_zero) 
        return res 