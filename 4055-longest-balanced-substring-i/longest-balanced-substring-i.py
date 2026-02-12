
class Solution: 
    def longestBalanced(self, s: str) -> int: 
        n=len(s) 
        res=0 
        
        for i in range(n) :
            freq=[0]*26  
            unique_elements=0 
            max_freq=0 
            for j in range(i, n) : 
                idx=ord(s[j])-ord("a") 

                if freq[idx]==0 : 
                    unique_elements+=1 
                
                freq[idx]+=1 

                if freq[idx]>=max_freq : 
                    max_freq=freq[idx] 
                
                if max_freq*unique_elements == (j-i+1) : 
                    res=max(res, j-i+1)
        return res 