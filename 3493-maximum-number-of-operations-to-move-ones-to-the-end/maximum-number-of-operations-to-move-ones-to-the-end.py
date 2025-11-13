
class Solution:
    def maxOperations(self, s: str) -> int:
        isSorted=True 
        n=len(s)
        for i in range(n-1) : 
            if int(s[i])>int(s[i+1]) : 
                isSorted=False 
                break 
        
        if isSorted : 
            return 0 
        
        res=0 
        i=0 
        ones=0 
        while i<n : 
            if s[i]=="1" : 
                ones+=1 
            else : 
                res+=ones 
                while i+1<n and s[i+1]=="0" :
                    i+=1       
            i+=1 
        return res 