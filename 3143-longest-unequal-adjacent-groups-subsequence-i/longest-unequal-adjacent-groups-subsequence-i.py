class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:  
        n=len(words) 
        res=[] 
        for i in range(n) : 
            if i==0 or groups[i]!=groups[i-1] : 
                res.append(words[i]) 
        return res 