class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0 : 
            return False 
        res=""
        while n>0 : 
            res=str(n%4)+res 
            n=n//4 
        
        if res.count("1")==1 and res.count("0")==len(res)-1 : 
            return True 
        return False 