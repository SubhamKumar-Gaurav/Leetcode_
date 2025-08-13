class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0 : 
            return False 

        def pow3(n) : 
            res="" 
            while n>0 : 
                res=str((n%3))+res  
                n=n//3 
            return res 
        
        a=pow3(n)
        if a.count("1")==1 and a[0]=="1" and a.count("0")==len(a)-1 : 
            return True 
        return False 