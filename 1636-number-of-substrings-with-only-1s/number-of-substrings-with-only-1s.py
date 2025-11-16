class Solution:
    def numSub(self, s: str) -> int:
        n=len(s)
        MOD=1000000007 
        ans=0 
        if s[0]=="0" : 
            curr=0 
        else : 
            curr=1 
      
        for i in range(1, n) : 
            if s[i]=="1" : 
                curr+=1 
            else : 
                ans+=((curr)*(curr+1))//2
                if ans>MOD : 
                    ans=ans%MOD 
                curr=0 
                
        if s[-1]=="1" : 
            ans+=((curr)*(curr+1))//2 
            if ans>MOD : 
                ans=ans%MOD 
        return ans