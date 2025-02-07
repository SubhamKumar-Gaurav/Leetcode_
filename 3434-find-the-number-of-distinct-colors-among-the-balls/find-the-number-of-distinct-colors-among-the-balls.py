class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:  
        n=len(queries) 
        ans=[0]*n 
        mp={}  # storing the ball and its color 
        colour=defaultdict(int)  # tracking the distinct colours
        i=0 
        for x,c in queries : 
            if x in mp : 
                colour[mp[x]]-=1 
                if colour[mp[x]]==0 : 
                    colour.pop(mp[x])  
            mp[x]=c 
            colour[c]+=1 
            ans[i]=len(colour) 
            i+=1 
        return ans 