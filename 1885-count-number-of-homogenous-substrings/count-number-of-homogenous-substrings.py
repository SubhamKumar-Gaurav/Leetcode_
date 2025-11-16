class Solution:
    def countHomogenous(self, s: str) -> int:
        n=len(s)
        if n==1 : 
            return 1 

        MOD=1000000007  
        ans=0 
        curr=1 
        currChar=s[0] 
        for i in range(1, n) : 
            if s[i-1]==s[i] : 
                curr+=1 
            else : 
                ans+=((curr)*(curr+1))//2 
                if ans>MOD : 
                    ans=ans%MOD 
                currChar=s[i] 
                curr=1 

        ans+=((curr)*(curr+1))//2 
        if ans>MOD : 
            ans=ans%MOD 
        return ans 
