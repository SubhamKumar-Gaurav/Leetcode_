class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int: 
        ans=float("inf") 
        wc=0 
        bc=0 
        for i in range(k) : 
            if blocks[i]=="W" : 
                wc+=1 
            else : 
                bc+=1 
        ans=min(ans, wc)
        for i in range(k, len(blocks)) :  
            if blocks[i]=="W" : 
                wc+=1 
            else : 
                bc+=1 
            if blocks[i-k]=="W" : 
                wc-=1 
            else : 
                bc-=1 
            ans=min(ans, wc)
        return ans 