class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefix(s1, s2) : 
            if len(s1)>len(s2) : 
                return False 
            else : 
                if s1==s2[:len(s1)] : 
                    return True 
                else : 
                    return False 
        def isSuffix(s1, s2) : 
            if len(s1)>len(s2) : 
                return False 
            else : 
                temp=s2[::-1] 
                if s1[::-1]==temp[:len(s1)] : 
                    return True 
                else : 
                    return False
        c=0  
        n=len(words)
        for i in range(n) :  
            for j in range(i+1,n) : 
                if isPrefix(words[i], words[j]) and isSuffix(words[i], words[j]) : 
                    c+=1 
        return c