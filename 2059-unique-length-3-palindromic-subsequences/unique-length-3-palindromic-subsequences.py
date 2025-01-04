class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set() 
        left=set() 
        right={}
        for i in s : 
            if i in right : 
                right[i]+=1 
            else : 
                right[i]=1 
        
        for m in s : 
            right[m]-=1 
            for c in left : 
                if right[c]>0 : 
                    res.add((m,c)) 
            left.add(m)
        return len(res)