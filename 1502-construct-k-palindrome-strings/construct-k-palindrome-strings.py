class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k : 
            return False 
        d={}
        for i in s : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 
        odd=0 
        for i in d : 
            if d[i]%2 : 
                odd+=1 
        return odd<=k