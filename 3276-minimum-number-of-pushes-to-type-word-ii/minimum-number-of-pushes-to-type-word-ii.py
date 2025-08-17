class Solution:
    def minimumPushes(self, word: str) -> int: 
        d={} 
        for i in word : 
            if i in d : 
                d[i]+=1 
            else : 
                d[i]=1 
        freq=sorted(d.values(), reverse=True) 
        ans=0 
        for i in range(len(freq)) : 
            if i<8 : 
                ans+=freq[i] 
            elif 8<=i<16 : 
                ans+=(2*freq[i]) 
            elif 16<=i<24 : 
                ans+=(3*freq[i]) 
            else : 
                ans+=(4*freq[i]) 
        return ans 