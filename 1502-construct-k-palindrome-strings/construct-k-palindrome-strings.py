class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k : 
            return False 
        freq=[0]*26 
        for i in s : 
            freq[ord(i)-ord('a')]+=1 
        odd=0 
        for i in range(len(freq)) : 
            if freq[i]%2 : 
                odd+=1 
        return odd<=k 