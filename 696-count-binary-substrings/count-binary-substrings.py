class Solution: 
    def countBinarySubstrings(self, s: str) -> int: 
        consecutive=[] 
        curr=1 
        for i in range(1, len(s)) : 
            if s[i]==s[i-1] : 
                curr+=1 
            else : 
                consecutive.append(curr) 
                curr=1 
        consecutive.append(curr)
         
        ans=0 
        for i in range(1, len(consecutive)) : 
            ans+=min(consecutive[i], consecutive[i-1]) 
        return ans 