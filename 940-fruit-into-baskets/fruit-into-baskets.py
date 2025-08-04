from collections import defaultdict 
class Solution:
    def totalFruit(self, fruits: List[int]) -> int: 
        n=len(fruits) 
        d=defaultdict(int) 
        i=0 
        j=0 
        ans=0 
        while i<n and j<n : 
            while j<n and i<n and len(d)<=2 : 
                d[fruits[j]]+=1 
                if len(d)<=2 : 
                    ans=max(ans, j-i+1) 
                else : 
                    j+=1 
                    break 
                j+=1 
            d[fruits[i]]-=1 
            if d[fruits[i]]==0 : 
                del d[fruits[i]] 
            i+=1 
        return ans 