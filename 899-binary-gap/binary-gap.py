class Solution:
    def binaryGap(self, n: int) -> int:
        s=bin(n)[2:] 
        last_one=0 
        ans=0 
        for i in range(1, len(s)) : 
            if s[i]=="1" : 
                ans=max(ans, i-last_one) 
                last_one=i 
        return ans 