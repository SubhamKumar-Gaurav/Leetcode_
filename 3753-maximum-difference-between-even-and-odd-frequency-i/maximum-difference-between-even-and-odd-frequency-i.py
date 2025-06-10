class Solution:
    def maxDifference(self, s: str) -> int:
        d={} 
        for i in s : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 
        odd=[] 
        even=[] 
        for i in d : 
            if d[i]%2 : 
                odd.append(d[i])
            else : 
                even.append(d[i]) 
        odd.sort() 
        even.sort() 
        return odd[-1]-even[0]