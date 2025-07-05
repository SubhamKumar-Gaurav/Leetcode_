class Solution:
    def findLucky(self, arr: List[int]) -> int: 
        d={} 
        for i in arr : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 
        ans=0 
        for i in d : 
            if d[i]==i : 
                ans=max(ans, i) 
        if ans!=0 : 
            return ans
        return -1