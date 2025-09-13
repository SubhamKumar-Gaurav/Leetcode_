class Solution:
    def maxFreqSum(self, s: str) -> int: 
        vowels={"a", "e", "i", "o", "u"} 
        dv=defaultdict(int) 
        dc=defaultdict(int)
        for i in s : 
            if i in vowels : 
                dv[i]+=1 
            else : 
                dc[i]+=1 
        maxv=0 
        maxc=0 
        for i in dv : 
            maxv=max(maxv, dv[i]) 
        for i in dc : 
            maxc=max(maxc, dc[i]) 
        return maxv+maxc

        