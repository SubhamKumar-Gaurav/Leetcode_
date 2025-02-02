class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s) 
        res=0 
        i=0 
        prev=[-1]*256 
        for j in range(n) : 
            i=max(i, prev[ord(s[j])]+1) 
            maxEnd=j-i+1 
            res=max(res, maxEnd) 
            prev[ord(s[j])]=j 
        return res 