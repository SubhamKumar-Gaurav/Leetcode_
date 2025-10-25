class Solution:
    def totalMoney(self, n: int) -> int: 
        i=0 
        monday=1 
        res=0  
        while i<n : 
            res+=monday 
            prev=monday
            i+=1
            monday+=1 
            j=0 
            while j<6 and i<n : 
                res+=prev+1 
                prev+=1 
                j+=1 
                i+=1
        return res 
            
            