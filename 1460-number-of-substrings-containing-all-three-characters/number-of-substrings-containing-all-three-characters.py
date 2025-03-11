class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d=defaultdict(int)
        res=0 
        l=0 
        for r in range(len(s)) : 
            d[s[r]]+=1 
            while len(d)>=3 : 
                res+=(len(s)-r)
                d[s[l]]-=1 
                if d[s[l]]==0 : 
                    d.pop(s[l])
                l+=1
        return res 