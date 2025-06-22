
class Solution:
    def minDeletions(self, s: str) -> int: 
        d={} 
        for i in s : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 

        used_freq=set() 
        res=0 
        for c, freq in d.items() : 
            while freq>0 and freq in used_freq : 
                freq-=1 
                res+=1 
            used_freq.add(freq)
        return res 