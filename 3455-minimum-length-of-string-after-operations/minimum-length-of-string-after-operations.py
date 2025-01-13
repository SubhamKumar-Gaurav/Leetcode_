class Solution:
    def minimumLength(self, s: str) -> int:
        freq=Counter(s)
        c=0 
        for i in freq : 
            if freq[i]%2==0 : 
                c+=2 
            else : 
                c+=1 
        return c